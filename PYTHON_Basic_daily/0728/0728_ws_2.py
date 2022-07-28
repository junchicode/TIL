from datetime import date

class Person:
    '''
    생성자 1. __init__
    생성자 2. 이름과 태어난 년도를 인자로 받는다
    @classmethod
    details(name, year
    '''
    #매직함수 __init__을 이용한 생성자 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #클래스 메서드를 활용한 생성자 
    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)
        
    def check_age(self): #instance method
        if self.age > 19:
            return False
        else:
            return True
    


p1 = Person('john',33)
print(p1.name)
print(p1.age)
print(f'미성년자 : {p1.check_age()}')

p2 = Person.details('Peter', 2004)
print(p2.name)
print(p2.age)
print(f'미성년자 : {p2.check_age()}')