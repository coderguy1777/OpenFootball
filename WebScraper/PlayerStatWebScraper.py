import urllib3
from json import *
import http
import aiohttp
import webbrowser

class WebScrap:
    def __init__(self, nameofplayer):
        self.nameofplayer = nameofplayer
        self.playerstats = {}
