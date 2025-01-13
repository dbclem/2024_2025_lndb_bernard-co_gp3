import tkinter as tk
from main import*

# programming = ['Java', 'Python', 'C++', 
            #    'C#', 'JavaScript', 'NodeJS', 
            #    'Kotlin', 'VB.Net', 'MySql', 'SQLite']
programming = []

for element in global_dico_all_choices_price:
    petite_faim_buttons = Button(main_user_window, text=(f"{element['name']} - {element['price']} $" ), height=2, width=50, 
                        command=lambda element=element:
                        [add_to_commande(element), refresh_price(main_user_window),
                            update_total_price(), display_petite_faim(),
                            print(global_list_commande)])
    petite_faim_buttons.pack(pady=10)

# Création de la fenêtre principale
window = tk.Tk()
window.title("Exemple de Scrollbar")
window.geometry("275x100")

# Création du widget Listbox
listbox = tk.Listbox(window)

# Création du widget Scrollbar
scrollbar = tk.Scrollbar(window)


# Configuration de la relation entre le Listbox et le Scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Ajout des éléments à la liste
for item in programming:
    listbox.insert(tk.END, item)

# Placement des widgets dans la fenêtre
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lancement de la boucle principale
window.mainloop()