#!/usr/bin/python3
'''
Documentation
'''

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, args):
        '''
        Quit command to exit the program
        '''
        raise SystemExit

    def do_EOF(self, args):
        '''
        EOF
        '''
        return True

    def do_help(self, args):
        '''
        Help
        '''
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        '''
        an empty line + ENTER shouldn't execute anything
        '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()