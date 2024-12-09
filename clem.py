from data import*
from tkinter import*


def commande_window () : 
    voir_la_commande_window = Tk()
    voir_la_commande_window.title("Ma commande")
    voir_la_commande_window.geometry("412x700")

    list_commande = ["frites","pates", "pizza"]

    for value in list_commande :
        commande_label = Label (voir_la_commande_window, text = value)
        commande_label.pack (pady=10)
        





















    voir_la_commande_window.mainloop()




commande_window()