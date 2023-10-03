from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# from numpy import *
from perlin_noise import PerlinNoise
import random

app = Ursina()
window.fullscreen_resolution = (1920, 1080)
window.fullscreen = True
gug = load_texture("ura.png")
Zombie = load_texture("zombie.png")


def input(key):
    if key == "escape":
        quit()


def update():
    if player.y < -3:
        player.y = 10
    zombie1.look_at(player, 'back')
    zombie1.rotation_x = 0
    genTerr()


noise = PerlinNoise(octaves=2, seed=random.randint(1, 9999999))
amp = 6
freq = amp * 4

shells = []
shellWidth = 20

for i in range(shellWidth*shellWidth):
    ent = Entity(model='cube', texture=gug, collider='box')
    shells.append(ent)


def genTerr():
    global amp, freq
    for i in range(len(shells)):
        x = shells[i].x = floor((i / shellWidth) + player.x - 0.5 * shellWidth)
        z = shells[i].z = floor((i % shellWidth) + player.z - 0.5 * shellWidth)
        y = shells[i].y = floor(noise([x / freq, z / freq]) * amp)


# for i in range(dist * dist):
#     cube = Entity(model='cube', texture=gug, collider="mesh")
#     cube.x = floor(i / dist)
#     cube.z = floor(i % dist)
#     cube.y = floor(noise([cube.x / freq, cube.z / freq]) * amp)
# ZombieModel = load_model('zombie.obj')
# zombie1 = Entity(model=ZombieModel, texture=Zombie, scale=1, x=dist / 2, y=0.5, z=dist / 2)
# zombie1.gravity = 0.65
# for x in range(0, 15):
#     for y in range(0, 15):
#         Entity(model='cube', texture=gug, collider="mesh", scale=(1, 1, 1), position=(x, 0, y))
# # cube = Entity(model='cube', texture=gug, collider="mesh", scale=(2, 2, 2), position=(1, 0, 5))
player = FirstPersonController()

player.gravity = 0.65
ZombieModel = load_model('zombie.obj')
zombie1 = Entity(model=ZombieModel, texture=Zombie, scale=1, double_sided=True, y=1,)

# app.run()
