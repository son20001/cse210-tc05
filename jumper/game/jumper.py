FAILED = False

class Jumper:
    """
    
    Attributes:
        life (int): A chance that player try answering
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Word): An instance of Word.
        """
        self.life = 4
        
    def decrease_life(self):
        """Determines whether or not the Word can throw again according to 
        the rules. 

        Args: 
            self (Word): An instance of Word.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """
        self.life -= 1

    def get_life(self):
        """
        Args: 
            self (Word): An instance of Word.
        
        Returns:
            int: return life
        """
        return self.life

    def is_alive(self):
        """
        Args: 
            self (Word): An instance of Word.
        
        Returns:
            boolean: Return True if life is greater than 0, or return false
        """
        if self.life > 0:
            return True
        else:
            return False
