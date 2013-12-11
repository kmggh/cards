#!/usr/bin/env python

"""Test a playing card."""

import cards
import random
import unittest

RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

SHUFFLED_DECK = ("('2C', '9H', '3C', 'QS', '4C', '4S', '5C', '5H', '6C', "
                 "'KH', '7C', '8S', '8C', '3H', '9C', '7H', '10C', 'JH', "
                 "'JC', '2S', 'QC', '6S', 'KC', '10S', 'AC', 'AS', '2D', "
                 "'4H', '3D', '6H', '4D', '8H', '5D', '10H', '6D', 'QH', "
                 "'7D', 'AH', '8D', '3S', '9D', '5S', '10D', '7S', 'JD', "
                 "'9S', 'QD', 'JS', 'KD', 'KS', 'AD', '2H')")

_SHUFFLED_DECK = ("('AC', '5H', 'KC', '6S', 'JC', 'JS', 'QC', 'QH', '10C', "
                 "'9H', '3C', '2S', '2C', 'KH', '5C', '3H', '4C', '7H', "
                 "'7C', 'AS', '6C', '10S', '9C', '4S', '8C', '8S', 'AD', "
                 "'JH', 'KD', '10H', 'JD', '2H', 'QD', '4H', '10D', '6H', "
                 "'3D', '8H', '2D', 'KS', '5D', 'QS', '4D', '3S', '7D', "
                 "'5S', '6D', '7S', '9D', '9S', '8D', 'AH')")


class FakeRandom(object):
  """A Fake Random object class."""

  def __init__(self):
    pass

  def random(self):
    """Random number function."""

    return 0.5


class TestSuites(unittest.TestCase):
  def test_suites(self):
    self.assertEqual(str(cards.CLUBS), 'Clubs')
    self.assertEqual(str(cards.DIAMONDS), 'Diamonds')
    self.assertEqual(str(cards.HEARTS), 'Hearts')
    self.assertEqual(str(cards.SPADES), 'Spades')


class TestRank(unittest.TestCase):
  def test_ranks(self):
    for rank_str in cards.RANKS_STR:
      a_rank = cards.Rank(rank_str)

  def test_precedence(self):
    for index in range(len(RANKS) - 1):
      self.assertTrue((cards.RANKS[index] < cards.RANKS[index + 1]))
      self.assertTrue((cards.RANKS[index].index() <
                       cards.RANKS[index + 1].index()))

  def test_str(self):
    for a_rank, a_str in zip(cards.RANKS, RANKS):
      self.assertEqual(str(a_rank), a_str)

  def test_eq(self):
    rank1 = cards.Rank('5')
    rank2 = cards.Rank('5')
    self.assertEqual(rank1, rank2)

  def test_not_eq(self):
    rank1 = cards.Rank('5')
    rank2 = cards.Rank('4')
    self.assertTrue((rank1 != rank2))

  def test_index(self):
    self.assertEqual(cards.Rank('5').index(), 5)
    self.assertEqual(cards.Rank('J').index(), 11)
    self.assertEqual(cards.Rank('A').index(), 14)


class TestCard(unittest.TestCase):
  def setUp(self):
    self.a_card = cards.Card(cards.Rank('2'), cards.CLUBS)

  def test_create(self):
    self.assertNotEqual(self.a_card, None)
    self.assertIsInstance(self.a_card, cards.Card)

  def test_str(self):
    self.assertEqual(str(self.a_card), '2C')

  def test_str_king(self):
    self.a_card = cards.Card(cards.Rank('K'), cards.HEARTS)
    self.assertEqual(str(self.a_card), 'KH')

  def test_str_ten(self):
    self.a_card = cards.Card(cards.Rank('10'), cards.DIAMONDS)
    self.assertEqual(str(self.a_card), '10D')

  def test_long_str(self):
    self.assertEqual(self.a_card.long_str(), '2 clubs')

  def test_str_king(self):
    self.a_card = cards.Card(cards.Rank('K'), cards.HEARTS)
    self.assertEqual(self.a_card.long_str(), 'K hearts')

  def test_str_ten(self):
    self.a_card = cards.Card(cards.Rank('10'), cards.DIAMONDS)
    self.assertEqual(self.a_card.long_str(), '10 diamonds')


class TestDeck(unittest.TestCase):
  def setUp(self):
    self.deck = cards.Deck()

  def test_create(self):
    self.assertNotEqual(self.deck, None)
    self.assertIsInstance(self.deck, cards.Deck)

  def test_sorted_deck(self):
    self.assertEqual(str(self.deck.list[0]), '2C')
    self.assertEqual(str(self.deck.list[13]), '2D')
    self.assertEqual(str(self.deck.list[24]), 'KD')
    self.assertEqual(str(self.deck.list[25]), 'AD')
    self.assertEqual(str(self.deck.list[34]), '10H')
    self.assertEqual(str(self.deck.list[51]), 'AS')

  def test_shuffle(self):
    fake = FakeRandom()

    self.deck.shuffle(fake.random)
    # random.shuffle(self.deck.list, fake.random)
    self.assertEqual(str(self.deck), SHUFFLED_DECK)

  def test_draw(self):
    self.assertEqual(str(self.deck.draw()), '2C')
    self.assertEqual(str(self.deck.draw()), '3C')
    self.assertEqual(len(self.deck.list), 50)


if __name__ == '__main__':
  unittest.main()
