#!/usr/bin/env python
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Test a card hand."""

import cards
import hand
import unittest

HAND_NAME = 'Kirk.'

NOTHING_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                cards.Card(cards.Rank('3'), cards.DIAMONDS),
                cards.Card(cards.Rank('5'), cards.HEARTS),
                cards.Card(cards.Rank('6'), cards.SPADES),
                cards.Card(cards.Rank('J'), cards.CLUBS))

FLUSH_HAND = (cards.Card(cards.Rank('2'), cards.HEARTS),
              cards.Card(cards.Rank('3'), cards.HEARTS),
              cards.Card(cards.Rank('5'), cards.HEARTS),
              cards.Card(cards.Rank('6'), cards.HEARTS),
              cards.Card(cards.Rank('J'), cards.HEARTS))

PAIR_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
             cards.Card(cards.Rank('2'), cards.DIAMONDS),
             cards.Card(cards.Rank('3'), cards.HEARTS),
             cards.Card(cards.Rank('4'), cards.SPADES),
             cards.Card(cards.Rank('5'), cards.CLUBS))

TWO_PAIR_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                 cards.Card(cards.Rank('2'), cards.DIAMONDS),
                 cards.Card(cards.Rank('3'), cards.HEARTS),
                 cards.Card(cards.Rank('3'), cards.SPADES),
                 cards.Card(cards.Rank('5'), cards.CLUBS))

THREE_KIND_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                   cards.Card(cards.Rank('2'), cards.DIAMONDS),
                   cards.Card(cards.Rank('2'), cards.HEARTS),
                   cards.Card(cards.Rank('4'), cards.SPADES),
                   cards.Card(cards.Rank('5'), cards.CLUBS))

FULL_HOUSE_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                   cards.Card(cards.Rank('2'), cards.DIAMONDS),
                   cards.Card(cards.Rank('2'), cards.HEARTS),
                   cards.Card(cards.Rank('4'), cards.SPADES),
                   cards.Card(cards.Rank('4'), cards.CLUBS))

FOUR_KIND_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                  cards.Card(cards.Rank('2'), cards.DIAMONDS),
                  cards.Card(cards.Rank('2'), cards.HEARTS),
                  cards.Card(cards.Rank('2'), cards.SPADES),
                  cards.Card(cards.Rank('4'), cards.CLUBS))

STRAIGHT_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                 cards.Card(cards.Rank('3'), cards.DIAMONDS),
                 cards.Card(cards.Rank('4'), cards.HEARTS),
                 cards.Card(cards.Rank('5'), cards.SPADES),
                 cards.Card(cards.Rank('6'), cards.CLUBS))

STRAIGHT_FLUSH_HAND = (cards.Card(cards.Rank('2'), cards.CLUBS),
                       cards.Card(cards.Rank('3'), cards.CLUBS),
                       cards.Card(cards.Rank('4'), cards.CLUBS),
                       cards.Card(cards.Rank('5'), cards.CLUBS),
                       cards.Card(cards.Rank('6'), cards.CLUBS))


class TestHand(unittest.TestCase):
  def setUp(self):
    self.hand = hand.Hand(PAIR_HAND)

  def test_create(self):
    self.assertNotEqual(self.hand, None)

  def test_is_pair(self):
    self.assertTrue(hand.Hand(PAIR_HAND).is_pair())
    self.assertFalse(hand.Hand(NOTHING_HAND).is_pair())
    self.assertFalse(hand.Hand(TWO_PAIR_HAND).is_pair())
    self.assertFalse(hand.Hand(THREE_KIND_HAND).is_pair())
    self.assertTrue(hand.Hand(FULL_HOUSE_HAND).is_pair())
    self.assertFalse(hand.Hand(FOUR_KIND_HAND).is_pair())
    self.assertFalse(hand.Hand(FLUSH_HAND).is_pair())

  def test_is_two_pair(self):
    self.assertFalse(hand.Hand(PAIR_HAND).is_two_pair())
    self.assertFalse(hand.Hand(NOTHING_HAND).is_two_pair())
    self.assertTrue(hand.Hand(TWO_PAIR_HAND).is_two_pair())
    self.assertFalse(hand.Hand(THREE_KIND_HAND).is_two_pair())
    self.assertFalse(hand.Hand(FULL_HOUSE_HAND).is_two_pair())
    self.assertFalse(hand.Hand(FOUR_KIND_HAND).is_two_pair())
    self.assertFalse(hand.Hand(FLUSH_HAND).is_two_pair())

  def test_is_three_kind(self):
    self.assertFalse(hand.Hand(PAIR_HAND).is_three_kind())
    self.assertFalse(hand.Hand(NOTHING_HAND).is_three_kind())
    self.assertFalse(hand.Hand(TWO_PAIR_HAND).is_three_kind())
    self.assertTrue(hand.Hand(THREE_KIND_HAND).is_three_kind())
    self.assertTrue(hand.Hand(FULL_HOUSE_HAND).is_three_kind())
    self.assertFalse(hand.Hand(FOUR_KIND_HAND).is_three_kind())
    self.assertFalse(hand.Hand(FLUSH_HAND).is_three_kind())

  def test_is_full_house(self):
    self.assertFalse(hand.Hand(PAIR_HAND).is_full_house())
    self.assertFalse(hand.Hand(NOTHING_HAND).is_full_house())
    self.assertFalse(hand.Hand(TWO_PAIR_HAND).is_full_house())
    self.assertFalse(hand.Hand(THREE_KIND_HAND).is_full_house())
    self.assertTrue(hand.Hand(FULL_HOUSE_HAND).is_full_house())
    self.assertFalse(hand.Hand(FOUR_KIND_HAND).is_full_house())
    self.assertFalse(hand.Hand(FLUSH_HAND).is_full_house())

  def test_is_four_kind(self):
    self.assertFalse(hand.Hand(PAIR_HAND).is_four_kind())
    self.assertFalse(hand.Hand(NOTHING_HAND).is_four_kind())
    self.assertFalse(hand.Hand(TWO_PAIR_HAND).is_four_kind())
    self.assertFalse(hand.Hand(THREE_KIND_HAND).is_four_kind())
    self.assertFalse(hand.Hand(FULL_HOUSE_HAND).is_four_kind())
    self.assertTrue(hand.Hand(FOUR_KIND_HAND).is_four_kind())
    self.assertFalse(hand.Hand(FLUSH_HAND).is_four_kind())

  def test_is_flush(self):
    self.assertTrue(hand.Hand(FLUSH_HAND).is_flush())

  def test_rank_freq(self):
    freq = self.hand.rank_freq()

    self.assertEqual(freq['2'], 2)
    self.assertEqual(freq['3'], 1)
    self.assertEqual(freq['4'], 1)
    self.assertEqual(freq['5'], 1)

  def test_freq_values(self):
    a_dict = self.hand.freq_values([2, 1, 1, 1])

    self.assertEqual(a_dict[2], 1)
    self.assertEqual(a_dict[1], 3)

  def test_classify(self):
    self.assertEqual(hand.Hand(PAIR_HAND).classify(), 'Pair')
    self.assertEqual(hand.Hand(NOTHING_HAND).classify(), 'Nothing')
    self.assertEqual(hand.Hand(TWO_PAIR_HAND).classify(), 'Two pair')
    self.assertEqual(hand.Hand(THREE_KIND_HAND).classify(), 'Three of a kind')
    self.assertEqual(hand.Hand(FULL_HOUSE_HAND).classify(), 'Full House')
    self.assertEqual(hand.Hand(FOUR_KIND_HAND).classify(), 'Four of a kind')
    self.assertEqual(hand.Hand(STRAIGHT_HAND).classify(), 'Straight')
    self.assertEqual(hand.Hand(FLUSH_HAND).classify(), 'Flush')
    self.assertEqual(hand.Hand(STRAIGHT_FLUSH_HAND).classify(),
                     'Straight Flush')

  def test_straight(self):
    self.assertTrue(hand.Hand(STRAIGHT_HAND).is_straight())
    self.assertFalse(hand.Hand(NOTHING_HAND).is_straight())
    self.assertFalse(hand.Hand(PAIR_HAND).is_straight())

  def test_is_sequence(self):
    self.assertTrue(self.hand.is_sequence((3, 4, 5, 6, 7)))
    self.assertFalse(self.hand.is_sequence((3, 4, 5, 7)))

  def test_is_straight_flush(self):
    self.assertTrue(hand.Hand(STRAIGHT_FLUSH_HAND).is_straight_flush())
    self.assertFalse(hand.Hand(STRAIGHT_HAND).is_straight_flush())
    self.assertFalse(hand.Hand(FLUSH_HAND).is_straight_flush())

  def test_improve_pair(self):
    self.hand = hand.Hand(PAIR_HAND)
    card = self.hand.improve_pair()

    # We toss the lowest card not in the pair.
    self.assertEqual(str(card), '3H')
    self.assertEqual(len(self.hand._cards), 4)

  def test_improve_hand_pair(self):
    self.hand = hand.Hand(PAIR_HAND)
    card = self.hand.improve_hand()

    # We toss the lowest card not in the pair.
    self.assertEqual(str(card), '3H')
    self.assertEqual(len(self.hand._cards), 4)

  def test_improve_twopair(self):
    self.hand = hand.Hand(TWO_PAIR_HAND)
    card = self.hand.improve_pair()

    # We toss the lowest card not in the pair.
    self.assertEqual(str(card), '5C')
    self.assertEqual(len(self.hand._cards), 4)

  def test_improve_three_kind(self):
    self.hand = hand.Hand(THREE_KIND_HAND)
    card = self.hand.improve_pair()

    # We toss the lowest card not in the pair.
    self.assertEqual(str(card), '4S')
    self.assertEqual(len(self.hand._cards), 4)

  def test_improve_four_kind(self):
    self.hand = hand.Hand(FOUR_KIND_HAND)
    card = self.hand.improve_pair()

    # We toss the lowest card not in the pair.
    self.assertEqual(str(card), '4C')
    self.assertEqual(len(self.hand._cards), 4)


if __name__ == '__main__':
  unittest.main()
