# import modules
import requests
import bs4
import time
import datetime


"""
TODO: 
1. Check if blog spans multiple pages.(Check for <span class="last"> 
 for full range.  If it does, loop through and pull all of them.
2. Generate markdown file 
"""

# for number in range(1,[last_page]):
#     time.sleep(1) # don't generate too many requests
#     url = "http://cheesetrees.net/page/{}".format(number)


# Create empty lists by year to hold article components. NOTE: This only works for 2015 and 2016.  
# Need a better way to do this later.
tf_posts = []
ts_posts = []


url = "http://cheesetrees.net"
r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, "html.parser")

articles = soup.findAll('article', {'class':'post user_show'})

for article in articles:
  try:

    # Get the elements of the article that you need
    id = article.get('id') # get the article ID
    article_title = article('a')[0].getText().encode('utf-8') # get the article title
    datestring = article('time')[0].get('datetime').encode('utf-8') # get the datetime--it returns a sting
    datetime = datetime.datetime.strptime(datestring, "%Y-%m-%d") # get the datestring to an actual datetime data type
    month = new.strftime("%B") # get the month name from it
    link = 'http:'+article('a')[0].get('href').encode('utf-8') # get the anchor link, append protocol 
    mdown_link = '1. [%s](%s)' % (article_title,link) # create markdown hyperlink using href and title text
    year = int(datestring.split('-')[0])
    if year == 2016:
      ts_posts.append(mdown_link.strip("'") + ';' + month)
    elif year == 2015:
      tf_posts.append(mdown_link.strip("'") + ';' + month)
    else:
      print "%s didn't have a recent year" % (article_title)

    for post in tf_posts:
      print post
    
    for post in ts_posts:
      print post

  except Exception as e:
      pass

