from bs4 import BeautifulSoup
import urllib2
import re
tag = raw_input('Enter the tag of the problem to fetch all problems of this type - ')

spojUrl = 'http://www.spoj.com/problems/tag/'+tag
f = urllib2.urlopen(spojUrl)
html = f.read()
soup = BeautifulSoup(html)

problemsList = soup.find_all('tbody')[0].find_all('a', {'href':re.compile('^/problems/[/w/W]*')})

problemsDict = {}
for problem in problemsList:
	problemCode = problem["href"][10:]
	problemName = problem.get_text()
	problemsDict[problemCode] = problemName


'''
This program will ask for the spoj username and then fetch the content from the 
url - http://www.spoj.com/users/userName/

'''

userName = raw_input('Enter the spoj username : ')

spojUrl = 'http://www.spoj.com/users/'+userName


x = urllib2.urlopen(spojUrl)
html = x.read()
soup = BeautifulSoup(html)
listOfSuccessfulSubmission = soup.find_all('table', class_='table table-condensed')[0].find_all('td')
listOfSolvedProblemCodes = []
for submission in listOfSuccessfulSubmission:
	problemCode = submission.get_text()
	if problemCode:
		listOfSolvedProblemCodes.append(problemCode)

#print len(listOfSolvedProblemCodes)
#print len(problemsDict)
#print userName+ ' has solved',len(listOfSolvedProblemCodes),'problems on Spoj.'
unsolvedProblems =set([item for item in problemsDict]).difference(set(listOfSolvedProblemCodes))

print 'there are '+str(len(unsolvedProblems))+' problems left to be solved under the '+tag+' category'

#print unsolvedProblems
