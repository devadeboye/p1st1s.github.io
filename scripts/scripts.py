from browser import document, bind, html


def profile_pics_selector():
    """
    choose appropriate profile pics based on screen size
    """
    # use project element to detect if device is mobile
    mobile_view = document["project_small_display"].style.display
    pp_wrapper = document["profile_pics_cont"]
    small_img = "./img/about_pics_small.JPG"
    normal_img = "./img/about_pics.JPG"
    if mobile_view != "none":
        pp_wrapper <= html.IMG(
            src=small_img,
            alt="picture of emmanuel"
        )
    else:
        pp_wrapper <= html.IMG(
            src=normal_img,
            alt="picture of emmanuel"
        )

@bind("#menu_icon", "click")
def show_menu(event):
    """
    show menu item on small display
    """
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
    #if menu.style.display == "none":
    #    menu_button.style.display = "hide"
    #    close_button.style.display = "block"
    #    menu.style.display = "block"


@bind("#close_icon", "click")
def hide_menu(event):
    """
    hide menu item on small display
    """
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


@bind("#show_email", "click")
def show_email(event):
    document["show_email"].textContent = "adeboye3a@gmail.com"


# choose appropriate profile pics based on screen size
profile_pics_selector()