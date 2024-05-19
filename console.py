#!/usr/bin/python
"""
the Entry point
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    class that uesed to display prompt
    """
    prompt = "(hbnb) "

    def do_quit(self, _):
        """
        implement quit function
        """
        return True

    def help_quit(self, arg):
        """help to get info about quiting"""

        print("Quit command to exit the program")
    
    def emptyline(self):
        """Do nothing on empty line"""
        pass

    do_EOF = do_quit
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
