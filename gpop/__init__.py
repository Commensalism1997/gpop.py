import requests
from html.parser import HTMLParser
"""Module that will help you collect data from GPOP"""
class _ProfileParser(HTMLParser):
    """Internal class used for collecting data from profiles"""
    def __init__(self):
        super().__init__()
        self._foundc = False
        self._foundl = False
        self.coins = None
        self.level = None
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'class' and attr[1] == 'topbar2-cat-value gshopcoin2':
                self._foundc = True
    def handle_data(self, data):
        if self._foundc:
            self.coins = int(data)
    def handle_endtag(self, tag):
        self._foundc = False
        self._foundl = False
def get_coins(user : str) -> int:
    page = requests.get(f'https://gpop.io/profile/@{user}').text
    parser = _ProfileParser()
    parser.feed(page)
    return parser.coins
    
