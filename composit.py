""" Problem when to use composite design """

# Imagine we are studying an organizational structure which consists of General Managers, Managers, and Developers. 
# A General Manager may have many Managers working under him and a Manager may have many developers under him.
# Suppose, you have to determine the total salary of all the employees. So, How would you determine that ?
# An ordinary developer will definitely try the direct approach, go over each employee and calculate the total salary. 
# Looks easy? not so when it comes to implementation. Because we have to know the classes of all the employees General 
# Manager, Manager, and Developers.It seems even an impossible task to calculate through a direct approach in 
# Tree-based structure.

class Leaf:
    
    def __init__(self,*args):
        self.position = args[0]

    def show_details(self):
        print("\t",self.position)

class Composite:
    
    def __init__(self,*args):
        self.position = args[0]
        self.children = []

    def add(self,children):
        self.children.append(children)

    def remove(self,children):
        self.children.remove(children)

    def show_details(self):
        print(self.position)
        for child in self.children:
            print("\t",end=" ")
            child.show_details()

if __name__ == "__main__":
    
    top = Composite("General Manager")
    mid = Composite("Manager")
    basic = Composite("Human Resources Manager")

    mid_e = Leaf("Dev1")
    mid_e1 = Leaf("Dev2")

    basic_e = Leaf("Accoutant1")
    basic_e1 = Leaf("Accountant2")

    mid.add(mid_e)
    mid.add(mid_e1)

    basic.add(basic_e)
    basic.add(basic_e1)

    top.add(mid)
    top.add(basic)

    top.show_details()