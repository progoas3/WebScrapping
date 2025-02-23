import requests
from bs4 import BeautifulSoup

class ExtractData:
    
    def __init__(self, url, tag_title, tag_priece, tag_priece_descount):
        self.url = url
        self.tag_priece = tag_priece
        self.tag_title = tag_title
        self.tag_priece_descount = tag_priece_descount
        
    def getTitle(self, r):
        soap = BeautifulSoup(r.text, "lxml")
        prieces = [priece.get_text(strip=True) for priece in soap.select(self.tag_priece)]
        prieces_des = [priece_de.get_text(strip=True) for priece_de in soap.select(self.tag_priece_descount)]
        titles = [title.get_text(strip=True) for title in soap.select(self.tag_title)]
        
        products = list(zip(titles, prieces, prieces_des))
        
        print(products[0])
        return products
        
    def connect(self):
        r = requests.get(self.url)
        result = self.getTitle(r)
        return result

class Main:
    
    def __init__(self, url, tag_title, tag, tag_priece_descount):
        self.extractor = ExtractData(url, tag_title, tag, tag_priece_descount)
        
    def extract(self):
        self.extractor.connect()