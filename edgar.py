from tkinter import *
from main import global_liste_commande_operateur

def destroy_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

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

        commande_frame = Frame(demande_frame, bg="#1A355B", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        commande_frame.pack(pady=10)

        commande_label = Label(commande_frame, text=text_commande, font=("Helvetica", 10), bg="#1A355B", fg="white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
        commande_label.pack(pady=10)

        accepter_button = Button(commande_frame, text="Accepter", font=("Helvetica", 10), bg="#1A355B", fg="white",
                                 highlightbackground="black", highlightcolor="black", highlightthickness=1,
                                 command=lambda commande=commande: [accepter_commande(commande), destroy_all_widgets(demande_frame),
                                                                    destroy_all_widgets(process_frame), add_commandes(demande_frame, process_frame, commande_terminees_frame), add_commandes_en_cours(process_frame, commande_terminees_frame)])
        accepter_button.pack(pady=10, side=RIGHT)

        refuser_button = Button(commande_frame, text="Refuser", font=("Helvetica", 10), bg="#1A355B", fg="white",
                                highlightbackground="black", highlightcolor="black", highlightthickness=1,
                                command=lambda commande=commande: [refuser_commande(commande), destroy_all_widgets(demande_frame), add_commandes(demande_frame, process_frame, commande_terminees_frame)])
        refuser_button.pack(pady=10, side=LEFT)

def add_commandes_en_cours(process_frame, commande_terminees_frame):
    global global_liste_en_cours
    for commande in global_liste_en_cours:
        if "plat" not in commande:
            text_commande = f"{commande['name']} - {commande['price']} €"
        else:
            text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

        en_cours_frame = Frame(process_frame, bg="#1A355B", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        en_cours_frame.pack(pady=10)

        en_cours_label = Label(en_cours_frame, text=text_commande, font=("Helvetica", 10), bg="#1A355B", fg="white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
        en_cours_label.pack(pady=10, padx=20)

        terminer_button = Button(en_cours_frame, text="Terminer", font=("Helvetica", 10), bg="#1A355B", fg="white",
                                 highlightbackground="black", highlightcolor="black", highlightthickness=1,
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

        terminees_frame = Frame(commande_terminees_frame, bg="#1A355B", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        terminees_frame.pack(pady=10)

        terminees_label = Label(terminees_frame, text=text_commande, font=("Helvetica", 10), bg="#1A355B", fg="white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
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
    
    # creation de la frame principale
    main_frame = Frame(operateur_window, bg="#0d2c56")
    main_frame.pack(fill=BOTH, expand=True)
    
    # Label de la page
    label = Label(main_frame, text="Interface Opérateur", font=("Helvetica", 20), bg="#0d2c56", fg="white")
    label.pack(pady=20)

    # creation de la frame des demandes initial
    demande_frame_intial = Frame(main_frame, bg="#0d2c56", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    demande_frame_intial.pack(side=LEFT, expand=True)

    # Label des demandes
    label_demande = Label(demande_frame_intial, text="Demandes", font=("Helvetica", 15), bg="#0d2c56", fg="white")
    label_demande.pack(padx=100, pady=10)

    # creation de la frame des demandes
    demande_frame = Frame(demande_frame_intial, bg="#0d2c56", width=200, height=200)
    demande_frame.pack(expand=True)

    # creation de la frame des process initial
    process_frame_initial = Frame(main_frame, bg="#0d2c56", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    process_frame_initial.pack(side=LEFT, expand=True)

    # Label des process
    label_process = Label(process_frame_initial, text="en cours", font=("Helvetica", 15), bg="#0d2c56", fg="white")
    label_process.pack(padx=100, pady=10)

    # creation de la frame des process
    process_frame = Frame(process_frame_initial, bg="#0d2c56", width=200, height=200)
    process_frame.pack(side=LEFT, expand=True) 

    # creation de la frame des commandes initial
    commande_terminees_frame_initial = Frame(main_frame, bg="#0d2c56", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    commande_terminees_frame_initial.pack(side=LEFT, expand=True)

    # Label des commandes terminées
    label_commande_terminees = Label(commande_terminees_frame_initial, text="Commandes terminées", font=("Helvetica", 15), bg="#0d2c56", fg="white")
    label_commande_terminees.pack(padx=85, pady=10)

    # creation de la frame des commandes terminées
    commande_terminees_frame = Frame(commande_terminees_frame_initial, bg="#0d2c56", width=200, height=200)
    commande_terminees_frame.pack(side=LEFT, expand=True)

    # creation d'un bouton refresh
    refresh_button = Button(main_frame, text="Refresh", font=("Helvetica", 10), bg="#1A355B", fg="white", command=lambda: [destroy_all_widgets(demande_frame), add_commandes(demande_frame, process_frame)])
    refresh_button.place(relx=0.1, rely=0.1, anchor=CENTER)

    add_commandes(demande_frame, process_frame, commande_terminees_frame)
    operateur_window.mainloop()

main_operateur_window()