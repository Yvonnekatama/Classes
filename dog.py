class Dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age


    def description(self):
        return (f"My dog's name is {self.name} she is {self.age} years old and she is a {self.breed}")

    def play(self):
        return(f"{self.name} likes to play fetch.")

