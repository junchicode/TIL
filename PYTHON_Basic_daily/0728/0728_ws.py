class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
               
class Rectangle:
    
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def get_area(self):
        w = abs(self.p1.x - self.p2.x)
        h = abs(self.p1.y - self.p2.y)
        return w*h
        
    def get_perimeter(self):
        w = abs(self.p1.x - self.p2.x)
        h = abs(self.p1.y - self.p2.y)
        
        return w*2+h*2 
        
    def is_square(self):
        w = abs(self.p1.x - self.p2.x)
        h = abs(self.p1.y - self.p2.y)
        if w == h:
            return True
        else:
            return False

p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3, p4)  
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
