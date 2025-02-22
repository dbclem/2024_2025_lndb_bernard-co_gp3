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



root = Tk()
root.title ('canva test scroll')
root.iconbitmap ('images/logo_bernard&co.ico')
root.geometry ('500x500')

bouton = Button(root, text='test')
bouton.pack(pady=20)

label = Label(bouton, text='label')
label.pack()
root.mainloop()