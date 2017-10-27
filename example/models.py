# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatSession(models.Model):
	channel_name = models.CharField(max_length=50)
	user_1 = models.IntegerField()
	user_2 = models.IntegerField()
	date = models.DateTimeField(auto_now=True, blank=True)

class ChatLog(models.Model):
	session_id = models.ForeignKey('ChatSession', on_delete=models.CASCADE, blank=False, default=0)
	messages = models.CharField(max_length=1000, null=True, blank=False)
	date = models.DateTimeField(auto_now=True, blank=True)
	sender_id = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='sender_id', blank=False, default=0)
	receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_id', blank=False, default=0)

	def __str__(self):
		return self.sender_id + " to " + self.receiver_id + " : " + self.messages