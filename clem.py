from tkinter import* 
from data import*

def bouton1_action():
    print("Bouton 1 cliqué !")

def bouton2_action():
    print("Bouton 2 cliqué !")

def bouton3_action():
    print("Bouton 3 cliqué !")

# Créer la fenêtre principale
fenetre = Tk()
fenetre.title("Page d'accueil")
fenetre.geometry("840x480")


# Créer un frame pour centrer les boutons
frame = Frame(fenetre)
max_width = 840
frame.pack(expand=True)

# Ajouter les boutons

bouton1 = Button(frame, text=data[0]{"nom"}, height=2, width=50)
bouton2 = Button(frame, text=data[1]{"nom"}, height=2, width=50)
bouton3 = Button(frame, text=data[2]{"nom"}, height=2, width=50)

# Alignement vertical avec expansion
bouton1.pack(pady=10)
bouton2.pack(pady=10)
bouton3.pack(pady=10)


# Lancer la boucle principale
fenetre.mainloop()
