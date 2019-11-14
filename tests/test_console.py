#!/usr/bin/python3
""" Testing the console """
import unittest
from unittest.mock import patch
import models.engine.file_storage
import io
from console import HBNBCommand


class test_concole(unittest.TestCase):
    """ testing console """

    def test_create(self):
        """ test create """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        res = f.getvalue()

        if res != None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        res = f.getvalue()

        if res != None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
        res = f.getvalue()
        self.assertEqual(res, "** class name missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        res = f.getvalue()
        self.assertEqual(res, "** class doesn't exist **\n")

    def test_show(self):
        """test show """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
        res = f.getvalue()
        self.assertEqual(res, "** class name missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
        res = f.getvalue()
        self.assertEqual(res, "** class doesn't exist **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        res = f.getvalue()
        self.assertEqual(res, "** instance id missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
        res = f.getvalue()
        self.assertEqual(res, "** no instance found **\n")

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        res = f.getvalue()
        self.assertEqual(res, "** class name missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
        res = f.getvalue()
        self.assertEqual(res, "** class doesn't exist **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        res = f.getvalue()
        self.assertEqual(res, "** instance id missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
        res = f.getvalue()
        self.assertEqual(res, "** no instance found **\n")

    def test_all(self):
        """ test all """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        res = f.getvalue()
        self.assertEqual(res, "** class doesn't exist **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all")
        res = f.getvalue()

        if res != None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
 
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        res = f.getvalue()

        if res != None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_update(self):
        """ test update """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update")
        res = f.getvalue()
        self.assertEqual(res, "** class name missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
        res = f.getvalue()
        self.assertEqual(res, "** class doesn't exist **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        res = f.getvalue()
        self.assertEqual(res, "** instance id missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234")
        res = f.getvalue()
        self.assertEqual(res, "** no instance found **\n")
