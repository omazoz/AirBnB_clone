#!/usr/bin/python3
"""Module for class HBNBCommand
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import cmd
import models
import re


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
                listobj = models.storage.all()
                objl = []
                for obj in models.storage.all():
                    x = obj.__str__()
                    x = x.split('.')
                    print(listobj[obj].__str__())
                    if line == x[0]:
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

    def default(self, line):
        """ default task 11
        """
        functions = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update}

        args_line = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args_line:
            args_line = args_line.groups()
        if not args_line or len(args_line) < 2 \
            or args_line[0] not in HBNBCommand.__list_classes \
                or args_line[1] not in functions.keys():
            super().default(line)
        if args_line[1] in ["all", "count"]:
            functions[args_line[1]](args_line[0])
        elif args_line[1] in ["show", "destroy"]:
            functions[args_line[1]](args_line[0] + ' ' + args_line[2])
        elif args_line[1] == "update":
            params = re.match(r"\"(.+?)\", (.+)", args_line[2])
            if params.groups()[1][0] == '{':
                dic_p = eval(params.groups()[1])
                for k, v in dic_p.items():
                    functions[args_line[1]](args_line[0] + " " +
                                            params.groups()[0] +
                                            " " + k + " " + str(v))
            else:
                rest = params.groups()[1].split(", ")
                functions[args_line[1]](args_line[0] +
                                        " " + params.groups()[0] + " " +
                                        rest[0] + " " + rest[1])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
