import requests
from bs4 import BeautifulSoup
import argparse

class crtShClass():

    def __init__(self,domain):
        self.url = "https://crt.sh/?q=%25."+domain
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.cookies = {}
        self.foundURLsList = []

    def subdomainScrape(self):
        r = requests.get(self.url,headers=self.headers,timeout=10)
        soup = BeautifulSoup(r.content,'html.parser')

        tableRows = soup.find_all('table')[2].find_all('tr')

        for row in tableRows:
            try:
                subdomain = row.find_all('td')[4].text
                subdomain = subdomain.replace("*.","")
                if subdomain not in self.foundURLsList:
                    self.foundURLsList.append(subdomain)
            except Exception as e:
                pass

    def run(self):
        self.subdomainScrape()

    def printSubdomains(self):
        for subdomain in self.foundURLsList:
            print(subdomain)


parser = argparse.ArgumentParser()
parser.add_argument("-d","--domain", help="Domain Name; EX: example.com")
args = parser.parse_args()

crtsh = crtShClass(args.domain)
crtsh.run()
crtsh.printSubdomains()
