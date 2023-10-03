from menushka import *
from pygame import *

while True:
    start = False
    mixer.music.load("music/menu-music.wav")
    mixer.music.play(-1)
    while not start:
        start = play_button.check()
        sc.fill((202, 228, 241))
        sc.blit(bg, (0, 0))
        sc.blit(title, (5, 5))
        exit_button.draw()
        play_button.draw()
        for e in event.get():
            display.update()
    mixer.music.unload()
    quit()
    from rty import *
    init()
    mixer.music.load("music/in-game-music.wav")
    mixer.music.play(-1)
    
    app.run()

