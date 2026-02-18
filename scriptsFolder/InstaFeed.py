import requests
import re

USERNAME = "g323_boomer"

def update_readme():
    url = f"https://rsshub.app/instagram/user/g323_boomer"
    
    try:
        response = requests.get(url, timeout=15)
        images = re.findall(r'<img src="(.*?)"', response.text)[:3]
    except Exception as e:
        print(f"Error fetching RSS: {e}")
        return

    if not images:
        print("No images found. The RSS feed might be blocked or empty.")
        return

    entries = []
    for thumb in images:
        link = f"https://www.instagram.com/g323_boomer/"
        entries.append(f"[![post]({thumb})]({link})")

    block = "## Latest Editing Work\n\n" + " ".join(entries) + "\n"

    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    start = ""
    end = ""

    if start in readme and end in readme:
        new_readme = readme.split(start)[0] + start + "\n" + block + "\n" + end + readme.split(end)[1]
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)
        print(f"Successfully updated README with {len(images)} images!")
    else:
        print("Error: Could not find markers and in README.md")

if __name__ == "__main__":
    update_readme()
