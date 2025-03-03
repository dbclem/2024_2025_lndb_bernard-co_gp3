from data import*
from tkinter import*
from tools import destroy_all_widgets
from PIL import Image, ImageTk


global_liste_en_cours = []
global_list_commande_terminees = []

def refuser_commande(commande):
    global_liste_commande_operateur.remove(commande)
    print(global_liste_commande_operateur)

def accepter_commande(commande):
    if commande in global_liste_en_cours:
        global_list_commande_terminees.append(commande)
        global_liste_en_cours.remove(commande)
    else:
        global_liste_en_cours.append(commande)
        global_liste_commande_operateur.remove(commande)
    print(global_liste_en_cours)
    print(global_list_commande_terminees)

def add_commandes(demande_frame, process_frame, commande_terminees_frame):
    print(global_liste_commande_operateur)
    for commande in global_liste_commande_operateur:
        if "plat" not in commande:
            text_commande = f"{commande['name']} - {commande['price']} €"
        else:
            text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

        commande_frame = Frame(demande_frame, bg="#ffbf00", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        commande_frame.pack(pady=10)

        commande_label = Label(commande_frame, text=text_commande, font=("Helvetica", 12, "bold"), bg="#ffbf00", fg="#0f5741")
        commande_label.pack(pady=10)

        accepter_button = Button(commande_frame, text="Accepter", font=("Helvetica", 10, "bold"), bg="#0f5741", fg="white"
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=1
                                    ,activebackground = "#ffbf00", activeforeground = "#0f5741", 
                                 command=lambda commande=commande: [accepter_commande(commande), destroy_all_widgets(demande_frame),
                                                                    destroy_all_widgets(process_frame), add_commandes(demande_frame, process_frame, commande_terminees_frame), add_commandes_en_cours(process_frame, commande_terminees_frame)])
        accepter_button.pack(pady=10, side=RIGHT)

        refuser_button = Button(commande_frame, text="Refuser", font=("Helvetica", 10, "bold"), bg="#0f5741", fg="white"
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=1
                                    ,activebackground = "#ffbf00", activeforeground = "#0f5741",
                                command=lambda commande=commande: [refuser_commande(commande), destroy_all_widgets(demande_frame), add_commandes(demande_frame, process_frame, commande_terminees_frame)])
        refuser_button.pack(pady=10, side=LEFT)

def add_commandes_en_cours(process_frame, commande_terminees_frame):
    global global_liste_en_cours
    for commande in global_liste_en_cours:
        if "plat" not in commande:
            text_commande = f"{commande['name']} - {commande['price']} €"
        else:
            text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

        en_cours_frame = Frame(process_frame, bg="#ffbf00", width=200, height=200
                                   , highlightbackground="black", highlightcolor="black", highlightthickness=2)
        en_cours_frame.pack(pady=10)

        en_cours_label = Label(en_cours_frame, text=text_commande, font=("Helvetica", 12, "bold"), bg="#ffbf00", fg="#0f5741"
                                   , highlightbackground="black")
        en_cours_label.pack(pady=10, padx=20)

        terminer_button = Button(en_cours_frame, text="Terminer", font=("Helvetica", 10, "bold"), bg="#0f5741", fg="white"
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=1, activebackground = "#ffbf00"
                                    , activeforeground = "#0f5741",
                                 command=lambda commande=commande: [accepter_commande(commande), destroy_all_widgets(en_cours_frame),
                                                                    destroy_all_widgets(process_frame), add_commandes_en_cours(process_frame, commande_terminees_frame),
                                                                    destroy_all_widgets(commande_terminees_frame) ,add_commandes_terminees(commande_terminees_frame)])
        terminer_button.pack(pady=10)

def add_commandes_terminees(commande_terminees_frame):
    global global_list_commande_terminees
    for commande in global_list_commande_terminees:
        if "plat" not in commande:
            text_commande = f"{commande['name']} - {commande['price']} €"
        else:
            text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

        terminees_frame = Frame(commande_terminees_frame, bg="#ffbf00", width=200, height=200
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=2)
        terminees_frame.pack(pady=10)

        terminees_label = Label(terminees_frame, text=text_commande, font=("Helvetica", 12, "bold"), bg="#ffbf00", fg="#0f5741")
        terminees_label.pack(pady=30, padx=20)

def main_operateur_window():
    """
    Fonction qui affiche la fenêtre de l'opérateur
    """
    global operateur_window
    operateur_window = Tk()
    screen_width = operateur_window.winfo_screenwidth()
    screen_height = operateur_window.winfo_screenheight()
    operateur_window.title("Opérateur")
    operateur_window_width = screen_width // 2
    operateur_window_height = screen_height
    operateur_window.geometry(f"{operateur_window_width}x{operateur_window_height}+{screen_width // 2}+0")
    operateur_window.config(bg="#fff5f1")
    

    main_frame = Frame(operateur_window, bg="#fff5f1")
    main_frame.pack(fill=BOTH, expand=True)
    

    label = Label(main_frame, text="Interface Opérateur", font=("Helvetica", 20, "bold"), bg="#fff5f1", fg="#0f5741")
    label.pack(pady=20)

    demande_frame_intial = Frame(main_frame, bg="#fff5f1", width=200, height=200, highlightbackground="#0f5741", highlightcolor="#0f5741", highlightthickness=5)
    demande_frame_intial.pack(side=LEFT, expand=True)

    label_demande = Label(demande_frame_intial, text="Demandes", font=("Helvetica", 15, "bold"), bg="#fff5f1", fg="#0f5741")
    label_demande.pack(padx=100, pady=10)


    demande_frame = Frame(demande_frame_intial, bg="#fff5f1", width=200, height=200)
    demande_frame.pack(expand=True)


    process_frame_initial = Frame(main_frame, bg="#fff5f1", width=200, height=200, highlightbackground="#0f5741", highlightcolor="#0f5741", highlightthickness=5)
    process_frame_initial.pack(side=LEFT, expand=True)

    label_process = Label(process_frame_initial, text="En cours", font=("Helvetica", 15, "bold"), bg="#fff5f1", fg="#0f5741")
    label_process.pack(padx=100, pady=10)


    process_frame = Frame(process_frame_initial, bg="#fff5f1", width=200, height=200)
    process_frame.pack(side=LEFT, expand=True) 

    commande_terminees_frame_initial = Frame(main_frame, bg="#fff5f1", width=200, height=200, highlightbackground="#0f5741", highlightcolor="#0f5741", highlightthickness=5)
    commande_terminees_frame_initial.pack(side=LEFT, expand=True)


    label_commande_terminees = Label(commande_terminees_frame_initial, text="Commandes \n terminées", font=("Helvetica", 15, "bold"), bg="#fff5f1", fg="#0f5741")
    label_commande_terminees.pack(padx=85, pady=10)

    commande_terminees_frame = Frame(commande_terminees_frame_initial, bg="#fff5f1", width=177, height=177)
    commande_terminees_frame.pack(side=LEFT, expand=True)


    refresh_button = Button(main_frame, text="Refresh", font=("Helvetica", 15, "bold"), bg="#0f5741", fg="white"
                            , activebackground = "#ffbf00", activeforeground = "#0f5741"
                            , command=lambda: [destroy_all_widgets(demande_frame), add_commandes(demande_frame, process_frame, commande_terminees_frame)])
    refresh_button.place(relx=0.1, rely=0.1, anchor=CENTER)

    add_commandes(demande_frame, process_frame, commande_terminees_frame)
    operateur_window.mainloop()



"""
couleur :
        jaune pour les boutons--> #ffbf00   
        blanc cassé pour l'arriere plan -->#fff5f1
        vert pour les textes --> #0f5741
"""
"""
    changer les couleurs des boutons de la navitation en vert avec ecriutre blanche
    mettre toutes les ecritures en gras
    si possible changer les actives colors vert avce eriture blanche
"""

main_user_window = Tk()
screen_width = main_user_window.winfo_screenwidth()
screen_height = main_user_window.winfo_screenheight()
main_user_window.title("Bernard&co")
main_user_window.configure(bg = "#fff5f1")
main_user_window_width = screen_width // 2
main_user_window_height = screen_height
main_user_window.geometry(f"{main_user_window_width}x{main_user_window_height}+0+0")
main_user_window.iconbitmap("images\Be_-CO.ico")



def validate_admin(username, password) : 
    # any() retourne True si au moins un élément de l'itérable est vrai
    user_valid = any(user["username"] == username and user["password"] == password for user in liste_mdp)
    if user_valid:
        main_operateur_window()  
    else:
        error_label = Label(main_user_window, text="Nom d'utilisateur ou mot de passe incorrect", font=("Avenir", 12), fg="red", bg="#fff5f1")
        error_label.pack(pady=5)
        error_label.after(2000, error_label.destroy)


def display_admin_check(main_user_window) : 
    destroy_all_widgets(main_user_window)

    admin_frame = Frame(main_user_window, bg="#fff5f1")
    admin_frame.place(relx=0.5, rely=0.3, anchor=CENTER)
    username_label = Label(admin_frame, text="Nom d'utilisateur", font=("Avenir", 15, "bold"),fg = "#0f5741", bg="#fff5f1")
    username_label.pack(pady=5)
    username_entry = Entry(admin_frame, font=("Avenir", 15, "bold"), bg="#ffbf00", fg="#0f5741")
    username_entry.pack(pady=5)
    
    password_label = Label(admin_frame, text="Mot de passe", font=("Avenir", 15, "bold"), fg = "#0f5741", bg="#fff5f1")
    password_label.pack(pady=5)
    password_entry = Entry(admin_frame, show="*", font=("Avenir", 15, "bold"), bg="#ffbf00", fg="#0f5741")
    password_entry.pack(pady=5)


    nav_buttons_frame = Frame(admin_frame, bg="#fff5f1")
    nav_buttons_frame.pack(side=BOTTOM, pady=10)

    validate_button = Button(nav_buttons_frame, text="Valider", font=("Avenir", 12, "bold"), bg="#0f5741", fg="white", activebackground = "#ffbf00", activeforeground= "#0f5741",
                                command=lambda: validate_admin(username_entry.get(), password_entry.get()))
    validate_button.pack(side = RIGHT, padx = 10)
    nav_retour_button = Button(nav_buttons_frame, text="Retour ",  font=("Avenir", 12, "bold"), fg = "white", bg = "#0f5741",
                                activebackground = "#ffbf00", activeforeground = "#0f5741", command=lambda window=main_user_window: 
                                [destroy_all_widgets(window), reset_commandes(), display_restaurants_names()])
    nav_retour_button.pack(side=LEFT)

def display_restaurants_names () :  
    admin_button = Button(main_user_window, text="Admin", font=("Avenir", 15, "bold"),  fg = "white", bg="#0f5741", 
                            activebackground = "#ffbf00", activeforeground = "#0f5741", command=lambda : display_admin_check(main_user_window))
    admin_button.pack(side=TOP, pady=20, padx=20)
    main_text = Label(main_user_window, text="Choisissez votre restaurant", font=("Avenir", 25, "bold"), bg="#fff5f1", fg = "#0f5741", padx=20, pady=10)
    main_text.place(relx=0.5, rely=0.3, anchor=CENTER)


    for index, restaurant in enumerate(data):
        image = Image.open(restaurant["image_path"])
        image = image.resize((180, 100))  # Ajustez la taille de l'image
        photo = ImageTk.PhotoImage(image)  # Convertir pour Tkinter
        """ enumerate --> Parcourt data recupère la position index et la valeur restaurant 
                    index --> 0, 1, 2, ...
                    restaurant --> {nom : restaurant}

            open_restaurant_page prend i qui est index et qui se mais a jour a dynamiquement
        """
        Bouton_restaurant = Button(main_user_window, text=restaurant["nom"],
                                    image = photo, compound = "right", padx = 70, height=80, width=460, font=("Avenir", 20, "bold"), fg = "#0f5741", bg = "#ffbf00", 
                                    activebackground = "#0f5741", activeforeground = "white",
            command=lambda i=index: [destroy_all_widgets(main_user_window), restaurant_page(i)])
        Bouton_restaurant.image = photo
        Bouton_restaurant.place(relx=0.5, rely=0.5 + index * 0.1, anchor=CENTER)


def add_to_commande (formule, total_price_label) : 
    global global_list_commande
    global global_total_price
    global_list_commande.append(formule)
    global_total_price += formule["price"]
    print(f"La {formule['name']} a été ajoutée au panier au price de {formule['price']}.")
    update_total_price(total_price_label)

def check_if_the_menu_not_empty(dico_choices_in_the_menu, index, total_price_label) : 
    is_not_valid = False
    for value in dico_choices_in_the_menu.values() :
        if value == "" :
            is_not_valid = True
            break
        else : 
            is_not_valid = False

    if is_not_valid :
        choice_not_finished_text = Label(main_user_window, text="Vous n'avez pas fini votre commande !", font=("Avenir", 20), bg="#fff5f1", fg="#0f5741")
        choice_not_finished_text.pack(side=BOTTOM, pady=10)
        choice_not_finished_text.after(2000, lambda : choice_not_finished_text.destroy())
    else : 
        add_to_commande(dico_choices_in_the_menu, total_price_label)
        refresh_whitout_widjet(main_user_window, total_price_label)
        menus_page(index, total_price_label)
        print(global_list_commande)


def add_element_to_dico_final (element, key, dico_choices_in_the_menu) :
    dico_choices_in_the_menu[element] = key

def display_add_message(window, element) : 
    global  main_user_window_width
    add_message_frame = Frame(window, bg="#fff5f1", bd=2, relief="solid", highlightbackground="#0f5741", highlightthickness=2)
    add_message_frame.place(x=main_user_window_width - 10, y=20, anchor=NE)
    add_message = Label(add_message_frame, text=f"{element} a été sélectionné ! ", font=("Avenir", 15), bg="#fff5f1", fg="#0f5741")
    add_message.pack(side=TOP, pady=10)
    add_message_frame.after(5000, lambda : add_message_frame.destroy())


def display_elements_of_the_menu (index, name, element, dico_choices_in_the_menu, i) :
    main_element_in_commande_frame = Frame(main_user_window, bg="#fff5f1")
    main_element_in_commande_frame.pack(side=TOP, pady=10)

    main_element_text = Label(main_element_in_commande_frame, text=element, font=("Avenir", 15), fg = "#0f5741", bg="#fff5f1")
    main_element_text.grid(row=0, column=i, padx=5, pady=5)

    row_one_frame = Frame(main_element_in_commande_frame, bg = "#fff5f1")
    row_one_frame.grid(row=1, column=i, padx=5, pady=5)

    for key in list(data[index]["menus"][name][element].keys()) : 
        element_buttons = Button(row_one_frame, text=key, height=2, width=50, fg = "#0f5741", bg = "#ffbf00", 
                                    activebackground = "#0f5741", activeforeground = "white", font=("Avenir", 10, "bold"),
                    command=lambda key=key : 
                    [add_element_to_dico_final(element, key, dico_choices_in_the_menu), display_add_message(main_user_window, key)])
        element_buttons.pack(pady=5)


def in_menu_page (index, name, price, total_price_label):
    nav_in_the_menu_frame = Frame(main_user_window, bg="#fff5f1")
    nav_in_the_menu_frame.pack(side=TOP, pady=10)

    retour_menus_button = Button(nav_in_the_menu_frame, text="Retour", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741", 
                                activebackground = "#ffbf00", activeforeground = "#0f5741",  command=lambda : 
                                    [destroy_all_widgets(main_user_window), menus_page(index, total_price_label)])
    retour_menus_button.pack(side=LEFT, pady=10, padx=10)
    
    valide_the_menu_button = Button(nav_in_the_menu_frame, text="Valider", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                                    activebackground = "#ffbf00", activeforeground = "#0f5741",  command=lambda : 
                                    [check_if_the_menu_not_empty(dico_choices_in_the_menu, index, total_price_label)]) 
    valide_the_menu_button.pack(side=LEFT, pady=10, padx=10)
            
    dico_choices_in_the_menu = {
                                "name" : name,
                                "price" : 0,
                                "temps" : 0,
                            }
    i = 0
    for element in list (data[index]["menus"][name].keys()) : 
        if element == "price" or element == "temps" : 
            dico_choices_in_the_menu["price"] = price
            dico_choices_in_the_menu["temps"] = data[index]["menus"][name]["temps"]
        else :
            i += 1
            dico_choices_in_the_menu[element] = ""  
            display_elements_of_the_menu(index, name, element, dico_choices_in_the_menu, i)

def menus_page(index, total_price_label):
    menus_frame = Frame(main_user_window, bg="#fff5f1")
    menus_frame.place(relx=0.5, rely=0.2, anchor=CENTER)

    for name, price in global_tuple_menu_price:
        menus_buttons = Button(menus_frame, text=(f"{name} - {price} €" ), height=2, width=50, font=("Avenir", 11, "bold"), fg = "#0f5741", bg = "#ffbf00",
                            activebackground = "#0f5741", activeforeground = "white", 
                            command=lambda name=name, price=price: [refresh_whitout_widjet(main_user_window, total_price_label), in_menu_page(index, name, price, total_price_label)])
        menus_buttons.pack(pady=10)
    
    petite_faim_button = Button(menus_frame, text="Petite faim", height=2, width=50, fg = "#0f5741", bg = "#ffbf00", 
                            activebackground = "#0f5741", activeforeground = "white", font=("Avenir", 11, "bold"), 
                            command=lambda :[refresh_whitout_widjet(main_user_window, total_price_label), petite_faim_page(index, total_price_label)])
    petite_faim_button.pack(pady=10)
    navigation_in_menus_page(index, total_price_label)

def petite_faim_page (index, total_price_label) : 

    nav_petite_faim_frame = Frame(main_user_window, bg="#fff5f1")    
    nav_petite_faim_frame.pack(side=TOP, pady=10)
    retour_petite_faim_button = Button(nav_petite_faim_frame, text="Retour", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                                    activebackground = "#ffbf00", activeforeground = "#0f5741",  command=lambda :
                                    [refresh_whitout_widjet(main_user_window, total_price_label), menus_page(index, total_price_label)]) 
    retour_petite_faim_button.pack(side=LEFT, pady=10, padx=10)


    for element in global_dico_all_choices_price:
        petite_faim_buttons = Button(main_user_window, text=(f"{element['name']} - {element['price']} €" ), font=("Avenir", 10, "bold"), height=2, width=50, fg = "#0f5741", bg = "#ffbf00",
                            activebackground = "#0f5741", activeforeground = "white", 
                            command=lambda element=element:
                            [add_to_commande(element, total_price_label), refresh_whitout_widjet(main_user_window, total_price_label),
                                update_total_price(total_price_label), petite_faim_page(index, total_price_label), display_add_message(main_user_window, element["name"]),
                                print(global_list_commande)])
        petite_faim_buttons.pack(pady= 5)

def update_total_price(total_price_label):
    if total_price_label.winfo_exists():
        total_price_label.config(text=f"Prix total : {global_total_price} €")

def navigation_in_menus_page(index, total_price_label):    
    nav_buttons_frame = Frame(main_user_window, bg="#fff5f1")
    nav_buttons_frame.place(relx=0.5, rely=0.85, anchor=CENTER)

    nav_retour_button = Button(nav_buttons_frame, text="Retour",  font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                            activebackground = "#ffbf00", activeforeground = "#0f5741", command=lambda window=main_user_window: 
                            [destroy_all_widgets(window), reset_commandes(), display_restaurants_names()])
    nav_retour_button.pack(side=LEFT, padx=10)

    nav_voir_commande_button = Button(nav_buttons_frame, text="| Panier |", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                                    activebackground = "#ffbf00", activeforeground = "#0f5741", 
                                    command=lambda : [refresh_whitout_widjet(main_user_window, total_price_label), all_commande_page(index, total_price_label)])
    nav_voir_commande_button.pack(side=LEFT, padx=10)

    nav_valide_button = Button(nav_buttons_frame, text="Valider", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                                activebackground = "#ffbf00", activeforeground = "#0f5741", command=lambda : check_commande_not_empty(index))
    nav_valide_button.pack(side=LEFT, padx=10) 

def remove_in_global_list_command_total_price(element):
    global global_list_commande
    global_list_commande.remove(element)
    global global_total_price
    global_total_price -= element["price"]
    print(f"Item {element} supprimé")


def refresh_whitout_widjet(window, widjet):
    """Efface tous les widgets et réexécute le code pour recréer la page.
        et reafficher les elements du panier et la titre de la page 
    """
    for widget in window.winfo_children():
        if widget != widjet:
            widget.destroy()


def all_commande_page (index, total_price_label) :
    if global_list_commande == [] : 
        panier_vide_text = Label(main_user_window, text="Votre panier est vide", font=("Avenir", 23, "bold"), fg = "#0f5741", bg="#fff5f1")
        panier_vide_text.place(relx=0.5, rely=0.1, anchor=CENTER)
        
    else : 
        main_commande_text = Label(main_user_window, text="Votre panier :" , font=("Avenir", 20, "bold"), fg = "#0f5741", bg="#fff5f1")
        main_commande_text.place(relx=0.5, rely=0.1, anchor=CENTER)
        click_to_supp_text = Label(main_user_window, text="Appuyez pour supprimer", font=("Avenir", 12), fg = "#0f5741", bg="#fff5f1")
        click_to_supp_text.place(relx=0.5, rely=0.13, anchor=CENTER) 

        for index , element in enumerate(global_list_commande):
            if "plat" not in element : 
                text = f"{element['name']} - {element['price']} €"
            else :
                # commande faite a partir de chatgpt qui permet de modifier réactivement le texte
                text = " - ".join([f"{value} $" if key == "price" else f"{value}" for key, value in element.items() if key != "temps"])

            element_of_commande_button = Button(main_user_window, text=text, font=("Avenir", 12, "bold"), fg = "#0f5741", bg = "#ffbf00", 
                                                activebackground = "#0f5741", activeforeground = "white", command=lambda index=index, element=element: 
                                                [remove_in_global_list_command_total_price(element), refresh_whitout_widjet(main_user_window, total_price_label),
                                                all_commande_page(index, total_price_label), update_total_price(total_price_label)])
            element_of_commande_button.place(relx=0.5, rely=0.2 + index * 0.05, anchor=CENTER)

    retour_commande_button = Button(main_user_window, text="Retour", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741", 
                        activebackground = "#ffbf00", activeforeground = "#0f5741", command=lambda : 
                        [refresh_whitout_widjet(main_user_window, total_price_label), menus_page(index, total_price_label)])
    retour_commande_button.place(relx=0.5, rely=0.85, anchor=CENTER)



def valide_page (index):
    destroy_all_widgets(main_user_window)

    finish_frame = Frame(main_user_window, bg="#fff5f1")
    finish_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    valide_page_text = f"Votre commande s'élève à un montant de {global_total_price} €"
    main_valide_page_text = Label(finish_frame, text=valide_page_text, font=("Avenir", 20), bg="#fff5f1", fg = "#0f5741")
    main_valide_page_text.pack(side=TOP, pady=10)

    nav_finish_frame = Frame(finish_frame, bg="#fff5f1")
    nav_finish_frame.pack(side=BOTTOM, pady=10)
    retour_a_la_commande_button = Button(nav_finish_frame, text="revenir a la commande", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                                        activebackground = "#ffbf00", activeforeground = "#0f5741",
                                            command= lambda i=index : [destroy_all_widgets(main_user_window), restaurant_page(i)])
    retour_a_la_commande_button.pack(side=LEFT, padx=10)
    nouvelle_commande_button = Button(nav_finish_frame, text="Nouvelle commande", font=("Avenir", 15, "bold"), fg = "white", bg = "#0f5741",
                                    activebackground = "#ffbf00", activeforeground = "#0f5741",
                                            command= lambda : [destroy_all_widgets(main_user_window), reset_commandes(), main_window()])
    nouvelle_commande_button.pack(side=LEFT, padx=10)

def check_commande_not_empty (index) : 
    if global_list_commande == [] : 
        panier_vide_text = Label(main_user_window, text="Votre panier est vide", font=("Avenir", 20), bg="#fff5f1", fg="#0f5741")
        panier_vide_text.place(relx=0.5, rely=0.9, anchor=CENTER)
        panier_vide_text.after(2000, lambda : panier_vide_text.destroy())
    else : 
        valide_page(index)


def reset_commandes():
    global global_liste_commande_operateur
    global global_tuple_menu_price
    global global_list_commande
    global global_dico_all_choices_price
    global global_total_price
    global_liste_commande_operateur.extend(global_list_commande)
    global_tuple_menu_price = []
    global_list_commande = []
    global_dico_all_choices_price = []
    global_total_price = 0
    
    print("Panier vidé")

def restaurant_page(index):
        """
            s'active autant de fois que de nombre de restaurant 
            le nom du restaurant data[index]["nom"] --> on va cherher dans la liste data avec l'indice index 
                                                        puis on prend le "nom" 
                                                        restaurant_name eest donc facilement réutilisable 
        """
        i = index
        
        global global_tuple_menu_price
        global_tuple_menu_price = []

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

    
        total_price_label = Label(main_user_window, text="",  font=("Avenir", 13, "bold"), bg="#fff5f1", fg = "#0f5741")
        total_price_label.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        menus_page(i, total_price_label)


def main_window():
    """
    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    display_restaurants_names()
    main_user_window.mainloop()



global_list_commande = []
global_tuple_menu_price = []
global_dico_all_choices_price = []
global_total_price = 0
global_liste_commande_operateur = []
main_window()
