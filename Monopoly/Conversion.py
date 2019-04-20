"""
File that contails a class for all conversions.
"""

from SquareClasses import *

class Conversions:
    def jsonToObj(dict1):

        if "__class__" in dict1:
            class_name = dict1.pop("__class__")
            module_name = dict1.pop("__module__")
            module = __import__(module_name)
            class_ = getattr(module,class_name)
            obj = class_(**dict1)
        else:
            obj = dict1
        return obj
