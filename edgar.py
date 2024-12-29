from tkinter import *


def main_operateur_window():
    """
    Fonction qui affiche la fenêtre de l'opérateur
    """
    global operateur_window
    operateur_window = Tk()
    operateur_window.title("Opérateur")
    operateur_window.geometry("800x800")
    operateur_window.config(bg="white")
    
    # creation de la frame principale
    main_frame = Frame(operateur_window, bg="white", width=700, height=700)
    main_frame.pack(fill=BOTH, expand=True)
    
    # Label de la page
    label = Label(main_frame, text="Interface Opérateur", font=("Helvetica", 20), bg="white")
    label.pack(pady=20)

    # creation de la frame des demandes
    demande_frame = Frame(main_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    demande_frame.pack(side=LEFT, padx=10, pady=20)

    # Label des demandes
    label_demande = Label(demande_frame, text="Demandes", font=("Helvetica", 15), bg="white")
    label_demande.pack(pady=20)
    
    # creation de la frame des process
    process_frame = Frame(main_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    process_frame.pack(side=LEFT, padx=10, pady=200)

    # Label des process
    label_process = Label(process_frame, text="en cours", font=("Helvetica", 15), bg="white")
    label_process.pack(pady=20)

    # creation de la frame des commandes terminées
    commande_frame = Frame(main_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    commande_frame.pack(side=LEFT, padx=10, pady=20)

    # Label des commandes terminées
    label_commande = Label(commande_frame, text="Commandes terminées", font=("Helvetica", 15), bg="white")
    label_commande.pack(pady=20)

    operateur_window.mainloop()

main_operateur_window()