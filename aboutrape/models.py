from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    supervisor = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='supervisor_of')
    description = models.CharField(max_length=1000)
    url = models.URLField("Website", blank=True)

class Category(models.Model):
  name = models.CharField(max_length=60)
  description = models.CharField(max_length=1000)

  def __unicode__(self):
      return self.name

  def to_dict(self):
    return {"name": self.name, "description": self.description}

  class Meta:
    db_table = "category"
    ordering = ['name']

class Comment(models.Model):
  body = models.CharField(max_length=1000)
  category = models.ForeignKey(Category)

  class Meta:
      db_table = "comment"

  def __unicode__(self):
      return self.body