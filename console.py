#!/usr/bin/python3
"""
console.py
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()