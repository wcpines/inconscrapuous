# Do I need to pull all these in?
from IPython import embed
from inconscrapuous import Scraper
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.jinja_env.cache = None
app.secret_key = 'some_secret'

@app.route('/')
def home():
    """Show the home page with a basic form."""
    embed()
    return render_template('home.html', animation = "bigEntrance")

@app.route('/scrape', methods=['POST'])
def scrape():
    """When the user provides a URL, run the scraper and redirect to the TOC page."""
    url = request.form.get("url").strip().lower() # normalize form input
    if url and "http://" in url:
        error = None
        scraper = Scraper()
        scraper.get_parsed_articles(url)
        article_dicts = scraper.article_dict_list
        year_info = scraper.year_info()
        return render_template('toc.html', article_dicts = request.args.get('article_dicts'), year_info = request.args.get('year_info'), animation="")
    else:
        error = "Please provide a valid URL"
        flash(error)
        return redirect(url_for('home'), animation = None)

if __name__ == '__main__':
    app.run(debug=True)


# QUESTIONS/TODO:
    #  - Throwing erros?
    #      - URL missing
    #      - URL invalid
    #  - Cache busting properly
    #  - Using JS in another template to preview markdown
    #  - Make button correct size
    #  - Make compatible with FF and GC


