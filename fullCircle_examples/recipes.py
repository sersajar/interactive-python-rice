# crating a simple database
import apsw

# Opening/creating database

connection = apsw.Connection("cookbook1.db3")
cursor = connection.cursor()
sql = 'DROP TABLE IF EXISTS Recipes'
cursor.execute(sql)
sql = 'DROP TABLE IF EXISTS Instructions'
cursor.execute(sql)
sql = 'DROP TABLE IF EXISTS Ingredients'
cursor.execute(sql)

# we define a string variable called sql, and assignit the command to create the table
sql = 'CREATE TABLE Recipes (pkID INTEGER PRIMARY KEY, name TEXT, serves TEXT, source TEXT)'
cursor.execute(sql)

# create other tables
sql = 'CREATE TABLE Instructions (pkID INTEGER PRIMARY KEY, instructions TEXT, recipeID NUMERIC)'
cursor.execute(sql)

sql = 'CREATE TABLE Ingredients (pkID INTEGER PRIMARY KEY, ingredients TEXT, recipeID NUMERIC)'
cursor.execute(sql)

# create first recipe
sql = 'INSERT INTO Recipes (name, serves, source) VALUES ("Spanish Rice", 4, "Greg Walters")'
cursor.execute(sql)

#find out the value that was assigned to the pkID in the recipe table
sql = "SELECT last_insert_rowid()"
cursor.execute(sql)
for x in cursor.execute(sql):
	lastid = x[0]

sql = 'INSERT INTO Instructions (recipeID, instructions)\
    VALUES (%s, " Brown hamburger. Stir in all other ingredients. Bring to boil. Stir.\n \
Lower to simmer. Cover and cook dor 20 min or until all liquid is absorved.")' % lastid
cursor.execute(sql)

sql = 'INSERT INTO Ingredients (recipeID, ingredients) VALUES (%s, " 1 cup parboiled Rice\n lola")' % lastid
cursor.execute(sql)
