from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')

def summarize_paragraph(paragraph, sentences_count=100):
    parser = PlaintextParser.from_string(paragraph, Tokenizer("ukrainian"))

    summarizer = LsaSummarizer(Stemmer("ukrainian"))
    summarizer.stop_words = get_stop_words("ukrainian")

    summary = summarizer(parser.document, sentences_count)
    return summary

if __name__ == "__main__":
    paragraph = open("misha_app/text.txt", "r", encoding="utf-8").read()
    sentences_count = 100
    summary = summarize_paragraph(paragraph, sentences_count)

    with open('text2.txt', 'w', encoding="utf-8") as f:
        for sentence in summary:
            f.write(str(sentence))
            f.write("\n")