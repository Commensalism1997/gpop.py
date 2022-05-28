import requests
from html.parser import HTMLParser
from collections import namedtuple
"""Module that will help you collect data from GPOP"""
GPopUserData = namedtuple('GPopUserData', ('level', 'time', 'played', 'created', 'views', 'coins', 'gbobs'))
class _ProfileParser(HTMLParser):
    """Internal class used for collecting data from profiles"""
    def __init__(self):
        super().__init__()
        self._found = False
        self._data = []
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'class' and attr[1] in ('topbar2-cat-value', 'topbar2-cat-value gshopcoin2'):
                self._found = True
    def handle_data(self, data):
        if self._found:
            self._data.append(data)
    def handle_endtag(self, tag):
        self._found = False

class _HOFParser(HTMLParser):
    """Internal class used for collecting data from Hall of Fame"""
    def __init__(self):
        super().__init__()
        self._found = False
        self._data = []
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'class' and attr[1] == 'leaderboard-entry-username':
                self._found = True
    def handle_data(self, data):
        if self._found:
            self._data.append(data)
    def handle_endtag(self, tag):
        self._found = False

def get_data(user : str) -> GPopUserData:
    page = requests.get(f'https://gpop.io/profile/@{user}').text
    parser = _ProfileParser()
    parser.feed(page)
    data = GPopUserData(*parser._data)
    return data
def get_HOF() -> tuple:
    page = requests.get('https://gpop.io/halloffame').text
    parser = _HOFParser()
    parser.feed(page)
    return (tuple(parser._data[0:50]), tuple(parser._data[50:]))
