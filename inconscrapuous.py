import bs4
import datetime
import requests
import time


class Scraper:
    """Class to scrape pages"""
    def __init__(self, year_list = [],  article_dict_list = []):
        self.year_list = year_list
        self.article_dict_list = article_dict_list


    def cook_soup(self, url):
        """Scrape the given url and return html as a soup object."""
        r = requests.get(url)
        html = r.content
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup


    def get_articles(self, url):
        """
        Iterate through every page in the blog and find all articles.
        Append the list retreieved from each page to a 2D list; article_sets.

        When there is no 'next' and no 'previous', just scrape that page and stop.
        When there is a 'next' and a 'previous', get the next page, then scrape it.
        When there is no 'next' and a previous, scrape that (last) page and stop.

        e.g. HTML:
              <nav class="pagination">
                <span class="prev">
                  <a rel="previous" href="/page/1">←   Prev</a>
                </span>
                <span class="next">
                  <a rel="next" href="/page/3">Next   →</a>
                </span>
              </nav>
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
            print "next article is {}".format(next_url)
            #  time.sleep(1)  # don't generate too many requests too quickly
        else:
            page_articles = soup.find_all('article', {'class': 'post user_show'})
            article_sets.append(page_articles)
        return article_sets


    def parse_info(self, articles):
        """
        For each article scraped, extract the 1) title, 2) date published (y/m/d),
        and 3) URL. (1) and (3) are formatted into a markdown-style link. Add those
        values to a dict (aricle_dict) and append each dict to the master list
        (article_dict_list)

        Also add the year to the year_list, to be used for generating headings.
        """

        for article in articles:
            try:
                article_title = article('a')[0].getText().encode('utf-8')
                datestring = article('time')[0].get('datetime').encode('utf-8')
                parsed_date = datetime.datetime.strptime(datestring, "%Y-%m-%d")
                month = parsed_date.strftime("%B")
                link = 'http:'+article('a')[0].get('href').encode('utf-8')
                mdown_link = '- [%s](%s)' % (article_title, link)
                year = int(datestring.split('-')[0])

                article_dict = {
                        'link': mdown_link,
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
        for articles in article_sets:
            self.parse_info(articles)

        return self.article_dict_list


    #  def output_toc(self):
    #      self.year_list = sorted(set(year_list)) # Unique and ordered years
    #      current_year = datetime.datetime.now().year
    #      oldest_article_year = self.year_list[0]
    #      year_count = (current_year - oldest_article_year) + 1

    #      output = \
    #              """=================================================================================
    #      || ^^ Here's your archive.  You can copy/paste the output below into its own post
    #      =================================================================================\n"""
    #      print '#Archive'
    #      for number in range(0, year_count+1):  # need to include the current year, so expand year count...kind of dumb)
    #      print '\n##Posts from %i' % (current_year - number)
    #      for d in self.article_dict_list:
    #          if d['year'] == (current_year - number):
    #              print d['link'] + "  " + "*(" + d['date'] + ")*"
    #      print output


