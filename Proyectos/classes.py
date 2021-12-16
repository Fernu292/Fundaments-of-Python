class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def vol(self):
       # return volume
       total = (w*h)
       return total
       
       
     
w = int(input())
h = int(input())

obj = Rectangle(w, h)
#call the function
print(obj.vol())