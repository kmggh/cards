README Poker
============




Ken Guyton
Mon 2013-11-25 19:11:35 -0500




One of my colleagues is taking another class.  Time to try another
little exercise.

This program represents playing cards, a deck, a player, and a hand of
cards.  The hand object has the ability to classify what kind of hand
it is and to try to improve the hand by discarding a card and drawing
another.  At the moment the only strategy is to discard the lowest
non-N-kind card if it is a N-of-a-kind hand (including pairs).


To Run
------

    ./play_poker.py

    ./play_lots_of_poker.py


Bugs
----

An improvement would be to add some statistics, at least a breakdown
by percentages to the play_lots_of_poker.py script.

Currently you have to change program parameters by changing the code.
