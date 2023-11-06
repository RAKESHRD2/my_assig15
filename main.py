 
from my_classes.subclass_1 import Subclass1
from my_classes.subclass_2 import Subclass2


if __name__ == "__main__":
    obj1 = Subclass1(6)
    result1 = obj1.do_something()
    print(f"Result from Subclass1: {result1}")

    obj2 = Subclass2(15)
    result2 = obj2.do_something()
    print(f"Result from Subclass2: {result2}")

    
