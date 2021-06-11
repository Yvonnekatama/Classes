# class Dog:
#     def __init__(self,name,breed,age):
#         self.name=name
#         self.breed=breed
#         self.age=age


#     def description(self):
#         return (f"My dog's name is {self.name} she is {self.age} years old and she is a {self.breed}")

#     def play(self):
#         return(f"{self.name} likes to play fetch.")

class Products:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.fruit=[]
        self.veggie=[]
    def pack(self):
        proli=[self.p1,self.p2]
        for item in proli:
            if item=='mango':
                self.fruit.append(item)
                print ("It goes to fruit")
            else:
                if item=='potato':
                    self.veggie.append(item)
                    print ("It goes to veggie")


# product=Products("mango","potato")