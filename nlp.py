'''
Functions to process a files theme and set a main idea of a document
'''
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# not sure what will work best, so I'll have to do a few different appraoches at varying degree
# going to start simple and gradually get more complex

### CONSTANTS ###
STOPWORDS = set(stopwords.words("english"))
PUNCTUATION = set(string.punctuation)

#### CLEAN TEXT DATA ####

def tag_words():
    '''label words as their type to only analyze the nouns'''
    pass

def clean_punctuation(raw_data):
    '''remove all punctuation by iterating over the input 1 char at a time'''

    for i, char in enumerate(raw_data):
        if char in PUNCTUATION:
            if(i == len(raw_data)):
                raw_data = raw_data[:i] + " "
            else:
                raw_data = raw_data[:i] + " " + raw_data[i+1:]
    
    return raw_data

def clean_useless_words(words):
    '''get rid of all stopwords'''
    cleaned_words = []

    for word in words:
        if not word in STOPWORDS:
            cleaned_words.append(word.lower())
    
    return cleaned_words

def clean_useless_words_sentences(sentences):
    for sent in sentences:
        pass
    
    return sentences

def process_file(input):
    '''
    seperate the docuemnt into array of words
    
    input: a string of unprocessed data
    '''
    no_punc = clean_punctuation(input) # get rid of punctuation
    
    # two appraoches
    words = word_tokenize(no_punc)
    # sentences = sent_tokenize(input)

    # cleaning -- remove stop words
    useful_words = clean_useless_words(words)
    # useful_sentences = clean_useless_words_sentences(sentences)

    return useful_words

def tokenize_sentence(input):
    '''seperate document into array of sentences'''
    # sentences = sent_tokenize(input)
    pass

def stem_words():
    '''relate similar words to each other'''
    pass


#### ANALYZE TEXT FUNCTIONS ####

def keyword_count():
    '''given some document return the most 5 common key words'''
    pass

#### FUZZY MATCHING ####
def identify():
    '''given the top 5 words match to a category'''
    pass

if __name__ == '__main__':
    # print(type(PUNCTUATION))

    # d = sent_tokenize("God is Great! I won a lottery.")

    ### test data ###
    a = process_file("This, is a test sentence .... ")
    b = process_file("A   hello ")
    c = process_file("God is Great! I won a lottery.")

    # print(clean_useless_words_sentences(c))

    print(c)
    # print(process_file(b))
    # print(process_file(c))

