from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# from numpy import *
from perlin_noise import PerlinNoise
from random import *

app = Ursina()

player = FirstPersonController()
player.cursor.visible = False
player.gravity = 0.65
player.y = 20

window.fullscreen_resolution = (1920, 1080)
window.exit_button.visible = False
window.fullscreen = True
gug = "grass.png"
# Zombie = "zombie.png"
frameTex = 'frame.png'
block = load_model("assets/cubik.obj")
frame = Entity(model=block, texture=frameTex)


class BTYPE:
    Grass = 'grass.png'
    GrassModel = 'cubik.obj'
    Dirt = 'blocks/dirt.png'
    Wood = 'blocks/wood.png'
    Leaves = 'blocks/leave.png'
    Sand = 'blocks/sand.png'
    Bricks = 'blocks/brick.png'


Btype = BTYPE.Grass
Mtype = BTYPE.GrassModel


def input(key):
    if key == "escape":
        quit()
    if key == 'right mouse up':
        e = duplicate(frame)
        e.collider = 'mesh'
        e.model = Mtype
        e.texture = Btype


def update():
    if player.y < -3:
        player.y = 10

    frame.position = floor(player.position + camera.forward * 5)
    frame.y = frame.y + 2
    # zombie1.look_at(player, 'back')
    # zombie1.rotation_x = 0
    genTerr()


noise = PerlinNoise(octaves=2, seed=randrange(1, 9999999999999999999999999999999999999))
amp = 0
freq = 24

shells = []
shellWidth = 16

for i in range(shellWidth * shellWidth):
    cube = load_model("assets/cubik.obj")
    ent = Entity(model=cube, texture=gug, collider='box')
    shells.append(ent)


def genTerr():
    global amp, freq
    for i in range(len(shells)):
        x = shells[i].x = floor((i / shellWidth) + player.x - 0.5 * shellWidth)
        z = shells[i].z = floor((i % shellWidth) + player.z - 0.5 * shellWidth)
        y = shells[i].y = floor(noise([x / freq, z / freq]) * amp)


# ZombieModel = load_model('zombie.obj')
# zombie1 = Entity(model=ZombieModel, texture=Zombie, scale=1, double_sided=True, y=1, )

# app.run()
