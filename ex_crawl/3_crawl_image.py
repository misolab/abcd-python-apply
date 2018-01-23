import os
import urllib.request
from bs4 import BeautifulSoup


url = "http://abcds.kr"


html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")


imgs = soup.find_all("img")

for img in imgs:
    print(imgs)
    img_src = img.attrs['src']

    if "https" in img_src:
        print("https 라서 PASS-" + img_src)
        continue

    url = os.path.split(img_src)
    file_name = url[-1]
    print("file_name -" + file_name)

    # urllib.request.urlretrieve(img_src, file_name)
    img = urllib.request.urlopen(img_src).read()
    with open(file_name, "wb+") as f:
        f.write(img)