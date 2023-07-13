#!/usr/bin/python3
"""a program called console.py"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    # classes = {
    #     'BaseModel': BaseModel,
    #     'User': User,
    #     'Place': Place,
    #     'State': State,
    #     'City': City,
    #     'Amenity': Amenity,
    #     'Review': Review
    # }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a given class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        key = args[0] + '.' + args[1]
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        key = args[0] + '.' + args[1]
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        instances = storage.all()

        if not arg:
            print([str(value) for value in instances.values()])
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        print([str(value) for key, value in instances.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        key = args[0] + '.' + args[1]
        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = instances[key]
        attribute = args[2]
        value = args[3]

        try:
            value = json.loads(value)
        except ValueError:
            pass

        setattr(instance, attribute, value)
        instance.save()

    def do_help(self, arg):
        """Display help messages"""
        commands = {
            'quit': 'Quit command to exit the program',
            'EOF': 'Exit the program with Ctrl+D (EOF)',
            'create': 'Create a new instance of a given class',
            'show': 'Print the string representation of an instance',
            'destroy': 'Delete an instance based on the class name and id',
            'all': 'Print all string representations of instances',
            'update': 'Update an instance based on the class name and id'
        }

        if arg:
            if arg in commands:
                print(commands[arg])
            else:
                print("** No help available for '{}'".format(arg))
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            for command, description in commands.items():
                print("{:<10} {}".format(command, description))


if __name__ == '__main__':
    HBNBCommand().cmdloop()