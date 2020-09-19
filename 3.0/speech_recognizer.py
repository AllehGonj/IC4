import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

nltk.download('averaged_perceptron_tagger')
nltk.download('state_union')

trainingText = state_union.raw("2005-GWBush.txt")
sampleText = state_union.raw("2006-GWBush.txt")
trainingTokenizer = PunktSentenceTokenizer(trainingText)

tokenized = trainingTokenizer.tokenize(sampleText)

def processContent():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tags = nltk.pos_tag(words)
            print(*tags, sep="\n")

    except Exception as e:
        print(str(e))

processContent()