import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# text = "¿Quién eres tú? ¡Hola! ¿Dónde estoy?"
stop_words = set(stopwords.words("spanish"))

def stopWords(sentence):
    filtered_sentence = []

    word = word_tokenize(sentence)

    for w in word:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(filtered_sentence)



