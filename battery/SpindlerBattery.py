from datetime import datetime
from car import Car

class spindler(Car):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_service_date = datetime.today().date()
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if(service_threshold_date < self.current_service_date):
            return True
        else:
            return False