Bernard & Co 



1 --> fenetre opérateur 
  Gérer les commandes faites à distance et les commandes faites en présentiel = centralisation 
  Pourvoir accepter et refuser des commandes 
  refresh la page pour actualiser 

2 --> fenetre utilisateur 
  Voir les réstaurants dispo --> ils sont disposés en liste de boutons à la verticale

une fois un restaurant cliqué


afficher la liste de menu du restaurant chaque menu est clicable  
  dans le menu --> les choix sont affichés et cliquable 
    le choix dans le menu est modifiable automatiquement en cliquant sur un autre choix
    le menu ne peut être validé si tous les composants n'ont pas été saisis (plat , boisson, dessert)
    un message vous le fera remarquer
  une fois la commande du menu terminée appuyer sur "Validé" pour l'enregister

afficher en dessous des menus, les petites faims : 
  tout les choix sont disponible a l'unité 


une barre de navigation est afficher en bas de la page d'accueille du restaurant :

  bouton retour --> retour a la page d'accueille avec les choix de chaque restaurant, si un panier a été rempli, il est supprimé

  bouton voir la commande --> affiche l'ensemble des commandes affectuées en différenciant les menus des petites faims 
                              pour les supprimer il suffit de cliquer dessus comme c'est spécifié en haut de page 

  bouton validé --> emmène sur une page qui donne le montant total de la commande 
                    avec deux boutons : --> revenir a la commande si un element à été oublié
                                        --> payer permet de finir la commande et de l'envoyer à l'opératuer




  
  
3 --> structure de données = data 
    une liste regroupant l'ensemble des restos

        un sous dico --> fiche du resto {"nom", "adresse", {horaires}, "avis", {menu}}

          menu --> {{formule1}, {formule2}, {formule3}}
              formule1 --> {"Plat", "Boisson", "price"}
              formule2 --> {"Plat", "Dessert", "price"}
              formule3 --> {"Plat", "Boisson", "Dessert", "price"}

        petites faims = l'ensemble des plats / desserts / Boisson sans doubons grace a set()



