#!/usr/bin/python3
""" console for AirBnb """
import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel,
           "Amenity": Amenity,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "User": User}


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quits the program """
        return True

    def emptyline(self):
        """ handles empty lines """
        pass

    def do_EOF(self, args):
        """ Reads EOF and exits """
        return True

    def do_create(self, args):
        """ creates a new instance of BaseModel """
        if not args:
            print("** class name missing **")
        elif args in classes.keys():
            new = classes[args]()
            new.save()
            storage.reload()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Shows instance based on class and id
        args comes in as two values class and id <class ID> """
        if not args:
            print("** class name missing **")
            print("** instance id missing **")
            return
        args = args.split()
        objs = storage.all()
        if not args[0] in classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key in objs.keys():
                if args[1] in key.split(".")[1]:
                    print(objs[key])
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destroys instance based on class and id
            args comes in as two values class and id <class ID> """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        objs = storage.all()
        if not args[0] in classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            print("args[1] - > ", args[1])
            print("keys - >", objs.keys())
            for key in list(objs):
                if args[1] in key.split(".")[1]:
                    del objs[key]
                    storage.save()
                    return
            print("** no instance found **") 

    def do_all(self, args):
        """Prints all instances based or not on the class name """
        args = args.split()
        objs = storage.all()
        if args and args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            for key in objs.keys():
                if args:
                    if args[0] == key.split(".")[0]:
                        print(objs[key])
                else:
                     print(objs[key])

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        args = args.split()
        size = len(args)
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif not arg[0] in classes.keys():
            print("** class doesn't exist **")
        elif size < 2:
            print("** instance id missing **")
        elif not args[1] in objs.keys():
            print("** no instance found **")
        elif size < 3:
            print("** attribute name missing **")
        elif size < 4:
            print("** value missing **")
        else:
            objs[args[1]][args[2]] = args[3]
            storage.save()

    def default(self, args):
        """ capture User.method() """
        if "." not in args:
            print("*** Unknown syntax: {}".format(args))
            return
        args = args.split(".")
        objs = storage.all()
        if args[0] not in classes:
            print("*** Unknown syntax: {}".format(".".join(args)))
            return
        if args[1][0:7] == "count()":
            print(objs.keys())
            count = 0
            for key in objs.keys():
                if args[0] == key.split(".")[0]:
                    count -= -count ** 0
            print(count)
        elif args[1][0:5] == "show(":
                _in = args[1].split("(")
                _id = _in[1][0:-1]
                _class = args[0]
                self.do_show(_class + " " + _id)
        else:
            print("*** Unknown syntax: {}".format(".".join(args)))
            

    # help functions
    def help_quit(self):
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
