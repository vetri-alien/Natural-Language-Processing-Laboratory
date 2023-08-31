import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
sentence = "programmer, the programmer doing the program in computer"
words = word_tokenize(sentence)
for word in words:
    print(word,":",ps.stem(word))
