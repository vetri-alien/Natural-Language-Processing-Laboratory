import re

def calculate_jaccard_similarity(text1,text2):
    def tokenize(text):
        words = re.findall(r'\w+', text.lower())
        return set(words)

    set1=tokenize(text1)
    set2=tokenize(text2)

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    jaccard_similarity=intersection/union

    return jaccard_similarity

text1="I am in Kollam"
text2="I am in Sivakasi"
similarity=calculate_jaccard_similarity(text1, text2)
print("Jaccard Similarity:", similarity)