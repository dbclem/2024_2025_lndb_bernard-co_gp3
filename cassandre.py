from data import*
from tkinter import*
from PIL import Image, ImageTk

"""
couleur : noir --> #FFFFFF
        bleu --> #3533cd
        degradé lineaire 90°
police : Avenir
"""
def reset_commande():
    global global_choice_price
    global_choice_price = []
    global global_list_commande
    global_list_commande = []
    global total_price
    total_price = 0
    print("Panier vidé")

def destroy_widgets(window):
    for widget in window.winfo_children():
        widget.destroy()


def main_window():
    """
    main_user_window est une variable global pour pouvoir la réccupérer pour chaques fonctions
    et pouvoir la détruire

    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    main_user_window = Tk()
    screen_width = main_user_window.winfo_screenwidth()
    screen_height = main_user_window.winfo_screenheight()
    main_user_window.title("Bernard&co")
    main_user_window_width = screen_width // 2
    main_user_window_height = screen_height
    main_user_window.geometry(f"{main_user_window_width}x{main_user_window_height}")
    main_user_window.iconbitmap("images/logo_bernard&co.ico")
    # main_user_window.configure(bg="#3533cd")



    def display_restaurant_name () :  
        main_text = Label(main_user_window, text="Choisissez votre restaurant", font=("Avenir", 30))
        main_text.pack(expand=True)
        


        """creation d'une frame pour y placer seulement les boutons qui mène a des restaurants"""
        frame = Frame(main_user_window)
        frame.pack(expand=True)



        for index, restaurant in enumerate(data):
            image = Image.open(restaurant["image_path"])
            image = image.resize((300, 170))  # Ajustez la taille de l'image
            photo = ImageTk.PhotoImage(image)  # Convertir pour Tkinter



            """ enumerate --> Parcourt data recupère la position index et la valeur restaurant 
                        index --> 0, 1, 2, ...
                        restaurant --> {nom : restaurant}

                open_restaurant_window prend i qui est index et qui se mais a jour a dynamiquement
            """
            Bouton_restaurant = Button(frame, text=restaurant["nom"],
                                       image = photo, compound = "right", padx = 100, height=170, width=820, font=("Avenir", 20), fg = "#000000",
                command=lambda i=index: [destroy_widgets(main_user_window), restaurant_window(i)])
            Bouton_restaurant.image = photo
            Bouton_restaurant.pack(pady=5)
            #add picture of restaurant


    def restaurant_window(index):
        """
            s'active autant de fois que de nombre de restaurant 
            le nom du restaurant data[index]["nom"] --> on va cherher dans la liste data avec l'indice index 
                                                        puis on prend le "nom" 
                                                        restaurant_name est donc facilement réutilisable 
        """
        
        
        global global_choice_price 
        """            
            creation d'un tuple (choix, prix) pour pouvoir afficher le prix dans la commande
            la commande et le prix sont donc lié
        """
        for key in list(data[index]["menus"].keys()):
            prix = data[index]["menus"][key]["prix"]
            global_choice_price.append((key, prix))


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
            
        def display_menu():
            global global_list_commande
            for key, value in global_choice_price:
                menu_button = Button(main_user_window, text=(f"{key} - {value} $" ), height=2, width=50, 
                                    command=lambda key=key, value=value: add_to_commande(key, value))
                menu_button.pack(pady=10)
            naviagtion_button()
            #add picture of formule (plat, dessert, boisson)


        def update_total_price():
            total_price_label.config(text=f"Prix total : {global_total_price} $")

    
    
        total_price_label = Label(main_user_window, text="", font="Avenir")
        total_price_label.pack(side=BOTTOM, pady=20)



        """
        creation d'une frame qui se place en bas de la page grace a BOTTOM
            deux boutons a l'interieur : retour --> revenir a la page d'accueil 
                                                    aligné en bas au milieu par la gauche 
                                        validée --> validée la commande --> inactif pour l'insant
                                                    aligné avec le bouton retour il se place à sa gauche   
        """

        def naviagtion_button():    
            button_frame = Frame(main_user_window)
            button_frame.pack(side=BOTTOM, pady=20)

            bouton_retour = Button(button_frame, text="Retour", font="Avenir", command=lambda window=main_user_window: 
                                    [destroy_widgets(window), reset_commande(), display_restaurant_name()])
            bouton_retour.pack(side=LEFT, padx=10)

            bouton_voir_commande = Button(button_frame, text="Voir la commande", font="Avenir", 
                                            command=lambda : 
                                            [refresh_price(), display_commande()])
            bouton_voir_commande.pack(side=LEFT, padx=10)

            bouton_valide = Button(button_frame, text="Valider", font="Avenir", command=check_commande)
            bouton_valide.pack(side=LEFT, padx=10)



        def delete_in_global_list_total_price(item):
            # Suppression de l'élément dans global_list_commande
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
            if global_list_commande == [] : 
                label_nothing = Label(main_user_window, text="Votre panier est vide", font="Avenir")
                label_nothing.pack(pady=10)
                
            else : 
                main_commande_text = Label(main_user_window, text="Votre panier :" , font=("Avenir", 20))
                main_commande_text.pack()
                sous_label_text = Label(main_user_window, text="Appuiez pour supprimer", font=("Avenir", 10))
                sous_label_text.pack()

                for i, (choice, prix) in enumerate(global_list_commande):
                    print(f"Création du bouton pour l'élément {i}: {choice} au prix de {prix}")

                    # Création d'un bouton pour chaque élément de la liste
                    button_of_choice = Button(main_user_window, text=f"{choice}" + " " + f"{prix}  $", font="Avenir", 
                                                command=lambda item=(choice, prix): 
                                                [delete_in_global_list_total_price(item), refresh_price(), 
                                                display_commande(), update_total_price()])
                    button_of_choice.pack(pady=10)

            button_retour_comande = Button(main_user_window, text="Retour", font="Avenir", command=lambda : 
                                [refresh_price(), display_menu()])
            button_retour_comande.pack(side=BOTTOM, pady=10)


        def temps_attente ():
            global global_list_commande
            temps = 0 
            for key, _ in global_list_commande : 
                temps += data[index]["menus"][key]["temps"]
            return temps


        def valide_message ():
            destroy_widgets(main_user_window)

            valide_message_text = f"Votre commande a bien été validée \n pour un montant de {global_total_price} $"
            main_valide_text = Label(main_user_window, text=valide_message_text, font=("Avenir", 20))
            main_valide_text.pack(expand=True, anchor='center')

            temps_attente_text = f"Votre commande sera prête \n dans {temps_attente()} minutes"
            main_temps_attente_text = Label(main_user_window, text=temps_attente_text, font=("Avenir", 20))
            main_temps_attente_text.pack(expand=True, anchor='center')
            



        def check_commande () : 
            if global_list_commande == [] : 
                label_nothing = Label(main_user_window, text="Votre panier est vide", font=("Avenir", 20))
                label_nothing.pack(side=BOTTOM, pady=10)
                label_nothing.after(2000, lambda : label_nothing.destroy())
            else : 
                valide_message()

        display_menu()

    display_restaurant_name()
    main_user_window.mainloop()





global_list_commande = []
global_choice_price = []
global_total_price = 0

main_window()

