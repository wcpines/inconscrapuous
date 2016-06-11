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
#  time.sleep(1) # don't generate too many requests
#  url = "http://cheesetrees.net/page/{}".format(number)


# Create empty lists by year to hold article components.
# NOTE: This only works for 2015 and 2016.
# Need a better way to do this later.


url = "http://cheesetrees.net"
r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, "html.parser")
articles = soup.findAll('article', {'class': 'post user_show'})

dict_list = []

for article in articles:
    try:
        article_title = article('a')[0].getText().encode('utf-8')
        datestring = article('time')[0].get('datetime').encode('utf-8')
        new = datetime.datetime.strptime(datestring, "%Y-%m-%d")
        month = new.strftime("%B")
        link = 'http:'+article('a')[0].get('href').encode('utf-8')
        mdown_link = '- [%s](%s)' % (article_title, link)
        year = int(datestring.split('-')[0])

        d = {
            'link': mdown_link,
            'date': datestring,
            'year': year
        }
        dict_list.append(d)
    except Exception as e:
        pass


print '#Archive'

print '##Posts from 2016'

for d in dict_list:
    if d['year'] == 2016:
        print d['link'] + "  " + "(" + d['date'] + ")"

print '##Posts from 2015'

for d in dict_list:
    if d['year'] == 2015:
        print d['link'] + "  " + "(" + d['date'] + ")"
