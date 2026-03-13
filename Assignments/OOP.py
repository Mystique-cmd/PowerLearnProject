class SuperHero:
    def __init__ (self, name, power, city ):
        self.name = name
        self.power = power
        self.city = city
        
    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"
    
    def use_power(self):
        return f"{self.name} uses {self.power}!"
    
class TechHero(SuperHero):
    def __init__(self, name, power, city, gadget):
        super().__init__(name, power, city)
        self.gadget = gadget

    #polymorphism : overriding the base method    
    def use_power(self):
        return f"{self.name} activates {self.gadget} to use {self.power}!"
    
    def reveal_gadget(self):
        return f"{self.name}'s gadget is {self.gadget}."
    
hero1 = SuperHero("MightyMan", "super strength", "Metro City")
hero2 = TechHero("TechnoGirl", "invisibility", "TechVille", "InvisoCloak")   

print(hero1.introduce())         
print(hero1.use_power()) 
        
print(hero2.introduce())         
print(hero2.use_power())         
print(hero2.reveal_gadget())     