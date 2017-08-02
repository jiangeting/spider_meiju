#coding=utf-8
"""for meijutt websit"""
__auther__="jzt"
import requests
from bs4 import BeautifulSoup
import pyperclip
urllist=[]
titlelist=[]
baseurl="http://www.meijutt.com"
__headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
__payload = {}
def display(list):
    x=0
    for i in list:
        x+=1
        print(x,", ",i)
    return input("choices:")
def search(s):
    """search"""    
    __payload = {'searchword': s.encode("gbk")}
    r=requests.post('http://www.meijutt.com/search.asp',data=__payload,headers=__headers)
    r.encoding='gbk'
    soup = BeautifulSoup(r.text,"html.parser")
    targettag=soup.find_all("div",attrs={"class":"bor_img3_right"})
    if targettag is not None:
        for i in targettag:
           urllist.append(i.a.attrs["href"])
           titlelist.append(i.a.attrs["title"])
    find()

def find():
    if titlelist.count==0:
        print("no items found")
    else:
        choice=display(titlelist)
        try:          
            url=baseurl+urllist[int(choice)-1]
            print(url)
        except Exception as e:
            print(e)
        urllist.clear()
        titlelist.clear()
        r=requests.get(url)
        r.encoding="gbk"
        soup=BeautifulSoup(r.text,"html.parser")
        choice=input("1.download  2.baiduyun \n")
        if choice=='1':
            tags=soup.find("div","down_list")  
            if tags==None:
                  print("no results")
            else:
                for tag in tags.find_all("input"):
                    urllist.append(tag.attrs["value"])
                    titlelist.append(tag.attrs["file_name"])                  

        elif choice=='2':
            tag=soup.find("div",attrs={"class":"wp-list"})           
            if tag==None:
                print("no results")
            else:
                tags=tag.find_all("a")
                for title in tag.find_all("li"):
                    titlelist.append(title.text)

                for tag in tags:
                    urllist.append(tag.attrs["href"]) 
        else :
            print("no such options")
            eixt()   
        try:
            choice=display(titlelist)
            print(urllist[int(choice)-1])
            pyperclip.copy(urllist[int(choice)-1])
            print("链接已经复制到粘贴版，直接ctrl+v即可粘贴")
        except Exception as e:
            print(e)

 
if __name__=="__main__":
    search("血路狂飙")




    




