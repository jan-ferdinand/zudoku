---
layout: home
---
Peggy and Victor are competing on who can solve a certain Sudoku puzzle the fastest.
After racking her brain for hours, Peggy finds the solution – and she's first!
Now, she wants to prove to Victor that she has indeed solved the Sudoku.
Peggy is a good sport, and she doepsn't want to ruin Victor's fun.
This means that she cannot just show the solution to Victor.
Peggy appears to be in a pickle.

Luckily, Peggy has recently heard of _Zero-Knowledge Proof Systems_.
They seem to be the perfect solution to her problem.

This website shows how Peggy and Victor can use the  **zudoku** Zero-Knowledge Proof System to convince Victor that Peggy knows the solution while not giving Victor any hint about the solution.

This is immediately useful in proving knowledge of Sudoku solutions – obviously a very common problem.
Apart from that, it also demonstrates that Zero-Knowledge technology is not (necessarily) magic.
Also, zudoku does not need any maths.[^no-math]

# zudoku

The **zudoku**[^zudoku] proof system is an _interactive protocol_.
That means Peggy and Victor have to interact with one another for the entire thing to work.
Furthermore, they need a very few tools:
1. The Sudoku puzzle they are competing over, and
1. cards with one of the digits 1 to 9 on one side. All the cards need to have the same backside.

## crypto terms

### zero-knowledge

### correctness

### soundness

# further reading

For a technical, in-depth, hands-on tutorial on STARKs, I recommend [Alan Szepieniec](https://asz.ink/)'s excellent [STARK Anatomy](https://aszepieniec.github.io/stark-anatomy/).
Another great ressource, foccussed on SNARKs, is Z-Cash's [technology overview](https://z.cash/technology/zksnarks/).

# credits

I learned about zudoku from [Jörn Müller-Quade](https://crypto.iti.kit.edu/english/head-of-institute.php), who also introduced me to the marvelous world of crypto.[^crypto]


[^no-math]: Even though Sudokus are commonly presented with digits, you can use any symbols you want.
[^zudoku]: Zero-Knowledge (ZK) + Sudoku ⇒ *z*udo*k*u.
[^crypto]: [Crypto means Cryptography](https://en.wikipedia.org/wiki/Crypto_naming_controversy).