import urllib.request as req
import bs4
with open("movie.txt","w",encoding="utf-8") as file:        
    target = "好雷"
    for i in range(0,3):
        url = "https://www.ptt.cc/bbs/movie/index.html"
        if i == 1:
            target = "普雷"
        if i == 2:
            target = "負雷" 
        for i in range(0,10):
            request = req.Request(url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
            with req.urlopen(request) as response:
                data = response.read().decode("utf-8")
            root = bs4.BeautifulSoup(data, "html.parser")
            divTitles = root.find_all("div",class_="title")
            for title in divTitles :
                if title.a != None and title.a.string[1:3] == target:
                    file.write(title.a.string+"\n")
            previousPage= "https://www.ptt.cc"+root.find("a", string="‹ 上頁")["href"]
            url =  previousPage
    

    
    



