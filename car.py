class Car:
    def __init__(self,model,make,color,registration):
        self.model=model
        self.make=make
        self.color=color
        self.registration=registration
    def park(self):
        return f"The {self.model}-{self.make},color {self.color} of registration {self.registration} is parked at the mall"
    def  speed(self):
        return f" My {self.model} can move upto 200km/hr if serviced well"    