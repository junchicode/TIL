class Circle:
    pi = 3.14
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return Circle.pi *  self.r * self.r
    
    def circumfernece(self):
        return 2 * Circle.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
circleinst = Circle(3,2,4)
print(circleinst.circumfernece()) # 둘레
print(circleinst.area()) # 넓이
