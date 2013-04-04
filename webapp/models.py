#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


# Models

class UserProfile(models.Model):

    user = models.ForeignKey(User)


class Idea(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    tags = models.TextField(blank=True, null=True, default='')
    votes = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def get_tag_list(self):
        if len(self.tags) > 0:
            return self.tags.split(',')
        else:
            return False


class Tag(models.Model):

    idea = models.ForeignKey(Idea)
    name = models.CharField(max_length=200)

