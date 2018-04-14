from bs4 import BeautifulSoup
import requests, csv


source = requests.get("http://worldstarhiphop.com/videos/").text
soup = BeautifulSoup(source, "html5lib")

with open("wshh_scrape.csv", "w") as world:
    csv_file = csv.writer(world)
    csv_file.writerow(["Index", "Description", "Link"])
    for index, char in enumerate(soup.find_all("section", class_ = "box"), start = 1):
        try:
            getInfo = char.find("img", class_ = "lazy")["alt"]
            getUrl = char.find("a", itemprop = "url", class_ = "video-box")["href"]
            url = f"http://www.worldstarhiphop.com{getUrl}"
            wshh = str(index) + ") " + "Description: " + getInfo + "\n" + url
            print(wshh)
            print("\n")
        except:
            getInfo = None
        csv_file.writerow([str(index), getInfo, str(url)])


  