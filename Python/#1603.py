"""
1603. Design Parking System

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        self.cartype = {"1": big, "2": medium, "3": small}


    def addCar(self, carType: int) -> bool:
        c = str(carType)
        if self.cartype[c] > 0:
            self.cartype[c] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

"""
Runtime: 152 ms, faster than 17.26% of Python3 online submissions for Design Parking System.
Memory Usage: 14.9 MB, less than 27.31% of Python3 online submissions for Design Parking System.
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        self.slots = [0, big, medium, small]


    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        else:
            return False

"""
Runtime: 132 ms, faster than 91.32% of Python3 online submissions for Design Parking System.
Memory Usage: 14.9 MB, less than 27.31% of Python3 online submissions for Design Parking System.
"""
