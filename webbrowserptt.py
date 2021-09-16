# 抓取網頁原始碼帶cookie 並且抓取多頁
import urllib.request as req 
def  getData(url):
    #建立一個request 物件 附加request headers 的資訊 
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
    })

    with req.urlopen(request) as  response:
        data=response.read().decode("utf-8")
    #print(data)
    #解析原始碼
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")#讓beautisoup協助我們解析 html格式文件
    titles=root.find_all("div",class_="title")#尋找 class="title" 的 div標籤
    for title in titles:
        #print(title)
        if title.a != None: #如果標題包含a標籤(沒有被刪除)就印出來
            #print(title.a.href.string)    
            print(title.a.string)    
    #抓去上一頁的連結
    nextlink = root.find("a",string="‹ 上頁")#找尋內文是< 上頁的 a標籤         
    return nextlink["href"]

pageurl ="https://www.ptt.cc/bbs/Gossiping/index.html"

count=0
while count<5:
    pageurl="https://www.ptt.cc"+getData(pageurl)
    count+=1

