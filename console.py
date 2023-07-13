#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from typing import Tuple, Optional
import inspect


class_names_str = [
    "BaseModel", "User", "Place", "State",
    "City", "Amenity", "Review"
]
all_data = storage.all()


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        return True

    def do_EOF(self, args: str) -> bool:
        return True

    import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel or User."""
        if arg == "BaseModel":
            new_instance = BaseModel()
        elif arg == "User":
            new_instance = User()
        else:
            print("** class doesn't exist **")
            return

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        class_name = arg.split()[0] if arg else None
        all_objs = storage.all()
        instances = []
        if class_name:
            for key, value in all_objs.items():
                if key.split('.')[0] == class_name:
                    instances.append(str(value))
        else:
            for value in all_objs.values():
                instances.append(str(value))
        print(instances)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        setattr(all_objs[key], attribute_name, attribute_value)
        all_objs[key].save()

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


    def complete_add(self, text: str) -> str:

        options = [
            'quit', 'help', 'all', 'show', 'destroy', 'update', 'BaseModel',
            'User', 'Place', 'State', 'City', 'Amenity', 'Review'
        ]
        if text:
            return [option for option in options if option.startswith(text)]
        else:
            return options

    def default(self, line: str) -> None:

        print_string = f"Command '{line}' not found, "
        print_string += f"please type help to display the commands availables"
        print(print_string)


    def emptyline(self) -> None:

        pass


    def do_count(self, args: str) -> None:

        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        if arg_list and arg_list[0] not in class_names_str:
            print("** class doesn't exist **")
            return
        class_count = 0
        for key in all_data.keys():
            to_compare = key.split('.')[0]
            if to_compare == arg_list[0]:
                class_count += 1
        print(class_count)


    def _parse_args(self, arguments: str) -> Tuple[str, str]:

        try:
            method = arguments.split('(')[0].strip('.')
            raw_args = arguments.split('(')[1].strip(')')

            is_dict = False
            for i in raw_args:
                if i == '{':
                    is_dict = True
            if is_dict:
                line_parse = raw_args.split('{')
                id_string = line_parse[0].replace('"', '').replace(",", "")
                dict = "{" + line_parse[1]
                args = f"{id_string} {dict}"
            else:
                ag_lt = raw_args.split(", ")
                if len(ag_lt) == 3:
                    if isinstance(eval(ag_lt[2]), int):
                        args = (raw_args.replace(',', '')).replace('"', '')
                    else:
                        arg = (ag_lt[0] + " " + ag_lt[1]).replace('"', '')
                        args = arg + " " + ag_lt[2]
                else:
                    args = (raw_args.replace(',', '')).replace('"', '')
        except Exception as e:
            print("Syntax Error")
            print("Error: ", e)
            return

        callerframerecord = inspect.stack()[1]

        frame = callerframerecord[0]

        info = inspect.getframeinfo(frame)


        name_function = info.function.strip("do_")

        if args != "":
            internal_args = f"{name_function} {args}"
        else:
            internal_args = f"{name_function}"

        return (method, internal_args)


    def _execute(self, method: str, internal_args: str) -> None:

        try:
            eval("self.do_{}".format(method))(internal_args)
        except Exception:
            print("Be sure that the argument is valid")


    def do_BaseModel(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


    def do_User(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


    def do_Place(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


    def do_Amenity(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


    def do_City(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


    def do_Review(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


    def do_State(self, arguments: str) -> None:

        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
