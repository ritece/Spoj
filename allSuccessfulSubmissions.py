import urllib2
from bs4 import BeautifulSoup 
import re

'''
This program will ask for the spoj username and then fetch the content from the 
url - http://www.spoj.com/users/userName/

'''

userName = raw_input('Enter the spoj username of a user to know the number of problems they have solved : ')

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

print userName+ ' has solved',len(listOfSolvedProblemCodes),'problems on Spoj.'


