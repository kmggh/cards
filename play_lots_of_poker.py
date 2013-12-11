#!/usr/bin/env python
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Play many poker hands."""

import cards
import hand
import player

NUM_HANDS = 1000


def improve_hand(the_player, deck):
  """Optionally throw out a card and draw another one."""

  this_hand = hand.Hand(the_player.cards())

  if this_hand.improve_hand():
    the_player._cards = list(this_hand._cards)
    the_player.draw(deck)


def play_hand():
  """Play a single hand and return the result.

  Returns:
    A str which is the classification of this hand.
  """

  deck = cards.Deck()
  deck.shuffle()

  player1 = player.Player('Player1')

  for unused_i in range(5):
    player1.draw(deck)

  # It's interesting to adjust the number of calls to improve_hand().
  improve_hand(player1, deck)
  improve_hand(player1, deck)

  return hand.Hand(player1.cards()).classify()


def main():
  results = {}
  for unused_count in range(NUM_HANDS):
    result = play_hand()
    if result in results:
      results[result] += 1
    else:
      results[result] = 1

  print 'Results\n'
  for key, value in results.items():
    print value, key


if __name__ == '__main__':
  main()
