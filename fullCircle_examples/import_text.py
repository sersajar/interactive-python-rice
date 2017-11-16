import urllib
from BeautifulSoup import *

url = "http://www.thegeekstuff.com/2009/09/the-ultimate-wget-download-guide-with-15-awesome-examples/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
	script.extract()    # rip it out

# get text
text = soup.getText()

# break into lines and remove leading and trailing space on each
lines = [line.strip() for line in text.splitlines()]
# break multi-headlines into a line each
chunks = [phrase.strip() for line in lines for phrase in line.split(" ")]
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print text
