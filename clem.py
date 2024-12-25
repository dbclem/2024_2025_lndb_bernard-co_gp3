from data import*
from tkinter import*
from tools import*

"""
couleur : noir --> #000000
        bleu --> #3533cd
        degradé lineaire 90°
"""
def reset_commande():
    global global_list_commande
    global_list_commande = []
    global total_price
    total_price = 0
    print("Panier vidé")


def main_window():
    """
    main_user_window est une variable global pour pouvoir la réccupérer pour chaques fonctions
    et pouvoir la détruire

    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    main_user_window = Tk()
    main_user_window.title("Bernard&co")
    main_user_window.geometry("412x700")
    main_user_window.iconbitmap("images/logo_bernard&co.ico")
    main_user_window.configure(bg="#3533cd")




    main_text = Label(main_user_window, text="Choisissez votre restaurant", font=("Calibri", 20))
    main_text.pack(expand=True)
    


    """creation d'une frame pour y placer seulement les boutons qui mène a des restaurants"""
    frame = Frame(main_user_window)
    frame.pack(expand=True)



    for index, restaurant in enumerate(data):
        """ enumerate --> Parcourt data recupère la position index et la valeur restaurant 
                    index --> 0, 1, 2, ...
                    restaurant --> {nom : restaurant}

            open_restaurant_window prend i qui est index et qui se mais a jour a dynamiquement
        """
        Bouton_restaurant = Button(frame, text=restaurant["nom"], height=2, width=50, font="Calibri", 
            command=lambda i=index: open_restaurant_window(i))
        Bouton_restaurant.pack(pady=5)



    main_user_window.mainloop()


def valide_window():
    valide_window = Tk()
    valide_window.title("Valider la commande")
    valide_window.geometry("412x700")

    main_valide_text = Label(valide_window, text="Votre commande a \n bien été validée", font=("Calibri", 20))
    main_valide_text.pack()

    valide_window.mainloop()


# def commande_window():
#     global global_list_commande
#     print(global_list_commande)

#     commande_window = Tk()
#     commande_window.title("Voir la commande")
#     commande_window.geometry("412x700")

#     # Afficher le titre de la commande



#     commande_window.mainloop()





def open_restaurant_window(index):
    """
        s'active autant de fois que de nombre de restaurant 
        le nom du restaurant data[index]["nom"] --> on va cherher dans la liste data avec l'indice index 
                                                    puis on prend le "nom" 
                                                    restaurant_name eest donc facilement réutilisable 
    """
    main_user_window.destroy()
    


    restaurant_name = data[index]["nom"]
    restaurant_window = Tk()
    restaurant_window.title(f"Bernard&co - {restaurant_name}")
    restaurant_window.geometry("412x700")
    


    display_restaurant_name = Label(restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()

    global global_choice_prix 
    """            
        creation d'un tuple (choix, prix) pour pouvoir afficher le prix dans la commande
        la commande et le prix sont donc lié
    """
    for key in list(data[index]["menus"].keys()):
        prix = data[index]["menus"][key]["prix"]
        global_choice_prix.append((key, prix))


    def add_to_commande (choix, prix) : 
        """"
            ajout de l'element choisi dans la liste global_list_commande
        """
        global global_list_commande
        global global_total_price
        global_list_commande.append((choix, prix))
        global_total_price += prix
        print(f"La {choix} a été ajoutée au panier au prix de {prix}.")
        update_total_price()
        
    def diplay_menu():
        global global_list_commande
        for key, value in global_choice_prix:
            menu_button = Button(restaurant_window, text=(key + diplays_prix(key)), height=2, width=50, 
                                 command=lambda key=key, value=value: add_to_commande(key, value))
            menu_button.pack(pady=10)
        naviagtion_button()

    def diplays_prix(key):
        prix = data[index]["menus"][key]["prix"]
        return f"  {prix} $"

    def update_total_price():
        total_price_label.config(text=f"Prix total : {global_total_price} $")

 
 
    total_price_label = Label(restaurant_window, text="", font="Calibri")
    total_price_label.pack(side=BOTTOM, pady=20)



    """
     creation d'une frame qui se place en bas de la page grace a BOTTOM
        deux boutons a l'interieur : retour --> revenir a la page d'accueil 
                                                aligné en bas au milieu par la gauche 
                                    validée --> validée la commande --> inactif pour l'insant
                                                aligné avec le bouton retour il se place à sa gauche   
    """

    def naviagtion_button():    
        button_frame = Frame(restaurant_window)
        button_frame.pack(side=BOTTOM, pady=20)

        bouton_retour = Button(button_frame, text="Retour", font="Calibri", command=lambda : 
                                [restaurant_window.destroy(), reset_commande(), main_window()])
        bouton_retour.pack(side=LEFT, padx=10)

        bouton_voir_commande = Button(button_frame, text="Voir la commande", font="Calibri", 
                                        command=lambda index = restaurant_window : 
                                        [refresh_restaurant_page(index), display_commande()])
        bouton_voir_commande.pack(side=LEFT, padx=10)

        bouton_valide = Button(button_frame, text="Valider", font="Calibri", command=valide_window)
        bouton_valide.pack(side=LEFT, padx=10)



    def delete_in_global_list_total_price(item):
        # Suppression de l'élément dans global_list_commande
        global global_list_commande
        global_list_commande.remove(item)
        global global_total_price
        global_total_price -= item[1]
        print(f"Item {item} supprimé")

    def refresh_restaurant_page(window):
        """Efface tous les widgets et réexécute le code pour recréer la page.
            et reafficher les elements du panier et la titre de la page 
        """
        for widget in window.winfo_children():
            if widget != total_price_label:
                widget.destroy()

    def display_commande () :
        if global_list_commande == [] : 
            label_nothing = Label(restaurant_window, text="Votre panier est vide", font="Calibri")
            label_nothing.pack(pady=10)
            
        else : 
            main_commande_text = Label(restaurant_window, text="Votre panier :" , font=("Calibri", 20))
            main_commande_text.pack()
            sous_label_text = Label(restaurant_window, text="Appuiez pour supprimer", font=("Calibri", 10))
            sous_label_text.pack()

            for i, (choice, prix) in enumerate(global_list_commande):
                print(f"Création du bouton pour l'élément {i}: {choice} au prix de {prix}")

                # Création d'un bouton pour chaque élément de la liste
                button_of_choice = Button(restaurant_window, text=f"{choice}" + " " + f"{prix}  $", font="Calibri", 
                                            command=lambda item=(choice, prix): 
                                            [delete_in_global_list_total_price(item), refresh_restaurant_page(restaurant_window), 
                                            display_commande(), update_total_price()])
                button_of_choice.pack(pady=10)

        button_retour_comande = Button(restaurant_window, text="Retour", font="Calibri", command=lambda : 
                            [refresh_restaurant_page(restaurant_window), diplay_menu()])
        button_retour_comande.pack(BOTTOM, pady=10)



    diplay_menu ()
    restaurant_window.mainloop()





global_list_commande = []
global_choice_prix = []
global_total_price = 0

main_window()

"""probleme :
        - les formules s'affiche correctement la premeiere fois 
        - mais lorsque l'on change de restaurant les formules ne s'affichent plus
        - sur le meme restaurant les formules se cumulent elles s'affiche plusieurs fois 
        - donc il faudrait corriger cela au niveau sans doute du bouton retour  
"""

"""probleme 2 :
    - une fois le programme lancé --> il marche normalement 
    - mais si on ferme la fenetre principale, une autre se reouvre automatiquement     - 
"""