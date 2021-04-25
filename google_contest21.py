from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

e = Entity(model='cube', color=color.orange, scale=1, rotation=(0,0,0), texture='brick')

#class Player(Entity):
    # def __init__(self, **kwargs):
    #     super().__init__()
    #     self.model='cube'
    #     self.color = color.red
    #     self.scale_y = 2

    #     for key, value in kwargs.items():
    #         setattr(self, key, value)

    # def input(self, key):
    #     if key == 'space':
    #         self.animate_x(2, duration=1)

    # def update(self):
    #     self.x += held_keys['d'] * time.dt * 10
    #     self.x -= held_keys['a'] * time.dt * 10

#player = Player(x=-1)


class Brick(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'brick',
            color = color.rgb(165, 42, random.uniform(0.9,1)),
            highlight_color = color.lime)

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime)
class mmm():
    def input(self, key):
        if Brick.hovered:
            if key == 'left mouse down':
                voxel = Brick(position = Brick.position + mouse.normal)

            if key == 'right mouse down':
                destroy(Brick)

            if key == 'p':
                print(Brick.position)

app = Ursina()

for z in range(15):
    for x in range(15):
        voxel = Voxel(position = (x,0,z))
voxel = Brick(position = (5,1,5))



player = FirstPersonController()

app.run()