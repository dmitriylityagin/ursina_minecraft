from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# from numpy import *
from perlin_noise import PerlinNoise
from random import *

app = Ursina()

player = FirstPersonController()
player.cursor.visible = True
player.gravity = 0.65
player.y = 20
player.x = 0
player.z = 0

window.fullscreen_resolution = (1920, 1080)
window.exit_button.visible = False
window.fullscreen = True
gug = "grass.png"
# Zombie = "zombie.png"
# frameTex = 'frame.png'
block = load_model("assets/cubik.obj")


# frame = Entity(model=block, texture=frameTex)


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


class Voxel(Button):
    global Btype

    def __init__(self, position=(0, 0, 0), texture=Btype, type="breakable"):
        self.pos = position
        self.type = type
        super().__init__(
            parent=scene, model='assets/cubik',
            scale=1, texture=texture, position=position,
            origin_y=0.5, color=color.color(0, 0, uniform(1, 255))
        )

    #  добавляем input — встроенную функцию взаимодействия с блоком Voxel:
    #     		если нажали на ПКМ — появится блок
    #     		если нажали на ЛКМ — удалится
    def input(self, key):
        global Btype
        if self.hovered:
            if key == "1":
                Btype = BTYPE.Grass
            if key == "2":
                Btype = BTYPE.Dirt
            if key == "3":
                Btype = BTYPE.Wood
            if key == "4":
                Btype = BTYPE.Leaves
            if key == "5":
                Btype = BTYPE.Sand
            if key == "6":
                Btype = BTYPE.Bricks
            if key == "left mouse down":
                if self.type == "breakable":
                    destroy(self)
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=Btype)


#
# for i in range(0, 15):
#     for j in range(0, 15):
#         Voxel(position=(i, 0, j))


def input(key):
    if key == "escape":
        quit()


def update():
    if player.y < -3:
        player.y = 10

    genTerr()

    # frame.position = floor(player.position + camera.forward * 5)
    # frame.y = frame.y + 2
    # zombie1.look_at(player, 'back')
    # zombie1.rotation_x = 0


noise = PerlinNoise(octaves=2, seed=randrange(1, 9999999999999999999999999999999999999))
amp = 0
freq = 24

shells = []
shellWidth = 16

for i in range(shellWidth * shellWidth):
    vox = Voxel(type="nb")
    shells.append(vox)


def genTerr():
    global amp, freq
    for i in range(len(shells)):
        x = shells[i].x = floor((i / shellWidth) + player.x - 0.5 * shellWidth)
        z = shells[i].z = floor((i % shellWidth) + player.z - 0.5 * shellWidth)
        y = shells[i].y = floor(noise([x / freq, z / freq]) * amp)

# ZombieModel = load_model('zombie.obj')
# zombie1 = Entity(model=ZombieModel, texture=Zombie, scale=1, double_sided=True, y=1, )
# app.run()
