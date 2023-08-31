from nltk import ngrams
sentence = "The adventurous hiker explored lush forests, discovering hidden waterfalls and caves."
n = 7
ng7 = ngrams(sentence.split(),n)
for grams in ng7:
    print(grams)

sentence = "The adventurous hiker explored lush forests, discovering hidden waterfalls and caves."
n = 7
ncg7 = ngrams(sentence,n)
for grams in ncg7:
    print(grams)
