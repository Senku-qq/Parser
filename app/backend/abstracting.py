from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')


def summarize_paragraph(paragraph, sentences_output_amount=2, language="english"):
    """Summarizes the paragraph using LSA algorithm
    Args: paragraph - string (input text), sentences_output_amount - int (amount of output sentances), language - string"""
    parser = PlaintextParser.from_string(paragraph, Tokenizer(language))

    summarizer = LsaSummarizer(Stemmer(language))
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(parser.document, sentences_output_amount)
    
    return summary

def normalize_text(summary):
    """Converts summary from list of sentences to string
    Args: text - string
    Returns: string"""
    return "\n".join([str(i) for i in summary])

if __name__ == "__main__":
    text = "This is a test text. It will be summarized. The summary will be displayed."
    summary = summarize_paragraph(text, sentences_output_amount=2)
    print(normalize_text(summary))