# import modules
import requests
import bs4
import time


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
    id = article.get('id')
    article_title = article('a')[0].getText().encode('utf-8')
    date = article('time')[0].get('datetime').encode('utf-8')
    link = 'http:'+article('a')[0].get('href').encode('utf-8')
    mdown_link = '1. [%s](%s)' % (article_title,link)
    year = int(date.split('-')[0])
    month = date.split('-')[1]
    if year = 2016
      ts_posts.append(mdown_link.strip("'"))
    elif year = 2015
      tf_posts.append(mdown_link.strip("'"))
    else 
      continue "%s didn't have a recent year" % (article_title)



    if month == '1':
      month_name == 'January'
    elif month == '2':
      month_name == 'February'
    elif month == '3':
      month_name == 'March'
    elif month == '4':
      month_name == 'April'
    elif month == '5':
      month_name == 'May'
    elif month == '6':
      month_name == 'June'
    elif month == '7':
      month_name == 'July'
    elif month == '8':
      month_name == 'August'
    elif month == '9':
      month_name == 'September'
    elif month == '10':
      month_name == 'October'
    elif month == '11':
       month_name == 'November'
    elif month == '12':
      month_name == 'December'

    ad = {
      'title': article_title,
      'month': month_name
    }
    print ad

  except Exception as e:
      pass



print mdown_link

    

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

