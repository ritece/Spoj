from bs4 import BeautifulSoup
import urllib2
import re
spojUrl = 'http://www.spoj.com/problems/tags'
f = urllib2.urlopen(spojUrl)
html = f.read()
soup = BeautifulSoup(html)

tagList = soup.find_all('a',{'href':re.compile('^/problems/tag/[\w\W]*')})
	
for tag in tagList:
	print tag.get_text()
