# import modules
import requests
import bs4
import time

# create empty list to hold all dictionaries.
title_list = []

"""
TODO: 
1. Check if blog spans multiple pages.(Check for <span class="last"> 
 for full range.  If it does, loop through and pull all of them.
2. Generate markdown file 
3. Sort by post date: 
  <time datetime="2016-04-30" class="article_time"> Apr 30, 2016</time>
"""

# for number in range(1,[last_page]):
#     time.sleep(1) # don't generate too many requests
#     url = "http://cheesetrees.net/page/{}".format(number)


url = "http://cheesetrees.net"

r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, "html.parser")


articles = soup.findAll('h1', {'class': "article_title"})
for article in articles:
    text = article.getText().strip('\n')
    link = article('a')[0].get('href').encode('utf-8')
    protocol = 'http'
    full_url = protocol + link

    if len(text) > 0:
        article_title = text.encode('utf-8')
        mdown_link = '1. [%s](%s)' % (article_title,full_url)
        title_list.append(mdown_link.strip("'"))

for title in title_list:
  print title
