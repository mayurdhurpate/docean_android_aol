from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	token=models.CharField(max_length=1000)
	email=models.CharField(unique=True,max_length=100)
	phone_no=models.CharField(max_length=20,null=True,blank=True)
	image_url=models.CharField(max_length=100,null=True,blank=True)
	social_id=models.CharField(max_length=100)
	role=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return "%s %s" % (self.name,self.email)
	def __unicode__(self):
		return "%s %s" % (self.name,self.email)
	
class Noti(models.Model):
	api_key=models.CharField(max_length=1000)
	def __str__(self):
                return "%s" % (self.api_key)
	def __unicode__(self):
                return "%s" % (self.api_key)


class Message(models.Model):
    sender = models.CharField(max_length=100)
    message = models.CharField(max_length=1000,null=True,blank=True)
    token = models.CharField(max_length=1000)
    message_id = models.CharField(max_length=1000,null=True,blank=True)
    title = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
                return "%s %s" % (self.sender,self.message)
    def __unicode__(self):
                return "%s %s" % (self.sender,self.message)
