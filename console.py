#!/usr/bin/python
"""
the Entry point
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    class that uesed to display prompt
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        implement quit function
        """
        return True

    def help_quit(self, arg):
        """help to get info about quiting"""

        print("Quit command to exit the program")
    
    def EOF(self, arg):
        """end of the file, handle no command inserted"""
        print()
        return True
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
