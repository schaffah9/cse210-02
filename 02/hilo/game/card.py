class Card:
    """One of a set of 52 small rectangular pieces of stiff paper each with a number and one of four signs (suits) printed on it.

    The responsibility of Card is to keep track of its value and suit.
   
    Attributes:
        value (int): The number appearing on the card.
        suit (string): The suit appearing on the card.
    """

    def __init__(self, value, suit):
        """Constructs a new instance of Card with a value and suite attribute.
        
        Args:
            self (Card): an instance of Card.
            value (int): value of the Card.
            suit (string): suit of the Card.
        """
        self.value = value
        self.suit = suit

    def show(self):
        """Shows the card to the user by return its value and suit.

        Args:
            self (Card): An instance of Card.
        """
        return f'{self.value} {self.suit}'