
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup as bs
import requests

link1 = raw_input('enter your link')
link = requests.get(link1)


__URL = "http://maktabkhooneh.org"
__Course = "course/"
__Videos = "videos/"

req = requests.get(link1)

req = req.text
soup = BeautifulSoup(req, 'html.parser')



for link in soup.find_all("a", class_ = "lesson-links"):
    
    link = link.get("href")
    link = __URL + link

    _req = requests.get(link)
    _req = _req.text
    _soup = BeautifulSoup(_req , 'html.parser')
    
    for links in _soup.find_all("a", class_ = "hq-video-dl"):
        links = links.get("href")
        links = __URL + links
        print links
        print '\n'

