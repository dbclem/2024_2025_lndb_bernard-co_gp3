from data import*
from tkinter import*
from tools import destroy_all_widgets

"""
couleur : noir --> #000000
        bleu --> #3533cd
        degradé lineaire 90°
"""
"""
    pour cassandre :
    tu peux commencer le design a partir de ca, la code apres va pas bcp bouger 
    il reste deux problemes a regler : la couleur verte des boutons 
    et la verification des choix dans le menu

    et il reste a rajouter une option petit fain pour prendre qlq chode a l'unité   
"""


def reset_commandes():
    global global_tuple_menu_price
    global_tuple_menu_price = []
    global global_list_commande
    global_list_commande = []
    global total_price
    total_price = 0
    print("Panier vidé")


def main_window():
    """
    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    main_user_window = Tk()
    main_user_window.title("Bernard&co")
    main_user_window.geometry("412x700")
    main_user_window.iconbitmap("images/logo_bernard&co.ico")
    # main_user_window.configure(bg="#3533cd")

    def display_restaurants_names () :  
        main_text = Label(main_user_window, text="Choisissez votre restaurant", font=("Calibri", 20))
        main_text.pack(expand=True)

        restaurants_frame = Frame(main_user_window)
        restaurants_frame.pack(expand=True)

        for index, restaurant in enumerate(data):
            """ enumerate --> Parcourt data recupère la position index et la valeur restaurant 
                        index --> 0, 1, 2, ...
                        restaurant --> {nom : restaurant}

                open_restaurant_window prend i qui est index et qui se mais a jour a dynamiquement
            """
            restaurants_buttons = Button(restaurants_frame, text=restaurant["nom"], height=2, width=50, font="Calibri", 
                command=lambda i=index: [destroy_all_widgets(main_user_window), restaurant_window(i)])
            restaurants_buttons.pack(pady=5)


    def restaurant_window(index):
        """
            s'active autant de fois que de nombre de restaurant 
            le nom du restaurant data[index]["nom"] --> on va cherher dans la liste data avec l'indice index 
                                                        puis on prend le "nom" 
                                                        restaurant_name eest donc facilement réutilisable 
        """
        
        global global_tuple_menu_price 
        """            
            creation d'un tuple (choix, prix) pour pouvoir afficher le prix dans la commande
            la commande et le prix sont donc lié
        """
        for key in list(data[index]["menus"].keys()):
            prix = data[index]["menus"][key]["prix"]
            global_tuple_menu_price.append((key, prix))




        # def on_button_click(index):
        #     global global_buttons
        #     # Remettre tous les boutons en blanc
        #     for i, button in enumerate(global_buttons):
        #         button.config(bg="white")
        #     # Mettre le bouton cliqué en vert
        #     global_buttons[index].config(bg="green")

        def add_to_commande (formule) : 
            global global_list_commande
            global global_total_price
            global_list_commande.append(formule)
            global_total_price += formule["price"]
            print(f"La {formule['name']} a été ajoutée au panier au prix de {formule['price']}.")
            update_total_price()

        def check_the_menu_not_empty(dico_choices_in_the_menu) : 
            """fonction pas encore terminée : suggestion --> hecker si un bouton de chaque catégorie a été cliqué"""
            if dico_choices_in_the_menu["plat"] == "" :
                choice_not_finished_text = Label(main_user_window, text="Veuillez choisir un plat", font=("Calibri", 20))
                choice_not_finished_text.pack(side=BOTTOM, pady=10)
                choice_not_finished_text.after(2000, lambda : choice_not_finished_text.destroy())
            else : 
                add_to_commande(dico_choices_in_the_menu)
                refresh_price(main_user_window)
                display_menus()
                print(global_list_commande)

        def add_element_to_dico_final (element, key, dico_choices_in_the_menu) :
            dico_choices_in_the_menu[element] = key
            
        def element_in_commande (name, element, dico_choices_in_the_menu, choice_the_menu_frame) :
            main_element_text = Label(choice_the_menu_frame, text=element, font=("Calibri", 10), underline=True)
            main_element_text.pack(pady=10)

            global global_buttons
            global_buttons = []
            for i, key in enumerate(list(data[index]["menus"][name][element].keys())) : 
                element_buttons = Button(choice_the_menu_frame, text=key, height=2, width=50, 
                                    command=lambda i=i, key=key : 
                                    [add_element_to_dico_final(element, key, dico_choices_in_the_menu)])
                element_buttons.pack(pady=10)
                global_buttons.append(element_buttons)

        def display_the_menu (name, price):
            choice_the_menu_frame = Frame(main_user_window)
            choice_the_menu_frame.pack(expand=True)
            dico_choices_in_the_menu = {
                                        "name" : name,
                                        "price" : 0,
                                        "temps" : 0,
                                        "plat" : "",
                                        "dessert" : "",
                                        "boisson" : ""
                                    }

            for element in list (data[index]["menus"][name].keys()) : 
                if element == "prix" or element == "temps" : 
                    dico_choices_in_the_menu["price"] = price
                    dico_choices_in_the_menu["temps"] = data[index]["menus"][name]["temps"]
                else :
                    element_in_commande(name, element, dico_choices_in_the_menu, choice_the_menu_frame)

            nav_in_the_menu_frame = Frame(choice_the_menu_frame)
            nav_in_the_menu_frame.pack(side=BOTTOM, pady=10)
            retour_menus_button = Button(nav_in_the_menu_frame, text="Retour", font="Calibri", command=lambda : 
                                         [destroy_all_widgets(choice_the_menu_frame), display_menus()])
            retour_menus_button.pack(side=LEFT, pady=10, padx=10)
            valide_the_menu_button = Button(nav_in_the_menu_frame, text="Valider", font="Calibri", command=lambda : 
                                            [check_the_menu_not_empty(dico_choices_in_the_menu)]) 
            valide_the_menu_button.pack(side=LEFT, pady=10, padx=10)
                    
            

        def display_menus():
            for name, price in global_tuple_menu_price:
                menus_buttons = Button(main_user_window, text=(f"{name} - {price} $" ), height=2, width=50, 
                                    command=lambda name=name, price=price:
                                    [refresh_price(main_user_window)
                                      ,display_the_menu(name, price)])
                menus_buttons.pack(pady=10)
            naviagtion_button()

        def update_total_price():
            total_price_label.config(text=f"Prix total : {global_total_price} $")    
    
        total_price_label = Label(main_user_window, text="", font="Calibri")
        total_price_label.pack(side=BOTTOM, pady=20)

        def naviagtion_button():    
            nav_buttons_frame = Frame(main_user_window)
            nav_buttons_frame.pack(side=BOTTOM, pady=20)

            nav_retour_button = Button(nav_buttons_frame, text="Retour", font="Calibri", command=lambda window=main_user_window: 
                                    [destroy_all_widgets(window), reset_commandes(), display_restaurants_names()])
            nav_retour_button.pack(side=LEFT, padx=10)

            nav_voir_commande_button = Button(nav_buttons_frame, text="Voir la commande", font="Calibri", 
                                            command=lambda : 
                                            [refresh_price(main_user_window), display_commande()])
            nav_voir_commande_button.pack(side=LEFT, padx=10)

            nav_valide_button = Button(nav_buttons_frame, text="Valider", font="Calibri", command=check_commande_not_empty)
            nav_valide_button.pack(side=LEFT, padx=10)


        def remove_in_global_list_command_total_price(element):
            global global_list_commande
            global_list_commande.remove(element)
            global global_total_price
            global_total_price -= element["price"]
            print(f"Item {element} supprimé")

        def refresh_price(window):
            """Efface tous les widgets et réexécute le code pour recréer la page.
                et reafficher les elements du panier et la titre de la page 
            """
            for widget in window.winfo_children():
                if widget != total_price_label:
                    widget.destroy()

        def display_commande () :
            if global_list_commande == [] : 
                panier_vide_text = Label(main_user_window, text="Votre panier est vide", font="Calibri")
                panier_vide_text.pack(pady=10)
                
            else : 
                main_commande_text = Label(main_user_window, text="Votre panier :" , font=("Calibri", 20))
                main_commande_text.pack()
                click_to_supp_text = Label(main_user_window, text="Appuiez pour supprimer", font=("Calibri", 10))
                click_to_supp_text.pack()

                for element in global_list_commande:
                    text = f"{element['name']} - {element['price']} $ \n {element['plat']} - {element['dessert']} - {element['boisson']}"
                    element_of_commande_button = Button(main_user_window, text=text, font=("Calibri", 10), command=lambda : 
                                                        [remove_in_global_list_command_total_price(element), refresh_price(main_user_window),
                                                         display_commande(), update_total_price()])
                    element_of_commande_button.pack(pady=10)

            retour_commande_button = Button(main_user_window, text="Retour", font="Calibri", command=lambda : 
                                [refresh_price(main_user_window), display_menus()])
            retour_commande_button.pack(side=BOTTOM, pady=10)


            


        def temps_attente ():
            """
                Calcul du temps d'attente en fonction des menus choisis
                key --> nom du menu
                _ --> valeur du menu qui n'est pas utilisé
            """
            global global_list_commande
            temps = 0 
            for key in global_list_commande : 
                temps += key["temps"]
            return temps

        def valide_message ():
            destroy_all_widgets(main_user_window)

            valide_message_text = f"Votre commande a bien été validée \n pour un montant de {global_total_price} $"
            main_valide_message_text = Label(main_user_window, text=valide_message_text, font=("Calibri", 20))
            main_valide_message_text.pack(expand=True, anchor='center')

            temps_attente_text = f"Votre commande sera prête \n dans {temps_attente()} minutes"
            main_temps_attente_text = Label(main_user_window, text=temps_attente_text, font=("Calibri", 20))
            main_temps_attente_text.pack(expand=True, anchor='center')
            
        def check_commande_not_empty () : 
            if global_list_commande == [] : 
                panier_vide_text = Label(main_user_window, text="Votre panier est vide", font=("Calibri", 20))
                panier_vide_text.pack(side=BOTTOM, pady=10)
                panier_vide_text.after(2000, lambda : panier_vide_text.destroy())
            else : 
                valide_message()

        display_menus()

    display_restaurants_names()
    main_user_window.mainloop()





global_list_commande = []
global_tuple_menu_price = []
global_total_price = 0
global_buttons = []
main_window()
