# Do I need to pull all these in?
from IPython import embed
from inconscrapuous import Scraper
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.jinja_env.cache = None
app.secret_key = 'some_secret'

@app.route('/test')
def test():
    if request.method == 'GET':
        return render_template('test.html')

@app.route('/')
def home():
    """
    Show the home page with a basic form. If homepage reached due to a redirect
    (i.e. an error) then prevent logo from animating.
    """

    if request.args.getlist('err'):
        animation = "shake"
    else:
        animation = "bigEntrance"

    return render_template('home.html', animation = animation)

@app.route('/scrape', methods=['GET','POST'])
def scrape():
    if request.method == 'GET':
        return redirect(url_for('home'))
    else:
        url = request.form.get("url").strip().lower() # normalize form input
        scraper = Scraper()
        try:
            scraper.get_parsed_articles(url)
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('home', err = 't'))
        else:
            article_dicts = scraper.article_dict_list
            year_info = scraper.year_info()
            return render_template('toc.html', article_dicts = article_dicts, year_info = year_info, animation="")


if __name__ == '__main__':
    app.run(debug=True)

