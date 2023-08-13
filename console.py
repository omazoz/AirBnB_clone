#!/usr/bin/python3
"""Module for class HBNBCommand
"""
from models.base_model import BaseModel
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Class command interpreter"""
    prompt = "(hbnb) "
    __list_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        ]

    def do_quit(self, line):
        """Quit to exit"""
        return True

    def do_EOF(self, line):
        """EOF to exit"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.__list_classes:
            print("** class doesn't exist **")
        else:
            obj = eval(line)
            obj.save(self)
            # print(obj.id)
            # models.storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        x = line.split()
        list_obj = models.storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif x[0] not in HBNBCommand.__list_classes:
            print("** class doesn't exist **")
        elif len(x) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(x[0], x[1]) not in list_obj.keys():
            print("** no instance found **")
        else:
            print(list_obj["{}.{}".format(x[0], x[1])])

    def do_destroy(self, line):
        """Delete a class instance of a given id."""
        list_obj = models.storage.all()
        x = line.split()

        if len(x) == 0:
            print("** class name missing **")
        elif x[0] not in HBNBCommand.__list_classes:
            print("** class doesn't exist **")
        elif len(x) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(x[0], x[1]) not in list_obj.keys():
            print("** no instance found **")
        else:
            del list_obj["{}.{}".format(x[0], x[1])]
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
