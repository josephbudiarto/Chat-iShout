# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from example.models import ChatSession
from example.models import ChatLog
from django.db.models import Q

from drealtime import iShoutClient
ishout_client = iShoutClient()

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
	users = User.objects.exclude(id=request.user.id)
	channel = ChatSession.objects.get(id = 1) #CHANGE WITH PARAMETER GET Using token!!
	logs = ChatLog.objects.filter(session_id = channel.id).select_related()

	return render(request, 'home.html',{'users': users, 'username' : request.user.username, 'user_id': request.user.id, 'logs' : logs, 'channel_name': channel.channel_name})


def logout_view(request):
	logout(request)
	return redirect('home')

@login_required(login_url='/accounts/login/')
def alert(request):
	r = request.GET.get

	ishout_client.emit(
		int(r('user')),
		'alertchannel',
		data = {'msg': r('username_sender') + ' is calling you!'}
	)
	return HttpResponseRedirect(reverse('home'))

@login_required(login_url='/accounts/login/')
def send(request):
	
	r = request.GET.get
	msg = request.POST.get('msg')

	if msg:
		msg = msg.replace("<script>", "")
		msg = msg.replace("</script>", "")
		msg = msg.replace("<SCRIPT>", "")
		msg = msg.replace("</SCRIPT>", "")
		channel = ChatSession.objects.get(id=1) #CHANGE WITH GET PARAMETER
		a = ChatLog(session_id = ChatSession.objects.get(id=1), messages=msg, sender_id=User.objects.get(id=r('user_id_sender')), receiver_id=User.objects.get(id=r('user')))
		a.save()

	ishout_client.emit(
		int(r('user')),
		channel.channel_name,
		data = {'msg': msg, 'username': r('username_sender'), 'channel_name': channel.channel_name}
	)
	return HttpResponseRedirect(reverse('home'))