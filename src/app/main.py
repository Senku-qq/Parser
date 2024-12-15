from misha_package import translation
from misha_package import abstracting
from misha_package import parser
from misha_package import check_robots

if __name__ == "__main__":

    print("Welcome to the text summarizer!\n\
This program will summarize the text from the page and translate it to the language you want.\n\
You can find the text in the file\n", "-"*37)
    
    url = input("Enter the URL of the page to summarize: ")
    filename = input("Enter the filename to save the text: ")
    lang = input("Enter your language code: ")

    if check_robots.check_robots(url):
        text = parser.get_text(url, filename)

        if text:
            text = translation.translate_text(text, 'ru')

            file = open("summary.txt", "w", encoding="utf8")
            for text_part in text:
                summary = abstracting.summarize_paragraph(text_part)
                file.write(summary)