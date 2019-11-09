#!/usr/bin/python3
""" Creates a unique FileStorage instance for application """

import file_storage.py


storage = FileStorage()
reload(storage)
