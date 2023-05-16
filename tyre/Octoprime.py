from car import Car

# import array or sensor
class spindler(Car):
    def __init__(self, arr):
        self.arr = arr
        self.one = arr[1]
        self.two = arr[2]
        self.three = arr[3]
        self.four = arr[4]
    
    def needs_service(self):
        if len(self.arr) != 4:
            print("Given array size should be equals to 4")
            return
        
        if(self.one + self.two + self.three + self.four >= 3):
            return True
        else:
            return False