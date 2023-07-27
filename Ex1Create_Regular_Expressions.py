import re

def detect_word_pattern(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        print("Word patterns detected:")
        for match in matches:
            print(match)
    else:
        print("No word patterns detected.")
# sample inputs and outputs
sample_inputs = [
    ("[0-9]+","The price is $25 and the quantity is 10."),
    ("[A-Z][a-z]+","John and Alice went to the park."),
    ("[aeiou]+","The quick brown for jumps over the lazy dog."),
    ("[0-9]{2}-[0-9]{2}-[0-9]{4}","The date is 12-31-2022."),
    ("[A-Za-z]+","12345 is a number.")
]

for pattern, text in sample_inputs:
    print("patterns:",pattern)
    print("Text:",text)
    detect_word_pattern(pattern, text)
    print("-------------------")
