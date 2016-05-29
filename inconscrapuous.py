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

# - [X]Using the soup object, get the articles
# - Loop through each article. 
  # - [X]Get date
  # - [X]Get id
  # - [X]Get article_title
  # - [X]Get link

# - [ ]Create list of dict (split lists by year here?)
# - [ ]Transform datefrom 2016/4/01 to [Month name], [Year]
# [ {id : date, article_title, link} ]

# For x in dict_list 

articles = soup.findAll('article', {'class':'post user_show'})

for article in articles:
  id = article.get('id')
  date = article('time')[0].get('datetime').encode('utf-8')
  link = article('a')[0].get('href').encode('utf-8')
  article_title = article('a')[0].getText().encode('utf-8')
  full_url = protocol + link

for article_title in title_list:
  print article_title

protocol = 'http:'
mdown_link = '1. [%s](%s)' % (article_title,full_url)
title_list.append(mdown_link.strip("'"))


"""
*--final formatting--*
#Archive 

##Posts in [year]

###Month 1

-Article link 
-Article link 

###Month 2

-Article link 
-Article link 
"""

