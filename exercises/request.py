import requests
from bs4 import BeautifulSoup

url = "https://teddycubaka.vercel.app/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

file = open("file.txt", "w")
file.write(soup.title.string)

print("End !")