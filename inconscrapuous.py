# import modules
import requests
import bs4
import time
import datetime

# TODO: 
# 1. Get date of last post on last page, make "posts from" year go until that posts year
# 2. Refactor garbarge lines
# 3. Fix Markdown formatting

range_url = "https://j2kun.svbtle.com/"

r = requests.get(range_url)
html = r.content
soup = bs4.BeautifulSoup(html, "html.parser")

# this can't be the right way to get this...
page_count = int(soup.findAll('span', {'class': 'last'})[0]('a')[0].get('href').encode('utf-8').split('/')[2])

for number in range(1, page_count):
    time.sleep(1)  # don't generate too many requests
    full_url = "https://j2kun.svbtle.com/page/{}".format(number)

    dict_list = []

    articles = soup.findAll('article', {'class': 'post user_show'})
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

current_year = datetime.datetime.now().year

print '##Posts from %i' % current_year

for d in dict_list:
    if d['year'] == current_year:
        print d['link'] + "  " + "(" + d['date'] + ")"

print '##Posts from %i' % (current_year - 1)

for d in dict_list:
    if d['year'] == (current_year - 1):
        print d['link'] + "  " + "(" + d['date'] + ")"

print '##Posts from %i' % (current_year - 2)

for d in dict_list:
    if d['year'] == (current_year - 2):
        print d['link'] + "  " + "(" + d['date'] + ")"
