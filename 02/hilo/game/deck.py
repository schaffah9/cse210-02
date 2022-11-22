from game.card import Card
import random

class Deck:
    """A set of 52 cards used for playing card games.

    The responsibility of Deck is to keep track of the Cards contained in it.
   
    Attributes:
        cards (list[Card]): A list of Card instances.
    """
    def __init__(self):
        """Constructs a new instance of Deck.

        Args:
            self (Deck): An instance of Deck.
        """
        self.cards = []
        self.build()

    def build(self):
        """Builds the Deck by adding Cards to it.

        Args:
            self (Deck): An instance of Deck.
        """
        suits = ['♠','♥','♦','♣']
        values = range(1,14)
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        """Changes the order of the Cards in the Deck randomly.

        Args:
            self (Deck): An instance of Deck.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """Takes a Card from the Deck and shows it to the user.

        Args:
            self (Deck): An instance of Deck.

        Returns: 
            Card: The Card instance taken from the Deck.
        """
        return self.cards.pop()