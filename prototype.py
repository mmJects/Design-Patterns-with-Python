""" Example when to use prototype design """
# Suppose we have a Shape class that produces different shapes such as circle, rectangle, square, etc and we 
# already have an object of it. Now we want to create the exact copy of this object. How an ordinary developer 
# will go? He/She will create a new object of the same class and will apply all the functionalities of the original
# objects and copy their values. But we can not copy each and every field of the original object as some may be 
# private and protected and are not available from the outside of the object itself. Problems are not over here! 
# you also become dependent on the code of other class which is certainly not a good practice in Software Development.

from abc import ABCMeta , abstractmethod
import copy

class course_at_GFG(metaclass = ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type
 
    def get_id(self):
        return self.id
 
    def set_id(self, sid):
        self.id = sid
 
    def clone(self):
        return copy.copy(self)

class MySQL_dbms(course_at_GFG):
    def __init__(self):
        super().__init__()
        self.type = "MySQL Database Managment System"
    
    def course():
        print("Inside MySQL_dbms::course() method")
    

class course_at_GFG_cache:
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = course_at_GFG_cache.cache.get(sid,None)
        return COURSE.clone()

    @staticmethod
    def load():
        dbms = MySQL_dbms()
        dbms.set_id("1")
        course_at_GFG_cache.cache[dbms.get_id()] = dbms

if __name__ == "__main__":
    course_at_GFG_cache.load()
    dbms = course_at_GFG_cache.get_course("1")
    print(dbms.get_type())