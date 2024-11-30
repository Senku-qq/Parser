# from sumy.nlp.tokenizers import Tokenizer
# from sumy.nlp.stemmers import Stemmer
# import nltk

# Download the punkt tokenizer
# nltk.download('punkt_tab')
# tokenizer = Tokenizer("english")

# # Tokenizer explained:
#  # text -> sentences -> words
# sentences = tokenizer.to_sentences("Hello, this is GeeksForGeeks! We are a computer science portal for geeks, offering a wide range of articles, tutorials, and resources on various topics in computer science and programming. Our mission is to provide quality education and knowledge sharing to help you excel in your career and academic pursuits.")
# #for sentence in sentences:
#     #print(tokenizer.to_words(sentence))

# #stemmer explained:
#  # stemming is the process of reducing a word to its root form
#  # blogging -> blog
#  # blogged -> blog
#  # blogs -> blog

# stemmer = Stemmer('en')
# stem = stemmer("Blogging")
# #print(stem)

# if __name__ == "main":
#     pass

# import re
# text = "aaa[21]aaaaaaaa[22]aaaaaa[23]"
# text = re.sub(r'\[\d+\]', '', text)
# print(text)



# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.luhn import LuhnSummarizer
# from sumy.nlp.stemmers import Stemmer
# from sumy.utils import get_stop_words
# import nltk
# nltk.download('punkt')

# def summarize_paragraph(paragraph, sentences_count=2):
#     parser = PlaintextParser.from_string(paragraph, Tokenizer("ukrainian"))

#     summarizer = LuhnSummarizer(Stemmer("ukrainian"))
#     summarizer.stop_words = get_stop_words("ukrainian")

#     summary = summarizer(parser.document, sentences_count)
#     return summary

# if __name__ == "__main__":
#     paragraph = ""
#     sentences_count = 2
#     summary = summarize_paragraph(paragraph, sentences_count)

#     for sentence in summary:
#         print(sentence)



from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')

def summarize_paragraph(paragraph, sentences_count=2):
    parser = PlaintextParser.from_string(paragraph, Tokenizer("ukrainian"))

    summarizer = LsaSummarizer(Stemmer("ukrainian"))
    summarizer.stop_words = get_stop_words("ukrainian")

    summary = summarizer(parser.document, sentences_count)
    return summary

if __name__ == "__main__":
    paragraph = open("misha_app/text.txt", "r", encoding="utf-8").read()
    sentences_count = 5
    summary = summarize_paragraph(paragraph, sentences_count)

    with open('text2.txt', 'w', encoding="utf-8") as f:
        for sentence in summary:
            f.write(str(sentence))
            f.write("\n")