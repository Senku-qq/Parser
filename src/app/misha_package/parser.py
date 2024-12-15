import requests
from bs4 import BeautifulSoup

def get_text(url, filename):
    """Downloads text from the page and saves it into the file
    Args: url - string, filename - string
    Returns: list of strings (text) or False if page can't be downloaded"""
    # download page
    response = requests.get(url)
    #if page downloaded successfully
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        #file to store text
        file = open(filename, "w", encoding="utf8")
        #find all paragraphs
        text = soup.find_all('p')
        for line in text:
            file.writelines(line.text.strip() + "\n")
        file.close()
        #logging
        print(f"Page {url} downloaded successfully into {filename}")
        return text
    else:
        #logging
        print(f"Can't get page {url}\nError: {response.status_code}")
        return False