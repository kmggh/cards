#!/usr/bin/env python

"""Test a card player."""

import cards
import player
import unittest

PLAYER_NAME = 'Kirk.'


class TestPlayer(unittest.TestCase):
  def setUp(self):
    self.player = player.Player(PLAYER_NAME)
    self.deck = cards.Deck()

  def test_create(self):
    self.assertNotEqual(self.player, None)
    self.assertEqual(self.player.cards(), ())

  def test_draw(self):
    self.player.draw(self.deck)
    self.assertEqual([str(c) for c in self.player.cards()], ['2C'])

  def test_cards_str(self):
    self.player.draw(self.deck)
    self.player.draw(self.deck)
    self.player.draw(self.deck)

    self.assertEqual(self.player.cards_str(), ('2C', '3C', '4C'))

  def test_cards_long_str(self):
    self.player.draw(self.deck)
    self.player.draw(self.deck)
    self.player.draw(self.deck)

    self.assertEqual(self.player.cards_long_str(), ('2 clubs', '3 clubs',
                                                    '4 clubs'))


if __name__ == '__main__':
  unittest.main()
