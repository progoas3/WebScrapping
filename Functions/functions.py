import requests
from bs4 import BeautifulSoup

class ExtractData:
    
    def __init__(self, url):
        self.url = url
        
    def imprimir(self):
        print(f"{self.url}")
        

class Main:
    
    def __init__(self, url):
        self.extractor = ExtractData(url)
        
    def pr(self):
        self.extractor.imprimir()