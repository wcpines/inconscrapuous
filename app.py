# Do I need to pull all these in?
from flask import Flask, request, render_template
#  import inconscrapuous

app = Flask(__name__)

#  @app.route('/', methods=['GET', 'POST'])
#      """
#      Show the home page with a basic form.  If the user provides a URL to scrape,
#      run the scraper
#      """

#      def homepage():
#          error = None  # Default to no error

#          if request.method == 'POST':
#              if (?) not in request.form['url'] # If the URL doesn't contain some stuff
#                  error = "Sorry, please provide a valid URL to page hosted on svbtle"
#                  return render_template('?', error=error) # error template tbd?  robably will just pass the error to Javascript
#              else
#                  return scrape_the_page(request.form['url'] ) # method should be a service object?

#          else

#              return render_template('home')

@app.route('/')
def hello():
    return render_template('hello.html', thing='thang')

if __name__ == '__main__':
    app.run()

@app.route('/', method='POST')
def hello():
    #  url = request.form.get("some_var")
    #  info = inconscrapuous.get_parsed_articles(url)
    return render_template('hello.html')# , info=info)

if __name__ == '__main__':
    app.run()


# Flow:
#  - Homepage
#  - Submit URL
#  - Check that URL has protocol
#  - Check that the site is actually svbtle
#      'svbtle' in requests.content == True
#  - Parse the URL into content
