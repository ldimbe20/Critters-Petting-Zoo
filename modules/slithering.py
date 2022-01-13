from datetime import date

class Cobra():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

# Gary = Cobra(1,"Gary","Snake")

class Python():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Gecko():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        
class Iguana():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        
Layla = Iguana(4, "Layla", "Lizard") 


class Salamander():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

Margot = Salamander(5, "Margot", "Lizard")      


