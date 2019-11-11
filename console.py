#!/usr/bin/python3
""" console for AirBnb """
import cmd


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quits the program """
        return True

    def emptyline(self):
        pass

    def do_EOF(self, args):
        """ Reads EOF and exits """
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
