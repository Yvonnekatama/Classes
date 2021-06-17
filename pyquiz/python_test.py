#  x = [100,110,120,130,140,150]
   




 #q2
def divisible_by_three(n):
    for nums in range(1,n):
        if nums%3==0:
            print(nums)
        else:
            print(nums)
divisible_by_three(50)
           
#q3
def numbers():
    x = [[1,2],[3,4],[5,6]]
    new_list=list(sum(x,[]))
    print(new_list)
numbers()

#q4
def letters():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    for duplicates in x:
        x.discard('duplicates')    
#q6
def divisible_by_seven():
    a=[]
    num=range(100,200)
    for n in num:
        if n%7==0:
            a.append(a)
    
divisible_by_seven()
#q7
def greet():
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
    for items in students:
        print(f"Hello {items.get('name')} you were born in the year{2021- (items.get('year'))}")
        
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
        
    def area(self):
        a=self.width * self.length
        print (f"The area of a rectange is {a}")
    def perimeter(self):
        p=2*self.length + 2*self.width
        print (f"The area of a rectangle is {p}")



rectangle=Rectangle(10,20)
rectangle.area()
rectangle.perimeter()


