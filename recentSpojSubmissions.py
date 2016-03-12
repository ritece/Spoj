import urllib2
from bs4 import BeautifulSoup 
import re

'''
This program will ask for the spoj username and then fetch the content from the 
url - http://www.spoj.com/status/userName/all

Each submission is grouped with the tag, tr and class name is like "kol" or "kol2 ".

So, after getting the html for a particular page, the data under each of the "tr" tag with class name starting with "Kol" has to be parsed.

For this regular expression -> "^kol[0-9a-zA-Z ]*"
is used.
'''

regex = "^kol[\w ]*"
userName = raw_input('Enter the spoj username for the user you want to fetch the submissions : ')

spojUrl = 'http://www.spoj.com/status/'+userName+'/all'

#Spoj displays 20 submissions per page, the data is paginated.
# there is a 'ul' tag with class 'pagination' which displays the horizontal bar with numbers, used to navigate for submissions.
#the horizontal bar has "less than" button, to navigate to the first page
#"Previous" button to navigate to the previous page
# numbered links which are from 1 to 5, giving the history of 100 recent submissions 
# "Next" button to navigate to the next page of submissions
#"greater thna" button to the last 81-100 recent submissions

x = urllib2.urlopen(spojUrl)
#x = open('test.html','r')
html = x.read()
soup = BeautifulSoup(html)
listOfSubmission = soup.find_all('tr',re.compile(regex))
successfulSubmissions = []
for submission in listOfSubmission:
	#check if it was a successful submission
        #based on the observation that the successful submission have a "status" code of '15'
	submissionResultStatusCode = submission.find_all('td', class_='statusres text-center')[0]['status']
	if submissionResultStatusCode == '15':
		problemCode = submission.find_all('td', class_ = 'sproblem text-center')[0].a['title']
		problemName = submission.find_all('td', class_ = 'sproblem text-center')[0].a.get_text()
		successfulSubmissions.append((problemCode, problemName))
x.close()

print successfulSubmissions
