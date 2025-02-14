from tkinter import *
from customtkinter import*
from tkinter import ttk

# class RoundedFrame(Canvas):
#     def __init__(self, parent, width, height, radius, **kwargs):
#         Canvas.__init__(self, parent, width=width, height=height, **kwargs)
#         self.radius = radius
#         self.width = width
#         self.height = height
#         self.draw_rounded_frame()

#     def draw_rounded_frame(self):
#         points = [
#             self.radius, 0,
#             self.width - self.radius, 0,
#             self.width, 0,
#             self.width, self.radius,
#             self.width, self.height - self.radius,
#             self.width, self.height,
#             self.width - self.radius, self.height,
#             self.radius, self.height,
#             0, self.height,
#             0, self.height - self.radius,
#             0, self.radius,
#             0, 0
#         ]
#         self.create_polygon(points, smooth=True, fill="#3533cd", outline="#3533cd")

# def create_rounded_button(canvas, x, y, width, height, radius, text, command):
#     points = [
#         x + radius, y,
#         x + width - radius, y,
#         x + width, y,
#         x + width, y + radius,
#         x + width, y + height - radius,
#         x + width, y + height,
#         x + width - radius, y + height,
#         x + radius, y + height,
#         x, y + height,
#         x, y + height - radius,
#         x, y + radius,
#         x, y
#     ]
#     button = canvas.create_polygon(points, smooth=True, fill="#3533cd", outline="#3533cd")
#     canvas.create_text(x + width / 2, y + height / 2, text=text, fill="white", font=("Helvetica", 12))
#     canvas.tag_bind(button, "<Button-1>", lambda event: command())

# def main_window():
#     """
#     la page affiche sous forme de liste tous les restaurants disponibles
#     """
#     global main_user_window
#     main_user_window = Tk()
#     screen_width = main_user_window.winfo_screenwidth()
#     screen_height = main_user_window.winfo_screenheight()
#     main_user_window.title("Bernard&co")
#     main_user_window_width = screen_width // 2
#     main_user_window_height = screen_height
#     main_user_window.geometry(f"{main_user_window_width}x{main_user_window_height}")
#     main_user_window.iconbitmap("images/logo_bernard&co.ico")
#     # main_user_window.configure(bg="#3533cd")

#     canvas = Canvas(main_user_window, width=main_user_window_width, height=main_user_window_height)
#     canvas.pack()

#     create_rounded_button(canvas, 50, 50, 200, 50, 20, "Bouton 1", lambda: print("Bouton 1 cliqué"))
#     create_rounded_button(canvas, 50, 150, 200, 50, 20, "Bouton 2", lambda: print("Bouton 2 cliqué"))

#     rounded_frame = RoundedFrame(canvas, 300, 200, 20)
#     rounded_frame.place(x=300, y=50)

#     main_user_window.mainloop()

# main_window()

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



# root = Tk()
# root.title ('canva test scroll')
# root.iconbitmap ('images/logo_bernard&co.ico')
# root.geometry ('500x500')

# main_frame = Frame (root)
# main_frame.pack (fill = BOTH, expand = 1)   

# canva_scroll_menu = Canvas(main_frame) 
# canva_scroll_menu.pack (side = LEFT, fill = BOTH, expand = 1)

# scrollbar_menu = ttk.Scrollbar(main_frame, orient = VERTICAL, command = canva_scroll_menu.yview)
# scrollbar_menu.pack (side = RIGHT, fill= Y)

# canva_scroll_menu.configure(yscrollcommand = canva_scroll_menu.set)
# canva_scroll_menu.bind ('<Configure>', lambda e : canva_scroll_menu.configure(scrollregion = canva_scroll_menu.bbox("all")))
            
# second_frame = Frame(canva_scroll_menu)
# canva_scroll_menu.create_window ((0,0), window = second_frame, anchor = "nw")
# for display_elements_of_the_menu in range (50):
#                 Button (second_frame, text = f'Button {display_elements_of_the_menu}').grid(row = display_elements_of_the_menu, column = 0)

# my_label = Label(second_frame, text = f"Element {display_elements_of_the_menu}").grid(row = 3, column = 2)
# for element_buttons in range (50):
#     Button (root, text = f'Button {element_buttons}').grid(row = element_buttons, column = 0, pady = 10, padx = 10)


# my_canvas = Canvas (main_frame)


root = Tk()
root.title ('test custom tkinter')
root.iconbitmap ('images/logo_bernard&co.ico')
root.geometry ('500x500')

main_frame = CTkFrame (master=root, bg_color= 'red', width = 500, height = 500)

root.mainloop()