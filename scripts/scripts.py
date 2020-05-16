from browser import document, bind


@bind("#menu_icon", "click")
def show_menu(event):
    menu = document["mobile_nav"]
    menu_button = document["menu_icon"]
    close_button = document["close_icon"]
    if "hide" in menu.classList:
        menu_button.classList.remove("show")
        menu_button.classList.add("hide")
        close_button.classList.remove("hide")
        close_button.classList.add("show")
        menu.classList.remove("hide")
        menu.classList.add("show")

@bind("#close_icon", "click")
def hide_menu(event):
    menu = document["mobile_nav"]
    menu_button = document["menu_icon"]
    close_button = document["close_icon"]
    if "show" in menu.classList:
        close_button.classList.remove("show")
        close_button.classList.add("hide")
        menu_button.classList.remove("hide")
        menu_button.classList.add("show")
        menu.classList.remove("show")
        menu.classList.add("hide")