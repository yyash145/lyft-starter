from car import Car

# import array or sensor

class spindler(Car):
    def __init__(self, arr):
        self.arr = arr
    
    def needs_service(self):
        if len(self.arr) != 4:
            print("Given array size should be equals to 4")
            return
        
        for tires in self.arr:
            if tires >= 0.9:
                return True
            else:
                return False
