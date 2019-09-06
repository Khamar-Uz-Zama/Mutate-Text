# -*- coding: utf-8 -*-
"""
@author: OME
"""

import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize 
from bs4 import BeautifulSoup
import random

wordNet_Lemmatizer = WordNetLemmatizer()

reviews = BeautifulSoup(open('C:/Users/ABCD/Desktop/Data Science/Article Spinner/review.txt').read(), features="lxml")
reviews = reviews.findAll('review_text')

triGrams = {}

for review in reviews:
    text = review.text.lower()
    tokens = word_tokenize(text) # Tokenize the sentence
    tokens = [wordNet_Lemmatizer.lemmatize(word=w) for w in tokens]

    for i in range(len(tokens)-2):
        key = (tokens[i], tokens[i+2])
        if key not in triGrams:
            triGrams[key] = []
            triGrams[key].append(tokens[i+1])
        
trigrams_with_probabilities = {}
for Mainkey, words in triGrams.items():
    d={}
    n = 0
    for word in words:
        if word not in d:
            d[word] = 0
        d[word] += 1
        n += 1
    for key,occurences in d.items():
        d[key] = occurences/n
        trigrams_with_probabilities[Mainkey] = d
        
        
def random_sample(d):
    r = random.random()
    cumulative = 0
    for w,p in d.items():
        cumulative += p
        if r< cumulative:
            return w

def mutate_text():
    review = random.choice(reviews)
    text = review.text.lower()
    print("Original----")
    print(text)
    tokens = nltk.tokenize.word_tokenize(text)
    for i in range(len(tokens) - 2):
        if random.random() < 0.5:
            k = (tokens[i], tokens[i+2])
            if k in trigrams_with_probabilities:
                w = random_sample(trigrams_with_probabilities[k])
                print(tokens[i+1]," replaced with ", w)
                tokens[i+1] = w
    print("Modified----")
    modified_text = " ".join(tokens)
    print(modified_text.replace(" .",".").replace(" ,",",").replace(" !","!").replace(" '","'").replace("' ' ","``").replace(" (","(").replace(" )",")"))


mutate_text()
