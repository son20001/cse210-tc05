import random

FAILED = False

class Word:
    """a code template that representes hidden answer of the game
    
    Attributes:
        word (string): it is the answer of the game.
        discovered_letter (list): list of letters in word that player discovered
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Word): An instance of Word.
        """
        self.word = "accept"
        self.discovered_letter = []
        
    def test_letter(self, letter):
        """return True

        Args: 
            self (Word): An instance of Word.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """
        if letter in self.word:
            self.discovered_letter.append(letter)
            return True
        else:
            return FAILED
    
    def is_completed(self):
        if len(self.discovered_letter) == 0:
            return False
        word = list(self.word)

        for i in range(len(word)):
            if word[i] in self.discovered_letter:
                word[i] = " "

        result = True
        for i in word:
            if i != " ":
                result = False

        return result
