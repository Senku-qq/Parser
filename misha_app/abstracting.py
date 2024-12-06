from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')


def summarize_paragraph(paragraph, sentences_count=2, language="english"):
    parser = PlaintextParser.from_string(paragraph, Tokenizer("language"))

    summarizer = LsaSummarizer(Stemmer("language"))
    summarizer.stop_words = get_stop_words("language")

    summary = summarizer(parser.document, sentences_count)
    return summary


def display_summary(summary):
    for sentence in summary:
        print(sentence)


if __name__ == "__main__":
    summarize_paragraph()
    display_summary()