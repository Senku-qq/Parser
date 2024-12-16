import requests
from bs4 import BeautifulSoup
import re

def get_text(url):
    """Downloads text from the page and saves it into the file
    Args: url - string, filename - string
    Returns: list of strings (text) or False if page can't be downloaded"""
    # download page
    response = requests.get(url)
    #if page downloaded successfully
    if response.status_code == 200:
        text = ""

        soup = BeautifulSoup(response.text, 'html.parser')
        #find all paragraphs
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            text += paragraph.text.strip() + '\n'
        #logging
        #print(f"Page {url} downloaded successfully")
        return text
    else:
        #logging
        print(f"Can't get page {url}\nError: {response.status_code}")
        return False
    
def clear(text, regular=r"\[\d+\]"):
    cleared = ""
    cleared += re.sub(regular, "",text)
    return cleared

if __name__ == "__main__":
    url = input("Enter the URL of the page to summarize: ")
    text = get_text(url)
    text = clear(text)
    print(text)