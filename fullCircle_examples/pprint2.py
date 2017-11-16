# pprint.oy
# exapmle of semi-useful functions


def toporbottom(character, width):
	# width is total width of returned line
	return '%s%s%s' % ('+', (character * (width-2)), '+')


def fmt(val1, leftbit, val2, rightbit):
	# prints two values padded with spaces
	# val1 is thing to print on left, val2 is thing to print on right
	# leftbit is width of left portion, rightbit is width of right portion
	part2 = '%.2f' %val2
	return '%s%s%s%s' % ('| ',val1.ljust(leftbit-2,' '),part2.rjust(rightbit-2,' '),' |')

# define the price of each item
# item1 = 3.00
# item2 = 15.00
itms = [['Soda', 1.45], ['Cookies', 2.75], ['Bread', 0.90], ['Milk', 2.30]]

# now print everything out...
print toporbottom('=', 40)

total = 0
for itm in range(len(itms)):
	print fmt(itms[itm][0], 30, itms[itm][1], 10)
	total += itms[itm][1]
print toporbottom('-', 40)
print fmt('Total', 30, total, 10)
print toporbottom('=',40)
