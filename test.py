# from tkinter import *
# from customtkinter import*
# # class RoundedFrame(Canvas):
# #     def __init__(self, parent, width, height, radius, **kwargs):
# #         Canvas.__init__(self, parent, width=width, height=height, **kwargs)
# #         self.radius = radius
# #         self.width = width
# #         self.height = height
# #         self.draw_rounded_frame()

# #     def draw_rounded_frame(self):
# #         points = [
# #             self.radius, 0,
# #             self.width - self.radius, 0,
# #             self.width, 0,
# #             self.width, self.radius,
# #             self.width, self.height - self.radius,
# #             self.width, self.height,
# #             self.width - self.radius, self.height,
# #             self.radius, self.height,
# #             0, self.height,
# #             0, self.height - self.radius,
# #             0, self.radius,
# #             0, 0
# #         ]
# #         self.create_polygon(points, smooth=True, fill="#3533cd", outline="#3533cd")

# # def create_rounded_button(canvas, x, y, width, height, radius, text, command):
# #     points = [
# #         x + radius, y,
# #         x + width - radius, y,
# #         x + width, y,
# #         x + width, y + radius,
# #         x + width, y + height - radius,
# #         x + width, y + height,
# #         x + width - radius, y + height,
# #         x + radius, y + height,
# #         x, y + height,
# #         x, y + height - radius,
# #         x, y + radius,
# #         x, y
# #     ]
# #     button = canvas.create_polygon(points, smooth=True, fill="#3533cd", outline="#3533cd")
# #     canvas.create_text(x + width / 2, y + height / 2, text=text, fill="white", font=("Helvetica", 12))
# #     canvas.tag_bind(button, "<Button-1>", lambda event: command())

# # def main_window():
# #     """
# #     la page affiche sous forme de liste tous les restaurants disponibles
# #     """
# #     global main_user_window
# #     main_user_window = Tk()
# #     screen_width = main_user_window.winfo_screenwidth()
# #     screen_height = main_user_window.winfo_screenheight()
# #     main_user_window.title("Bernard&co")
# #     main_user_window_width = screen_width // 2
# #     main_user_window_height = screen_height
# #     main_user_window.geometry(f"{main_user_window_width}x{main_user_window_height}")
# #     main_user_window.iconbitmap("images/logo_bernard&co.ico")
# #     # main_user_window.configure(bg="#3533cd")

# #     canvas = Canvas(main_user_window, width=main_user_window_width, height=main_user_window_height)
# #     canvas.pack()

# #     create_rounded_button(canvas, 50, 50, 200, 50, 20, "Bouton 1", lambda: print("Bouton 1 cliqué"))
# #     create_rounded_button(canvas, 50, 150, 200, 50, 20, "Bouton 2", lambda: print("Bouton 2 cliqué"))

# #     rounded_frame = RoundedFrame(canvas, 300, 200, 20)
# #     rounded_frame.place(x=300, y=50)

# #     main_user_window.mainloop()

# # main_window()

# class MyFrame(CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # add widgets onto the frame, for example:
#         self.label = CTkLabel(self)
#         self.label.grid(row=0, column=0, padx=20)


# class App(CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x200")
#         self.grid_rowconfigure(0, weight=1)  # configure grid system
#         self.grid_columnconfigure(0, weight=1)

#         self.my_frame = MyFrame(master=self)
#         self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


# app = App()
# app.mainloop()


from data import*
import customtkinter, tkinter

app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# create scrollable textbox
tk_textbox = tkinter.Text(app, highlightthickness=0)
tk_textbox.grid(row=0, column=0, sticky="nsew")

# create CTk scrollbar
ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

# connect textbox scroll event to CTk scrollbar
tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

app.mainloop()

import tkinter as tk
from tkinter import Frame, Label, Button

def add_element_to_dico_final (element, key, dico_choices_in_the_menu) :
            dico_choices_in_the_menu[element] = key
def display_elements_of_the_menu(name, element, dico_choices_in_the_menu, i, parent_frame, index):
    # Création du cadre principal
    main_element_in_commande_frame = Frame(parent_frame, bg="#1A355B", bd=2, relief="solid")
    main_element_in_commande_frame.pack(side=tk.TOP, pady=10, fill="x")

    main_element_text = Label(main_element_in_commande_frame, text=element, font=("Avenir", 15), fg="#FFFFFF", bg="#1A355B", bd=1, relief="solid")
    main_element_text.grid(row=0, column=0, padx=5, pady=5)

    # Création du Canvas et de la Scrollbar
    canvas = tk.Canvas(main_element_in_commande_frame, bg="#1A355B")
    scrollbar = tk.Scrollbar(main_element_in_commande_frame, orient="vertical", command=canvas.yview)
    
    scrollable_frame = Frame(canvas, bg="#1A355B")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Positionnement du Canvas et de la Scrollbar
    canvas.grid(row=1, column=0, sticky="nsew")
    scrollbar.grid(row=1, column=1, sticky="ns")

    # Ajout des boutons dans le scrollable_frame
    for key in list(data[index]["menus"][name][element].keys()):
        element_button = Button(scrollable_frame, text=key, height=2, width=50, fg="#FFFFFF", bg="#0d2c56",
                                activebackground="#1A355B", activeforeground="#FFFFFF",
                                command=lambda key=key: add_element_to_dico_final(element, key, dico_choices_in_the_menu))
        element_button.pack(pady=5, fill="x")

    return main_element_in_commande_frame  # Retourner le cadre si besoin