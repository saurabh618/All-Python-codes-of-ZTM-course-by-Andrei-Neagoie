# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:43:42 2020

@author: saura
"""
import requests
from bs4 import BeautifulSoup
import pprint    # pretty print - used to print with appropriate spacing, for readability

url = 'https://news.ycombinator.com/'
res = requests.get(url)

# print(res)    # Response 200 menas everything is good
# print(res.text)    
# this will have the entire html data in it. Exactly the same thing which we get when we click 'View Page Source'

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)
# this will also have the exact same thing as res.text, but it will keep in html format, and not in string format,
# and it will be easier to manupulate it

# print(soup.body)
# print(soup.body.contents)    # result comes in a 'list' in this case. But not with the previous cases.

# print(soup.find_all('div'))
# print(soup.find_all('a'))    # find all the 'a' tags - all the links
# print(soup.title)
# print(soup.a)     # it finds the first a tag
# print(soup.find('a'))    # it finds the first a tag

# print(soup.find(id="score_24273602"))
# print(soup.select("#score_24273602"))   # outputs in a list
# select grabs the data using a CSS selector, where '.' means 'class', '#' means 'id', etc.

# print(soup.select('a')[0])    
# grabs all the 'a' tags, and print only the first one, as this is a list, and we want the 0th item

# print(soup.select(".score")[0])# grabs all the class="score" tags

link = soup.select(".storylink")
# <a class="storylink" href="https://www.bbc.com/news/world-africa-53887947">Africa declared free of wild polio</a>
 
subtext = soup.select(".subtext")
# <span class="score" id="score_24273602">1061 points</span>

li = []

for i in range(len(link)):
    news_link = link[i].get("href", None)    # if the link is not there, the value will be taken as None
    news_title = link[i].getText()
    votes = subtext[i].select(".score")
    if len(votes):
        score = votes[0].getText().split(' ')[0]
    else:
        score = 0
        
    if int(score) > 100:
        li.append((news_title, news_link, int(score)))

li.sort(key = lambda x:x[2], reverse=True)
# li = sorted(li, key =lambda x:x[2], reverse=True)    # same as that of above

pprint.pprint(li)
