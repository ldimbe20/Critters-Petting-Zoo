class Goldfish():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
Goldie = Goldfish(6, "Goldie", "Fish")