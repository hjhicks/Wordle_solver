# Solves Those Bullshit Wordle Puzzles When They're Too Hard
The first input is what you know (the green letters). If you know that the fourth letter is an "e" your input should be: `___e_`.

The second input is the letters that are in the word but not ncessarily in the right place (the green and yellow letters). This includes the known letters. If you know that the word contains "e", "a", and "n", your input should be: `ean`.

The third input is the letters that are available for use (the green, yellow, and white letters). Potential input: `eioafgjzxvnm`

With these inputs, the program outputs:
```
annex
ganef
maven
nemea
nivea
zazen
```

From here, you can use your best judgement to make your guess.

Annex... the bullshit answer was Annex. I hate it here.

# Developer Notes
- Prolog could have done this easier
- I wrote this using as many ternaries and comprehensions as I could; enjoy figuring out what the hell my code does
- Go to hell
