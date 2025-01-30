from tkinter import *

def create_rounded_button(canvas, x, y, width, height, radius, text, command):
    points = [
        x + radius, y,
        x + width - radius, y,
        x + width, y,
        x + width, y + radius,
        x + width, y + height - radius,
        x + width, y + height,
        x + width - radius, y + height,
        x + radius, y + height,
        x, y + height,
        x, y + height - radius,
        x, y + radius,
        x, y
    ]
    button = canvas.create_polygon(points, smooth=True, fill="#3533cd", outline="#3533cd")
    canvas.create_text(x + width / 2, y + height / 2, text=text, fill="white", font=("Helvetica", 12))
    canvas.tag_bind(button, "<Button-1>", lambda event: command())

def main_window():
    """
    la page affiche sous forme de liste tous les restaurants disponibles
    """
    global main_user_window
    main_user_window = Tk()
    screen_width = main_user_window.winfo_screenwidth()
    screen_height = main_user_window.winfo_screenheight()
    main_user_window.title("Bernard&co")
    main_user_window_width = screen_width // 2
    main_user_window_height = screen_height
    main_user_window.geometry(f"{main_user_window_width}x{main_user_window_height}")
    main_user_window.iconbitmap("images/logo_bernard&co.ico")
    # main_user_window.configure(bg="#3533cd")

    canvas = Canvas(main_user_window, width=main_user_window_width, height=main_user_window_height)
    canvas.pack()

    create_rounded_button(canvas, 50, 50, 200, 50, 20, "Bouton 1", lambda: print("Bouton 1 cliqué"))
    create_rounded_button(canvas, 50, 150, 200, 50, 20, "Bouton 2", lambda: print("Bouton 2 cliqué"))

    main_user_window.mainloop()

main_window()   