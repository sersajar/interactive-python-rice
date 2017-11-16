class Dog():
	def __init__(self, dogname, dogcolor, dogheight, dogbuild, dogmood, dogage):
		self.name = dogname
		self.color = dogcolor
		self.height = dogheight
		self.build = dogbuild
		self.mood = dogmood
		self.age = dogage
		self.Hungry = False
		self.Tired = False

	def eat(self):
		if self.Hungry:
			print 'yum yum'
			self.Hungry = False
		else:
			print 'Sniff'

	def sleep(self):
		print 'ZZZZZZZZZZZZZZZZZZZZZ'
		self.Tired = False

	def bark(self):
		if self.mood == 'Grumpy':
			print 'GRRRRRRR bup bup'
		elif self.mood == 'Laid back':
			print 'yaw...ok...wof'
		elif self.mood == 'Crazy':
			print 'bark bark bark bark'
		else:
			print 'wof wof'


Beagle = Dog('kuma', 'gris', 'alto', 'fuerte', 'Crazy', 2)
print 'My name is %s' % Beagle.name
print 'My color is %s' % Beagle.color
print 'My mood is %s' % Beagle.mood
print 'I am hungry = %s' % Beagle.Hungry
Beagle.eat()
Beagle.Hungry = True
Beagle.eat()
Beagle.bark()
