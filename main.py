import random
from collections import defaultdict

text = open('che.txt', encoding='utf8').read()
corpus = text.split()
def make_triples(corpus):
     for i in range(len(corpus)-2):
         yield (corpus[i], corpus[i+1], corpus[i+2])

triples = make_triples(corpus)
def make_chain(triples):
    chain = defaultdict(list)
    for word_1, word_2, word_3 in triples:
        chain[(word_1, word_2)].append(word_3)
    return chain

chain = make_chain(triples)
def generate_text(chain, max_length=100):
    keys = list(chain.keys())
    first_words = random.choice([key for key in keys if key[0][0].isupper()])
    word_1, word_2 = first_words
    new_text = [word_1, word_2]
    while len(new_text) < max_length:
        word_1, word_2 = word_2, random.choice(chain[(word_1, word_2)])
        new_text.append(word_2)
    return ' '.join(new_text)

new_text = generate_text(chain)
print(new_text)