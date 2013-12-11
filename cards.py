"""A representation of playing cards."""

import random


class EnumerateError:
  """Raised when an enumeration is set to an invalid name."""


class EnumerateSuites(object):
  """Enumerate suites of cards."""

  def __init__(self, name):
    """Initialize with the name."""

    if name not in self.allowed_names():
      msg = 'Not a valid name: {0}.'.format(name)
      raise EnumerateError(msg)

    self.name = name

  def allowed_names(self):
    """The list of allowed names."""

    return ('Clubs', 'Diamonds', 'Hearts', 'Spades')

  def __str__(self):
    """Return the name."""

    return self.name

  def __eq__(self, other):
    """Test equality two instances.

    Args:
      other:  Another instance of the same type.
    Returns:
      The == the names.
    """

    return self.name == other.name

  def __ne__(self, other):
    """Compare two instances.

    Args:
      other:  Another instance of the same type.
    Returns:
      The !=  the names.
    """

    return self.name != other.name


CLUBS = EnumerateSuites('Clubs')
DIAMONDS = EnumerateSuites('Diamonds')
HEARTS = EnumerateSuites('Hearts')
SPADES = EnumerateSuites('Spades')

RANKS_STR = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

RANKS_DICT = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


class Rank(EnumerateSuites):
  """A rank representing the rank of a card."""

  def __init__(self, name):
    """Initialize with a name and an index."""

    EnumerateSuites.__init__(self, name)

    self._index = RANKS_DICT[name]

  def allowed_names(self):
    """Allowed rank names."""

    return RANKS_DICT.keys()

  def index(self):
    """Return the int index."""

    return self._index


RANKS = [Rank(s) for s in RANKS_STR]


class Card(object):
  """A representation of a playing card."""

  def __init__(self, rank, suite):
    """Initialize the rank and suite of a card.

    Args:
      rank: A Rank.
      suite: A suite from above.  E.g., CLUBS, DIAMONDS, etc.
    """

    self.rank = rank
    self.suite = suite

  def __str__(self):
    """Convert to a str."""

    return '{0}{1}'.format(str(self.rank), str(self.suite)[0])

  def long_str(self):
    """Convert to the long-style str."""

    return '{0} {1}'.format(str(self.rank), str(self.suite).lower())


class Deck(object):
  """A full deck of 52 cards, of all suites and ranks."""

  def __init__(self):
    """Initialize the full deck."""

    self.list = []

    for suite in (CLUBS, DIAMONDS, HEARTS, SPADES):
      for rank in RANKS:
        self.list.append(Card(rank, suite))

  def __str__(self):
    """Convert the deck to a str.  Return a tuple of str of each card."""

    return str(tuple([str(x) for x in self.list]))

  def draw(self):
    """Draw and return a card from the deck.

    Returns:
      A Card object.
    """

    return self.list.pop(0)

  def shuffle(self, random_function=random.random):
    """Shuffle the deck."""

    random.shuffle(self.list, random_function)
