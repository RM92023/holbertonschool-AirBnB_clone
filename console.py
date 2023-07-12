#!/usr/bin/python3
'''Import several modules'''
import cmd

'''Create the class HBNBCommand'''

class HBNBCommand(cmd.Cmd):
    '''Command interprete'''
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
    def emptyline(self):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()