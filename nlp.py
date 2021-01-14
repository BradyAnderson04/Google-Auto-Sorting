'''
Functions to process a files theme and set a main idea of a document
'''
import string
import heapq
import math

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# not sure what will work best, so I'll have to do a few different appraoches at varying degree
# going to start simple and gradually get more complex

### CONSTANTS ###
STOPWORDS = set(stopwords.words("english"))
PUNCTUATION = set(string.punctuation)

#### CLEAN TEXT DATA ####

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

def clean_useless_words_sentences(sentences, list_structure=False):
    '''
    use the same previous function on the group sentences

    combine sentences once punctuation and stopwords gone
    '''
    output = []

    for sent in sentences:
        no_punc = clean_punctuation(sent) # remove punctuation
        words = word_tokenize(no_punc) # tokenize
        words = clean_useless_words(words) # remove stopwords
        if(list_structure):
            output.append(" ".join(words)) # combine back into sentence string
        else:
            output.append(words)

    
    return output

def process_file(file_in):
    '''
    seperate the docuemnt into array of words
    
    input: a string of unprocessed data
    '''
    no_punc = clean_punctuation(file_in) # get rid of punctuation
    
    # two appraoches - one for each process and differrent level of analysis
    words = word_tokenize(no_punc)
    sentences = sent_tokenize(file_in)

    # cleaning -- remove stop words
    useful_words = clean_useless_words(words)
    useful_sentences = clean_useless_words_sentences(sentences)

    # Frequency analysis
    frequency_words = keyword_count(useful_words)

    # return useful_words, useful_sentences
    return frequency_words

def summarize_text(file_in):
    '''
    tokenize the text into words and sentences using weight to define value of sentence

    use a heapq to return the top 70% most valuable sentences

    error - need to make the key be a joined list of the words, also should add support for alternate forms of input data
    '''
    no_punc = clean_punctuation(file_in) # get rid of punctuation
    
    # two appraoches - one for each process and differrent level of analysis
    words = word_tokenize(no_punc)
    sentences = sent_tokenize(file_in)

    # cleaning -- remove stop words
    useful_words = clean_useless_words(words)
    useful_sentences = clean_useless_words_sentences(sentences)

    # Frequency analysis
    frequency_words = keyword_weights(useful_words)
    frequency_sents = sentence_weights(useful_sentences, frequency_words)

    heapq.nlargest(math.ceil(len(useful_sentences) * .7), frequency_sents, key=frequency_sents.get())

    summarized_text = " ".join(frequency_sents)

    return summarized_text 

#### ANALYZE TEXT FUNCTIONS ####

def stem_words():
    '''relate similar words to each other'''
    pass

def tag_words():
    '''label words as their type to only analyze the nouns'''
    pass

def keyword_count(word_list):
    '''given some document return the most 5 common key words'''
    counter = {}

    for word in word_list:
        if word in counter.keys():
            counter[word] = counter.get(word) + 1
        else:
            counter[word] = 1
    
    return counter

def keyword_weights(word_list):
    '''assign weight values to each word relative to the highest used word'''
    word_frequencies = keyword_count(word_list)
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    return word_frequencies

def sentence_weights(sent_list, word_weight):
    '''
    go through sentence word by word to calculate the frequency of a sentence

    make use of word_frequency code to get invidividual value of the worlds for collective value of a sentence

    code for this function from : https://stackabuse.com/text-summarization-with-nltk-in-python/
    '''
    sentence_scores = {}
    for sent in sent_list:
        for word in sent:
            if word in word_weight.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_weight[word]
                    else:
                        sentence_scores[sent] += word_weight[word]
    
    return sentence_scores

def sentence_keyword_count():
    '''a function used to count key words in sentence giving priority to the most common word and presenting all ties'''
    pass

def assign_wegihted_frequency():
    '''function that anzalyzes the output dictionary of a file and returns the weighted frequency of the top 70% of sentences'''

#### FUZZY MATCHING -- Not sure about this ####
def identify():
    '''given the top 5 words match to a category'''
    pass

if __name__ == '__main__':
    # print(type(PUNCTUATION))

    ### TEST STRINGS ###
    string_a = sent_tokenize("God is Great! I won a lottery.")
    string_b = 'Music is an art form, and a cultural activity, whose medium is sound. General definitions of music include common elements such as pitch (which governs melody and harmony), rhythm (and its associated concepts tempo, meter, and articulation), dynamics (loudness and softness), and the sonic qualities of timbre and texture (which are sometimes termed the "color" of a musical sound). Different styles or types of music may emphasize, de-emphasize or omit some of these elements. Music is performed with a vast range of instruments and vocal techniques ranging from singing to rapping; there are solely instrumental pieces, solely vocal pieces (such as songs without instrumental accompaniment) and pieces that combine singing and instruments. The word derives from Greek μουσική (mousike; "art of the Muses").[1] See glossary of musical terminology.In its most general form, the activities describing music as an art form or cultural activity include the creation of works of music (songs, tunes, symphonies, and so on), the criticism of music, the study of the history of music, and the aesthetic examination of music. Ancient Greek and Indian philosophers defined music in two parts: melodies, as tones ordered horizontally, and harmonies as tones ordered vertically. Common sayings such as "the harmony of the spheres" and "it is music to my ears" point to the notion that music is often ordered and pleasant to listen to. However, 20th-century composer John Cage thought that any sound can be music, saying, for example, "There is no noise, only sound."[2]The creation, performance, significance, and even the definition of music vary according to culture and social context. Indeed, throughout history, some new forms or styles of music have been criticized as "not being music", including Beethoven\'s Grosse Fuge string quartet in 1825,[3] early jazz in the beginning of the 1900s[4] and hardcore punk in the 1980s.[5] There are many types of music, including popular music, traditional music, art music, music written for religious ceremonies and work songs such as chanteys. Music ranges from strictly organized compositions—such as Classical music symphonies from the 1700s and 1800s—through to spontaneously played improvisational music such as jazz, and avant-garde styles of chance-based contemporary music from the 20th and 21st centuries.Music can be divided into genres (e.g., country music) and genres can be further divided into subgenres (e.g., country blues and pop country are two of the many country subgenres), although the dividing lines and relationships between music genres are often subtle, sometimes open to personal interpretation, and occasionally controversial. For example, it can be hard to draw the line between some early 1980s hard rock and heavy metal. Within the arts, music may be classified as a performing art, a fine art or as an auditory art. Music may be played or sung and heard live at a rock concert or orchestra performance, heard live as part of a dramatic work (a music theater show or opera), or it may be recorded and listened to on a radio, MP3 player, CD player, smartphone or as film score or TV show.In many cultures, music is an important part of people\'s way of life, as it plays a key role in religious rituals, rite of passage ceremonies (e.g., graduation and marriage), social activities (e.g., dancing) and cultural activities ranging from amateur karaoke singing to playing in an amateur funk band or singing in a community choir. People may make music as a hobby, like a teen playing cello in a youth orchestra, or work as a professional musician or singer. The music industry includes the individuals who create new songs and musical pieces (such as songwriters and composers), individuals who perform music (which include orchestra, jazz band and rock band musicians, singers and conductors), individuals who record music (music producers and sound engineers), individuals who organize concert tours, and individuals who sell recordings, sheet music, and scores to customers. Even once a song or piece has been performed, music critics, music journalists, and music scholars may assess and evaluate the piece and its performance.'

    ### test data ###
    # a = process_file("This, is a test sentence .... ")
    # b = process_file("A   hello ")
    # c = process_file("God is Great! I won a lottery.")

    # print(clean_useless_words_sentences(c))

    print(process_file(string_b))
    # print(process_file(b))
    # print(process_file(c))

    # d = sent_tokenize("God is Great! I won a lottery.")
    # print(clean_useless_words_sentences(d))


