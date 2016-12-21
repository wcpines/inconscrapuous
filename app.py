# Do I need to pull all these in?
from flask import Flask, request render_template

@app.route('/', methods=['GET', 'POST'])
    """
    Show the home page with a basic form.  If the user provides a URL to scrape,
    run the scraper
    """
    def homepage():
        error = None  # Default to no error

        if request.method == 'POST':
            if (?) not in request.form['url'] # If the URL doesn't contain some stuff
                error = "Sorry, please provide a valid URL to page hosted on svbtle"
                return render_template('?', error=error) # error template tbd?  robably will just pass the error to Javascript
            else
                return scrape_the_page(request.form['url'] ) # method should be a service object?

        else

            return render_template('home')

