import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

# sent = "¿Quién eres tú? ¡Hola! ¿Dónde estoy?"

def wordTokenizer(sentence):
    print(sent_tokenize(sentence))
    print(word_tokenize(sentence))
