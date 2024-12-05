from tkinter import* 
from data import*
from tools import*

def show_main_window():
    """
        creation de la fenetre principale 
        nommer --> Bernard&co
        taille par défaut --> 412x700
        fenetre d'accueil 
        bouton 1 / 2 / 3 --> representation à la suite des différents réstaurants a la suite 
    """
    global main_user_window
    main_user_window = Tk()
    main_user_window.title("Bernard&co")
    main_user_window.geometry("412x700")

    main_text = Label(main_user_window, text="Choisissez votre restaurant", font="Calibri")
    main_text.pack(expand=True)
    
    frame = Frame(main_user_window)
    frame.pack(expand=True)

    bouton1 = Button(frame, text=data[0]["nom"], height=2, width=50, font="Calibri", command=top_restaurant)
    bouton2 = Button(frame, text=data[1]["nom"], height=2, width=50, font="Calibri", command=mid_restaurant)
    bouton3 = Button(frame, text=data[2]["nom"], height=2, width=50, font="Calibri", command=buttom_restaurant)

    bouton1.pack(pady=5)
    bouton2.pack(pady=5)
    bouton3.pack(pady=5)

    main_user_window.mainloop()



def top_restaurant():
    main_user_window.destroy()
    
    restaurant_name = data[0]["nom"]
    top_restaurant_window = Tk()
    top_restaurant_window.title(f"Bernard&co - {restaurant_name}")
    top_restaurant_window.geometry("412x700")
    
    display_restaurant_name = Label(top_restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()

    # Frame pour les boutons en bas
    button_frame = Frame(top_restaurant_window)
    button_frame.pack(side=BOTTOM, pady=20)

    bouton_retour = Button(button_frame, text="Retour", font="Calibri", command=lambda: [top_restaurant_window.destroy(), show_main_window()])
    bouton_retour.pack(side=LEFT, padx=10)

    bouton_validee = Button(button_frame, text="Validée", font="Calibri", command=lambda: print(f"Réservation validée pour {restaurant_name}"))
    bouton_validee.pack(side=LEFT, padx=10)

    top_restaurant_window.mainloop()

def mid_restaurant():
    main_user_window.destroy()

    restaurant_name = data[1]["nom"]
    mid_restaurant_window = Tk()
    mid_restaurant_window.title(f"Bernard&co - {restaurant_name}")
    mid_restaurant_window.geometry("412x700")
    
    display_restaurant_name = Label(mid_restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()

    # Frame pour les boutons en bas
    button_frame = Frame(mid_restaurant_window)
    button_frame.pack(side=BOTTOM, pady=20)

    bouton_retour = Button(button_frame, text="Retour", font="Calibri", command=lambda: [mid_restaurant_window.destroy(), show_main_window()])
    bouton_retour.pack(side=LEFT, padx=10)

    bouton_validee = Button(button_frame, text="Validée", font="Calibri", command=lambda: print(f"Réservation validée pour {restaurant_name}"))
    bouton_validee.pack(side=LEFT, padx=10)

    mid_restaurant_window.mainloop()

def buttom_restaurant():
    main_user_window.destroy()

    restaurant_name = data[2]["nom"]
    buttom_restaurant_window = Tk()
    buttom_restaurant_window.title(f"Bernard&co - {restaurant_name}")
    buttom_restaurant_window.geometry("412x700")
    
    display_restaurant_name = Label(buttom_restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()

    # Frame pour les boutons en bas
    button_frame = Frame(buttom_restaurant_window)
    button_frame.pack(side=BOTTOM, pady=20)

    bouton_retour = Button(button_frame, text="Retour", font="Calibri", command=lambda: [buttom_restaurant_window.destroy(), show_main_window()])
    bouton_retour.pack(side=LEFT, padx=10)

    bouton_validee = Button(button_frame, text="Validée", font="Calibri", command=lambda: print(f"Réservation validée pour {restaurant_name}"))
    bouton_validee.pack(side=LEFT, padx=10)

    buttom_restaurant_window.mainloop()

# Lancer la fenêtre principale au démarrage
show_main_window()
