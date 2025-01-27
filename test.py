import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Créez une fenêtre principale
main_user_window = ttk.Window(themename="cosmo")

# Créez un style personnalisé pour le bouton avec un dégradé horizontal
style = ttk.Style()
style.configure("Gradient.TButton", font=("Avenir", 12), padding=10)
style.map("Gradient.TButton",
          background=[("active", "#FFFFFF"), ("!active", "#0066FF")],
          relief=[("pressed", "sunken"), ("!pressed", "raised")])

# Créez un bouton avec le style personnalisé
button = ttk.Button(main_user_window, text="Bouton Restaurant", style="Gradient.TButton")
button.pack(pady=10)

main_user_window.mainloop()