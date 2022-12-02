#!/usr/bin/python3
""" Defines the entry point to the AirBnB Console project """
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage

classes = ['BaseModel',
           'User',
           'State',
           'City',
           'Place',
           'Amenity',
           'Review']

<<<<<<< HEAD
=======
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

# ============== Helper Functions ===============


def parser(line):
    """Parses arguments parsed to our HBNBCommands
    Returns an array of strings

    Args:
        line(str): String passed to cmd
    """

    # Regex gets all sub strings within quotation marks and
    # stores it an av_quoted array in order to treat is as a unit
    av_quoted = re.findall(r'["\']([^"\']+)["\']', line)

    # Each quoted sub string is replaced in line with
    # a place holder "quoted_str"
    line = re.sub(r'["\']([^"\']+)["\']', "quoted_str", line)

    # The regex returns a list of all space-demarcated substrings
    argv = re.findall(r"(\b[^\s]+\b)", line)

    quoted_str_index_counter = 0
    # The placeholder "quoted_str" is replaced with the original
    # quoted string
    for idx, arg in enumerate(argv):
        if arg == "quoted_str":
            argv[idx] = av_quoted[quoted_str_index_counter]
            quoted_str_index_counter += 1
    return argv


def verify_id(id, argv):
    """Verifies if given id exists and returns True when it does
>>>>>>> DrPlain_branch

class HBNBCommand(cmd.Cmd):
    """ Defines a line-oriented command processor
    (a command-line interface) that extends the cmd module """
    # assign a custom prompt
    prompt = '(hbnb) '

    # initialize object

    def do_quit(self, line):
        """ Quit command to exit the program """
        sys.exit()  # success

    def do_EOF(self, line):
        """ <Ctrl + D> to exit the program """
        print(),  # to exit properly(with a new line)
        return True  # to the cmdloop's stop flag

    # override cmd.emptyline - re-executes last cmd if emptyline
    def emptyline(self):
        pass  # do nothing

    # override cmd.precmd - re-write line if in the form <class>.cmd
    def precmd(self, line):
<<<<<<< HEAD
        # for cls in self.classes:
        if '.' in line:
            # if line.startswith(cls):
            cmd_strs = line.split('.')
            # check if command has args as in show(id)
            args = cmd_strs[1].split('(')
            command = args[0]
            cls = cmd_strs[0]
            # check that the command is a command not some attribute
            if len(cls.split()) > 1:
                # doesn't need the splitting at .
                return cmd.Cmd.precmd(self, line)
            # print('command: ', command)
            # print('args: ', args)
            if args and len(args) > 1 and len(args[1]):
                if len(args[1].split(',')) == 1:
                    # the likes of User.show("id")
                    args = (args[1].strip(')')).strip('"')
                    # print('single arg args')
                else:
                    # the likes of User.update("id", "att", "attr_val")
                    args = args[1].strip(')')
                    # print('multiple args args')
                    if '{' in args:
                        # print('possible dict')
                        pass
                    # format multi_args eg into id att "attr_val"
                    multi_args = []
                    for idx, arg in enumerate(args.split(',')):
                        if (idx < 2) or len((arg.strip(' ')).split(' ')) == 1:
                            multi_args.append((arg.strip(' ')).strip('"'))
                        else:
                            multi_args.append(arg)  # as quoted stringi
                    # print(multi_args)
                    args = ' '.join(multi_args)
                # print('actual args: ', args)
                cmd_strs = []
                cmd_strs.append(args)
                cmd_strs.append(cls)
                cmd_strs.append(command)
            else:
                cmd_strs[1] = cmd_strs[1].strip('()')
            line = ' '.join(reversed(cmd_strs))
            # print(line)
=======
        if '.' in line and '(' in line:
            #cls, comd = line.split('.')
            cls, comd = line.split('(')[0].split('.')
            #comd = comd.split('(')[0]

            # Gets the arg inside bracket
            cmd_args = line.split('(')[1]
            if '{' not in cmd_args:
                cmd_args = cmd_args.split(', ')
                for idx, arg in enumerate(cmd_args):
                    cmd_args[idx] = arg.strip(')')
                    if len(cmd_args) == 0:
                        line = f"{comd} {cls}"
                    elif len(cmd_args) >= 1:
                        id = cmd_args[0]
                        if len(cmd_args) == 1:
                            line = f"{comd} {cls} {id}"
                        elif len(cmd_args) == 2:
                            attr_name = cmd_args[1]
                            line = f'{comd} {cls} {id} {attr_name}'
                        elif len(cmd_args) == 3:
                            attr_name = cmd_args[1]
                            value = cmd_args[2]
                            line = f'{comd} {cls} {id} {attr_name} {value}'
            elif '{' in cmd_args:
                cmd_args = list(re.findall(
                    r'(["\'].+["\']), (\{.*\})', cmd_args)[0])
                dict_args = eval(cmd_args[1])
                id = cmd_args[0]
                line = f"{comd} {cls} {id} {dict_args}"
>>>>>>> DrPlain_branch
        return cmd.Cmd.precmd(self, line)

    # ========= helper methods ===========

    @staticmethod
    def get_value(args):
        """ returns a value from args """
        attr_value = args[3]
        if len(args) > 4:
            value = ' '.join(args[3:])
            # print(value)
            if value[0] == '"':
                values = value.split('"')
                attr_value = values[1]
        else:
            attr_value = attr_value.strip('"')
        return attr_value

    def get_class_objects(self, line, objects):
        """ returns a list of the objects in <line> class """
        obj_list = []
        for cls in classes:
            if line == cls:
                for obj, val in objects.items():
                    cls_name = (obj.split('.'))[0]
                    # if an object is of given class, print it
                    if cls_name == line:
                        obj_list.append(str(val))
                return obj_list
        else:
            # some other class provided
            print("** class doesn't exist **")
            return (-1)

    @staticmethod
    def handle_attributes_dict(attrs):
        """ rebuilds arguments from a dictionary """
        # attrs is a str of attr_names and corresponding values
        attrs = attrs.strip('}')
        # print(attrs)
        list_ = attrs.split()
        # print(list_)
        # rebuild args to order expected
        values = []
        attr_dict = {}
        for idx, attr in enumerate(list_):
            if ':' in attr:
                # print('attr_name: ', attr)
                if idx != 0:
                    # assign prev attr_name, its value
                    attr_dict[name.strip("'")] = ' '.join(values)
                    # empty values to hold next attr's values
                    values = []
                name = attr.strip('"":')
            else:
                values.append(attr.strip('" ""'))
        # add last name: values pair
        attr_dict[name.strip("'")] = ' '.join(values)
        # print(attr_dict)
        return attr_dict

    # ========== end of helper functions ==============

    # ++++ custom console commands ++++ #

    def do_create(self, line):
        """ Create command to create a new instance """
        # check that class name is included in command
        if line:
            # check if class is valid
            for class_ in classes:
                if class_ in line:
                    # new = method()
                    new = eval(class_)()
                    new.save()
                    print(new.id)
                    break
            else:
                # provided_class doesn't exist
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, line):
        """ <show object_id> prints the string representation of
        an instance based on class name and id """
        # check that class name & id are provided along with command
        if line:
            args = line.split()
            # check that class exists
            if args[0] and args[0] not in classes:
                print("** class doesn't exist **")
            else:
                # class exists, check id is provided
                if len(args) > 1:
                    # check that an object with [id] exists
                    # get the string objects
                    objects = storage.all()
                    # search for [this_id] object representation
                    args[1] = args[1].strip('"')
                    this_key = f"{args[0]}.{args[1]}"
                    for obj, str_rep in objects.items():
                        if obj == this_key:
                            # print this_obj (its str rep)
                            print(str_rep)  # the object
                            break  # from objects looping
                    else:
                        # objects exhausted before [this_obj] is found
                        print("** no instance found **")
                else:
                    # id not provided (arg[1] missing)
                    print("** instance id missing **")
        else:
            # line empty (no args)
            print("** class name missing **")

    def do_destroy(self, line):
        """ <destroy class_name object_id> deletes an instance based on
        the class name and id (& saves the change into the JSON file) """
        # check that class name & id are provided along with command
        if line:
            args = line.split()
            # check that class exists
            if args[0] and args[0] not in classes:
                # if args[0] and args[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                # class exists, check id is provided
                if len(args) > 1:
                    # check that an object with [id] exists
                    # get the string objects (as reloaded)
                    objects = storage.all()
                    # search for [this_id] object representation
                    args[1] = args[1].strip('"')
                    this_key = f'{args[0]}.{args[1]}'
                    for obj, str_rep in objects.items():
                        if obj == this_key:
                            # delete the obj, str_rep pair
                            del (objects[obj])
                            # reserialize objects into file (to reflect change)
                            storage.save()
                            break
                    else:
                        # objects exhausted before [this_obj] is found
                        print("** no instance found **")
                else:
                    # id not provided (arg[1] missing)
                    print("** instance id missing **")
        else:
            # line empty (no args)
            print("** class name missing **")

    def do_all(self, line):
        """ <all> or <all class_name> prints all string representation
        of all instances based or not on the class name """
        # check if class_name is provided (for filter)
        # get all objects and only print out BaseModel instances
        objects = storage.all()
        if line:
            # check the classname provided exists
            objs = self.get_class_objects(line, objects)
            if objs == -1:
                pass  # class doesn't exist
            else:
                print(objs)
        else:
            # print all instances (no filter)
            obj_list = []
            for obj, val in objects.items():
                obj_list.append(str(val))
            print(obj_list)

    def do_update(self, line):
<<<<<<< HEAD
        """ <update class_name object_id attribute_name attribute_value>
        updates the instance [class_name.object_id]'s attribute
        [attribute_name] to [attribute_value] if [attribute_name]
        already exists. Adds the attribute [name]->[value] pair otherwise
        (& saves the change into the JSON file) """
        # check that class name & id are provided along with command
        if line:
            args = line.split()
            dict_args = {}
            if '{' in line:
                # pass to the function, the dictionary part
                dict_args = self.handle_attributes_dict((line.split('{'))[1])
            # check that class exists
            if args[0] and args[0] not in classes:
                print("** class doesn't exist **")
            else:
                # class exists, check id is provided
                if len(args) > 1:
                    objects = storage.all()
                    args[1] = args[1].strip('"')
                    this_key = f'{args[0]}.{args[1]}'
                    for obj, str_rep in objects.items():
                        if obj == this_key:
                            # object exists: update or add attribute
                            # check if a dictionary of attributes' provided
                            if dict_args:
                                # print("dictionary case")
                                for k, v in dict_args.items():
                                    self.update_attribute(args, str_rep, k, v)
                            else:
                                # print("normal case")
                                # just a single attribute-value pair to update
                                self.update_attribute(args, str_rep)
                            break
                    else:
                        # objects exhausted before [this_obj] is found
                        print("** no instance found **")
                else:
                    # id not provided (arg[1] missing)
                    print("** instance id missing **")
        else:
            # line empty (no args)
            print("** class name missing **")
=======
        """Updates an instance based on the class and id by adding attribute
        """
        # A list of all lines to be updated
        all_lines = []

        if '{' in line:
            dict_args = re.findall(r'(\{.*\})', line)[0]
            line = re.sub(r'(\{.*\})', "dict", line)
            dict_args = eval(dict_args)
            argv = parser(line)
            for k, v in dict_args.items():
                line = f'{argv[0]} "{argv[1]}" "{k}" "{v}"'
                all_lines.append(line)
        else:
            all_lines.append(line)

        # A loop to update every line in all_lines
        for line in all_lines:
            argv = parser(line)
            if len(argv) == 0:
                print("** class name missing **")
            elif argv[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            elif len(argv) == 2:
                if verify_id(argv[1], argv) is False:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")

            elif len(argv) == 3:
                if verify_id(argv[1], argv) is False:
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                if verify_id(argv[1], argv) is False:
                    print("** no instance found **")
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
>>>>>>> DrPlain_branch

    def do_count(self, line):
        """ returns the number of objects in a given class """
        if not line:
            print("** class name missing **")
        else:
            # get objects in the class
            objects = storage.all()
            objs = self.get_class_objects(line, objects)
            # print count if class exists
            if objs != -1:
                print("{}".format(len(objs) if len(objs) else 0))

    def update_attribute(self, args, str_rep, *attr_args):
        """ performs the update process on the basis of how many attributes
        should be updated (how many times the updating happens per
        cmdloop) """
        # if attr_args is defined, comes in order(attr_name, attr_value)
        if attr_args:
            args[2], args[3] = attr_args[0], attr_args[1]
        # make update (either way)
        if len(args) > 2:
            # check if attribute already exists
            for k, val in (str_rep.to_dict()).items():
                if k == args[2].strip('"'):
                    # attribute already exists
                    # check if attr_value provided
                    if len(args) > 3:
                        # attr_value provided, cast+update
                        attr_val = self.get_value(args)
                        attr_val = type(val)(attr_val)
                        setattr(str_rep, k, attr_val)
                        # reserialize objects into file
                        str_rep.save()
                    else:
                        print("** value missing **")
                    break  # from for loop
                else:
                    # attribute doesn't exist, add it
                    # print("entirely new attribute")
                    if len(args) > 3:
                        # extend object dict_rep
                        attr_value = self.get_value(args)
                        if attr_value.isnumeric():
                            attr_value = int(attr_value)
                        elif attr_value[0].isnumeric() and '.' in attr_value:
                            attr_value = float(attr_value)
                        setattr(str_rep, args[2].strip('"\''), attr_value)
                        # reserialize __objects into file
                        str_rep.save()
                    else:
                        print("** value missing **")
                    break
        else:
            # attribute_name missing
            print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
