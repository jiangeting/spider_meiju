#coding=utf-8
import requests
from bs4 import BeautifulSoup
import meijutt
#r = requests.get('http://www.meijutt.com/new100.html')
#r.encoding='gbk'
#soup = BeautifulSoup(r.text,"html.parser")
##print(soup.prettify())
#s=soup.select("h5 a")
#=%E8%A1%80%E8%B7%AF%E7%8B%82%E9%A3%99
#=%D1%AA%C2%B7%BF%F1%EC%AD
name=input("输入想看的美剧:")
meijutt.search(name)
input("press enter to exit")