from game.deck import Deck

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (Deck): Deck of Cards used to play the game.
        is_playing (boolean): Whether or not the game is being played.
        point_total (int): The score for the entire game.
        current_card (Card): The Card currently showing.
        next_card (Card): Next Card drawn.
        play (string): play made by the player.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.is_playing = True
        self.point_total = 300
        
        self.deck.shuffle()
        self.current_card = self.deck.draw_card()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print('Welcome to HiLo. Let\'s begin')
        while self.is_playing:
            if len(self.deck) < 5:
                self.deck = Deck()

            self.next_card = self.deck.draw_card()

            print()
            self.ask_play()
            self.do_updates()
            self.do_outputs()

    def ask_play(self):
        """Ask the user if the next card will be higher or lower than the current card.

        Args:
            self (Director): An instance of Director.
        """
        self.show_current_card()
        is_valid_play = None
        while not is_valid_play:
            self.play = input("Higher or lower? [h/l] ").lower()
            is_valid_play = self.validate_play(self.play)

    def show_current_card(self):
        """Shows the user the current card in play.

        Args:
            self (Director): An instance of Director.
        """
        print(f'The card is: {self.current_card.show()}')

    def validate_play(self, play):
        """Checks if the play is valid or not.

        Args:
            play (string): user input.

        Returns:
            valid (boolean): True if valid; False if otherwise.
        """
        valid = (play == 'h' or play == 'l')
        if not valid:
            print('Invalid play. Please try again')
        return valid

    def do_updates(self):
        """Updates game state.

        Args:
            self (Director): An instance of Director.
        """
        result = self.evaluate_play()
        self.point_total += result

        self.current_card = self.next_card

    def evaluate_play(self):
        """Computes the resulting score of the play and returns it.

        Args:
            self (Director): An instance of Director.

        Returns:
            int: Resulting score of the play.
        """
        if self.next_card.value == self.current_card.value:
            return 0
        
        if self.play == 'h':
            guessed_right = (self.next_card.value > self.current_card.value)
        if self.play == 'l':
            guessed_right = (self.next_card.value < self.current_card.value)

        return 100 if guessed_right else -75

    def do_outputs(self):
        """Displays next card and the score. Also asks the player if they want to keep playing. 

        Args:
            self (Director): An instance of Director.
        """
        self.show_next_card()
        print(f'Your score is {self.point_total}')
        if self.point_total <= 0:
            self.is_playing = False
        
        if not self.is_playing:
            self.end_game()
        else:
            is_valid_answer = None
            while not is_valid_answer:
                answer = input('Play again? [y/n] ').lower()
                is_valid_answer = self.validate_answer(answer)
            self.is_playing = (answer == 'y')
            if not self.is_playing:
                self.end_game()
    
    def show_next_card(self):
        """Shows the user the next card in play.

        Args:
            self (Director): An instance of Director.
        """
        print(f'Next card was: {self.next_card.show()}')
    
    def validate_answer(self, answer):
        """Checks if the input answer is valid or not.

        Args:
            answer (string): user input.

        Returns:
            valid (boolean): True if valid; False if otherwise.
        """
        valid = (answer == 'y' or answer == 'n')
        if not valid:
            print('Invalid answer. Please try again')
        return valid

    def end_game(self):
        print("Game over! Thanks for playing.")
        