from Ecole.personne import Personne
from Ecole.contact import Contact
from datetime import datetime, timedelta

class Etudiant(Personne, Contact):
    def __init__(self, nom, prenom, promotion,mobile,    mail, dob=None):
        self.nom=nom
        self.prenom=prenom
        self.promotion=promotion
        self.dob=dob
        self.mobile = mobile
        self.mail = mail

    def info(self):
        Personne.info()
        print(self.promotion)

    def info_complete(self):
        self.info()
        Contact.info()

    def semestre(self):
        date_jour = datetime.now()
        diff = promotion - date_jour.year #ex : 2027 - 2025 = 2
        if (diff <= 0 or (diff == 0 and date_jour.month > 6 )):
            print('cursus fini')
        elif diff == 0: # dernier semestre
            print(6)
        elif (diff == 1 and date_jour.month > 6 ): #5em semestre
            print(5)
        elif (diff == 1 and date_jour.month <= 6 ): #4em semestre
            print(4)
        elif (diff == 2 and date_jour.month > 6): #3em semestre
            print(3)
        elif (diff == 2 and date_jour.month <= 6): #2em semestre
            print(2)
        elif (diff == 3 and date_jour.month > 6): #1er semestre
            print(1)
        else:
            print("0 ou pas inscrit")
