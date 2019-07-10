# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## 1. tokenizing Words and Sentences with NLTK

from nltk.tokenize import sent_tokenize, word_tokenize
example_text = "Hello Mr.smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkis-blue. You should not eat cardboard."

# sent_tokenize
print(sent_tokenize(example_text))

# word tokenize
print(word_tokenize(example_text))

# 단어 하나하나씩 출력
for i in word_tokenize(example_text):
    print(i)
    

## 2. stopwords with NLTK
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words=set(stopwords.words("english"))
print(stop_words)

example_sentence = "This is an example showing off stop word filtration."
words = word_tokenize(example_sentence)

print(words)

filtered_sentence = list()

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print(filtered_sentence)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)

## 3. stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"

stem = list()
words = word_tokenize(new_text)
for w in words:
    stem.append(ps.stem(w))
print(stem)
    

## 4. part of speech tagging with NLTK
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# unsupervised_tokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content(sentences):
    try:
        for i in sentences:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
            
    except Exception as e:
        print(str(e))
        
process_content(tokenized)

    
## 5. chunking
def process_content(sentences):
    try:
        for i in sentences:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            
            chunked = chunkParser.parse(tagged)
            
            chunked.draw()
            
    except Exception as e:
        print(str(e))
        
process_content(tokenized)


## 6. chinking
chunkGram = r"""Chunk: {<.*>+}
                        }<VB.?|IN|DT>+{"""

## 7. lemmatizing
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))

## 10. wordnet
from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print(syns)


print(syns[0])
print(syns[0].lemmas())
print(syns[0].lemmas()[0].name)
print(syns[0].name)
print(syns[0].definition())
print(syns[0].examples())


# 동의어, 반의어
synonyms = list()
antonyms = list()

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
            
print(set(synonyms))
print(set(antonyms))

# 단어의 유사도
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w1 = wordnet.synset("hat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w1 = wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))


w1 = wordnet.synset("ship.n.01")
w1 = wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))


