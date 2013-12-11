# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""A representation of a card player.

A player can draw and hold cards.
"""


class Player(object):
  """The player class."""

  def __init__(self, name):
    """Initialize the player and his name.

    Args:
      name: str.
    """

    self.name = name
    self._cards = []

  def cards(self):
    """Return a tuple of the cards the player is holding."""

    return tuple(self._cards)

  def draw(self, deck):
    """Draw a card from the deck."""

    self._cards.append(deck.draw())

  def cards_str(self):
    """Print out the held cards.

    Returns:
      A str with each card as its str representation.
    """

    return tuple([str(c) for c in self.cards()])

  def cards_long_str(self):
    """Return the held cards in the longer format with suites spelled out.

    Returns:
      A str with each card in a long representation.
    """

    sorted_cards = sorted(self._cards, key=lambda c: c.rank)

    return tuple([c.long_str() for c in sorted_cards])
