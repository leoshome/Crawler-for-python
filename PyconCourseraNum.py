
import requests
from bs4 import BeautifulSoup

urlLst = ['http://pycontw.kktix.cc/events/python-crawler', 'http://pycontw.kktix.cc/events/play-modeling-mining']
def getPersonNum(urlLst):
    for coursera in urlLst:
        res = requests.get(coursera)
        soup = BeautifulSoup(res.text)
        items = soup.select('div')[1]
        title = items.select('h1')[0].text
        personNum = items.select('span.info-count')[0].text
        print(title, '--->目前報名人數', personNum)
        print()

getPersonNum(urlLst)




