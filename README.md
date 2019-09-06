# Mutate-Text

## Pre-Process the text

1. Lowercase the text because we know that uppercase words mean same as lowercased words.
2. Tokenize the words.
  Example:
    if text = "Tokenize the words" </br>
    then output after tokenizing will be tokens = ['Tokenize', 'the', 'words']
3. Lemmatize them. This converts the words to their basic form or their root word. 'words' become 'word'

```

for review in reviews:
    text = review.text.lower()
    tokens = word_tokenize(text) # Tokenize the sentence
    tokens = [wordNet_Lemmatizer.lemmatize(word=w) for w in tokens]

```
## Create Tri-Grams
Create a dictionary of tuples. In this case, the 1st and the 3rd word are keys while the 2nd word is the value. </br>
The output will loke something like : </br>
{ </br>
('I', 'take'): ['can', 'should', 'will', 'will', 'will'] </br>
('I', 'not'):  ['am','will'] </br>
} </br>

Note that the values will be repeated so it can be used while calculating probability

```
    for i in range(len(tokens)-2):
        key = (tokens[i], tokens[i+2])
        if key not in triGrams:
            triGrams[key] = []
            triGrams[key].append(tokens[i+1])
```

## Add probabilities to Tri-Grams
Using the above triGrams, we add probability based on the occurences of the word </br>
Just divide the numbe of occurences of the word with the count of the  total number of words in that particular text. </br>
Output:
{ </br>
('I', 'take'): ['can':0.20, 'should':0.20, 'will':0.6] </br>
('I', 'not'):  ['am':0.5,'will':0.5] </br>
} </br>


```
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
```

Now for testing the code, preprocess the text, random-sample it based on above probabilities, repace the word from the dictionary

