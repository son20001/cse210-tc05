class Console:
    def __init__(self):
        pass
    def print_jumper(self, jumper):
        if jumper.get_life() == 4:
            print('  ___\n /___\\\n \\   /\n  \\ /\n   0\n  /|\\\n  / \\\n\n^^^^^^^ ')
        elif jumper.get_life() == 3:
            print(' /___\\\n \\   /\n  \\ /\n   0\n  /|\\\n  / \\\n\n^^^^^^^ ')
        elif jumper.get_life() == 2:
            print(' \\   /\n  \\ /\n   0\n  /|\\\n  / \\\n\n^^^^^^^ ')
        elif jumper.get_life() == 1:
            print('  \\ /\n   0\n  /|\\\n  / \\\n\n^^^^^^^ ')
        elif jumper.get_life() == 0:
            print('   x\n  /|\\\n  / \\\n\n^^^^^^^ ')

    def print_word(self, word):
        for i in word.word:
            result = False
            for letter in word.discovered_letter:
                if letter == i:
                    result = True
            if result == True:
                print(i + " ", end = '')
            else:
                print("_ ", end = '')
        print("")

        
    def read_letter(self, question):
        return input(question)