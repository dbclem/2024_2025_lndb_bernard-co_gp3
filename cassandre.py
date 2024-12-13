from tkinter import* 
from data import*
from tools import*

global_list_commande = []

def main_window():
    """
    main_user_window est une variable global pour pour*voir la réccupérer pour chaques fonctions
    et pouvoir la détruire

    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    main_user_window = Tk()
    main_user_window.title("Bernard&co")
    main_user_window.geometry("412x700")



    main_text = Label(main_user_window, text="Choisissez votre restaurant", font="Calibri")
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



    def add_to_commande (choix) : 
        global global_list_commande
        global_list_commande.append(choix)
        print (f"La {choix} a été ajouter au panier.")

    canvas = Canvas(restaurant_window)
    canvas.pack(expand=True, fill=BOTH)

    scrollbar = Scrollbar(restaurant_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    

    for key in list ( data[index]["menus"].keys()) : 
        menu_frame = Button(restaurant_window, text=key, height=2, width=50, command = lambda key=key : add_to_commande(key))
        menu_frame.pack(pady=10)


        """ Affichage des plats, desserts et boissons du restaurant """
    menu_frame = Frame(restaurant_window)
    menu_frame.pack(expand=True)

    # Affichage des plats
    plat_label = Label(menu_frame, text="Plats", font=("Calibri", 14))
    plat_label.pack(pady=5)

    for plat in list(data[index]["menus"]["formule patus 1"]["plat"]["paninis"].keys()):
        plat_button = Button(menu_frame, text=plat, height=2, width=50, command=lambda plat=plat: add_to_commande(plat))
        plat_button.pack(pady=5)

    for plat in list(data[index]["menus"]["formule patus 1"]["plat"]["pates"].keys()):
        plat_button = Button(menu_frame, text=plat, height=2, width=50, command=lambda plat=plat: add_to_commande(plat))
        plat_button.pack(pady=5)

    # Affichage des desserts
    dessert_label = Label(menu_frame, text="Desserts", font=("Calibri", 14))
    dessert_label.pack(pady=5)

    for dessert in list(data[index]["menus"]["formule patus 1"]["dessert"].keys()):
        dessert_button = Button(menu_frame, text=dessert, height=2, width=50, command=lambda dessert=dessert: add_to_commande(dessert))
        dessert_button.pack(pady=5)

    # Affichage des boissons
    boisson_label = Label(menu_frame, text="Boissons", font=("Calibri", 14))
    boisson_label.pack(pady=5)

    for boisson in list(data[index]["menus"]["formule patus 1"]["boisson"].keys()):
        boisson_button = Button(menu_frame, text=boisson, height=2, width=50, command=lambda boisson=boisson: add_to_commande(boisson))
        boisson_button.pack(pady=5)
        
    menu_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


    """
     creation d'une frame qui se place en bas de la page grace a BOTTOM
        deux boutons a l'interieur : retour --> revenir a la page d'accueil 
                                                aligné en bas au milieu par la gauche 
                                    validée --> validée la commande --> inactif pour l'insant
                                                aligné avec le bouton retour il se place à sa gauche   
    """
    
    button_frame = Frame(restaurant_window)
    button_frame.pack(side=BOTTOM, pady=20)

    bouton_retour = Button(button_frame, text="Retour", font="Calibri", command=lambda: [restaurant_window.destroy(), main_window()])
    bouton_retour.pack(side=LEFT, padx=10)

    bouton_validee = Button(button_frame, text="Voir la commande", font="Calibri", command=lambda: print(f"Réservation validée pour {restaurant_name}"))
    bouton_validee.pack(side=LEFT, padx=10)



    restaurant_window.mainloop()

main_window()