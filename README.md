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
