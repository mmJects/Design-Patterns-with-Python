# The bridge method is a Structural Design Pattern that allows us to separate the Implementation Specific Abstractions
# and Implementation Independent Abstractions from each other and can be developed considering as single entities.The 
# bridge Method is always considered as one of the best methods to organize the class hierarchy.



class ProducingAPI1:
    def produce(self,length,breadth,height):
        print(f"API1 is producing with {length},{breadth} and {height}")

class ProducingAPI2:
    def produce(self,length,breadth,height):
        print(f"API2 is producing with {length},{breadth} and {height}")

class Cuboid:

    def __init__(self,length,breadth,height,API):
        self._length = length
        self._breadth = breadth
        self._height = height
        self._producing_API = API

    def produce(self):
        self._producing_API.produce(self._breadth,self._height,self._length)

    def expand(self,times):
        self._length =  self._length * times
        self._breadth = self._breadth  * times
        self._height =  self._height * times

if __name__ == "__main__":
    cub = Cuboid(10,20,30,ProducingAPI1())
    cub.produce()

    
    