import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

nltk.download('punkt')

ps = SnowballStemmer('english')

words = ["cook", "cooker", "cooking", "cooked", "overcooked"]
# texto = "This is your last chance. After this, there is no turning back. You take the blue pill – the story ends, you wake up in your bed and believe whatever you want to believe. You take the red pill – you stay in Wonderland, and I show you how deep the rabbit hole goes."

def wordsStemmer(words):
    for w in words:
        print(ps.stem(w))

def sentenceStemmer(sentence):
    words = word_tokenize(sentence)
    wordsStemmer(words)

wordsStemmer(words)
