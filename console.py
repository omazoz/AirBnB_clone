#!/usr/bin/python3
""" Import models"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import cmd
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the AirBnB console"""

    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]
    string_attr = ["name", "amenity_id", "place_id", "state_id",
                "user_id", "city_id", "description", "text",
                "email", "password", "first_name", "last_name"]
    integer_attr = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    float_attr = ["latitude", "longitude"]

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance"""
        classes_list = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid(line):
            arg = line.split()
            if arg[0] in classes_list:
                new = classes_list[arg[0]]()
            storage.save()
            print(new.id)


    def valid(self, line, _id_flag=False, _att_flag=False):
        """validation of argument that pass to commands"""
        arg = line.split()
        length = len(line.split())
        if length == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
            return False
        if length < 2 and _id_flag:
            print("** instance id missing **")
            return False
        if _id_flag and arg[0]+"."+arg[1] not in storage.all():
            print("** no instance found **")
            return False
        if length == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if length == 3 and _att_flag:
            print("** value missing **")
            return False
        return True

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if self.valid(line, True):
            arg = line.split()
            key = arg[0]+"."+arg[1]
            print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance"""
        if self.valid(line, True):
            arg = line.split()
            key = arg[0]+"."+arg[1]
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """Prints all instances"""
        arg = line.split()
        length = len(arg)
        l = []
        if length >= 1:
            if arg[0] not in HBNBCommand.list_classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if arg[0] in k:
                    l.append(str(v))
        else:
            for k, v in storage.all().items():
                l.append(str(v))
        print(l)

    def casting(self, line):
        """cast string to float or int if possible"""
        try:
            if "." in line:
                line = float(line)
            else:
                line = int(line)
        except ValueError:
            pass
        return line

    def do_update(self, line):
        """Updates an instance by adding or updating attribute"""
        if self.valid(line, True, True):
            arg = line.split()
            key = arg[0]+"."+arg[1]
            if arg[3].startswith('"'):
                match = re.search(r'"([^"]+)"', line).group(1)
            elif arg[3].startswith("'"):
                match = re.search(r'\'([^\']+)\'', line).group(1)
            else:
                match = arg[3]
            if arg[2] in HBNBCommand.string_attr:
                setattr(storage.all()[key], arg[2], str(match))
            elif arg[2] in HBNBCommand.integer_attr:
                setattr(storage.all()[key], arg[2], int(match))
            elif arg[2] in HBNBCommand.float_attr:
                setattr(storage.all()[key], arg[2], float(match))
            else:
                setattr(storage.all()[key], arg[2], self.casting(match))
            storage.save()

    def count(self, line):
        """count the number of instances of a class"""
        c = 0
        for key in storage.all():
            if line[:-1] in key:
                c += 1
        print(c)

    def _exec(self, line):
        """helper function parsing filtring"""
        methods = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
        }
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", line)
        arg = match[0][0]+" "+match[0][2]
        l = arg.split(", ")
        l[0] = l[0].replace('"', "").replace("'", "")
        if len(l) > 1:
            l[1] = l[1].replace('"', "").replace("'", "")
        arg = " ".join(l)
        if match[0][1] in methods:
            methods[match[0][1]](arg)

    def default(self, line):
        """default if there no command found"""
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", line)
        if len(match) != 0 and match[0][1] == "update" and "{" in line:
            d = re.search(r'{([^}]+)}', line).group()
            d = json.loads(d.replace("'", '"'))
            for k, v in d.items():
                _arg = line.split("{")[0]+k+", "+str(v)+")"
                self._exec(_arg)
        elif len(match) != 0:
            self._exec(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
