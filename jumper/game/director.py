from game.console import Console
from game.jumper import Jumper
from game.word import Word

FAILED = False

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        word (Word): An instance of the class of objects known as Word.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
        self.letter = ""
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """

        self.do_outputs()
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.letter = self.console.read_letter("Guess a letter [a-z]: ")
        
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
        if self.word.test_letter(self.letter) == FAILED:
            self.jumper.decrease_life()
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        self.console.print_word(self.word)
        self.console.print_jumper(self.jumper)
        if (not self.jumper.is_alive()) or (self.word.is_completed()):
            self.keep_playing = False
