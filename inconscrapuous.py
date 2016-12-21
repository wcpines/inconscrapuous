import bs4
import datetime
import requests
import time

# URL of blog to be scraped
blog_url = raw_input('Svbtle blog Url (include protocol)>>> ')

# list for holding article key-value info defined in `d`, L.37
post_dict_list = []

# list for determining oldest posts year, see L74
year_list = []

# define a function for getting the blog html in a soup object
def cook_soup(url):
    r = requests.get(url)
    html = r.content
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup

# define function for extracting article info and dumping into dicts / lists
def parse_info(articles):
    for article in articles:
        try:
            article_title = article('a')[0].getText().encode('utf-8')
            datestring = article('time')[0].get('datetime').encode('utf-8')
            parsed_date = datetime.datetime.strptime(datestring, "%Y-%m-%d")
            month = parsed_date.strftime("%B")
            link = 'http:'+article('a')[0].get('href').encode('utf-8')
            mdown_link = '- [%s](%s)' % (article_title, link)
            year = int(datestring.split('-')[0])

            post_dict = {
            'link': mdown_link,
            'date': datestring,
            'year': year
            }
            post_dict_list.append(post_dict)
            year_list.append(year)

        except Exception as e:
            pass


# Check if the blog spans multiple pages.
soup = cook_soup(blog_url)
last_one = soup.findAll('span', {'class': 'last'})

# If it doesn't just grab the info from the first page.
if not last_one:
    articles = soup.findAll('article', {'class': 'post user_show'})
    parse_info(articles)

# TODO: This next loop is duplicating page 22, skipping 23, and getting 24.
# This appears be an issue with Svbtle's pagination.  Try editing URL manually
# to see issue

else:
    page_count = int(last_one[0]('a')[0].get('href').encode('utf-8').split('/')[2])
    alist = []
    for number in range(1, page_count + 1):  # include the last page
        full_url = blog_url + "/page/{}".format(number)
        soup = cook_soup(full_url)
        articles = soup.findAll('article', {'class': 'post user_show'})
        alist.append(articles) # add page's article set to list--2D array
        time.sleep(1)  # don't generate too many requests too quickly


    for articles in alist:
        parse_info(articles)

# Loop for appropriate number of headings  to determine number of year headings
current_year = datetime.datetime.now().year
oldest_post_year = sorted(year_list)[0]
year_count = (current_year - oldest_post_year) + 1

output = \
"""=================================================================================
|| ^^ Here's your archive.  You can copy/paste the output below into its own post
=================================================================================\n"""
print '#Archive'
for number in range(0, year_count):  # need to include the current year, so expand year count...kind of dumb)
    print '\n##Posts from %i' % (current_year - number)
    for post_dict in post_dict_list:
        if post_dict['year'] == (current_year - number):
            print post_dict['link'] + "  " + "*(" + post_dict['date'] + ")*"

print output

