from datetime import date

class Hippo():
    def __init__(self, name, species, shift):
        self.id = 1
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
    def __str__(self):
        return f"{self.name} is a {self.species}" 
Nora=Hippo(name="Nora", species="mammal", shift="PM")
 

class Goat():
    def __init__(self, name, species, shift):
        self.id = 2
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
    def __str__(self):
        return f"{self.name} is a {self.species}" 
        


class Horse():
    def __init__(self, name, species, shift):
        self.id = 3
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
    def __str__(self):
        return f"{self.name} is a {self.species}" 
        

        
        
class Chicken():
    def __init__(self, name, species, shift):
        self.id = 4
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
    
    def __str__(self):
        return f"{self.name} is a {self.species}" 
        


class Pig():
    def __init__(self, name, species, shift):
        self.id = 5
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        
    def __str__(self):
        return f"{self.name} is a {self.species}" 


class Goldfish():
    def __init__(self, name, species):
        self.id = 6
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
    def __str__(self):
        return f"{self.name} is a {self.species}" 
        
Goldie = Goldfish( "Goldie", "Fish")

class Dolphin():
    def __init__(self,  name, species):
        self.id = 7
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
    def __str__(self):
        return f"{self.name} is a {self.species}" 
                    
Linda = Dolphin( "Linda", "Mammal")

class Walrus():
    def __init__(self, name, species):
        self.id = 8
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
def __str__(self):
        return f"{self.name} is a {self.species}" 
        
Wilber = Walrus( "Wilber", "mammal")
                    
                    
class Mermaid():
    def __init__(self, name, species):
        self.id = 9
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
def __str__(self):
        return f"{self.name} is a {self.species}" 
                    
class Shark():
    def __init__(self,  name, species, food):
        self.id = 10
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
        
def feed(self):     
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

def __str__(self):
        return f"{self.name} is a {self.species}" 

Susie = Shark( "Susie", "mammal", "clams")


class Cobra():
    def __init__(self, name, species):
        self.id = 10
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
    def __str__(self):
        return f"{self.name} is a {self.species}" 

Gary = Cobra("Gary","Snake")

class Python():
    def __init__(self, name, species, food):
        self.id = 12
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    
    def feed(self):     
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
        return f"{self.name} is a {self.species}"     

Sandra = Python(name="Sandra", species="Lizard", food="lemons")   
print(Sandra.feed())

class Gecko():
    def __init__(self, name, species, food):
        self.id = 13
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    
    def feed(self):     
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
        return f"{self.name} is a {self.species}" 
    
Tim = Gecko(species= "lizard", name="Tim", food = "Gummybears")  
print(Tim.feed())     
        
class Iguana():
    def __init__(self, name, species, food):
        self.id = 14
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    
    def feed(self):     
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
        return f"{self.name} is a {self.species}"    

lizzie=Iguana("Lizzie","lizard", food="doritos")

print(lizzie.feed())

class Salamander():
    def __init__(self, name, species, food):
        self.id = 15
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):     
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}') 
      
    def __str__(self):
        return f"{self.name} is a {self.species}"    


Norbert = Salamander("Norbert", "Salamander", "cheetos" )


class Snake_Pit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithering creatures"
        self.animals = list()
        
Snake_Pit.animals.append(Norbert)

for animal in Snake_Pit.animals:
     print(f'You can find {animal.name} the {animal.species} in {Snake_Pit.attraction_name}')
     
#chapter 7