import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib3

http = urllib3.PoolManager()
url = 'https://www.giants.com/team/stats/'

rep = requests.get(url)
soup = BeautifulSoup(rep.content, "html.parser")

for links in soup.find_all('a'):
    print(links.get('href'))
    if links.get('href') == '/team/players-roster/':
        print(links.get('href'))