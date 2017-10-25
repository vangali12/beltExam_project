# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def createUser(self, postData, request):
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

		tempUser = self.create(
			name=postData['name'],
			alias=postData['alias'],
			email=postData['email'],
			password=hash1,
			dob=postData['dob'])
		return tempUser

	def register_validator(self, postData):
		errors={}
		if len(postData['name']) < 2:
			errors["shortFirst"] = "First name must be more than 2 charactes long."
		if len(postData['alias']) < 2:
			errors["shortLast"] = "Last name must be more than 2 characters long."
		if not EMAIL_REGEX.match(postData['email']):
			errors["emailformat"] = "Email format must be _____@___.com"
		if (User.objects.filter(email=postData['email'])):
			errors["exists"] = "This email already exists in our database. Please enter a different email or login below."
		if (postData['password'] != postData['confPassword']):
			errors["noMatch"] = "Your password does not match. Please try again."
		return errors
	def login_validator(self, postData, request):
		errors={}
		if not (User.objects.filter(email=postData['email'])):
			errors["doesntexists"] = "This email does not exist in our database. Please register above."
		elif bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()) == False:
			errors['wrongPassword'] = "Incorrect Password. Please try again."
		if ('currentUser' in request.session):
			errors["loggedIn"] = "Someone is already logged in. Please log out before trying to log in."
		return errors

# class RelationshipManager(models.Manager):
	

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateField()
	relationships = models.ManyToManyField(
		'self',
		through='Relationship',
		symmetrical=False,
		related_name='related_to+')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Relationship(models.Model):
	from_person = models.ForeignKey(User, related_name='from_people')
	to_person = models.ForeignKey(User,related_name='to_people')
	# objects = RelationshipManager()
	