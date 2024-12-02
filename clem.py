from tkinter import* 
from data import*

def top_restaurant():
    main_user_window.destroy()
    
    restaurant_name  = data[0]["nom"]

    top_restaurant_window = Tk()
    top_restaurant_window.title(f"Bernard&co - {restaurant_name}" )
    top_restaurant_window.geometry("412x700")
    
    display_restaurant_name = Label(top_restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()

    top_restaurant_window.mainloop()


def mid_restaurant():
    main_user_window.destroy()

    restaurant_name  = data[1]["nom"]

    mid_restaurant_window = Tk()
    mid_restaurant_window.title(f"Bernard&co - {restaurant_name}" )
    mid_restaurant_window.geometry("412x700")
    
    display_restaurant_name = Label(mid_restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()

    mid_restaurant_window.mainloop()


def buttom_restaurant():
    main_user_window.destroy()

    restaurant_name  = data[2]["nom"]
 
    buttom_restaurant_window = Tk()
    buttom_restaurant_window.title(f"Bernard&co - {restaurant_name}" )
    buttom_restaurant_window.geometry("412x700")

    display_restaurant_name = Label(buttom_restaurant_window, text=restaurant_name, font=(20))
    display_restaurant_name.pack()



    buttom_restaurant_window.mainloop()

# Créer la fenêtre principale
main_user_window = Tk()
main_user_window.title("Bernard&co")
main_user_window.geometry("412x700")

main_text = Label(main_user_window, text="Choisissez votre restaurant", font="Calibri")
main_text.pack(expand=True)
# Créer un frame pour centrer les boutons
frame = Frame(main_user_window)
frame.pack(expand=True)

#ajouter une image dans les boutons 
# image_logo_patus = PhotoImage(main_user_window,  file="images/logo_patus.png")
# canvas_logo_patus = Canvas(main_user_window, width=50, height=50 ) #--> importation de la photo impossible 
# canvas_logo_patus.create_image(image=image_logo_patus)
# canvas_logo_patus.pack()



# Ajouter les boutons
bouton1 = Button(frame, text=data[0]["nom"], height=2, width=50, font="Calibri", command=top_restaurant)
bouton2 = Button(frame, text=data[1]["nom"], height=2, width=50, font="Calibri", command=mid_restaurant)
bouton3 = Button(frame, text=data[2]["nom"], height=2, width=50, font="Calibri", command=buttom_restaurant)




# Alignement vertical avec expansion
bouton1.pack(pady=5)
bouton2.pack(pady=5)
bouton3.pack(pady=5)


# Lancer la boucle principale
main_user_window.mainloop()
