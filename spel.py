import pgzrun

WIDTH = 700
HEIGHT = 400

marknivå = HEIGHT - 100

spelare = Actor("spelare", (100,100))
mark = Actor("grön mark", (100,420))

gravitation = 0.8
hastighet = 0

def draw():
    screen.fill((0,0,80))
    mark.draw()
    spelare.draw()

def update():
    update_spelare()

def update_spelare():
    global hastighet
    spelare.y += hastighet
    hastighet += gravitation

    if spelare.y > marknivå:
        hastighet = 0

pgzrun.go()