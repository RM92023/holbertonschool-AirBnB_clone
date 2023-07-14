#!/usr/bin/python3
'''Import several files or library'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


'''Create class HBNBCommand'''


class HBNBCommand(cmd.Cmd):

    """
    This is a command-line interface for
    interacting with the program.
    """
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
