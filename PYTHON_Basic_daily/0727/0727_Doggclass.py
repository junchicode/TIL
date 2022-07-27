class Doggy:
    
    num_of_dogs = 0 # 클래스 변수
    birth_of_dogs = 0 # 클래스 변수

    def __init__(self, name, bread): # 생성자
        self.name = name
        self.bread = bread 
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1   
    
    def bark(self):
        return '멍'
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    @classmethod
    def get_status(cls):
        return f'Birth : {cls.birth_of_dogs}, Current count: {cls.num_of_dogs}'
    
dog1 = Doggy('아리','포메라니안')
print(dog1.get_status())
    
