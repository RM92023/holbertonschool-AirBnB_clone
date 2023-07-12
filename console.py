#!/usr/bin/python3
'''Import several modules'''
import cmd
import json
from models.base_model import BaseModel

'''Create the class HBNBCommand'''

class HBNBCommand(cmd.Cmd):
    '''Command interprete'''
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
    def emptyline(self):
        pass
    
    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = arg
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                with open("file.json", 'r') as file:
                    data = json.load(file)
                    key = "{}.{}".format(class_name, instance_id)
                    if key in data:
                        instance_data = data[key]
                        instance = BaseModel(**instance_data)
                        print(instance)
                    else:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                with open("file.json", 'r+') as file:
                    data = json.load(file)
                    key = "{}.{}".format(class_name, instance_id)
                    if key in data:
                        del data[key]
                        file.seek(0)
                        json.dump(data, file)
                        file.truncate()
                    else:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        class_name = arg.split()[0] if arg else None
        try:
            with open("file.json", 'r') as file:
                data = json.load(file)
                instances = []
                if class_name:
                    for key, value in data.items():
                        if key.split('.')[0] == class_name:
                            instance = BaseModel(**value)
                            instances.append(str(instance))
                else:
                    for value in data.values():
                        instance = BaseModel(**value)
                        instances.append(str(instance))
                print(instances)
        except FileNotFoundError:
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

            try:
                with open("file.json", 'r+') as file:
                    data = json.load(file)
                    key = "{}.{}".format(class_name, instance_id)
                    if key in data:
                        instance_data = data[key]
                        instance = BaseModel(**instance_data)
                        if hasattr(instance, attribute_name):
                            setattr(instance, attribute_name, attribute_value)
                            data[key] = instance.to_dict()
                            file.seek(0)
                            json.dump(data, file)
                            file.truncate()
                        else:
                            print("** attribute doesn't exist **")
                    else:
                        print("** no instance found **")
            except FileNotFoundError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()