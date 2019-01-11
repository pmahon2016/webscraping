import requests
from bs4 import BeautifulSoup as BS
import re

with open('webresults.html','w') as webfile:

    r = requests.get('https://www.newyorktimes.com')

    print(r.status_code)

    # print(r.content)

    soup = BS(r.content, 'html.parser')

    my_results = soup.prettify()

    # print(my_results)

    # for link in soup.find_all('a'):
    #     print(link.get('href'))

    webfile.write(my_results)

    p = re.compile(r'Kardashian')

    match = re.findall(p, my_results)

    #
    print(len(match))

    for line in match:
        print(line)

