import cmd
import sys
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = FileStorage()
        self.storage.reload()

    def emptyline(self):
        """
        Do nothing when empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when End-of-File character is reached (Ctrl+D).
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        save it to the JSON file, and print the id.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an
        instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        objects = self.storage.all()

        if obj_key in objects:
            print(objects[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        objects = self.storage.all()

        if obj_key in objects:
            del objects[obj_key]
            self.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representations of all
        instances based on the class name or all classes.
        """
        objects = self.storage.all()

        if arg:
            class_name = arg.strip()
            if class_name not in self.storage.classes():
                print("** class doesn't exist **")
                return

            filtered_objects = {
                k: v for k, v in objects.items() if class_name in k
            }

            print([str(v) for v in filtered_objects.values()])
        else:
            print([str(v) for v in objects.values()])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        objects = self.storage.all()

        if obj_key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        obj = objects[obj_key]

        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def postloop(self):
        """
        Print a new line after executing the command.
        """
        print()

    def precmd(self, line):
        """
        Store the current command in the file attribute for later use.
        """
        self.file.write(line + '\n')
        return line

    def preloop(self):
        """
        Load the previous commands from the file if provided.
        """
        try:
            self.file = open('.hbnb_history', 'r')
            self.history = self.file.readlines()
            self.history = [cmd.strip() for cmd in self.history]
            self.file.close()
        except IOError:
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
