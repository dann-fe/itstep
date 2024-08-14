import requests

url = "https://www.google.com"

response = requests.get(url)

print(response.text)

with open("classes/py/8-12-24/googlesrc.html", mode = "w", encoding="utf-8") as file:
    file.write(response.text)

def download_page(url, filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"classes/py/8-12-24/{filename}.html", mode = "w", encoding="utf-8") as file:
            file.write(response.text)
    else: 
        print(response.status_code)

download_page("https://www.youtube.com", "youtube")