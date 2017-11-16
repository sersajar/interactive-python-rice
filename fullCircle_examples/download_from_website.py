import urllib

num = 40
while True:
	name = 'issue%s' % str(num)
	try:
		urllib.urlretrieve("http://dl.fullcirclemagazine.org/%s_en.pdf" % name, "%s_en.pdf" % name)
		num += 1
	except:
		print 'there is no more files'
		exit()