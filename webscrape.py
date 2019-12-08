import requests  # requests lib
from bs4 import BeautifulSoup as BS  # don't need all of BeautifulSoup
import re

with open('webresults.html', 'w') as savefile:
    r = requests.get('https://www.yahoo.com')
    print(r.status_code)

    soup = BS(r.content, 'html.parser')

    texthtml = (soup.get_text())

    my_result = soup.prettify()

    savefile.write(my_result)

    p = re.compile(r'news[^\<|\>]{100}')

    match = re.findall(p, texthtml)

print(len(match))
for i in match:
    print(match)

