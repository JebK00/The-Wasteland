import pyxel, random
pyxel.init(128, 128, title="little-fighter")
pyxel.load("res.pyxres")
vaisseau_x = 60
vaisseau_y = 60
ennemis_liste = []

def vaisseau_deplacement(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120) :
            y = y + 1
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0) :
            y = y - 1
    return x, y
    
def ennemis_creation(ennemis_liste):
    if (pyxel.frame_count % 50 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste

def ennemis_deplacement(ennemis_liste):
    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if  ennemi[1]>128:
            ennemis_liste.remove(ennemi)
    return ennemis_liste

def ennemis_suppression():
    for ennemi in ennemis_liste:
            if ennemi[0] <= vaisseau_x and ennemi[0]+8 >= vaiseau_y and ennemi[1]+8 >= vaisseau_y:
                ennemis_liste.remove(ennemi)


def update():
    global vaisseau_x, vaisseau_y, ennemis_liste
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    ennemis_liste = ennemis_creation(ennemis_liste)
    ennemis_liste = ennemis_deplacement(ennemis_liste)

def draw():
    pyxel.cls(11)
    for ennemi in ennemis_liste:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 16, 16, 16)
    pyxel.blt(vaisseau_x,vaisseau_y,0,0,0,16,16)


pyxel.run(update, draw)
