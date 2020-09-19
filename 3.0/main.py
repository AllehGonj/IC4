import enquiries
from words_tokenizer import wordTokenizer
from stops_words import stopWords
from stemmer import sentenceStemmer
from lemmatizer import wordLemmatizer

options = ["Words Tokenizer", "Stop Words", "Stemming", "Lemmatizing"]

def main():
    sentence = input('\nPlease enter the sentence for processing: ')
    choice = enquiries.choose('Choose one of these options: ', options)
    optionMenu(choice, sentence)

def optionMenu(option, sentence):
    choices = {
        1: wordTokenizer,
        2: stopWords,
        3: sentenceStemmer,
        4: wordLemmatizer
    }
    choices[options.index(option) + 1](sentence)

if __name__ == "__main__":
    main()