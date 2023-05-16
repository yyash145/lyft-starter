from car import Car

# import array or sensor
# let dummy array be:
array = [0.89, 0.91, 0.92, 0.90]

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
        
        count = 0
        if(self.one >= 0.9):
            count += 1
        if(self.two >= 0.9):
            count += 1
        if(self.three >= 0.9):
            count += 1
        if(self.four >= 0.9):
            count += 1

        if count > 0:
            return True
        else:
            return False
