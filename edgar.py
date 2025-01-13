from tkinter import *
from main import global_list_commande


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
    operateur_window.geometry(f"{operateur_window_width}x{operateur_window_height}")
    operateur_window.config(bg="white")
    
    # creation de la frame principale
    main_frame = Frame(operateur_window, bg="white")
    main_frame.pack(fill=BOTH, expand=True)
    
    # Label de la page
    label = Label(main_frame, text="Interface Opérateur", font=("Helvetica", 20), bg="white")
    label.pack(pady=20)

    # creation de la frame des demandes
    demande_frame = Frame(main_frame, bg="white", width=500, height=500, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    demande_frame.pack(side=LEFT, expand=True)

    # Label des demandes
    label_demande = Label(demande_frame, text="Demandes", font=("Helvetica", 15), bg="white")
    label_demande.pack(padx=100, pady=10)
    
    # creation de la frame des process
    process_frame = Frame(main_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    process_frame.pack(side=LEFT, expand=True)

    # Label des process
    label_process = Label(process_frame, text="en cours", font=("Helvetica", 15), bg="white")
    label_process.pack(padx=100, pady=10)

    # creation de la frame des commandes terminées
    commande_frame = Frame(main_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    commande_frame.pack(side=LEFT, expand=True)

    # Label des commandes terminées
    label_commande = Label(commande_frame, text="Commandes terminées", font=("Helvetica", 15), bg="white")
    label_commande.pack(padx=85, pady=10)


    def add_command_from_user_window ():
        """
        Fonction qui affiche la fenêtre pour ajouter une commande
        """
        global add_command_window
        add_command_window = Toplevel(operateur_window)
        add_command_window.title("Ajouter une commande")
        add_command_window.geometry("500x500")
        add_command_window.config(bg="white")
        add_command_window.resizable(False, False)

        # creation de la frame principale
        add_command_frame = Frame(add_command_window, bg="white")
        add_command_frame.pack(fill=BOTH, expand=True)

        # Label de la page
        label = Label(add_command_frame, text="Ajouter une commande", font=("Helvetica", 20), bg="white")
        label.pack(pady=20)

        # creation de la frame des plats
        plat_frame = Frame(add_command_frame, bg="white", width=500, height=500, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        plat_frame.pack(side=LEFT, expand=True)

        # Label des plats
        label_plat = Label(plat_frame, text="Plats", font=("Helvetica", 15), bg="white")
        label_plat.pack(padx=100, pady=10)

        # creation de la frame des desserts
        dessert_frame = Frame(add_command_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        dessert_frame.pack(side=LEFT, expand=True)

        # Label des desserts
        label_dessert = Label(dessert_frame, text="Desserts", font=("Helvetica", 15), bg="white")
        label_dessert.pack(padx=100, pady=10)

        # creation de la frame des boissons
        boisson_frame = Frame(add_command_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        boisson_frame.pack(side=LEFT, expand=True)

        # Label des boissons
        label_boisson = Label(boisson_frame, text="Boissons", font=("Helvetica", 15), bg="white")
        label_boisson.pack(padx=85, pady=10)

        # creation de la frame des boutons
        button_frame = Frame(add_command_frame, bg="white", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)        

    operateur_window.mainloop()

main_operateur_window()