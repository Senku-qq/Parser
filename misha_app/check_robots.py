import requests
import re
from urllib.robotparser import RobotFileParser

#get main page's url
def get_robots_url(url):
    pattern = r"(https?://[^/]+/)"
    main_page = re.match(pattern, url)

    return main_page.group(1) + "robots.txt"


#robots.txt checking
def robots_check(url):
    parser = RobotFileParser()
    parser.set_url(get_robots_url(url))
    parser.read()

    if parser.can_fetch('*', url):
        return True
    else:
        return

#test
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Linux"
    print(robots_check(get_robots_url(url)))