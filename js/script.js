function menu_btn(){
    var mob_nav = document.getElementById('mobile_nav');
    var menu_btn = document.getElementById('menu_button');
    var close = document.getElementById('close_btn');
    //mob_nav.classList.toggle('hide');
    mob_nav.classList.toggle('show');
    menu_btn.classList.toggle('hide');
    close.classList.toggle('show');
}

function close_b(){
    var mob_nav = document.getElementById('mobile_nav');
    var menu_btn = document.getElementById('menu_button');
    var close = document.getElementById('close_btn');

    mob_nav.classList.toggle('show');
    menu_btn.classList.toggle('hide');
    close.classList.toggle('show');
}