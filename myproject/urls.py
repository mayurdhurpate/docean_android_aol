"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from android.views import register
admin.autodiscover()

urlpatterns = [
	url(r'^register/$','android.views.register',name='register'),
	url(r'^broadcastreceive/$','android.views.message_receive',name='message_receive'),
    url(r'^broadcastreceive/$','android.views.message_receive',name='message_receive'),
    url(r'^add_topic/$','android.views.add_topic',name='add_topic'),
    url(r'^contacts/$','android.views.contacts_data',name='contacts_data'),
    url(r'^messages/$','android.views.message_data',name='message_data'),
    url(r'^image_upload/$','android.views.image_upload',name='image_upload'),
	url(r'^admin/', include(admin.site.urls)),
]
