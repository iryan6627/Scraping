from bs4 import BeautifulSoup
import requests

source = requests.get("http://coreyms.com/").text
soup = BeautifulSoup(source, "lxml")
for index,char in enumerate(soup.find_all("article"), start = 1):
    video_nav = char.find("iframe", class_ = "youtube-player")["src"]
    video_split = video_nav.split("/")[4]
    video_split = video_split.split("?")[0]
    youtubeFormat = str(index) + ")" + f"https://www.youtube.com/watch?v={video_split}"
    print(youtubeFormat)

