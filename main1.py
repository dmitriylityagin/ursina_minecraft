from menushka import *
from pygame import *
while True:
    start = False
    while not start:
        start = play_button.check()
        sc.fill((202, 228, 241))
        sc.blit(bg, (0, 0))
        sc.blit(title, (5, 5))
        exit_button.draw()
        play_button.draw()
        for e in event.get():
            display.update()
    quit()
    from rty import *

    # ZombieModel = load_model('zombie.obj')
    # zombie1 = Entity(model=ZombieModel, texture=Zombie, scale=1, x=dist / 2, z=dist / 2)
    app.run()
# cube = Entity(model='cube', texture=gug, collider="mesh", scale=(2, 2, 2), position=(1, 0, 5))
