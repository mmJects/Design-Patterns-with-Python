""" Example Problem when to use factory desing pattern """

# Imagine you want to join one of the elite batches of GeeksforGeeks. So, you will go there and ask about the 
# Fee structure, timings available, and batches about the course you want to join. After looking at the system, 
# they will tell you about the courses, their Fee structures, timings available and batches. That’s it! 
# (No! we are not done yet because we are good developers).Our main purpose is to design the system flexible, 
# reliable, organized and lubricative. what Unexperienced developers will do is that they will create a separate
# and unique class for each and every course provided by GeeksforGeeks. Then they will create separate object 
# instantiation for each and every class although which is not required every time. The main problem will arise 
# when GeeksforGeeks will start new courses and developers have to add new classes as well because their code is 
# not much flexible.

class Course:
    def __init__(self):
        self.Fee()
        self.available_batch()

    def Fee():
        raise NotImplementedError

    def available_batch():
        raise NotImplementedError

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

class Backend(Course):
    def Fee(self):
        self.fee = 7000

    def available_batch(self):
        self.batches = 4

def construct_course(cls):
    course = cls()
    course.Fee()
    course.available_batch()
    return course

if __name__ == "__main__":
    backend = Backend()
    course = construct_course(Backend)
    print(course)

""" Pros """

# 1. Reusability: While making the various representations of the products, we can use the same construction 
#    code for other representations as well.
# 2. Single Responsibility Principle: We can separate out both the business logic
#    as well as the complex construction code from each other.
# 3. Construction of the object: Here we construct our object step by step, defer construction steps or run 
#    steps recursively.