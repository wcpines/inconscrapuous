import bs4
import datetime
import requests
import time
import re

class Scraper:
    """Instantiate object to scrape pages"""
    def __init__(self, year_list = None,  article_dict_list = None):
        # Avoid duplication between instantiations
        #  http://stackoverflow.com/a/31798559/4667820
        if year_list is None:
            self.year_list = []
        if article_dict_list is None:
            self.article_dict_list = []


    def cook_soup(self, url):
        """
        Scrape the given url and return html as a soup object.  If a valid
        svbtle blog url is not provided, raise exceptions which can be used in
        flash messages to the user.
        """
        if re.compile('http').search(url) is None:
            raise Exception('Please provide a valid URL')
        try:
            r = requests.get(url)
        except Exception as e:
            raise Exception('Sorry, blog not found') # Handle all other exceptions the same
        if r.status_code is not 200:
            raise Exception('Sorry, blog not found')
        html = r.content
        if 'svbtle' not in html:
            raise Exception('URL does not resolve to a Svbtle Blog')
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup


    def get_articles(self, url):
        """
        Iterate through every page in the blog and find all articles.  Append
        the list retreieved from each page to a 2D list; article_sets.

        When there is no 'next' and no 'previous', just scrape the current page
        and stop.  When there is a 'next' and a 'previous', get the next page,
        then scrape it.  When there is no 'next' but there is a previous,
        scrape that (last) page and stop.
        """
        soup = self.cook_soup(url)
        article_sets = []
        while (len(soup.find_all('a', {'rel': 'next'})) > 0 and
               len(soup.find_all('a', {'rel': 'prev'})) < 1):
            next_page_path = soup.find('a', {'rel': 'next'}).get('href').encode('utf-8')
            page_articles = soup.find_all('article', {'class': 'post user_show'})
            article_sets.append(page_articles)
            next_url = url + next_page_path
            soup = self.cook_soup(next_url)
            print "scraping page {}".format(next_url)
        else:
            page_articles = soup.find_all('article', {'class': 'post user_show'})
            article_sets.append(page_articles)
            return article_sets


    def parse_first_article_info(self, article):
        """
        Handles the most recent article in the blog. On the homepage, this
        article does not have a date available, so it must be parsed and
        formatted for the archive separately.
        """
        article_title = article('a')[0].getText().encode('utf-8')
        link = 'http:'+article('a')[0].get('href').encode('utf-8')
        mdown_link = '[%s](%s)' % (article_title, link)

        first_article_dict = {
            'link': mdown_link.decode('utf-8')
        }
        self.article_dict_list.append(first_article_dict)


    def parse_info(self, articles):
        """
        For each article scraped, extract the 1) title, 2) date published
        (y/m/d), and 3) URL. (1) and (3) are formatted into a markdown-style
        link. Add values to a dict (aricle_dict) and append each dict to the
        master list (article_dict_list). Add the year to the year_list, to be
        used for generating headings.
        """

        for article in articles:
            try:
                article_title = article('a')[0].getText().encode('utf-8')
                datestring = article('time')[0].get('datetime').encode('utf-8')
                parsed_date = datetime.datetime.strptime(datestring, "%Y-%m-%d")
                month = parsed_date.strftime("%B")
                link = 'http:'+article('a')[0].get('href').encode('utf-8')
                mdown_link = '[%s](%s)' % (article_title, link)
                year = int(datestring.split('-')[0])

                article_dict = {
                    'link': mdown_link.decode('utf-8'),
                    'date': datestring,
                    'year': year
                }
                self.article_dict_list.append(article_dict)
                self.year_list.append(year)

            except Exception as e:
                pass

    def get_parsed_articles(self, url):
        """
        Calls each other method above to get the articles and iterates over the
        list to populate the dictionary list and list of years.
        """

        article_sets = self.get_articles(url)

        most_recent_article = article_sets[0].pop(0)
        self.parse_first_article_info(most_recent_article)

        for articles in article_sets:
            self.parse_info(articles)

        return (self.article_dict_list)


    def year_info(self):
        current_year = datetime.datetime.now().year
        oldest_article_year = min(self.year_list)
        newest_article_year = max(self.year_list)
        return {
            #  "current_year": current_year,
            "oldest_article_year": oldest_article_year,
            "newest_article_year": newest_article_year
        }
