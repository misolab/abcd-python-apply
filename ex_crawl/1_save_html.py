import urllib.request

url = "http://abcds.kr"

html = urllib.request.urlopen(url).read()
with open("abcds_kr.html", "wb+") as f:
    f.write(html)
