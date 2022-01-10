---
layout: home
---
Peggy and Victor are competing on who can solve a certain Sudoku puzzle the fastest.
After racking her brain for hours, Peggy finds the solution – and she's first!
Now, she wants to prove to Victor that she has indeed solved the Sudoku.
Peggy is a good sport, and she doesn't want to ruin the puzzle for Victor.
This means that she cannot just show the solution to Victor.
Peggy appears to be in a pickle.

Luckily, Peggy has recently heard of _Zero-Knowledge Proof Systems_.
They seem to be the perfect solution to her problem.

Peggy and Victor can use the **zudoku** Zero-Knowledge Proof System to convince Victor that Peggy knows the solution – and Victor won't get any hint about the solution.

**zudoku** is immediately useful in proving knowledge of Sudoku solutions – obviously a very common problem.
Apart from that, it also demonstrates that Zero-Knowledge technology is not (necessarily) magic.
**zudoku** is very intuitive, and does not need any mathematics.<label for="sn-no-maths" class="margin-toggle sidenote-number"> </label><input type="checkbox" id="sn-no-maths" class="margin-toggle"/>
<span class="sidenote">
	This is also true for Sudokus: instead of digits, you can use any symbols you want.
</span> 

# zudoku

The **zudoku**<label for="sn-zudoku" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-zudoku" class="margin-toggle"/> 
<span class="sidenote">
	Zero-Knowledge (ZK) + Sudoku ⇒ **zudoku**.
</span> 
proof system is an _interactive protocol_.
That means Peggy and Victor have to play together for the entire thing to work.
<!-- explain Sudoku rules? -->

Furthermore, Peggy needs some cards.
All cards need to have the same backside.
The front of a card is one of the digits appearing in the Sudoku.
Peggy will lay out her solution using these cards, so she needs at least nine cards of every digit.

Lastly, Peggy and Victor need the Sudoku puzzle they are playing **zudoku** with.
They have chosen a Sudoku called “AI Escargot”, which is extremely difficult to solve.
Victor has printed the Sudoku.
Printing the puzzle is not necessary, it just makes playing **zudoku** more convenient.

### setup

Once Peggy has her cards and Victor has the Sudoku, they start with the setup for **zudoku**.
Peggy and Victor use Peggy's cards to mimic the givens of the Sudoku:
every digit printed on the grid is covered with a card showing the same digit, with the digit visible.

When all printed digits are covered, the Sudoku essentially still looks the same.
However, instead of Victor's print-out, Peggy's cards are used.

### solve

Peggy puts the solution with her cards facing down into the free cells.
She needs to make sure that Victor can't tell which card she puts where – otherwise she would be giving him hints!

When Peggy is done putting down the solution, she turns around all cards that are still showing a digit.
The board is now completely filled with cards facing down.

### check

Now it's Victor's turn.
Theoretically, he could just turn all or some cards around – but that way he'd learn something about the solution!
Instead, Victor chooses whether he wants to check the Sudokus's rows, or the columns, or the boxes.

Victor chooses to check the rows.
He takes all nine cards in the first row, shuffles them, and turns them around.
Then he checks that all digits, 1 to 9, are there – none missing, none double.
Since Peggy has put the correct solution for the Sudoku, this is exactly what he finds.

Shuffling the cards makes sure that Victor does not know the position of a card on the board.
This way, even after turning the cards around, he doesn't know anynthing about the solution.

He proceeds to the next row, takes the cards, shuffles them, then turns them around.
Again, he checks that the rules of Sudoku are followed – all digits appear exactly once.

This way, Victor checks all rows.
If, in any row, he were to find some digit twice, he would know that the rules of Sudoku were violated – which would mean that Peggy did not actually put the solution in the board!
But Peggy has put the real solution, so for every row, Victor finds every digit exactly once.

### repeat

Even though Victor has confirmed that Peggy has put her cards in a way that the rows comply with the Sudoku rules, he is not convinced yet.
After all, the rules of Sudoku apply to rows, columns and boxes, not just to rows!
He tells Peggy that he wants to go again.

As before, they set up the Sudoku puzzle by placing cards face-up on the printed digits, and Peggy lays in the solution again.
Now, Victor can make the same choice as before:
check the rows, or the columns, or the boxes.
Again, he verifies that the corresponding sections comply with Sudoku rules by shuffling and turning over the cards.

If Victor is still not convinced, he asks Peggy to go again.
And again.
And maybe one more time?

Finally, Victor is convinced that Peggy does really know the solution.
But why can he be so sure that Peggy didn't cheat?

## catching cheaters

The mischievious Mallory overheard Peggy and Victor perform **zudoku**.
Mallory is not a great Sudoku puzzler, and she does not know the solution.
However, she thinks that using **zudoku**, she can trick Victor into believing that she knows the solution.

# further reading

For a technical, in-depth, hands-on tutorial on STARKs, I recommend [Alan Szepieniec](https://asz.ink/)'s excellent [STARK Anatomy](https://aszepieniec.github.io/stark-anatomy/).
Another great ressource, foccussed on SNARKs, is [Z-Cash's technology overview](https://z.cash/technology/zksnarks/).

# credits

I learned about **zudoku** from [Jörn Müller-Quade](https://crypto.iti.kit.edu/english/head-of-institute.php), who also introduced me to the marvelous world of crypto.<label for="mn-crypto" class="margin-toggle">&#8853;</label><input type="checkbox" id="mn-crypto" class="margin-toggle"/>
<span class="marginnote">
	[“Crypto” means Cryptography](https://en.wikipedia.org/wiki/Crypto_naming_controversy).
</span>

The Sudoku “AI Escargot” was created by [Arto Inkala](http://aisudoku.com/index_en.html) and is reproduced here with his friendly permission.

This website is statically rendered by [Jekyll](https://jekyllrb.com/) with the [Basically Basic](https://github.com/mmistakes/jekyll-theme-basically-basic) theme and hosted by [GitHub Pages](https://pages.github.com/).
