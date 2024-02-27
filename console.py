#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command-line interface for the AirBnB clone.
    It provides various commands for interacting with the application.
    """

    prompt = "(hbnb) "
    models = ["BaseModel"]

    def do_quit(self, args):
        """
        Quit the command-line interface.
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        Handle the end-of-file signal.
        """
        return True

    def do_help(self, args):
        """
        Display help information for a specific command or
        list all available commands.
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, args):
        """
        Create a new instance of a class.
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Display the string representation of an instance.
        Usage: show <class name> <id>
        """
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")

        key = args_list[0] + "." + args_list[1]

        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])



if __name__ == "__main__":
    HBNBCommand().cmdloop()
