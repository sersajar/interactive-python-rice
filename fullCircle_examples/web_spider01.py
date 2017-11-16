import urllib, re, sys
"""script para ver los enlaces de una web"""
url = str(sys.argv[1])  # equivale al 1er argumento pasado, en este caso una URL
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)

for link in links:
	print link

print 'Argument list:', str(sys.argv)
