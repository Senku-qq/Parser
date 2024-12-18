import translation
import abstracting
import parser
import check_robots


def main(url, filename):

    if check_robots.check_robots(url):
        text = parser.get_text(url)
        text = parser.clear(text)

        if text:
            lang = translation.get_language(text)

            sentences_amount = len(text.split("."))
            sentences_amount *= 0.4
            sentences_amount = int(sentences_amount)

            #logging
            #print(len(text), sentences_amount)

            if lang != "en":
                translated = translation.translate_text(text, lang)

                summary = abstracting.summarize_paragraph(translated, sentences_output_amount=sentences_amount)
                summary = translation.back_translate(text, summary)
            else:
                summary = abstracting.summarize_paragraph(text, sentences_output_amount=sentences_amount)

            file = open(filename, "w", encoding="utf8")
            for line in summary:
                file.write(str(line) + "\n")
            file.close()

            return summary


if __name__ == "__main__":
    print("Welcome to the text summarizer!\n\
This program will summarize the text from the page and translate it to the language you want.\n\
You can find the text in the file\n", "-"*37)
    
    url = input("Enter the URL of the page to summarize: ")

    if check_robots.check_robots(url):
        text = parser.get_text(url)
        text = parser.clear(text)
        if text:
            lang = translation.get_language(text)

            sentences_amount = len(text.split("."))
            sentences_amount *= 0.4
            sentences_amount = int(sentences_amount)

            if lang != "en":
                translated = translation.translate_text(text, lang)

                summary = abstracting.summarize_paragraph(translated, sentences_output_amount=sentences_amount)
                summary = translation.back_translate(text, summary)
            else:
                summary = abstracting.summarize_paragraph(text, sentences_output_amount=sentences_amount)
            print(summary)