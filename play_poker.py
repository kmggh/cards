#!/usr/bin/env python
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Play a hand of poker with two players."""

import cards
import hand
import player


def improve_hand(the_player, deck):
  """Optionally throw out a card and draw another one."""

  this_hand = hand.Hand(the_player.cards())

  if this_hand.improve_hand():
    the_player._cards = list(this_hand._cards)
    the_player.draw(deck)


def print_hands(player1, player2):
  """Print each player's hands."""

  print
  print 'Player1: ', player1.cards_long_str()
  print 'Player1: ', hand.Hand(player1.cards()).classify()
  print
  print 'Player2: ', player2.cards_long_str()
  print 'Player2: ', hand.Hand(player2.cards()).classify()
  print


def main():
  deck = cards.Deck()
  deck.shuffle()

  player1 = player.Player('Player1')
  player2 = player.Player('Player2')

  for a_player in player1, player2:
    for unused_i in range(5):
      a_player.draw(deck)

  print_hands(player1, player2)

  improve_hand(player1, deck)
  improve_hand(player2, deck)
  print_hands(player1, player2)

  improve_hand(player1, deck)
  improve_hand(player2, deck)
  print_hands(player1, player2)


if __name__ == '__main__':
  main()
