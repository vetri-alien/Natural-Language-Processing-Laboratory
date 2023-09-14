import nltk
sentence = "The clever fox escaped from the lion"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
chunks = chunk_parser.parse(pos_tags)
print(chunks)
chunks.draw()