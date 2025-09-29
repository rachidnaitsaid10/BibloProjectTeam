from Data import utilisateurs
from Data import aime_livres

def filter_utilisateur_adultes(users):
        if users[3] >= 18:
            return True

def affichage_utilisateur_adultes(users):
     adultes=list(filter(filter_utilisateur_adultes, users))
     print(adultes)

def noms_en_majuscule(users):
    return users[1].upper() , users[2].upper()

def affichage_noms_en_majuscule(users):
     noms_maj=list(map(noms_en_majuscule, utilisateurs))
     print(noms_maj)

def dictionnaire_utilisateurs_livre(lst_user,lst_aime_livre):
    dictio={}
    for (id_user, prenom, nom, age) in lst_user:
    
        livres_aimes = []
        for (id_livre, titre) in lst_aime_livre:
            if id_livre == id_user:
                
                livres_aimes.append(titre)
        dictio[id_user] = {
            "nom_complet": f"{prenom.upper()} {nom.upper()}",
            "age": age,
            "livres": livres_aimes
    }
    return dictio

def affichage_dictionnaire(dictio):
    for info in dictio.values():
        livres_names = "', '".join(info["livres"])
        print(f"{info['nom_complet']} ({info['age']} ans) aime : '{livres_names}'")

