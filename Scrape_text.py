"""
This is a program that performs Web Scraping for text.
It extracts all text in given webpage and saves it to input.txt.
"""

import urllib.request as req
from bs4 import BeautifulSoup as Soup
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()




print(__doc__)

url = input("Enter the URL that you want to scrape ")


request = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = req.urlopen(request)

parsed_url = urlparse(url)
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
domain = domain[:-1]

page = response.read().decode('utf-8')
res = Soup(page, "html.parser")
html = res.find_all(["p","h1","h2","h3","h4","h5","h6","strong"])
text=strip_tags(str(html))

file=open( "input.txt", "w")
file.write(text.strip())
file.close()