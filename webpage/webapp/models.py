from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Signup(models.Model):

	user=models.OneToOneField(User,on_delete=models.CASCADE)

# class homemodel(models.Model):
class Post(models.Model):

	Title = models.CharField(max_length= 1050)

	content = models.CharField(max_length=1250)

	profile_pic = models.ImageField(upload_to='picture',blank=True)

	author = models.CharField(max_length=1239,blank=True)

	name = models.CharField(max_length=200)

	class Meta:

		verbose_name_plural = 'Post'

# @receiver(pre_save, sender=sharemodel)

# def my_function_post_save(sender, instance,**kwargs):

# 	print('it is working or not ')

class Friends(models.Model):

	home = models.ForeignKey('Post',on_delete=models.CASCADE,null=True,blank=True)
    
	name = models.CharField(max_length=200)

	class Meta:

		verbose_name_plural = 'Friends'


# class Likes_dislike(models.Model):

# 	like = models.PositiveIntegerField()

# 	dislike = models.IntegerField()