import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://old.reddit.com/r/happy/"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    attrs = {'class': 'thing', 'data-domain': 'self.happy'}

    tt = list()
    
    for post in soup.find_all("div", attrs=attrs):
        title = post.find("p", class_="title").text
        tt.append(title)
        #print(title)

def goodNews(tracker): 
    return(tt[tracker])
       