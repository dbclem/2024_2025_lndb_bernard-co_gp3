from data import*
from tkinter import*
from tools import destroy_all_widgets

"""
couleur : noir --> #000000
        bleu --> #3533cd
        degradé lineaire 90°
"""
def reset_commandes():
    global global_menus_price
    global_menus_price = []
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
        
        global global_menus_price 

        """            
            creation d'un tuple (choix, prix) pour pouvoir afficher le prix dans la commande
            la commande et le prix sont donc lié
        """
        for key in list(data[index]["menus"].keys()):
            prix = data[index]["menus"][key]["prix"]
            global_menus_price.append((key, prix))


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
                

        def add_element_to_dico_final (element, key, dico_choices_in_the_menu) :
            dico_choices_in_the_menu[element] = key
            
        
        def element_in_commande (name, element, dico_choices_in_the_menu, choice_the_menu_frame) :
            main_element_frame = Frame(choice_the_menu_frame)
            main_element_frame.pack(expand=True)
            main_element_text = Label(main_element_frame, text=element, font=("Calibri", 10), underline=True)
            main_element_text.pack(pady=10)
            for key in list(data[index]["menus"][name][element].keys()) : 
                element_buttons = Button(main_element_frame, text=key, height=2, width=50, 
                                    command=lambda key=key : 
                                    [add_element_to_dico_final(element, key, dico_choices_in_the_menu)])
                element_buttons.pack(pady=10)

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

            retour_menus_button = Button(choice_the_menu_frame, text="Retour", font="Calibri", command=lambda : 
                                         [destroy_all_widgets(choice_the_menu_frame), display_menus()])
            retour_menus_button.pack(side=BOTTOM, pady=10)
            valide_the_menu_button = Button(choice_the_menu_frame, text="Valider", font="Calibri", command=lambda : 
                                            [check_the_menu_not_empty(dico_choices_in_the_menu)]) 
                    
            

        def display_menus():
            global global_list_commande
            for name, price in global_menus_price:
                menus_buttons = Button(main_user_window, text=(f"{name} - {price} $" ), height=2, width=50, 
                                    command=lambda name=name, price=price:
                                    [destroy_all_widgets(main_user_window)
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
                                            [refresh_price(), display_commande()])
            nav_voir_commande_button.pack(side=LEFT, padx=10)

            nav_valide_button = Button(nav_buttons_frame, text="Valider", font="Calibri", command=check_commande_not_empty)
            nav_valide_button.pack(side=LEFT, padx=10)



        def remove_in_global_list_command_total_price(item):
            global global_list_commande
            global_list_commande.remove(item)
            global global_total_price
            global_total_price -= item[1]
            print(f"Item {item} supprimé")

        def refresh_price():
            """Efface tous les widgets et réexécute le code pour recréer la page.
                et reafficher les elements du panier et la titre de la page 
            """
            for widget in main_user_window.winfo_children():
                if widget != total_price_label:
                    widget.destroy()

        def display_commande () :
            if global_dico_final_choices["name"] == "" : 
                panier_vide_text = Label(main_user_window, text="Votre panier est vide", font="Calibri")
                panier_vide_text.pack(pady=10)
                
            else : 
                main_commande_text = Label(main_user_window, text="Votre panier :" , font=("Calibri", 20))
                main_commande_text.pack()
                click_to_supp_text = Label(main_user_window, text="Appuiez pour supprimer", font=("Calibri", 10))
                click_to_supp_text.pack()

                for key, value in global_dico_final_choices.items() : 
                    if key != "name" and key != "price" and key != "temps" : 
                        main_commande_text = Label(main_user_window, text=f"{key} : {value}", font=("Calibri", 10))
                        main_commande_text.pack(pady=10)

            #     for i, (choice, prix) in enumerate(global_list_commande):
            #         print(f"Création du bouton pour l'élément {i}: {choice} au prix de {prix}")

            #         # Création d'un bouton pour chaque élément de la liste
            #         choiced_menu_button = Button(main_user_window, text=f"{choice}" + " " + f"{prix}  $", font="Calibri", 
            #                                     command=lambda item=(choice, prix): 
            #                                     [remove_in_global_list_command_total_price(item), refresh_price(), 
            #                                     display_commande(), update_total_price()])
            #         choiced_menu_button.pack(pady=10)

            # retour_commande_button = Button(main_user_window, text="Retour", font="Calibri", command=lambda : 
            #                     [refresh_price(), display_menus()])
            # retour_commande_button.pack(side=BOTTOM, pady=10)


        def temps_attente ():
            """
                Calcul du temps d'attente en fonction des menus choisis
                key --> nom du menu
                _ --> valeur du menu qui n'est pas utilisé
            """
            global global_list_commande
            temps = 0 
            for key, _ in global_list_commande : 
                temps += data[index]["menus"][key]["temps"]
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
global_menus_price = []
global_total_price = 0
global_dico_final_choices = {
    "name" : "",
    "price" : 0,
    "temps" : 0,
    "plat" : "",
    "dessert" : "",
    "boisson" : ""
}

main_window()
