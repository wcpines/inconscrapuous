This script provides a much needed feature for the Svbtle blogging platform:  Generate an ordered list of all of your posts for an easily browsable archive.

Inconscrapuous uses Python's Beautiful Soup [library](https://www.crummy.com/software/BeautifulSoup/) to scrape your Svbtle blog and print a markdown document that displays your article titles with links and dates for each entry.  You can then post this document as its own post (`YourBlogDomain.com/archive`) and link to it as appropriate. 

**Caveats:**

- This script prints to `stdout`, but you can run it through `pbcopy` for convenience.  Just discard the message at the end: 

```sh
python inconscrapuous.py | pbcopy
```

- Svbtle has weird pagination that may cause some pages to be dropped or duplicated.  I recommend scanning your result for dupes.


