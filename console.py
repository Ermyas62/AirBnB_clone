#!/usr/bin/python3
"""
    HBnB console is defined
"""

import cmd
import re
from shlex import split
from modles import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*))", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if bracketsis None:
            return[i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:curly_braces.span()[0]])
            ret1 = [i.strip(",") for i in lexer]
            ret1.append(curly_braces.group())
            return ret1


class HBNBCommand(cmd.Cmd):
    """
        HBNBnB command interprater is defined.
        Attributes:
            prompt (str): Command Propmt.
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }

    def emptylines(self):
        """Do nothing when recieving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalide"""
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_ipdate
            }
        match = re,search(r"\.", arg)
        if match ic not None:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match is not None:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arg1[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """quit command to exit the programm."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """"Usage: create <class>
        create a new class instance and print its id.
        """
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):


