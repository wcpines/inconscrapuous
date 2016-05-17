# import modules
import requests
import bs4
import csv
import time

# create empty list to hold all dictionaries.
title_dict_list = []

# TODO: 
 # Check if blog spans multiple pages.(Check for <span class="last"> for full range.)
 # If it does, loop through and pull all of them:


# for number in range(1,[last_page]):
#     time.sleep(1) # don't generate too many requests
#     url = "http://cheesetrees.net/page/{}".format(number)


url = "http://cheesetrees.net"

r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, "html.parser")
articles = soup.findAll('h1', {'class': "article_title"})

# for a in articles.findAll('h1', {'class': "article_title"})

for article in articles:
    text = article.getText().rstrip()

    if len(text) > 0:
        article_title = text.encode('utf-8')
        # Transform and Store the data in dictionary format.
        d = {'article_title': article_title, 'link': 'test'}
        title_dict_list.append(d)

# with open('Blog Archive', 'w') as text_file:
