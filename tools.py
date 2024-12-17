from tkinter import*
from main import global_list_commande


def reset_commande():
    global global_list_commande
    global_list_commande = []



def refresh_page(window):
    """Rafraîchit la fenêtre Tkinter passée en paramètre."""
    window.update_idletasks()
    print("la page a été rafraichit")