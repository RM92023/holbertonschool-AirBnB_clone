#!/usr/bin/python3
'''Import several modules'''
import cmd
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
    
    def create(selfo, arg):
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg
            try:
                new_instance = eval(class_name)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()