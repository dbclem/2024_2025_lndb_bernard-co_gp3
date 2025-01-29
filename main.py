from data import*
from tkinter import*
# from edgar import main_operateur_window
from tools import destroy_all_widgets
from PIL import Image, ImageTk

"""
couleur :
        bleu foncé pour les boutons--> #0066FF
        bleu clair pour l'arriere plan --> #DEF4FA
"""

def reset_commandes():
    global global_tuple_menu_price
    global_tuple_menu_price = []
    global global_list_commande
    global_list_commande = []
    global global_dico_all_choices_price
    global_dico_all_choices_price = []
    global total_price
    total_price = 0
    print("Panier vidé")


def main_window():
    """
    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    main_user_window = Tk()
    screen_width = main_user_window.winfo_screenwidth()
    screen_height = main_user_window.winfo_screenheight()
    main_user_window.title("Bernard&co")
    main_user_window.configure(bg = "#DEF4FA")
    main_user_window_width = screen_width // 2
    main_user_window_height = screen_height
    main_user_window.geometry(f"{main_user_window_width}x{main_user_window_height}")
    main_user_window.iconbitmap("images/logo_bernard&co.ico")

    def validate_admin(username, password) : 
        if username == dico_mdp["username"] and password == dico_mdp["password"] : 
            main_user_window.destroy()
            """main_operateur_window()"""

    def display_admin_check() : 
        destroy_all_widgets(main_user_window)

        username_label = Label(main_user_window, text="Nom d'utilisateur", font=("Avenir", 12))
        username_label.pack(pady=5)
        username_entry = Entry(main_user_window, font=("Avenir", 12))
        username_entry.pack(pady=5)
        
        password_label = Label(main_user_window, text="Mot de passe", font=("Avenir", 12))
        password_label.pack(pady=5)
        password_entry = Entry(main_user_window, show="*", font=("Avenir", 12))
        password_entry.pack(pady=5)
    
        validate_button = Button(main_user_window, text="Valider", font=("Avenir", 12), command=lambda: validate_admin(username_entry.get(), password_entry.get()))
        validate_button.pack(pady=10)

    def display_restaurants_names () :  
        admin_button = Button(main_user_window, text="Admin", font=("Avenir", 15),  fg = "#FFFFFF", bg="#0066FF", command=lambda : display_admin_check())
        admin_button.pack(side=TOP, pady=20, padx=20)

        main_text = Label(main_user_window, text="Choisissez votre restaurant", font=("Avenir", 20), bg="#0066FF", fg = "#FFFFFF")
        main_text.place(relx=0.5, rely=0.2, anchor=CENTER)


        for index, restaurant in enumerate(data):
            image = Image.open(restaurant["image_path"])
            image = image.resize((180, 100))  # Ajustez la taille de l'image
            photo = ImageTk.PhotoImage(image)  # Convertir pour Tkinter
            """ enumerate --> Parcourt data recupère la position index et la valeur restaurant 
                        index --> 0, 1, 2, ...
                        restaurant --> {nom : restaurant}

                open_restaurant_window prend i qui est index et qui se mais a jour a dynamiquement
            """
            Bouton_restaurant = Button(main_user_window, text=restaurant["nom"],
                                       image = photo, compound = "right", padx = 70, height=80, width=460, font=("Avenir", 20), fg = "#FFFFFF", bg = "#0066FF",
                command=lambda i=index: [destroy_all_widgets(main_user_window), restaurant_window(i)])
            Bouton_restaurant.image = photo
            Bouton_restaurant.place(relx=0.5, rely=0.5 + index * 0.1, anchor=CENTER)
        



    def restaurant_window(index):
        """
            s'active autant de fois que de nombre de restaurant 
            le nom du restaurant data[index]["nom"] --> on va cherher dans la liste data avec l'indice index 
                                                        puis on prend le "nom" 
                                                        restaurant_name eest donc facilement réutilisable 
        """
        
        global global_tuple_menu_price 
        """            
            creation d'un tuple (choix, price) pour pouvoir afficher le price dans la commande
            la commande et le price sont donc lié
        """
        for key in list(data[index]["menus"].keys()):
            price = data[index]["menus"][key]["price"]
            global_tuple_menu_price.append((key, price))


        global global_dico_all_choices_price
        unique_items = set()
        """
            ici set permet de ne pas avoir de doublon dans les choix
        """
        for menu_keys, menu in data[index]["menus"].items():
            for item_name, item_price in menu["plat"].items():
                dico_for_each_choice = {
                    "name": item_name,
                    "price": item_price,
                }
                unique_items.add(tuple(sorted(dico_for_each_choice.items())))
            if "dessert" in menu:
                for item_name, item_price in menu["dessert"].items():
                    dico_for_each_choice = {
                        "name": item_name,
                        "price": item_price,
                    }
                    unique_items.add(tuple(dico_for_each_choice.items()))
            if "boisson" in menu:
                for item_name, item_price in menu["boisson"].items():
                    dico_for_each_choice = {
                        "name": item_name,
                        "price": item_price,
                    }
                    unique_items.add(tuple(dico_for_each_choice.items()))

        # Convertir les tuples de retour en dictionnaires
        global_dico_all_choices_price = [dict(item) for item in unique_items]



        def add_to_commande (formule) : 
            global global_list_commande
            global global_total_price
            global_list_commande.append(formule)
            global_total_price += formule["price"]
            print(f"La {formule['name']} a été ajoutée au panier au price de {formule['price']}.")
            update_total_price()

        def check_the_menu_not_empty(dico_choices_in_the_menu) : 
            is_not_valid = False
            for value in dico_choices_in_the_menu.values() :
                if value == "" :
                    is_not_valid = True
                    break
                else : 
                    is_not_valid = False
        

            if is_not_valid :
                choice_not_finished_text = Label(main_user_window, text="Vous n'avez pas fini votre commande !", font=("Avenir", 20), bg="#DEF4FA")
                choice_not_finished_text.pack(side=BOTTOM, pady=10)
                choice_not_finished_text.after(2000, lambda : choice_not_finished_text.destroy())
            else : 
                add_to_commande(dico_choices_in_the_menu)
                refresh_price(main_user_window)
                display_menus()
                print(global_list_commande)

        def add_element_to_dico_final (element, key, dico_choices_in_the_menu) :
            dico_choices_in_the_menu[element] = key
            
        def element_in_commande (name, element, dico_choices_in_the_menu) :
            main_element_frame = Frame(main_user_window, bd=2, relief="solid", padx=5, pady=5, bg="#DEF4FA")
            main_element_frame.pack(pady=10)
            main_element_text = Label(main_element_frame, text=element, font=("Avenir", 15), bg="#DEF4FA")
            main_element_text.pack()

            for key in list(data[index]["menus"][name][element].keys()) : 
                element_buttons = Button(main_user_window, text=key, height=2, width=50, fg = "#FFFFFF", bg = "#0066FF",
                                    command=lambda key=key : 
                                    [add_element_to_dico_final(element, key, dico_choices_in_the_menu)])
                element_buttons.pack(pady=10)

        def display_the_menu (name, price):
            nav_in_the_menu_frame = Frame(main_user_window, bg="#DEF4FA")
            nav_in_the_menu_frame.pack(side=TOP, pady=10)

            retour_menus_button = Button(nav_in_the_menu_frame, text="Retour", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", command=lambda : 
                                         [destroy_all_widgets(main_user_window), display_menus()])
            retour_menus_button.pack(side=LEFT, pady=10, padx=10)
            
            valide_the_menu_button = Button(nav_in_the_menu_frame, text="Valider", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", command=lambda : 
                                            [check_the_menu_not_empty(dico_choices_in_the_menu)]) 
            valide_the_menu_button.pack(side=LEFT, pady=10, padx=10)
                    
            dico_choices_in_the_menu = {
                                        "name" : name,
                                        "price" : 0,
                                        "temps" : 0,
                                    }

            for element in list (data[index]["menus"][name].keys()) : 
                if element == "price" or element == "temps" : 
                    dico_choices_in_the_menu["price"] = price
                    dico_choices_in_the_menu["temps"] = data[index]["menus"][name]["temps"]
                else :
                    dico_choices_in_the_menu[element] = ""  
                    element_in_commande(name, element, dico_choices_in_the_menu)


            
        def display_petite_faim () : 

            nav_petite_faim_frame = Frame(main_user_window, bg="#DEF4FA")    
            nav_petite_faim_frame.pack(side=TOP, pady=10)
            retour_petite_faim_button = Button(nav_petite_faim_frame, text="Retour", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", command=lambda :
                                            [refresh_price(main_user_window), display_menus()]) 
            retour_petite_faim_button.pack(side=LEFT, pady=10, padx=10)

            main_petite_faim_frame = Frame(main_user_window, bd=2, relief="solid", padx=5, pady=5, bg="#DEF4FA")
            main_petite_faim_frame.pack(pady=10)
            for element in global_dico_all_choices_price:
                petite_faim_buttons = Button(main_petite_faim_frame, text=(f"{element['name']} - {element['price']} €" ), height=2, width=50, fg = "#FFFFFF", bg = "#0066FF", 
                                    command=lambda element=element:
                                    [add_to_commande(element), refresh_price(main_user_window),
                                     update_total_price(), display_petite_faim(),
                                     print(global_list_commande)])
                petite_faim_buttons.pack(pady=10)


                  

        def display_menus():
            for name, price in global_tuple_menu_price:
                menus_buttons = Button(main_user_window, text=(f"{name} - {price} €" ), height=2, width=50, fg = "#FFFFFF", bg = "#0066FF", 
                                    command=lambda name=name, price=price:
                                    [refresh_price(main_user_window)
                                      ,display_the_menu(name, price)])
                menus_buttons.pack(pady=10)
            
            petite_faim_button = Button(main_user_window, text="Petite faim", height=2, width=50, fg = "#FFFFFF", bg = "#0066FF", 
                                    command=lambda : 
                                    [refresh_price(main_user_window), display_petite_faim()])
            petite_faim_button.pack(pady=10)
            naviagtion_button()

        def update_total_price():
            total_price_label.config(text=f"Prix total : {global_total_price} €")    
            total_price_label.config(text=f"price total : {global_total_price} $")    
    
        total_price_label = Label(main_user_window, text="", font="Avenir", bg="#DEF4FA")
        total_price_label.pack(side=BOTTOM, pady=20)

        def naviagtion_button():    
            nav_buttons_frame = Frame(main_user_window, bg="#DEF4FA")
            nav_buttons_frame.pack(side=BOTTOM, pady=20)

            nav_retour_button = Button(nav_buttons_frame, text="Retour", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", command=lambda window=main_user_window: 
                                    [destroy_all_widgets(window), reset_commandes(), display_restaurants_names()])
            nav_retour_button.pack(side=LEFT, padx=10)

            nav_voir_commande_button = Button(nav_buttons_frame, text="Voir la commande", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", 
                                            command=lambda : 
                                            [refresh_price(main_user_window), display_commande()])
            nav_voir_commande_button.pack(side=LEFT, padx=10)

            nav_valide_button = Button(nav_buttons_frame, text="Valider", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", command=check_commande_not_empty)
            nav_valide_button.pack(side=LEFT, padx=10)
            
            def change_button_color(event):
                nav_valide_button.config(bg="green")  
            nav_valide_button.bind("<Button-1>", change_button_color)



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
                panier_vide_text = Label(main_user_window, text="Votre panier est vide", font="Avenir", bg="#DEF4FA")
                panier_vide_text.pack(pady=10)
                
            else : 
                main_commande_text = Label(main_user_window, text="Votre panier :" , font=("Avenir", 20), bg="#DEF4FA")
                main_commande_text.pack()
                click_to_supp_text = Label(main_user_window, text="Appuiez pour supprimer", font=("Avenir", 10), bg="#DEF4FA")
                click_to_supp_text.pack()

                for element in global_list_commande:
                    if "plat" not in element : 
                        text = f"{element['name']} - {element['price']} €"
                    else :
                        # commande faite a partir de chatgpt qui permet de modifier réactivement le texte
                        text = " - ".join([f"{value} $" if key == "price" else f"{value}" for key, value in element.items() if key != "temps"])

                    element_of_commande_button = Button(main_user_window, text=text, font=("Avenir", 10), fg = "#FFFFFF", bg = "#0066FF", command=lambda element=element: 
                                                        [remove_in_global_list_command_total_price(element), refresh_price(main_user_window),
                                                        display_commande(), update_total_price()])
                    element_of_commande_button.pack(pady=10)

            retour_commande_button = Button(main_user_window, text="Retour", font="Avenir", fg = "#FFFFFF", bg = "#0066FF", command=lambda : 
                                [refresh_price(main_user_window), display_menus()])
            retour_commande_button.pack(side=BOTTOM, pady=10)


        def valide_message (index):
            destroy_all_widgets(main_user_window)
            frame_nav_valide = Frame(main_user_window, bg="#DEF4FA")
            frame_nav_valide.pack(side=TOP, pady=10)

            valide_message_text = f"Votre commande a bien été validée \n pour un montant de {global_total_price} €"
            main_valide_message_text = Label(main_user_window, text=valide_message_text, font=("Avenir", 20), bg="#DEF4FA")
            main_valide_message_text.pack(expand=True, anchor='center')

            retour_a_la_commande_button = Button(frame_nav_valide, text="revenir a la commande", font=("Avenir", 10), fg = "#FFFFFF", bg = "#0066FF",
                                                 command= lambda i=index : [destroy_all_widgets(main_user_window), restaurant_window(i)])
            retour_a_la_commande_button.pack(side=LEFT, padx=10)
            nouvelle_commande_button = Button(frame_nav_valide, text="Faire une nouvelle commande", font=("Avenir", 10), fg = "#FFFFFF", bg = "#0066FF",
                                                 command= lambda : [main_user_window.destroy(), reset_commandes(), main_window()])
            nouvelle_commande_button.pack(side=LEFT, padx=10)


        def check_commande_not_empty () : 
            if global_list_commande == [] : 
                panier_vide_text = Label(main_user_window, text="Votre panier est vide", font=("Avenir", 20), bg="#DEF4FA")
                panier_vide_text.pack(side=BOTTOM, pady=10)
                panier_vide_text.after(2000, lambda : panier_vide_text.destroy())
            else : 
                valide_message(index)

        display_menus()

    display_restaurants_names()
    main_user_window.mainloop()





global_list_commande = []
global_tuple_menu_price = []
global_dico_all_choices_price = []
global_total_price = 0
main_window()
