from itertools import product
import string
from spellchecker import SpellChecker

spell = SpellChecker()

letters = string.ascii_lowercase

known = input("Use '_' for unknown letters: ")
has = input("What is in the word: ")
allowed = input("gib allowed alphabet: ")

indices = {know: index for know, index in zip(known, range(len(known))) if know in letters}
print(indices)
all_words = list(product(letters, repeat=5))
for letter in indices:
    all_words = [word for word in all_words if word[indices[letter]] is letter and all(let in word for let in has) and all(letta in allowed for letta in word)]
words = [''.join(x) for x in all_words]
with open('words.txt', 'w') as f:
    f.writelines([y+'\n' for y in words if y in spell])