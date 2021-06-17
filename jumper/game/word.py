from jumper.game.director import FAILED
import random

FAILED = False

class Word:
    """A code template for a person who throws dice. The responsibility of this 
    class of objects is to throw the dice, keep track of the values, the score 
    and determine whether or not it can throw again.
    
    Attributes:
        dice (list): A list of five numbers representing the dice values.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Word): An instance of Word.
        """
        self.word = "accept"
        self.discovered_letter = []
        
    def test_letter(self, letter):
        """Determines whether or not the Word can throw again according to 
        the rules. 

        Args: 
            self (Word): An instance of Word.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """
        if letter in self.word:
            return True
        else:
            return FAILED
