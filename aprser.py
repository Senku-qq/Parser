import requests
from bs4 import BeautifulSoup

# URL целевой страницы
url = "https://en.wikipedia.org/wiki/Linux"

# Загружаем содержимое страницы
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    file = open("parser.txt", "w+", encoding="utf8")
    # Ищем данные (например, заголовки статей)
    titles = soup.find_all('p')
    for title in titles:
        file.writelines(title.text.strip() + "\n")
    file.close()
else:
    print(f"Ошибка загрузки страницы: {response.status_code}")