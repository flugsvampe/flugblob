import pgzrun
from pgzhelper import *

WIDTH = 700
HEIGHT = 400

marknivå = HEIGHT - 100


bakgrund = Actor("bakgrund", (100,100))
spelare = Actor("spelare", (100,100))
mark = Actor("grön mark", (100,420))
StorBlob = Actor("röd blob", (400,100))

gravitation = 0.8
hastighet = 0
hastighet2 = 0
höger = 0
game_over = False

def draw():
    bakgrund.draw()
    mark.draw()
    StorBlob.draw()
    spelare.draw()

def update():
    global game_over
    global spelare
    global StorBlob
    if not game_over:
        update_StorBlob()
        update_spelare()

    if spelare.circle_collidepoint(87, StorBlob.x, StorBlob.y + 10):
        game_over = True


def update_spelare():
    global hastighet
    spelare.y += hastighet
    hastighet += gravitation
    spelare.x += höger
    if spelare.y > marknivå:
        hastighet = 0

def update_StorBlob():
    global hastighet2
    StorBlob.y += hastighet2
    hastighet2 += gravitation
    if (StorBlob.y + 16) > marknivå:
        hastighet2 = 0


def on_key_down(key):
    global hastighet
    global höger
    if spelare.y > marknivå:
        if key == key.W:
            hastighet = -12
    if key == key.D:
        höger = 3
    if key == key.A:
        höger = -3

def on_key_up(key):
    global höger
    if key == key.D:
        höger = 0
    if key == key.A:
        höger = 0


pgzrun.go()