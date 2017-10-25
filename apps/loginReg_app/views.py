# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt

from models import UserManager, User, Relationship
# , RelationshipManager

# FORMS

def logRegUserPage(request):
	return render(request, 'loginReg_app/loginRegisterPage.html')

def dashUserPage(request):
	# If user tries to access /dashboard without logging in, they are directed to the error page
	if 'currentUser' not in request.session:
		return render(request, 'loginReg_app/errorPage.html')
	# Load User Dashboard HTML
	else:
		context = {
		"users": User.objects.all(),
		"friends": Relationship.objects.filter(from_person = request.session['currentUser']).all(),
		}
		return render(request, 'loginReg_app/dashUserPage.html', context)

def profilePage(request, id):
	context = {
		"user": User.objects.get(id=id)
	}
	return render(request, 'loginReg_app/profilePage.html', context)

# USER ACTIONS

def loginUser(request):
	# Validate Log-in parameters
	errors = User.objects.login_validator(request.POST, request)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/')
	#  Save newly logged in user's id in session
	else:
		if 'currentUser' not in request.session:
			request.session['currentUser'] = User.objects.get(email=request.POST['email']).id
		return redirect('/friends')

def createUser(request):
	errors = User.objects.register_validator(request.POST)
	# Stop if errors exist
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/')
	# Allow if no errors
	else:
		# create user
		newUser = User.objects.createUser(request.POST, request)
		# create currentUser session variable
		if 'currentUser' not in request.session:
			request.session['currentUser'] = User.objects.last().id
		return redirect('/friends')

def logout(request):
	request.session.clear()
	return redirect('/')

def createRelationship(request, id):
	# erors = Relationship.objects.newRelationship_validator()
	# if len(errors):
	# 	for tag, error in errors.iteritems():
	# 		messages.error(request, error, extra_tags = tag)
	# 	return redirect('/friends')
	# else:
		Relationship.objects.create(from_person = User.objects.get(id=request.session['currentUser']), to_person = User.objects.get(id=id))
		Relationship.objects.create(to_person = User.objects.get(id=request.session['currentUser']), from_person = User.objects.get(id=id))
		return redirect('/friends')

def deleteRelationship(request, id):
	Relationship.objects.filter(from_person=request.session['currentUser']).filter(to_person=id).delete()
	Relationship.objects.filter(to_person=request.session['currentUser']).filter(from_person=id).delete()
	return redirect('/friends')