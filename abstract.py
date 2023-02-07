""" Example Problem when to use abstract desing pattern """

# Imagine you want to join one of the elite batches of GeeksforGeeks. So, you will go there and ask about the Courses 
# available, their Fee structure, their timings, and other important things. They will simply look at their system and 
# will give you all the information you required. Looks simple? Think about the developers how they make the system so 
# organized and how their website is so lubricative.
# Developers will make unique classes for each course which will contain its properties like Fee structure, timings, 
# and other things. But how they will call them and how will they instantiate their objects?
# Here arises the problem, suppose initially there are only 3-4 courses available at GeeksforGeeks, but later they 
# added 5 new courses. So, we have to manually instantiate their objects which is not a good thing according to the 
# developer’s side. 

class DataScience:
    def __init__(self) -> None:
        self.fee = 1000
    def __str__(self) -> str:
        return self.__class__.__name__

class Course_GFG:
    def __init__(self,course=None):
        self.course = course

    def get_info(self):
        course_info = self.course()
        print(f"We've a course named {course_info} and its price is {course_info.fee}$")

if __name__ == "__main__":
    check = Course_GFG(DataScience)
    check.get_info()


# Pros

# 1. It is easy to introduce new variants of the products without breaking the existing client code.
# 2. Products which we are getting from the factory are surely compatible with each other.
