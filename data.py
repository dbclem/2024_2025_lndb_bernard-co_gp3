
#Patus paninus debut
horaires_patus = {
    "lundi" : "11:00 - 14:30 ",
    "mardi" : "11:00 - 14:30 ",
    "mercredi" : "11:00 - 14:30 ",
    "jeudi" : "11:00 - 17:30 ",
    "vendredi" : "11:00 - 17:30 ",
    "samedi" : "Fermé",
    "dimanche" : "Fermé",    
}

plat_patus = { 
    "Tout Simple" : 7,
    "Végétarien" : 7,
    "Burger" : 7,
    "Carbo" : 8,
    "Bolo" : 8,
    "Mac n'cheese" : 8,
    "Pesto" : 8
}

desserts_patus = {
    "Cookie froid" : 3,
    "Cookie chaud" : 3,
    "Brownie" : 3
}
boissons_patus = {
    "Coca-Cola" : 2,
    "Ice-Tea" : 2,
    "Oasis" : 2,
    "Fanta" : 2,
    "Schweppes_agrumes" : 2
}

formule_patus_1 = {
    "plat" : plat_patus,
    "dessert" : desserts_patus,
    "boisson" : boissons_patus,
    "price" : 12,
    "temps" : 10
}
formule_patus_2 = { 
    "plat" : plat_patus,
    "dessert" : desserts_patus,
    "price" : 10,
    "temps" : 7
}
formule_patus_3 = { 
    "plat" : plat_patus,
    "boisson" : boissons_patus,
    "price" : 9,
    "temps" : 7
}


menus_patus = {
    "formule patus 1" : formule_patus_1,  
    "formule patus 2" : formule_patus_2, 
    "formule patus 3" : formule_patus_3,    
}

patus_paninus = {
    "nom" : "Patus Paninus",
    "adresse" : "12 rue du Parchamp",
    "horaires" : horaires_patus,
    "avis" : 4.8,      
    "menus" : menus_patus,
    "image_path" : "images/patus-paninus.jpg"
}
#Patus paninus fin 

#Casa del panini debut
horaires_casa = {    
    "lundi" : "09:00 - 14:00 ",
    "mardi" : "09:00 - 14:00 ",
    "mercredi" : "09:00 - 14:00 ",
    "jeudi" : "09:00 - 14:00 ",
    "vendredi" : "09:00 - 14:00 ",
    "samedi" : "Fermé",
    "dimanche" : "Fermé",
    }

paninis_casa = {
    "classico" : 8,
    "rimini" : 8,
    "roma" : 8,
    "venezia" : 8,
    "3 fromages" : 8,
    "seguin" : 8
}
paninis_XL_casa = {
    "royal" : 10,
    "cordon bleu" : 10,
    "cordon royal" : 10
}
grands_paninis_casa = {
    "grec" : 12,
    "burger" : 12,
    "raclette" : 12,
    "chita" : 12,
    "grand classico" : 12,
    "grand rimini" : 12,
    "grand roma" : 12,
    "grand venezia" : 12,
    "grand 3 fromages" : 12,
    "grand seguin" : 12
    }
desserts_casa = {
    "cookie" : 4,
    "donut" : 4,
    "panini nutella" : 4
}
boissons_casa = {
    "Coca-Cola" : 2.50,
    "Ice-Tea" : 2.50,
    "Oasis" : 2.50,
    "Fanta" : 2.50,
    "Schweppes agrumes" : 2.50
}

petite_formule_casa = {
    "plat" : paninis_casa,
    "dessert" : desserts_casa, 
    "boisson" : boissons_casa,
    "price" : 12,
    "temps" : 8
}
formule_XL_casa = {
    "plat" : paninis_XL_casa, 
    "boisson" : boissons_casa,
    "price" : 15,
    "temps" : 15
}
grande_formule_casa = {
    "plat" : grands_paninis_casa,
    "dessert" : desserts_casa,
    "price" : 13.50,
    "temps" : 10
}

menus_casa = {
    "petite formule casa" : petite_formule_casa,
    "formule XL casa" : formule_XL_casa,
    "garnde formule casa" : grande_formule_casa 
} 

la_casa_del_panini = {
    "nom" : "La casa del panini",
    "adresse" : "79 Avenue Jean Baptiste Clement",
    "horaires" : horaires_casa,
    "avis" : 4.8,      
    "menus" : menus_casa,
    "image_path" : "images/la_casa_del_panini.jpg" 
}
#Casa del panini fin



#grenier a pain debut
horaires_grenier_a_pain = {
    "lundi" : "Fermé",
    "mardi" : "07:30 - 20:00 ",
    "mercredi" : "07:30 - 20:00  ",
    "jeudi" : "07:30 - 20:00 ",
    "vendredi" : "07:30 - 20:00  ",
    "samedi" : "07:30 - 20:00 ",
    "dimanche" : "07:30 - 19:00 ",
}

sandwichs_grenier = {
    "jambon, emmental" : 4,
    "poulet, cruidités" : 4,
    "thon, crudités" : 4,
    "poulet, avocat" : 4,
    "saumon, fumé" : 4
}
salades_grenier = {
    "tomate, mozza" : 5,
    "chèvre, noix" : 5,
    "courgette, aubergine" : 5
}
quiches_grenier = {
    "lorraine" : 4.50,
    "saumon, épinard" : 4.50,
    "courgettes" : 4.50,
    "lardons, brocolis" : 4.50
}
plats_grenier = {
    "jambon, emmental" : 4,
    "poulet, cruidités" : 4,
    "thon, crudités" : 4,
    "poulet, avocat" : 4,
    "saumon, fumé" : 4,
    "tomate, mozza" : 5,
    "chèvre, noix" : 5,
    "courgette, aubergine" : 5, 
    "lorraine" : 4.50,
    "saumon, épinard" : 4.50,
    "courgettes" : 4.50,
    "lardons, brocolis" : 4.50

}

desserts_grenier = {
    "tarte citron" : 4,
    "tarte framboise" : 4,
    "flan" : 4,
    "éclair chocolat" : 4,
    "paris-brest" : 4
}
boissons_grenier = {
    "eau plate" : 2.50,
    "eau gazeuse" : 2.50,
    "minute maid orange" : 2.50,
    "ice-tea" : 2.50,
    "coca-cola" : 2.50
}
formule_grenier_1 = {
    "plat" : plats_grenier,
    "dessert" : desserts_grenier,
    "price" : 8,
    "temps" : 5 
}
formule_grenier_2 = {
    "plat" : plats_grenier,
    "boisson" : boissons_grenier,
    "price" : 8,
    "temps" : 5
    }
formule_grenier_3 = {
    "plat" : plats_grenier,
    "dessert" : desserts_grenier ,
    "boisson" : boissons_grenier,
    "price" : 10,
    "temps" : 5
}

menus_grenier_a_pain = {
    "formule grenier 1" : formule_grenier_1,
    "formule grenier 2" : formule_grenier_2,
    "formule grenier 3" : formule_grenier_3

}

grenier_a_pain = {
    "nom" : "Grenier à pain",
    "adresse" : "12 rue du Parchamp",
    "horaires" : horaires_grenier_a_pain,
    "avis" : 4.8,      
    "menus" : menus_grenier_a_pain,
    "image_path" : "images/le-grenier-a-pain.jpg" 
} 
#grenier a pain fin


data = [ patus_paninus, la_casa_del_panini, grenier_a_pain ]

liste_mdp = [
    {'username': 'clem', 'password': '123456'},
    {'username': 'edgar', 'password': 'qsdfgh'},
    {'username': 'cass', 'password': 'azerty'}
]