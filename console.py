#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import re
import cmd
import sys
import models
import argparse
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Contains all valid class names
CLASSES = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
]

# Gets the input string that will be passed to parser()
parser = argparse.ArgumentParser()
args = str(parser.parse_args())


# Parses input string and stores it in arg vector
def parser(args):
    """Parses arguments parsed to our HBNBCommands
    Returns an array of strings
    """

    # The regex returns a list of all space-demarcated substrings
    return re.findall(r"(\b[^\s]+\b)", args)


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project"""
    
    prompt = "(hbnb) "
    
    def precmd(self, line):
        """Overwrites the onecmd. This helps us to rearrange
        the arguments in the format of class.cmd() to fit into
        already existing do_foo methods in onecmd
        """

        # Contains list of all commands that require id
        cmd_list = ["update", "destroy", "show"]

        # checks for arguments in the format of class.cmd()
        if "." in line:
            argv = line.split('.')
            
            # Regex returns the command without the ending ()
            command = re.findall(r"^[a-z]+", argv[1])[0]

            if command in cmd_list:
                # Gets the id passed to commands requiring id
                id = re.findall(r"\((.*)\)", argv[1])[0]
                if command == "update":
                    args = id.split(' ')
                    line = f"{command} {argv[0]} {args[0]} {args[1]} {args[2]}"
                    print(line)
                else:
                    # Reconstructs the line to fit cmd class pattern
                    line = f"{command} {argv[0]} {id}"
            else:
                line = f"{command} {argv[0]}"

        # Returns the line as an argument to one cmd
        return cmd.Cmd.precmd(self, line)

    def do_EOF(self, line):
        """Implements EOF for the command interpreter
        """
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit()

    def emptyline(self):
        """Ensures that empty line + <ENTER> shouldn't execute anything
        """
        pass

    def do_create(self, args):
        """Creates a new instance of a class
        Saves it to the JSON file and prints the id
        """
        # argv is a vector containing parsed input string
        # Input string involves only args passed to function 
        argv = parser(args)

        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            model = eval(argv[0])()
            print(model.id)
            storage.save()

    def do_show(self, args):
        """Prints str repr of an instance based on the class name and id
        """
        argv = parser(args)
        if len(argv) == 0:
            print("** class name is missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_dict = storage.all()
            key = f"{argv[0]}.{argv[1]}"

            # checks if key is valid
            if all_dict.get(key):
                print(str(all_dict[key]))
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name & id and save the change
        """
        argv = parser(args)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_dict = storage.all()
            key = f"{argv[0]}.{argv[1]}"

            # checks if key is valid
            if all_dict.get(key):
                del all_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all str representation of all instances
        """

        argv = parser(args)

        all_dicts = storage.all()
        all_objects = [] 
        class_objects = [] # contains obj when class name is called

        for k, v in all_dicts.items():
            all_objects.append(str(v))
            if len(argv) != 0:
                cls = v.__class__.__name__
                if argv[0] == cls:
                    class_objects.append(str(v))
        if len(argv) == 0:
            print(all_objects)
        elif len(argv) == 1:
            if argv[0] in CLASSES:
                print(class_objects)
            
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class and id by adding attribute
        """
        argv = parser(args)

        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            all_dict = storage.all()
            key = f"{argv[0]}.{argv[1]}"
            if all_dict.get(key) is None:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        else:
            all_dict = storage.all()
            key = f"{argv[0]}.{argv[1]}"
            obj = all_dict.get(key)

            # if attribute name already exist, verify its type
            # and cast new value to the existing type
            if argv[2] in type(obj).__dict__:
                attr_type = type(obj.__class__.__dict__[argv[2]])
                setattr(obj, argv[2], attr_type(argv[3]))
            else:
                # if attribute does not exist, just assign to value
                setattr(obj, argv[2], argv[3])

            # save the updated objects
            storage.save()

    def do_count(self, args):
        """Retrives the count of instances of a class
        """
        argv = parser(args)
        count_class = 0
        count_all = 0
        all_dict = storage.all()
        for k, v in all_dict.items():
            if len(argv) != 0 and argv[0] in CLASSES:
                if argv[0] == v.__class__.__name__:
                    count_class += 1
            if len(argv) == 0:
                count_all += 1
        if len(argv) == 0:
            print(count_all)
        elif len(argv) == 1:
            if argv[0] in CLASSES:
                print(count_class)
            else:
                print("** class doesn't exist **")


# Exectutes module if executed as main
if __name__ == "__main__":
    # Creates a class and runs an infinite loop
    HBNBCommand().cmdloop()
