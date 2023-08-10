#Ex3 Stopword
import nltk
#nltk.download('stopwords')
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
data = "Life is a beautiful journey that is meant to be embraced to the fullest every day."
stopwords = set(stopwords.words('english'))
words = word_tokenize(data.lower())
wordsFiltered = []
for w in words:
    if w not in stopwords:
        wordsFiltered.append(w)
print("Words=",words)
print("Stopwords=",stopwords)
print("Filtered words=",wordsFiltered)