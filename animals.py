class Dog:
    
    scientific_name = "Canis lupus familiaris"

    def __init__ (self,name):
        self.name=name
        self.woofs=0
    
    def speak(self):
        print("Woof!")
        
    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()
            
    def count(self):
        self.woofs+=1
        for bark in range (self.woofs):
            self.speak()
            
class Cat:
    
    def __init__(self):
        self.mood='neutral'
    
    def speak(self):

        if self.mood=='happy':
            print('Purrr')
        if self.mood=='angry':
            print('Hiss')


class Chihuahua(Dog):
    origin='Mexico'
    
    def speak(self):
        print('Yappi!')
        
class Huskeis(Dog):
    origin='Serbia'
    
    def speak(self):
        print('Awoooo!')     