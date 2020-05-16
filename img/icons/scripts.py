from browser import document, bind


@bind("#option_type_switch", "click")
def toggle_option_type(event):
    text_options = document.select(".text_options")
    image_options = document.select(".image_options")
    for element in text_options:
        if "show" in element.classList:
            element.classList.remove("show")
            element.classList.add("hide")
        elif "hide" in element.classList:
            element.classList.remove("hide")
            element.classList.add("show")
    for element in image_options:
        if "hide" in element.classList:
            element.classList.remove("hide")
            element.classList.add("show")
        elif "show" in element.classList:
            element.classList.remove("show")
            element.classList.add("hide")
