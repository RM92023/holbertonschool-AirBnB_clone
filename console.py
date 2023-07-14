#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit the program."""
        return True

    def do_EOF(self, args):
        """Exit the program on EOF (Ctrl+D)."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def default(self, line):
        """Default handler for unknown commands."""
        print(f"Command '{line}' not found, please type help to display the available commands")

    def do_create(self, args):
        """Create a new instance of BaseModel."""
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Show the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        instance_id = arg_list[1]
        key = f"{arg_list[0]}.{instance_id}"
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on class name and id."""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        instance_id = arg_list[1]
        key = f"{arg_list[0]}.{instance_id}"
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Print all string representations of instances."""
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            arg_list = args.split()
            if arg_list[0] not in storage.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objects.items() if key.startswith(arg_list[0])])

    def do_update(self, args):
        """Update an instance based on class name and id."""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        instance_id = arg_list[1]
        key = f"{arg_list[0]}.{instance_id}"
        if key in objects:
            if len(arg_list) < 3:
                print("** attribute name missing **")
                return

            if len(arg_list) < 4:
                print("** value missing **")
                return

            setattr(objects[key], arg_list[2], eval(arg_list[3]))
            storage.save()
        else:
            print("** no instance found **")

    def do_count(self, args):
        """Count the number of instances of a class."""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if arg_list[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        count = sum(1 for key in objects.keys() if key.startswith(arg_list[0]))
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
