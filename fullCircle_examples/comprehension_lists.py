# create a list of numbers from 0 to 9
nums = []
for n in range(10):
	nums.append(n)
print "create a list of numbers from 0 to 9"
print nums

# the same list with compr.lists
nums1 = [n for n in range(10)]
print nums1
print

#  create a list of square numbers
squares = []
for square in range(10):
	squares.append(square**2)
print "create a list of square numbers"
print squares

# the same. Just remember the syntax: [ expression for item in list if conditional ]
squares1 = [square**2 for square in range(10)]
print squares1
print

# Multiply every part of a list by three and assign it to a new list.
list1 = [3, 4, 5]
multiplied = [num*3 for num in list1]
print "Multiply every part of a list by three"
print multiplied

multiplied2 = []
list2 = [3, 4, 5]
for num in list2:
	multiplied2.append(num*3)
print multiplied2
print

# create a list of odd numbers using if condition
numbers = [1,2,3,4,5,6,7,8,9,10]

odds = []
for num in numbers:
	if num % 2 == 1:
		odds.append(num)
print "create a list of odd numbers using if condition"
print odds

odds2 = [num for num in numbers if num % 2 == 1]
print odds2
print

# Show the first letter of each word
list_of_words = ["this", "is", "a", 'list', 'of', 'words']
firs_letters = [word[0] for word in list_of_words]
print "Show the first letter of each word"
print firs_letters

firs_letters2 = []
list_of_words2 = ["this", "is", "a", 'list', 'of', 'words']
for word in list_of_words2:
	firs_letters2.append(word[0])
print firs_letters2
print
