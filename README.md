

1 --> fenetre opérateur 
  Gérer les commandes faites à distance et les commandes faites en présentiel = centralisation 
  Pourvoir ajouter et retirer des menus 
  Envoyer un message si les commandes sont prêtes ( peut etre un peu avant ) 

2 --> fenetre utilisateur 
  Voir les réstaurants dispo --> ils sont disposés en liste de boutons à la verticale 
                                on voit son nom en gras en plsu grand avec l'adresse en dessous pas en gras 
                                
 une fois un restaurant cliqué
 afficher les détails du restautrant 
 les temps d'attente éstimé et l'affluence moyenne sur le jour voulu 
   afficher la liste de menu du restaurant 
   chaque menu est clicable en cochant 
    Pourvoir commander avec un bouton en bas "Validé" 
    
  une fois validé  
  Avoir le choix de payer en ligne ou en présentiel ( optionnel si l'opérateur est d'accord ) 
    Voir une estimation du temps d'attentente ( optionnel si l'opérateur est d'accord ) 
    
  
3 --> structure de données = data 
    une liste regroupant l'ensemble des restos

        un sous dico --> fiche du resto {"nom", "adresse", {horaires}, "avis", {menu}}

          menu --> {{formule1}, {formule2}, {formule3}, {Plats}, {Boissons}, {Desserts}, {Accompagnements}}
              formule1 --> {"Plat", "Boisson"}
              formule2 --> {"Plat", "Dessert"}            --> chaque attributs rappellent les informations des dico supérieurs 
              formule3 --> {"Plat", "Boisson", "Dessert"}

              Plats --> {{plat1}, {plat2}, {plat3}} --> la meme pour boissons / Desserts / Accompagnement
                    plat1 --> {"nom", "prix", "composition", "durée de prod"}  --> la meme pour boissons / Desserts / Accompagnement

