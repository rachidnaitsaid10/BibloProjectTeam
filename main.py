from Data import *
from books import *

print(utilisateurs)
print(aime_livres)
print(livres)
print("-"*220)

print(SortingData(livres))
Ancien(livres)
Récent(livres)
CreationDict(aime_livres)
PaginationList(utilisateurs)




def Search_Livre(MyList):
    Nom_Livre = input("Nom de la livre: ")
    if Nom_Livre != "":
        MonLivre = list(filter(lambda x: x["titre"] == Nom_Livre, MyList))
        print(MonLivre)
    else :
        print("Invalid Input")

def Search_Users(MyList):
    Nom_User = input("Nom de la user: ")
    if Nom_User != "":
        MonUser = list(filter(lambda x: x[1] == Nom_User, MyList))
        print(MonUser)
    else :
        print("Invalid Input")



def menu():
    Choix = 0
    while Choix != 3 or Choix > 3 or Choix != "":
        print("Bienvenue !!!!!")
        print("-"*15)
        print("1-Pour Rechercher livre :")
        print("2-Pour Rechercher utilisateurs :")
        print("3-Quitter   :")
        print("-"*15)
        Choix = int(input("Choix entre 1 et 3 : "))

        if Choix == 1:
            Search_Livre(livres)
        if Choix == 2:
            Search_Users(utilisateurs)

# menu()





