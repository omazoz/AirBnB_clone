#!/usr/bin/python3
"""Module for class HBNBCommand
"""
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """Class command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit to exit"""
        return True

    def do_EOF(self, line):
        """EOF to exit"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
