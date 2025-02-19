import requests
from bs4 import BeautifulSoup

class ExtractData:
    
    def __init__(self, url):
        self.url = url
        
    def connect(self):
        r = requests.get(self.url, auth=("user", "pass"))
        return r.status_code

class Main:
    
    def __init__(self, url):
        self.extractor = ExtractData(url)
        
    def pr(self):
        status = self.extractor.connect()
        print(status)