from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

with open ("data/scene_one.txt") as scene_one:
    print(sent_tokenize(scene_one))