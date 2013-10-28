#! usr/env/python
#scrapes the top ten links of HN and runs them through
#the alchemy API

import requests
from bs4 import BeautifulSoup
alch_auth = "" #get your own damn key





#takes in BeautifulSoup object
#returns a list of the top ten links on Hacker news
#change count to get more links
def get_top10(hacker_soup):
	top_ten = []
	count = 0
	for link in hacker_soup.find_all("a"):
		if "http" in link.get("href"):
			top_ten.append(link.get("href"))
			count += 1
		if count == 11:
			top_ten.pop(0)
			return top_ten


#takes in a url as a string
#returns a json string of the of the most important words in the article
#makes restful call the Alchemy API
def get_keywords(url):
	rank_keywords = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey="
	alch_r = requests.get(rank_keywords + alch_auth +"&outputMode=json&maxRetrieve=10&url=" + url)
	return alch_r.text
	

#eventually script will add the data to a mongoDB
if __name__ == '__main__':
	soup = BeautifulSoup(requests.get("https://news.ycombinator.com/").text)
	data = []
	for links in get_top10(soup):
		data.append(get_keywords(links))
	print data





