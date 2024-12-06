from check_robots import robots_check , get_robots_url
import abstracting
from parser import get_text
from translation import get_language
url = input("please enter the url you want to parse: ")
get_robots_url(url)
robots_check(url)    
if robots_check == True:
    get_text(url)
    file = open("parser.txt","r", encoding="utf-8")
    text = file.readlines()
    get_language(text)
    if get_language == "en":
        pass
    else:
        pass



if __name__ == "__main__":
    pass