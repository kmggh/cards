# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""A hand of cards that can identify poker hands."""


class Hand(object):
  """The hand of cards."""

  def __init__(self, cards):
    """Initialize the hand with a tuple of Cards.

    Args:
      cards:  tuple of cards.Card.
    """

    self._cards = cards

  def rank_freq(self):
    """Return the frequency of each card rank.

    Returns:
      A dict with keys as card ranks and values a int count.
    """

    freq = {}
    for card in self._cards:
      rank = str(card.rank)
      if rank not in freq:
        freq[rank] = 1
      else:
        freq[rank] += 1

    return freq

  def freq_values(self, values):
    """Return the frequency of a list of values.

    Arg:
      values: list of anything.
    Returns:
      A dict with keys (from the input values)and the value an int for how
      many times the key occurred.
    """

    freq = {}

    for value in values:
      if value not in freq:
        freq[value] = 1
      else:
        freq[value] += 1

    return freq

  def is_pair(self):
    """See if there's one pair in a hand."""

    rank_freq = self.rank_freq()
    values_freq = self.freq_values(rank_freq.values())

    # Does a rank occur twice and is it only one rank.
    return 2 in values_freq and values_freq[2] == 1

  def is_two_pair(self):
    """See if there are two pair in the hand."""

    rank_freq = self.rank_freq()
    values_freq = self.freq_values(rank_freq.values())

    # Do two ranks appear twice.
    return 2 in values_freq and values_freq[2] == 2

  def is_three_kind(self):
    """See if there are three of a kind in the hand."""

    rank_freq = self.rank_freq()

    return 3 in rank_freq.values()

  def is_full_house(self):
    """See if there is a full house in the hand."""

    rank_freq = self.rank_freq()

    return 3 in rank_freq.values() and 2 in rank_freq.values()

  def is_four_kind(self):
    """See if there are four of a kind in the hand."""

    rank_freq = self.rank_freq()

    return 4 in rank_freq.values()

  def is_flush(self):
    """See if the hand is a flush with all the same suite."""

    freq_values = self.freq_values([str(c.suite) for c in self._cards])

    return 5 in freq_values.values()

  def classify(self):
    """Classify a hand.

    Returns:
      A str which is the classification, 'Pair', 'Two Pair', etc.
    """

    hand_type = 'Nothing'

    if self.is_straight_flush():
      hand_type = 'Straight Flush'
    if self.is_four_kind():
      hand_type = 'Four of a kind'
    elif self.is_full_house():
      hand_type = 'Full House'
    elif self.is_flush():
      hand_type = 'Flush'
    elif self.is_straight():
      hand_type = 'Straight'
    elif self.is_three_kind():
      hand_type = 'Three of a kind'
    elif self.is_two_pair():
      hand_type = 'Two pair'
    elif self.is_pair():
      hand_type = 'Pair'

    return hand_type

  def is_straight(self):
    """See if the hand is a straight."""

    indices = sorted([c.rank.index() for c in self._cards])
    return self.is_sequence(indices)

  def is_sequence(self, ints):
    """Determine if the tuple of ints is a sequence.

    Args:
      ints: iterable of int.  We assume the iterable is **sorted**.
    Returns:
      A bool that is True if the difference between each successive int
      and the current int is 1.
    """

    for i in range(len(ints) - 1):
      if ints[i + 1] - ints[i] != 1:
        return False

    return True

  def is_straight_flush(self):
    """See if the hand is a straight flush."""

    return self.is_straight() and self.is_flush()

  def improve_pair(self):
    """Toss out the lowest card not in the pair.

    We assume the current hand has one pair.

    The card is removed from the hand and returned.

    Returns:
      The removed Card.
    """

    rank_freq = self.rank_freq()

    min_card = None
    min_index = 0

    for i in range(len(self._cards)):
      card = self._cards[i]
      if rank_freq[str(card.rank)] > 1:
        continue
      if min_card is None or card.rank.index() < min_card.rank.index():
        min_card = card
        min_index = i

    new_list = list(self._cards)
    del new_list[min_index]
    self._cards = tuple(new_list)

    return min_card

  def improve_hand(self):
    """Discard an appropriate card to try to improve the hand.

    If there is no improvement we can guess at, just return None
    meaning we'll keep the cards as is.

    Returns:
      The removed Card or None.
    """

    if (self.is_pair() or self.is_two_pair() or self.is_three_kind
        or self.is_four_kind()):
      return self.improve_pair()
    else:
      return None
