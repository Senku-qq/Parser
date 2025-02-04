#import our modules
from backend import translation
from backend import abstracting
from backend import parser
from backend import check_robots

import datetime
import logging

#logging into db/
logging.basicConfig(filename="db/backend.log",
level=logging.INFO,
format="%(asctime)s - %(levelname)s - %(message)s",
datefmt="%Y-%m-%d %H:%M:%S"
)

#parse and summarize the text
def main(url, filename=str(datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S")) + ".txt", prefered_language="en", percent=0.4):
    """ Summarize the text from the page and translate it to the language you want.
    Args: url - string, filename - string, prefered_language - string, percent - float(volume of the abstract)"""

    text = parsing(url)
    return abstract(text, filename, prefered_language, percent)

#parse the text from the page
def parsing(url):
    if check_robots.check_robots(url):
        text = parser.get_text(url)
        text = parser.clear(text)
    return text

#abstract the text
def abstract(text, filename=str(datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S")) + ".txt", prefered_language="en", percent=0.4):
    lang = translation.get_language(text)
    #calculate the amount of sentences for output
    sentences_amount = len(text.split("."))
    sentences_amount *= percent
    sentences_amount = int(sentences_amount)

    logging.info(f"Sentences amount: {len(text.split("."))}, Sentences for output: {sentences_amount}")

    #processing the translation (summarizing only english text)
    if prefered_language != "en":
        if lang != "en": translated = translation.translate_text(text, "en")
        summary = abstracting.summarize_paragraph(text, sentences_output_amount=sentences_amount)
        summary = abstracting.normalize_text(summary)
        summary = translation.translate_text(summary, prefered_language)
        logging.info(f"Prefered language option: {prefered_language}")

    else:
        logging.info(f"Default language option: {lang}")
        if lang == "en":
            summary = abstracting.summarize_paragraph(text, sentences_output_amount=sentences_amount)
            summary = abstracting.normalize_text(summary)
        else:
            translated = translation.translate_text(text, "en")
            summary = abstracting.summarize_paragraph(translated, sentences_output_amount=sentences_amount)
            summary = abstracting.normalize_text(summary)
            summary = translation.back_translate(text, summary)

    #writing the summary to the file
    file = open(filename, "w", encoding="utf8")
    file.write(summary)
    file.close()

    return summary

if __name__ == "__main__":
    print(datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S"))
    main(r"https://en.wikipedia.org/wiki/Linux", percent=0.2)