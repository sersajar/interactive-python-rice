#!/usr/bin/env python
# -*- coding: UTF-8 +-*
#-----------------------------------------------------------
# cookbook.py
#-----------------------------------------------------------

import apsw, string, webbrowser, os


class CookBook:
	def __init__(self):
		global connection, cursor
		self.total_count = 0
		connection = apsw.Connection("cookbook1.db3")
		cursor = connection.cursor()

	def print_all_recipes(self):  # RESPONSE 1
		# os.system('cls' if os.name == 'nt' else 'clear')
		print '%s %s %s %s' % ('Item'.ljust(5), 'Name'.ljust(30), 'Serves'.ljust(20), 'Source'.ljust(30))
		print '-' * 75
		sql = 'SELECT * FROM Recipes'
		cntr = 0
		for x in cursor.execute(sql):
			cntr += 1
			print '%s %s %s %s' % (str(x[0]).rjust(5), x[1].ljust(30), x[2].ljust(20), x[3].ljust(30))
			print '-' * 75
			self.total_count = cntr
			print

	def search_for_recipe(self):  # RESPONSE 2
		# print the search menu
		print '----------------------------------'
		print ' Search in'
		print '----------------------------------'
		print ' 1 - Recipe Name'
		print ' 2 - Recipe Source'
		print ' 3 - Ingredients'
		print ' 4 - Exit'
		searchin = raw_input('Enter Search Type -> ')
		if searchin != '4':
			if searchin == '1':
				search = 'Recipe Name'
			elif searchin == '2':
				search = 'Recipe Source'
			elif searchin == '3':
				search = 'Ingredients'
			parm = searchin
			response = raw_input('Search for what in %s (blank to exit) -> ' % search)
			if parm == '1':  # Recipe Name
				sql = "SELECT pkid,name,source,serves FROM Recipes WHERE name like '%%%s%%'" % response
			elif parm == '2':  # Recipe Source
				sql = "SELECT pkid,name,source,serves FROM Recipes WHERE source like '%%%s%%'" % response
			elif parm == '3':  # Ingredients
				sql = "SELECT r.pkid,r.name,r.serves,r.source,i.ingredients FROM Recipes r Left Join ingredients i\
						on (r.pkid = i.recipeid) WHERE i.ingredients like '%%%s%%' GROUP BY r.pkid" % response

			try:
				if parm == '3':
					print '%s %s %s %s %s' % ('Item'.ljust(5),'Name'.ljust(25),'Serves'.ljust(10),\
					                           'Source'.ljust(26),'Ingredient'.ljust(20))
					print '---------------------------------------------------------------------------------------------'
				else:
					print '%s %s %s %s' % ('Item'.ljust(5), 'Name'.ljust(25), 'Serves'.ljust(10), 'Source'.ljust(25))
					print '---------------------------------------------------------------------------------------------'
				for x in cursor.execute(sql):
					if parm == '3':
						print '%s %s %s %s %s' % (str(x[0]).rjust(5),x[1].ljust(25),\
						                          x[2].ljust(10),x[3].ljust(25),x[4].ljust(20))
					else:
						print '%s %s %s %s' % (str(x[0]).rjust(5), x[1].ljust(25), x[3].ljust(10), x[2].ljust(25))
			except:
				print 'An Error Occured'
			print '--------------------------------------------------------------------------------------'
			inkey = raw_input('Press a Key')

	def print_single_recipe(self, which):  # RESPONSE 3
		os.system('cls' if os.name == 'nt' else 'clear')
		# importing from Recipes
		sql = 'SELECT * FROM Recipes WHERE pkID = %s' % str(which)
		print '-' * 75
		for x in cursor.execute(sql):
			recipe_id = x[0]
			print "  Recipe nº: " + str(x[0])
			print "  Title: " + x[1]
			print "  Serves: " + x[2]
			print "  Source: " + x[3]
		print '-' * 75
		# importing Ingredients
		print '  Ingredient List: '
		print
		sql = 'SELECT * FROM Ingredients WHERE RecipeID = %s' % recipe_id
		for x in cursor.execute(sql):
			print x[1]
		print
		print
		# importing Instructions
		print '  Instructions: '
		print
		sql = 'SELECT * FROM Instructions WHERE RecipeID = %s' % recipe_id
		for x in cursor.execute(sql):
			print x[1]
		print '-' * 75
		res = raw_input('Press Enter -> ')
		os.system('cls' if os.name == 'nt' else 'clear')

	def delete_recipe(self, which):  # RESPONSE 4
		pass

	def enter_new_recipe(self):  # RESPONSE 5
		pass

	def print_recipe(self, which):  # RESPONSE 6
		pass


def menu():
	cbk = CookBook()  # Initialize the class
	loop = True
	os.system('cls' if os.name == 'nt' else 'clear')
	while loop:
		print
		print '=================================================='
		print '               RECIPE DATABASE'
		print '=================================================='
		print
		print '     1 - Show All Recipes'
		print '     2 - Search for recipe'
		print '     3 - Show a Recipe'
		print '     4 - Delete a Recipe'
		print '     5 - Add a Recipe'
		print '     6 - Print a Recipe'
		print '     0 - Exit'
		print
		print '=' * 50

		response = raw_input('Enter a selection -> ')
		print

		if response == '1':  # show all recipes
			os.system('cls' if os.name == 'nt' else 'clear')
			cbk.print_all_recipes()
			print 'Total Recipes - %s' % cbk.total_count
			print '-' * 75
			res = raw_input('Press Enter -> ')
			os.system('cls' if os.name == 'nt' else 'clear')

		elif response == '2':  # search for a recipe
			os.system('cls' if os.name == 'nt' else 'clear')
			cbk.search_for_recipe()

		elif response == '3':  # show a single recipe
			os.system('cls' if os.name == 'nt' else 'clear')
			cbk.print_all_recipes()
			try:
				res = int(raw_input('Select a Recipe -> '))

				if res <= cbk.total_count:
					os.system('cls' if os.name == 'nt' else 'clear')
					cbk.print_single_recipe(res)

				elif res > cbk.total_count:
					os.system('cls' if os.name == 'nt' else 'clear')
					print ' /----------------------------------------------\ '
					print '{ There are not so many recipes. Back to Menu... }'
					print ' \----------------------------------------------/\n'
				# else:
				# 	print 'Unrecognized command. Returning to menu.'
			except ValueError:
				os.system('cls' if os.name == 'nt' else 'clear')
				print ' /-----------------------------\ '
				print '{ Not a number... back to menu. }'
				print ' \-----------------------------/\n'

		elif response == '4':  # delete recipe
			os.system('cls' if os.name == 'nt' else 'clear')
			print
			print ' /------------------------------------------------------\ '
			print '{ ¡¡¡¿¿¿ DO YOU REALLY WANT TO ELIMINATE A RECIPE ???!!! }'
			print ' \------------------------------------------------------/ '
			print
			cbk.print_all_recipes()

		elif response == '5':  # add a recipe
			os.system('cls' if os.name == 'nt' else 'clear')
			cbk.enter_new_recipe()                                  # TODO

		elif response == '6':  # print a single recipe
			os.system('cls' if os.name == 'nt' else 'clear')
			print ' /----------------------\ '
			print "{      LET'S PRINT       }"
			print ' \----------------------/\n'
			cbk.print_all_recipes()
			print 'Total Recipes - %s' % cbk.total_count
			print '-' * 75
			res = raw_input('Press Enter -> ')
			os.system('cls' if os.name == 'nt' else 'clear')

		elif response == '0':  # exit the program
			print 'Good Bye'
			loop = False

		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print
			print ' /--------------------------------\ '
			print '{ Unrecognized command. Try again. }'
			print ' \--------------------------------/\n'


menu()
