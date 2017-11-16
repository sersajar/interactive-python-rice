#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------
# password_test.py
# example of if/else, lists, assignments, raw_input, comments and evaluations
# ----------------------------

# Assign the users and passwords
users = ['Fred', 'John', 'Steve', 'Ann', 'Mary']
passwds = ['acces', 'dog', '12345', 'kids', 'qwerty']

# Get username and password
usrname = raw_input('Enter your username => ')
pwd = raw_input('Enter your password => ')

# Check to see if user is in the list
if usrname in users:
	pos = users.index(usrname)  # get the position of users in the list
	if pwd == passwds[pos]:  # find the password at position
		print 'Hi there, %s. Acces granted.' % usrname
	else:
		print 'Password incorrect. Access denied.'
else:
	print "Sorry... I don't recognize you. Acces denied."
