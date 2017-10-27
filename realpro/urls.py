"""realpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from example import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^alert/$', views.alert, name="alert"),
    url(r'^send/$', views.send, name="send"),
    url(r'^accounts/login/$', auth_views.LoginView.as_view()),
    url(r'^accounts/logout/$', views.logout_view, name='logout'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/accounts/login'}),

]
