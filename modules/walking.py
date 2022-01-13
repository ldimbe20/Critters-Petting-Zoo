from datetime import date

class Hippo():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

Larry = Hippo(11, "Susie", "mammal")  

class Goat():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
Tammy = Goat(12, "Tammy", "mammal")

class Horse():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
Terry = Horse(13, "Terry", "mammal")
        
        
class Chicken():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
Henrietta = Chicken(14, "Henrietta", "mammal")

class Pig():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
Babe = Horse(15, "Babe", "mammal")




