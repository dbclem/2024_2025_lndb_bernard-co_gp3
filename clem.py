from tkinter import *
#from main import global_liste_commande_operateur

def destroy_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
global_liste_commande_operateur = [
    {"name": "Plat 1", "price": 10},
    {"name": "Plat 2", "price": 15},
    {"name": "Plat 3", "price": 20},
    {"name": "Plat 4", "price": 25},
    {"name": "Plat 5", "price": 30}
]
global_liste_en_cours = []
global_list_commande_terminees = []


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
    main_frame = Frame(operateur_window, bg="#fff5f1")
    main_frame.pack(fill=BOTH, expand=True)
    
    # Label de la page
    label = Label(main_frame, text="Interface Opérateur", font=("Helvetica", 20, "bold"), bg="#fff5f1", fg="#0f5741")
    label.pack(pady=20)


    # creation de la frame des demandes initial
    demande_frame_intial = Frame(main_frame, bg="#fff5f1", width=200, height=200, highlightbackground="#0f5741", highlightcolor="#0f5741", highlightthickness=5)
    demande_frame_intial.pack(side=LEFT, expand=True)

    # Label des demandes
    label_demande = Label(demande_frame_intial, text="Demandes", font=("Helvetica", 15, "bold"), bg="#fff5f1", fg="#0f5741")
    label_demande.pack(padx=100, pady=10)

    # creation de la frame des demandes
    demande_frame = Frame(demande_frame_intial, bg="#fff5f1", width=200, height=200)
    demande_frame.pack(expand=True)

    
    # creation de la frame des process initial
    process_frame_initial = Frame(main_frame, bg="#fff5f1", width=200, height=200, highlightbackground="#0f5741", highlightcolor="#0f5741", highlightthickness=5)
    process_frame_initial.pack(side=LEFT, expand=True)

    # Label des process
    label_process = Label(process_frame_initial, text="en cours", font=("Helvetica", 15, "bold"), bg="#fff5f1", fg="#0f5741")
    label_process.pack(padx=100, pady=10)

    # creation de la frame des process
    process_frame = Frame(process_frame_initial, bg="#fff5f1", width=200, height=200)
    process_frame.pack(side=LEFT, expand=True) 


    # creation de la frame des commandes initial
    commande_frame_initial = Frame(main_frame, bg="#fff5f1", width=200, height=200, highlightbackground="#0f5741", highlightcolor="#0f5741", highlightthickness=5)
    commande_frame_initial.pack(side=LEFT, expand=True)

    # Label des commandes terminées
    label_commande = Label(commande_frame_initial, text="Commandes \n terminées", font=("Helvetica", 15, "bold"), bg="#fff5f1", fg="#0f5741")
    label_commande.pack(padx=85, pady=10)

    # creation de la frame des commandes terminées
    commande_frame = Frame(commande_frame_initial, bg="#fff5f1", width=200, height=200)
    commande_frame.pack(side=LEFT, expand=True)

    # creation d'un bouton refresh
    refresh_button = Button(main_frame, text="Refresh", font=("Helvetica", 15, "bold"), bg="#0f5741", fg="white", command=lambda: [destroy_all_widgets(demande_frame), add_commandes()])
    refresh_button.place(relx=0.1, rely=0.1, anchor=CENTER)


    # creation de la fonction qui ajoute les commandes demandées
    def add_commandes ():
        print(global_liste_commande_operateur)
        global_liste_commande_operateur
        for commande in global_liste_commande_operateur :
            
            if "plat" not in commande : 
                text_commande = f"{commande['name']} - {commande['price']} €"
            else :
                # commande faite a partir de chatgpt qui permet de modifier réactivement le texte
                text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

            
            commande_frame = Frame(demande_frame, bg="#ffbf00", width=200, height=200, highlightbackground="black", highlightcolor="black", highlightthickness=2)
            commande_frame.pack(pady=10)

            commande_label = Label(commande_frame, text=text_commande, font=("Helvetica", 12, "bold"), bg="#ffbf00", fg="#0f5741")
            commande_label.pack(pady=5)

            accepter_button = Button(commande_frame, text="Accepter", font=("Helvetica", 10, "bold"), bg="#0f5741", fg="white"
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=1
                                    ,activebackground = "#ffbf00", activeforeground = "#0f5741"
                                    , command=lambda commande=commande: [accepter_commande(commande), destroy_all_widgets(demande_frame)
                                    , destroy_all_widgets(process_frame), add_commandes(), add_commandes_en_cours()])
            accepter_button.pack(pady=10,side=RIGHT)

            refuser_button = Button(commande_frame, text="Refuser", font=("Helvetica", 10, "bold"), bg="#0f5741", fg="white"
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=1
                                    ,activebackground = "#ffbf00", activeforeground = "#0f5741"
                                    , command=lambda commande=commande: [refuser_commande(commande), destroy_all_widgets(demande_frame), add_commandes()])
            refuser_button.pack(pady=10,side=LEFT)

    add_commandes()

    def refuser_commande(commande):
        global_liste_commande_operateur.remove(commande)
        print(global_liste_commande_operateur)

    def accepter_commande(commande):
        if commande in global_liste_en_cours :
            global_list_commande_terminees.append(commande)
            global_liste_en_cours.remove(commande)
        else :
            global_liste_en_cours.append(commande)
            global_liste_commande_operateur.remove(commande)
        print(global_liste_en_cours)
        print(global_list_commande_terminees)

    # creation de la fonction qui ajoute les commandes en cours
    def add_commandes_en_cours ():
        global global_liste_en_cours
        for commande in global_liste_en_cours :
            if "plat" not in commande : 
                text_commande = f"{commande['name']} - {commande['price']} €"
            else :
                # commande faite a partir de chatgpt qui permet de modifier réactivement le texte
                text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

            en_cours_frame = Frame(process_frame, bg="#ffbf00", width=200, height=200
                                   , highlightbackground="black", highlightcolor="black", highlightthickness=2)
            en_cours_frame.pack(pady=10)

            en_cours_label = Label(en_cours_frame, text=text_commande, font=("Helvetica", 12, "bold"), bg="#ffbf00", fg="#0f5741"
                                   , highlightbackground="black")
            en_cours_label.pack(pady=5, padx=10)

            terminer_button = Button(en_cours_frame, text="Terminer", font=("Helvetica", 10, "bold"), bg="#0f5741", fg="white"
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=1, activebackground = "#ffbf00"
                                    , activeforeground = "#0f5741"
                                    , command=lambda commande=commande: [accepter_commande(commande), destroy_all_widgets(process_frame)
                                    ,destroy_all_widgets(commande_frame), add_commandes_en_cours(), add_commandes_terminees()])
            terminer_button.pack(pady=10)
    
    def add_commandes_terminees ():
        global global_list_commande_terminees
        for commande in global_list_commande_terminees :
            if "plat" not in commande : 
                text_commande = f"{commande['name']} - {commande['price']} €"
            else :
                # commande faite a partir de chatgpt qui permet de modifier réactivement le texte
                text_commande = " \n ".join([f"{value} $" if key == "price" else f"{value}" for key, value in commande.items() if key != "temps"])

            terminees_frame = Frame(commande_frame, bg="#ffbf00", width=200, height=200
                                    , highlightbackground="black", highlightcolor="black", highlightthickness=2)
            terminees_frame.pack(pady=10)

            terminees_label = Label(terminees_frame, text=text_commande, font=("Helvetica", 12, "bold"), bg="#ffbf00", fg="#0f5741")
            terminees_label.pack(pady=30, padx=20)
    




    operateur_window.mainloop()

    

main_operateur_window()
