import requests
from bs4 import BeautifulSoup

def get_text(url):
    # download page
    response = requests.get(url)
    #if page downloaded successfully
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        #file to store text
        file = open(url, "w", encoding="utf8")
        #find all paragraphs
        titles = soup.find_all('p')
        for title in titles:
            file.writelines(title.text.strip() + "\n")
        file.close()
    else:
        print(f"Can't get page {url}\nError: {response.status_code}")