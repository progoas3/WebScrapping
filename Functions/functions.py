import requests
from bs4 import BeautifulSoup

class ExtractData:
    
    def __init__(self, url, tag):
        self.url = url
        self.tag = tag
        
    def getTitle(self, r):
        soap = BeautifulSoup(r.text, "lxml")
        return print(soap.select(self.tag)[0].getText())
        
    def connect(self):
        r = requests.get(self.url)
        result = self.getTitle(r)
        return result

class Main:
    
    def __init__(self, url, tag):
        self.extractor = ExtractData(url, tag)
        
    def extract(self):
        self.extractor.connect()