""" Real-life example to use adapter design"""

# Imagine you are creating an application that shows the data about all different types of vehicles present. It 
# takes the data from APIs of different vehicle organizations in XML format and then displays the information. But 
# suppose at some time you want to upgrade your application with a Machine Learning algorithms that work beautifully 
# on the data and fetch the important data only. But there is a problem, it takes data in JSON format only. It will 
# be a really poor approach to make changes in Machine Learning Algorithm so that it will take data in XML format.

class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"
    
    def wheeler(self):
        return "TwoWheeler"

class Truck:
    def __init__(self):
        self.name = "Truck"
    
    def wheeler(self):
        return "FourWheelers"

class Adapter:
    def __init__(self,obj,**adapted_methods):
        self.obj = obj
        self.__dict__.update(**adapted_methods)

    def __getattr__(self,attr: str):
        return getattr(self.obj,attr)

    def original_dict(self):
        return self.obj.__dict__

if __name__ == "__main__":
    objects = []

    cycle = MotorCycle()
    objects.append(Adapter(cycle,wheels=cycle.wheeler))

    vehicle = Truck()
    objects.append(Adapter(vehicle,wheels=vehicle.wheeler))

    for obj in objects:
        print(obj.name," is ",obj.wheels())
        print(obj.original_dict())

# Pros 

# Principle of Single Responsibility: We can achieve the principle of Single responsibility with Adapter Method
# because here we can separate the concrete code from the primary logic of the client.Flexibility: Adapter Method 
# helps in achieving the flexibility and reusability of the code.Less complicated class: Our client class is not 
# complicated by having to use a different interface and can use polymorphism to swap between different implementations 
# of adapters.Open/Closed principle: We can introduce the new adapter classes into the code without violating the 
# Open/Closed principle.

