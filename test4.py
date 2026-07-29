
import threading
import requests
from bs4 import BeautifulSoup

urls= ['https://www.langchain.com/langchain','https://www.langchain.com/langsmith','https://academy.langchain.com/',
]

def fetch_contents(urls):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetch {(soup.text)} character from {url}')

threads=[]
for url in urls:
    thread = threading.Thread(target = fetch_contents,args =(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
