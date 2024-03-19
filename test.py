import pyxel, random
pyxel.init(128, 128, title="little-fighter")
pyxel.load("res.pyxres")
bonhomme_x = 60
bonhomme_y = 60
ennemis_liste = []
points_de_structure = 10
print("Little Fighter")
print("A Hideo Kojima Game")
print("A Wasteland Studio Game")
print("Produced and Realised by Hideo Kojima")
print("Lead Programming: Nils Doucet")
print("Artistical Direction: Renan Laugier")
print("Technical and Engine Programming: Lucas Lex")
print("Collision Programming: Joachim Andersen from Andersen System")
print("From an idea of Lucas Lex, Renan Laugier, Nils Doucet and Hideo Kojima")
print("Thanks to Andersen System for technical help")
print("Copyright 2024 - France - Kojima Production - Wasteland Game")

def bonhomme_deplacement(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 113) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 96) :
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
    global vies
    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if  ennemi[1]>96:
            ennemis_liste.remove(ennemi)
    return ennemis_liste

def ennemis_suppression():
    global bonhomme_x, bonhomme_y, ennemis_liste
    ennemis_enlever = []
    for ennemi in ennemis_liste:
        ennemi_x, ennemi_y = ennemi
        if collision_cercle(ennemi_x, ennemi_y, 7.5, bonhomme_x, bonhomme_y, 7.5):
            ennemis_enlever.append(ennemi)
    
    for ennemi in ennemis_enlever:
        ennemis_liste.remove(ennemi)

def collision_cercle(cx1, cy1, r1, cx2, cy2, r2):
    return ((cx1-cx2)**2) + ((cy1-cy2)**2) <= (r1+r2)**2

def update():
    global bonhomme_x, bonhomme_y, ennemis_liste
    bonhomme_x, bonhomme_y = bonhomme_deplacement(bonhomme_x, bonhomme_y)
    ennemis_liste = ennemis_creation(ennemis_liste)
    ennemis_liste = ennemis_deplacement(ennemis_liste)
    ennemis_suppression()

def draw():
    pyxel.cls(11)
    for ennemi in ennemis_liste:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 16, 16, 16)
    pyxel.blt(bonhomme_x,bonhomme_y,0,0,0,16,16)
    pyxel.blt(0,128-16,0,0,32,15,47)
    pyxel.blt(15,128-16,0,16,32,31,47)
    pyxel.blt(30,128-16,0,0,32,15,47)
    pyxel.blt(45,128-16,0,16,32,31,47)
    pyxel.blt(60,128-16,0,0,32,15,47)
    pyxel.blt(75,128-16,0,16,32,31,47)
    pyxel.blt(90,128-16,0,0,32,15,47)
    pyxel.blt(105,128-16,0,16,32,31,47)
    pyxel.blt(120,128-16,0,0,32,15,47)

pyxel.run(update, draw)