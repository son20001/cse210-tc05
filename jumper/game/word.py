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
        """

        Args: 
            self (Word): An instance of Word.
            letter (String): a character from user input
        
        Returns:
            boolean: True if the letter is in word, False if the letter is not in word
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
