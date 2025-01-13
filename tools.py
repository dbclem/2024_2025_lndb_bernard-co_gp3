def destroy_all_widgets(window):
    for widget in window.winfo_children():
        widget.destroy()


