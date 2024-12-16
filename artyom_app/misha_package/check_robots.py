import requests
import re
from urllib.robotparser import RobotFileParser

#get main page's url
def get_main_url(url):
    """Returns main page's url
    Args: url - string
    Returns: main page's url string"""
    pattern = r"(https?://[^/]+/)"
    main_page = re.match(pattern, url)

    return main_page.group(1)


#robots.txt checking
def check_robots(url):
    """Checks if the page is allowed to be downloaded
    Args: url - string
    Returns: boolean"""
    parser = RobotFileParser()
    parser.set_url(get_main_url(url) + "robots.txt")
    parser.read()

    if parser.can_fetch('*', url):
        return True
    else:
        return False

#test
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Linux"
    print(check_robots(get_main_url(url)))