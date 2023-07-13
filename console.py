#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
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

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif arg == "User":
            new_user = User()
            new_user.save()
            print(new_user.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name == "User":
                try:
                    user = self.storage.get(User, instance_id)
                    print(user)
                except Exception:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        if arg == "User":
            users = self.storage.all(User).values()
            print([str(user) for user in users])
        elif not arg:
            all_objs = self.storage.all()
            print([str(obj) for obj in all_objs.values()])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name == "User":
                try:
                    user = self.storage.get(User, instance_id)
                    self.storage.delete(user)
                    self.storage.save()
                except Exception:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            if class_name == "User":
                try:
                    user = self.storage.get(User, instance_id)
                    setattr(user, attribute_name, attribute_value)
                    self.storage.save()
                except Exception:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

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
