import requests
from bs4 import BeautifulSoup

USERNAME = "g323_boomer"
URL = f"https://www.instagram.com/{USERNAME}/"

headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(URL, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

images = soup.find_all("img")[1:4]  # grab first 3 posts

entries = []
for img in images:
    thumb = img["src"]
    alt = img.get("alt", "Instagram post")
    link = f"https://www.instagram.com/{USERNAME}/"
    entries.append(f"[![post]({thumb})]({link})")

block = "## 🎬 Latest Editing Work\n\n" + " ".join(entries) + "\n"

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- IG-FEED:START -->"
end = "<!-- IG-FEED:END -->"

new_readme = readme.split(start)[0] + start + "\n" + block + "\n" + end + readme.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
