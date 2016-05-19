# import modules
import requests
import bs4
import time

# create empty list to hold all dictionaries.
title_dict_list = []

"""
TODO: 
 1. Check if blog spans multiple pages.(Check for <span class="last"> 
 for full range.  If it does, loop through and pull all of them.
 2. Sort by post date: 
  <time datetime="2016-04-30" class="article_time"> Apr 30, 2016</time>
"""

# for number in range(1,[last_page]):
#     time.sleep(1) # don't generate too many requests
#     url = "http://cheesetrees.net/page/{}".format(number)


url = "http://cheesetrees.net"

r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, "html.parser")

# links = soup.findAll()('a', href=True)

articles = soup.findAll('h1', {'class': "article_title"})
for article in articles:
    text = article.getText().rstrip(  )
    link = article.test

    if len(text) > 0:
        article_title = text.encode('utf-8')
        # Transform and Store the data in dictionary format.
        d = {'article_title': article_title, 'link': 'test'}
        title_dict_list.append(d)

# with open('Blog Archive', 'w') as text_file:
