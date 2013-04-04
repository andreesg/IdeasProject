#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import get_object_or_404, render
from webapp.models import UserProfile, Idea
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import operator


def dashboard(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        ideas_list = Idea.objects.all()

        sorted_list = sorted(ideas_list, key=lambda x: x.votes,
                             reverse=True)

        return render_to_response('webapp/dashboard.html',
                                  {'username': user.username,
                                  'ideas': sorted_list},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/webapp')


def quit(request):
    logout(request)
    return HttpResponseRedirect('/webapp')


def new_idea(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        tags = request.POST['hidden-tags']
        new_idea = Idea()
        new_idea.user = request.user
        new_idea.title = title
        new_idea.desc = desc
        new_idea.tags = tags
        new_idea.votes = 0
        new_idea.pub_date = datetime.datetime.now()
        new_idea.save()

        return HttpResponseRedirect('dashboard')
    else:
        return HttpResponseRedirect('/webapp')


def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('dashboard')
            else:

                # Return a 'disabled account' error message

                message = 'Account disabled'
                return render_to_response('webapp/index.html',
                        {'message': message},
                        context_instance=RequestContext(request))
        else:

            # Return an 'invalid login' error message.

            message = 'Invalid login'
            return render_to_response('webapp/index.html',
                    {'message': message},
                    context_instance=RequestContext(request))


def index(request):
    print 'USER + ' + request.user.username
    if request.user.is_authenticated():
        return HttpResponseRedirect('/webapp/dashboard')
    else:
        return render(request, 'webapp/index.html', {})


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/webapp')
    else:
        ideas_list = Idea.objects.all()

        sorted_list = sorted(ideas_list, key=lambda x: x.votes,
                             reverse=True)
        return render(request, 'webapp/profile.html',
                      {'username': request.user.username, 'ideas':sorted_list})

def delete(request, idea_id):
    
    print "delete idea"
    idea = get_object_or_404(Idea, pk=idea_id)
    if idea.user.username == request.user.username:
        idea.delete()

    return HttpResponseRedirect('/webapp/dashboard')

def up(request, idea_id):
    print 'vote up'
    idea = get_object_or_404(Idea, pk=idea_id)
    idea.votes += 1
    idea.save()

    return HttpResponseRedirect('/webapp/dashboard#idea' + str(idea_id))


def down(request, idea_id):
    print 'vote down'
    idea = get_object_or_404(Idea, pk=idea_id)
    idea.votes -= 1
    idea.save()

    return HttpResponseRedirect('/webapp/dashboard#idea' + str(idea_id))
