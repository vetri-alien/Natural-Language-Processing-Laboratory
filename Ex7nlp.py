import nltk
sentence = "hello I am vetriventhan"
token = nltk.word_tokenize(sentence)
ans = nltk.pos_tag(token)
for word,tag in ans:
    print(word,tag)