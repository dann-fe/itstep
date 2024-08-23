from urllib.request import urlretrieve

def download_img(url = str, filename = None):
    urlretrieve(url, filename="cat.jpg")
    print("image saved")


url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg"

download_img(url)