"""
This is a program that performs perform Web Scraping for links.
It identifies all <a> tags and writes the links present in href attribute to a HTML file called scroutput.html.
"""

import urllib.request as req
from urllib.parse import urlparse

from bs4 import BeautifulSoup as Soup

print(__doc__)

url = input("Enter the URL that you want to scrape ")

request = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = req.urlopen(request)

parsed_url = urlparse(url)
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
domain = domain[:-1]

page = response.read().decode('utf-8')
res = Soup(page, "html.parser")
links = res.find_all("a")

filename = "scroutput.html"
fileout = open(filename, "w")

items = []
t = 0

for link in links:
    li = str(link.get("href")).strip()
    if li != "":
        if li[0] == '/' or li[0] == '?':
            if len(li) > 1:
                d = domain
            else:
                continue
        else:
            d = ""
        if t == 0:
            i = 1
        if li not in ["None", "none", "javascript:void(0);", "javascript:void(0)", domain, domain + "/"] \
                and li[0] != '#':
            items.append(str(i) + ".  " + "<a href=\"" + d + li + "\"> " + d + li + "</a> <br>")
            t = 1
        i += 1

html = "<!DOCTYPE html> " \
       " <head>  <title> Links </title> </head>" \
       " <body>  URL: <a href=\"" + url + "\"> " + url + " </a> <br> <br>" + ''.join(items) + " </body>  </html>"

fileout.writelines(html)
fileout.close()

print(str(i - 1) + " URLs successfully saved to " + filename)

input('Press ENTER to exit')
