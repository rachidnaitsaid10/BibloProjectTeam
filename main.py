import Data
import users

user=Data.utilisateurs
aime_livre=Data.aime_livres
livres=Data.livres
def get_name (lst_user):
    nom_complet=[]
    for user in lst_user:
        nom_complet.append(f'{user[1]} {user[2]}')
    return nom_complet
    
def get_age(lst_user):
    age_user=[]
    for user in lst_user:
        age_user.append(user[3])
    return age_user

def get_nom_age(lst_nom,lst_age):
    lst_nom_age=list(zip(lst_nom,lst_age))
    print(lst_nom_age)


users.affichage_utilisateur_adultes(user)
users.affichage_noms_en_majuscule(user)
dic=users.dictionnaire_utilisateurs_livre(user,aime_livre)
print(dic)
users.affichage_dictionnaire(dic)
get_nom_age(get_name(user),get_age(user))




