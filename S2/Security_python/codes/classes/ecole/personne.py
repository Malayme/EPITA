class Personne:
    def __init__(self, nom, prenom, dob = None):
        self.nom = nom
        self.prenom = prenom
        self.dob = dob

    def info(self):
        print(f"{self.nom} {self.prenom}")
        if self.dob != None:
            print(f"{self.dob}")
