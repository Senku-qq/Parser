# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from sumy.nlp.stemmers import Stemmer
# from sumy.utils import get_stop_words
# import nltk
# nltk.download('punkt_tab')


# def summarize_paragraph(paragraph, sentences_count=2, language="english"):
#     parser = PlaintextParser.from_string(paragraph, Tokenizer("language"))

#     summarizer = LsaSummarizer(Stemmer(language))
#     summarizer.stop_words = get_stop_words("language")

#     summary = summarizer(parser.document, sentences_count)
#     return summary


# def display_summary(summary):
#     for sentence in summary:
#         print(sentence)


# if __name__ == "__main__":
#     file_with_clear_text = open("parser1.txt", "w", encoding="utf-8")
#     summarize_paragraph(file_with_clear_text)
#     display_summary()
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt', quiet=True)

def summarize_paragraph(paragraph, sentences_output_amount=2, language="english"):
    """Summarizes the paragraph using LSA algorithm
    Args: paragraph - string (input text), sentences_output_amount - int (amount of output sentances), language - string"""
    parser = PlaintextParser.from_string(paragraph, Tokenizer(language))

    summarizer = LsaSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)

    summary = summarizer(parser.document, sentences_output_amount)
    
    #make summary a all-in-one string
    arr = []
    for sentence in summary:
        arr.append(str(sentence))

    return " ".join(arr)

if __name__ == "__main__":
    text = "This is a test text. It will be summarized. The summary will be displayed."
    summary = summarize_paragraph(text, sentences_output_amount=2)
    print(summary)
