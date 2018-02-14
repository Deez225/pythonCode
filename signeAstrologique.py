def astr(jour, mois):

    if (mois == 3 and (jour >= 1 and jour <= 31)) or (mois == 4 and (jour >= 1 and jour <= 20)):
        return "Belier"
    elif (mois == 4 and (jour >= 21 and jour <= 30) or (mois == 5 and (jour >= 1 and jour <= 21))):
          return "Taureau"
    elif (mois == 5 and (jour >= 22 and jour <= 31) or (mois == 6 and (jour >= 1 and jour <= 21))):
          return "Gemeaux"
    elif (mois == 6 and (jour >= 23 and jour <= 30) or (mois == 7 and (jour >= 1 and jour <= 22))):
          return "Cancer"
    elif (mois == 7 and (jour >= 23 and jour <= 31) or (mois == 8 and (jour >= 1 and jour <= 22))):
          return "Lion"
    elif (mois == 8 and (jour >= 23 and jour <= 30) or (mois == 9 and (jour >= 1 and jour <= 22))):
          return "Vierge"
    elif (mois == 9 and (jour >= 23 and jour <= 31) or (mois == 10 and (jour >= 1 and jour <= 22))):
          return "Balance"
    elif (mois == 10 and (jour >= 23 and jour <= 30) or (mois == 11 and (jour >= 1 and jour <= 22))):
          return "Scorpion"
    elif (mois == 11 and (jour >= 23 and jour <= 31) or (mois == 12 and (jour >= 1 and jour <= 21))):
          return "Sagittaire"
    elif (mois == 12 and (jour >= 22 and jour <= 30) or (mois == 1 and (jour >= 1 and jour <= 20))):
          return "Capricorne"
    elif (mois == 1 and (jour >= 21 and jour <= 31) or (mois == 2 and (jour >= 1 and jour <= 19))):
          return "Verseau"
    elif (mois == 2 and (jour >= 20 and jour <= 30) or (mois == 3 and (jour >= 1 and jour <= 20))):
          return "Poisson"
    else:
          "Erreur"

          
jour = int(input("Entrer le jour: "))
mois = int(input("Entrer le mois: "))
#ckeck before print /*** to fixed ***/
print("Votre signe astrologique est: " + astr(jour, mois))
