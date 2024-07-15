class Dog():
    dogs = []
    
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
        
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
    
    @staticmethod
    def bark(n=0):
        """Barks n times"""
        for _ in range(n):
            print('Bark!')
            
tim = Dog('tim')
jim = Dog('jim')

print(Dog.num_dogs()) # @classmethod without self. creating an object

Dog.bark(5) # @staticmethod without __init__ (initialization)
