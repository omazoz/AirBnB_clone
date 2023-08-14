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
            print(eval(line)().id)
            models.storage.save()

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

    def do_all(self, line):
        """Prints all string representation of all instances"""

        if len(line) > 0:
            if line not in HBNBCommand.__list_classes:
                print("** class doesn't exist **")
            else:
                objl = []
                for obj in models.storage.all().values():
                    objl.append(obj.__str__())

                print(objl)
        else:
            objl = []
            for obj in models.storage.all().values():
                if len(line) > 0 and line == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(line) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, line):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        objdict = models.storage.all()
        x = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return False
        if x[0] not in HBNBCommand.__list_classes:
            print("** class doesn't exist **")
            return False
        if len(x) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(x[0], x[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(x) == 2:
            print("** attribute name missing **")
            return False
        if len(x) == 3:
            try:
                type(eval(x[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(x) >= 4:
            obj = objdict["{}.{}".format(x[0], x[1])]
            print(obj.__class__.__dict__.keys())
            if x[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[x[2]])
                obj.__dict__[x[2]] = valtype(x[3])
            else:
                obj[x[2]] = x[3]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
