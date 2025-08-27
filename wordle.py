from itertools import product
import string
from spellchecker import SpellChecker

spell = SpellChecker()

letters = string.ascii_lowercase

known = input("What do you have so far? Use '_' for unknown letters (green letters): ").lower()
if len(known) != 5:
    print('Quit being stupid. You can only have 5 letters.')
    quit()
has = input("What letters are definitely in the word (yellow and green letters): ").lower()
if len(has) > 5:
    print('Quit being stupid. You can only have 5 letters.')
    quit()
allowed = input("Which letters are still allowed (yellow, green, and white letters): ").lower()
if len(allowed) > 26:
    print('So you can have more letters that are in the alphabet? Go to hell.')
    quit()

indices = {index: know for know, index in zip(known, range(len(known))) if know in letters}

all_words = list(product(letters, repeat=5))
for idx in indices:
    all_words = [word for word in all_words if word[idx] is indices[idx] and all(let in word for let in has) and all(letta in allowed for letta in word)]
words = '\n'.join([y for y in [''.join(x) for x in all_words] if y in spell])
if len(words.split('\n')) < 10:
    print('\nPossible words are as follows:')
    print(words)
    print()
else:
    print('Too many to print, go read "words.txt"')
with open('words.txt', 'w') as f:
    f.write(words)