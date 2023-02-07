""" Real-life example when to use proxy design """

# Let’s understand the problem by considering the example of the College’s Database which takes care of all the 
# student’s records. For e.g., we need to find the name of those students from Database whose balance fee if 
# greater than 500. So, if we traverse the whole list of students and for each student object if we make a 
# separate connection to the database then it will be proved as an expensive task.Here comes the Proxy Method to 
# solve the above-discussed problem. We will create a proxy server or maybe a proxy connection to the database 
# and after that, we don’t have to create separate connections to the database for each student object.
# We will simply get our needed data using the proxy without wasting a huge amount of memory for the 
# creation of the object.

class College:
    def study(self):
        print("Studying in College")

class Proxy:
    def __init__(self):
        self.fee = 1000
        self.college = None

    def decide(self):
        print("Action in Proxy")
        if self.fee < 500:
            self.college = College()
            self.college.study()
        else:
            print("You have to pay the fee first..")

if __name__ == "__main__":
    college_proxy = Proxy()
    college_proxy.decide()

    college_proxy.fee = 100
    college_proxy.decide()