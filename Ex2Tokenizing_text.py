import nltk
def tokenize_text(text):
    tokens=nltk.word_tokenize(text)
    return tokens

sample_inputs=[

    "This is Tubelight",
    "Hi I am a Editor",
    "from  Madurai",

]

for input_text in sample_inputs:
    tokens=tokenize_text(input_text)
    print(tokens)
    print("-----------------------------------")