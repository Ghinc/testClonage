"""
#auteur : Johanna Ghinevra
#date : 08/09/2020
#version : 1
#description : atelier 2 L3


"""
#exercice 4

"""
REVIEW VOIR :
Ligne 18,
Ligne 21,
Ligne 42,
Ligne 43,
"""

from datetime import*

#Inutile de redéfinir la fonction ici il est meiux d'importer le fichier "atelier_2_exercice_1.py" tel que :
# import Exercice_2 ensuite il suffit d'appeler la fonction "est_bissextile tel que : Exercice_2.est_bissextile(année)
def est_bissextile(année:int)->bool :
    """ la fonction retourne true si l'année est bissexitile, false sinon,
    une année est bissextile si elle est divisible par 4 et pas par 100 ou bien
    divisible par 400"""

    if((année%4==0)and(année%100!=0))or(année%400==0):
        return(True) #return(True) inutle => return True
    else :
        return(False) # voir ligne 21


def date_est_valide(jour:int, mois:int, annee:int)->bool:
    """ la fonction date_est_valide retourne vrai si la date existe,faux sinon.
    les listes mois_30 correspondent aux mois qui ont 30jours ie avril,juin,septembre et novembre,
    tandis que les listes mois_31 correspondent aux mois qui ont 31jours (le reste sauf février qui ne possède que
    28jours sauf lorsque l'année est bissextile)"""
    mois_30 = [4, 6, 9, 11]
    mois_31 = [1, 3, 5, 7, 8, 10, 12]

    #REVIEW TROP DE RETURN => il est mieux  de stocker la réponse dans une variable et la return à la toute fin du code.
    #STOCKER LES JOURS À VERIFIER DANS DES CONSTANTES.
    if jour<29 and mois>0 and mois<13 : # peu importe le mois, il y'a au moins 28jours, on vérifie juste que le mois existe ]0,12[
        return(True) # voir ligne 21
    elif mois in mois_30 and jour<31: #si le mois  comporte  30jours,on vérifie que le jour n'est pas plus grand  que 30
        return(True) # voir ligne 21
    elif mois in mois_31 and jour<32:# si le mois comporte 31jours, on vérifie que le jour n'est pas plus grand que 31
        return(True) # voir ligne 21
    elif mois==2 and jour >28: # si le mois est février  et que le jour est plus grand que 28, on vérifie que l'année est bissextile
        if(est_bissextile(annee))and(jour==29): # et que le jour est égal à 29
            return(True) # voir ligne 21
        else:
            return(False) # voir ligne 21
    else:
        return(False) # voir ligne 21


def saisie_date_naissance(jour:int,mois:int,annee:int)-> datetime :
    """ on convertit nos jours,mois,années en date time en vérifiant que celle-ci soit bien valide"""
    if(date_est_valide(jour,mois,annee)):
        return(datetime(annee,mois,jour).date()) # voir ligne 21
    
def test_saisie():
    print("date valide : ", saisie_date_naissance(13,9,2000)) # voir ligne 21
    print("date super fausse : ", saisie_date_naissance(25,45,1987)) # voir ligne 21

def age(date_naissance : datetime)->int:
      """ calcul l'age d'un individu en fonction de sa date de naissance à quelques jours près, soustraction correspond à la différence
      entre la date d'aujourd'hui et la date de naissance"""
      soustraction = datetime.now().date() - date_naissance
      return(int(soustraction.days/365)) # voir ligne 21 # voir ligne 21 #on récupère l'âge sous la forme d'un entier, en le divisant par 365


def est_majeur(date_naissance : datetime)->bool:
    """ est_majeur retourne True si l'age de l'individu est au moins 18ans"""
    return(age(date_naissance)>=18) # voir ligne 21


def test_majeur():
    print("non :" ,est_majeur(saisie_date_naissance(30,9,2010)))
    print("non :", est_majeur(saisie_date_naissance(13,9,2002)))
    print("oui :", est_majeur(saisie_date_naissance(13,9,2000)))

def test_acces() ->str:
     """test_acces retourne un message d'autorisation d'accès selon si l'individu est majeur"""
     jour = int(input(" quel jour êtes vous né ?"))
     mois = int(input(" quel mois ?"))
     annee = int(input(" quelle année ?"))
     date_naissance = saisie_date_naissance(jour,mois,annee)
     nb_annees= age(date_naissance)
     msg = " vous avez " + str(nb_annees) + " années"
     if(est_majeur(date_naissance)): #si la personne est majeure, elle a accès autorisé sinon accès non autorisé
         msg = msg + " accès autorisé" 
     else :
         msg = msg + "accès non autorisé"

     return(msg)

print(test_acces())

