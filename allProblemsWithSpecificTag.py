from bs4 import BeautifulSoup
import urllib2
import re
tag = raw_input('Enter the tag of the problem to fetch all problems of this type - ')

spojUrl = 'http://www.spoj.com/problems/tag/'+tag
f = urllib2.urlopen(spojUrl)
html = f.read()
#html = open('test.html','r').read()
soup = BeautifulSoup(html)

problemsList = soup.find_all('tbody')[0].find_all('a', {'href':re.compile('^/problems/[/w/W]*')})

problemsDict = {}
for problem in problemsList:
	problemCode = problem["href"][10:]
	problemName = problem.get_text()
	problemsDict[problemCode] = problemName

print problemsDict
