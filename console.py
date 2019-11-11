#!/usr/bin/python3
""" console for AirBnb """
import cmd


class HBNBCommand(cmd.Cmd):
    """ """


    prompt = "(hbnb)"
    
    def do_quit(self, args):
        """ Quits the program """
        return True

    def do_EOF(self, args):
        """ Reads EOF and exits """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
