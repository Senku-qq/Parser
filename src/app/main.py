from bs4 import BeautifulSoup
import requests

# URL целевой страницы
class Parser:
    def parser(url): 
        # Загружаем содержимое страницы
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            file = open('text.txt','w', encoding="utf8")
            text = soup.find_all('p')
            for title in text:
                file.write(title.text.strip() + "\n")
            file.close()
        else:
            print(f"Ошибка загрузки страницы: {response.status_code}")

if __name__ == '__main__':
    tom = Parser
    tom.parser('https://en.wikipedia.org/wiki/Linux')
