from tkinter import* 
from data import*

def bouton1_action():
    print("Bouton 1 cliqué !")

def bouton2_action():
    print("Bouton 2 cliqué !")

def bouton3_action():
    print("Bouton 3 cliqué !")

# Créer la fenêtre principale
main_user_window = Tk()
main_user_window.title("Bernard&co")
main_user_window.geometry("412x700")


# Créer un frame pour centrer les boutons
frame = Frame(main_user_window)
frame.pack(expand=True)

#ajouter une image dans les boutons 
image_logo_patus = PhotoImage(file="images/logo_patus.png")
canvas_logo_patus = Canvas(frame, width=50, height=2 ) #--> importation de la photo impossible 
canvas_logo_patus.create_image(image=image_logo_patus)
canvas_logo_patus.pack()
# Ajouter les boutons
bouton1 = Button(frame, text=data[0]["nom"], height=2, width=50)
bouton2 = Button(frame, text=data[1]["nom"], height=2, width=50)
bouton3 = Button(frame, text=data[2]["nom"], height=2, width=50)




# Alignement vertical avec expansion
bouton1.pack(pady=5)
bouton2.pack(pady=5)
bouton3.pack(pady=5)


# Lancer la boucle principale
main_user_window.mainloop()
