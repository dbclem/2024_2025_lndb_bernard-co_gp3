def destroy_all_widgets(window):
    for widget in window.winfo_children():
        widget.destroy()

def refresh_page(page, def_redislaye_page) : 
    destroy_all_widgets(page)
    def_redislaye_page()

