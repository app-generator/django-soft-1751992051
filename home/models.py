# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Table1(models.Model):

    #__Table1_FIELDS__
    f1 = models.TextField(max_length=255, null=True, blank=True)
    f2 = models.TextField(max_length=255, null=True, blank=True)
    f3 = models.TextField(max_length=255, null=True, blank=True)

    #__Table1_FIELDS__END

    class Meta:
        verbose_name        = _("Table1")
        verbose_name_plural = _("Table1")



#__MODELS__END
