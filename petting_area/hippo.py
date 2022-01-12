class Hippo():
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

Larry = Hippo(11, "Susie", "mammal")  