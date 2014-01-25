#!/usr/bin/python
#filename: poemscrape
#Author Todd Pollak

#scrapes poems from Nation Poetry Foundation
#returns the html of a poem, author, title, and tags in a json format
# uses requests and BeautifulSoup to do the magic
#used in poetic app at Hack@brown

import requests
from bs4 import BeautifulSoup
import json


#takes in string url and returns json object needed from the poem as strings
def parse_poem(url):
        subj_lst = []
        
        soup = BeautifulSoup(requests.get(url).text)
        author = soup.find('span', attrs={'class': 'author'}).a.string
        title = soup.find('div', attrs={'id': 'poem-top'}).h1.string
        poem_html = soup.find('div', attrs={'class': 'poem'}) #gets html of poem
        
        for x in soup.find_all('p', attrs={'class': "section"}):
                if x.span.string =="Subjects":
                        for y in x.find_all('a'):
                                subj_lst.append(str(y.string))

        if not subj_lst: #no tags, useless
                return "empty"
        return {'title': str(title), 'author' : str(author), 
                        'poem': str(poem_html), 'tags' : subj_lst}        
        

# returns a json dump of poem info, change xrange to get more or less
def crawl_poems():
        poems = []
        for x in xrange(237100, 249800):
                try:
                        temp = parse_poem("http://www.poetryfoundation.org/poem/" 
                                                                        + str(x))
                        if temp != "empty": #only add if tags are present
                                poems.append(temp)
                except:
                        pass

        return json.dumps(poems)  


if __name__ == '__main__':
        print crawl_poems()
