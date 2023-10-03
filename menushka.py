from pygame import *

init()
sc = display.set_mode((1920, 1080), FULLSCREEN)
running = True
ext = image.load("assets/exit.png").convert_alpha()
play = image.load("assets/play.png").convert_alpha()
ext_on = image.load("assets/exit_on.png").convert_alpha()
play_on = image.load("assets/play_on.png").convert_alpha()
title = image.load("assets/minecraft_title.png").convert_alpha()
tit = title.get_rect()
bg = image.load("assets/bg.jpeg")


class Button:
    def __init__(self, x, y, image, scale, name):
        if name == "play":
            self.start = False
        self.name = name
        self.scale = scale
        width = image.get_width()
        height = image.get_height()
        self.image = transform.scale(image, (int(width * scale), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def check(self):
        return self.start

    def draw(self):
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.name == "exit":
                self.image = transform.scale(ext_on,
                                             (int(ext_on.get_width() * self.scale),
                                              (int(ext_on.get_height() * self.scale))))
            else:
                self.image = transform.scale(play_on,
                                             (int(play_on.get_width() * self.scale),
                                              (int(play_on.get_height() * self.scale))))
            if mouse.get_pressed()[0] == 1:
                if self.name == "exit":
                    quit()
                else:
                    self.start = True
        else:
            if self.name == "exit":
                self.image = transform.scale(ext,
                                             (int(ext.get_width() * self.scale),
                                              (int(ext.get_height() * self.scale))))
            else:
                self.image = transform.scale(play,
                                             (int(play.get_width() * self.scale),
                                              (int(play.get_height() * self.scale))))
        # else:
        #     if self.name == "exit:":
        #         self.image = ext
        #     else:
        #         self.image = play
        sc.blit(self.image, (self.rect.x, self.rect.y))


exit_button = Button(200, 550, ext, 0.25, "exit")
play_button = Button(200, 400, play, 0.25, "play")
# while running:
#     app.fill((202, 228, 241))
#     app.blit(bg, (0, 0))
#     app.blit(title, (5, 5))
#     exit_button.draw()
#     play_button.draw()
#     for e in event.get():
#         display.update()
# quit()
