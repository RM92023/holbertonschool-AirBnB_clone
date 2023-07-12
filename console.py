#!/usr/bin/python3
'''Import several modules'''
import cmd

'''Create the class HBNBCommand'''

class HBNBCommand(cmd.Cmd):
    '''Command interprete'''
    while True:
        try:
            command = input('(hbnb) ')
            
            if not command:
                continue

            if command == 'help':
                continue

            if command == 'quit':
                break
        except EOFError:
            break


if __name__ == '__main__':
    HBNBCommand().cmdloop()