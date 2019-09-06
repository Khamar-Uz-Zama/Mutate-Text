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

    for i in range(len(tokens)-2):
        key = (tokens[i], tokens[i+2])
        if key not in triGrams:
            triGrams[key] = []
            triGrams[key].append(tokens[i+1])

```
