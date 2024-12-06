
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

paninis_patus = {
    "Tout Simple",
    "Végétarien",
    "Burger"
}
pâtes_patus = {
    "Carbo'",
    "Bolo'",
    "Mac n' cheese",
    "Pesto"
}


plat_patus = { 
    "paninis" : paninis_patus,
    "pates" : pâtes_patus
}
desserts_patus = {
    "Cookie froid",
    "Cookie chaud",
    "Brownie"
}
boissons_patus = {
    "Coca-Cola",
    "Ice-Tea",
    "Oasis",
    "Fanta",
    "Schweppes_agrumes"
}

formule_patus_1 = {
    "plat" : plat_patus,
    "dessert" : desserts_patus,
    "boisson" : boissons_patus
}
formule_patus_2 = {
    "plat" : plat_patus,
    "dessert" : desserts_patus,
}
formule_patus_3 = {
    "plat" : plat_patus,
    "boisson" : boissons_patus
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
    "menus" : menus_patus
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
    "classico",
    "rimini",
    "roma",
    "venezia",
    "3 fromages",
    "seguin"
}
paninis_XL_casa = {
    "royal",
    "cordon bleu",
    "cordon royal"
}
grands_paninis_casa = {
    "grec",
    "burger",
    "raclette",
    "chita",
    "grand classico",
    "grand ;rimini",
    "grand roma",
    "grand venezia",
    "grand 3 fromages",
    "grand seguin"
    }
desserts_casa = {
    "cookie",
    "donut",
    "panini nutella"
}
boissons_casa = {
    "Coca-Cola",
    "Ice-Tea",
    "Oasis",
    "Fanta",
    "Schweppes agrumes"
}

petite_formule_casa = {
    "plat" : paninis_casa,
    "dessert" : desserts_casa, 
    "boisson" : boissons_casa
}
formule_XL_casa = {
    "plat" : paninis_XL_casa, 
    "boisson" : boissons_casa
}
garnde_formule_casa = {
    "plat" : grands_paninis_casa,
    "boisson" : boissons_casa,
    "dessert" : desserts_casa
}

menus_casa = {
    "petite formule casa" : petite_formule_casa,
    "formule XL casa" : formule_XL_casa,
    "garnde formule casa" : garnde_formule_casa 
} 

la_casa_del_panini = {
    "nom" : "La casa del panini",
    "adresse" : "79 Avenue Jean Baptiste Clement",
    "horaires" : horaires_casa,
    "avis" : 4.8,      
    "menus" : menus_casa 
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
    "jambon, emmental",
    "poulet, cruidités",
    "thon, crudités",
    "poulet, avocat",
    "saumon, fumé"
}
salades_grenier = {
    "tomate, mozza",
    "chèvre, noix",
    "courgette, aubergine"
}
quiches_grenier = {
    "lorraine",
    "saumon, épinard",
    "courgettes",
    "lardons, brocolis"
}
plats_grenier = {
"sandwichs" : sandwichs_grenier,
"salades" : salades_grenier,
"quiches" : quiches_grenier

}

desserts_grenier = {
    "tarte citron",
    "tarte framboise",
    "flan",
    "éclair chocolat",
    "paris-brest"
}
boissons_grenier = {
    "eau plate",
    "eau gazeuse",
    "minute maid orange",
    "ice-tea",
    "coca-cola"
}
formule_grenier_1 = {
    "plat" : plats_grenier,
    "dessert" : desserts_grenier 
}
formule_grenier_2 = {
    "plat" : plats_grenier,
    "boisson" : boissons_grenier
    }
formule_grenier_3 = {
    "plat" : plats_grenier,
    "dessert" : desserts_grenier ,
    "boisson" : boissons_grenier
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
    "menus" : menus_grenier_a_pain
} 
#grenier a pain fin


data = [ patus_paninus, la_casa_del_panini, grenier_a_pain ]
