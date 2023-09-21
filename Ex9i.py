import re
from collections import Counter
import math
def calculate_cosine_similarity(text1, text2):
    def tokenize(text):
        words=re.findall(r'\w+',text.lower())
        return Counter(words)
    vec1=tokenize(text1)
    vec2=tokenize(text2)
    intersection=set(vec1.keys()) & set(vec2.keys())

    dot_product=sum(vec1[word]*vec2[word] for word in intersection)
    magnitude1=math.sqrt(sum(vec1[word] ** 2 for word in vec1.keys()))
    magnitude2=math.sqrt(sum(vec2[word] ** 2 for word in vec2.keys()))
    cos_similarity=dot_product / (magnitude1*magnitude2)
    return cos_similarity
   
text1="I am in Kollam"
text2="I am in Sivakasi"
similarity=calculate_cosine_similarity(text1, text2)
print("cosine similarity:", similarity)
