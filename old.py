from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.interval.IntervalGlobal import *

base = ShowBase()

base.set_background_color(0, 0, 0)

model = base.loader.load_model('ball.dae')
model.reparent_to(base.render)

model.show_tight_bounds()
box = model.get_tight_bounds()
print(box)
model.set_pos(-(box[0][0]+box[1][0])/2, -(box[0][1]+box[1][1])/2, -(box[0][2]+box[1][2])/2)
box = model.get_tight_bounds()
print(box)
model.hide_bounds()

ball = base.render.attach_new_node('ball')
model.reparent_to(ball)
ball.reparent_to(base.render)
#
# ball.writeBamFile('ball.bam')
# exit()

ball.set_y(17.5)

spotlight = Spotlight('spotlight')
spot = base.render.attach_new_node(spotlight)
spot.set_pos(-25, -15, 30)
spot.look_at(ball)
base.render.set_light(spot)

ambient_light = AmbientLight('ambient light')
ambient_light.set_color((0.1, 0.1, 0.1, 1))
ambient = base.render.attach_new_node(ambient_light)
base.render.set_light(ambient)

ball.set_hpr(90, -60, 0)

grid = base.loader.load_model('./the_grid/scene.gltf')
grid.reparent_to(base.render)
# ball.writeBamFile('grid.bam')
# exit()

print(grid.get_tight_bounds())
grid.set_scale(0.005)
print(grid.get_tight_bounds())

grid.set_y(2)

grid.set_z(15)

grid.set_x(-18.3077 / 2)

print(grid.get_tight_bounds())

spot.node().set_shadow_caster(True)
base.render.set_shader_auto()

base.render.set_depth_offset(-3)

spot.node().set_shadow_caster(True, 8192, 8192)

base.set_frame_rate_meter(True)

print(ball.get_hpr())

rotate_interval = LerpHprInterval(nodePath=ball,
                                  duration=5,
                                  hpr=(90, -60, 360))
rotate_interval.loop()

move_right_interval = LerpPosInterval(nodePath=ball,
                                      duration=2,
                                      startPos=(-4, 17.5, 0),
                                      pos=(+4, 17.5, 0))
move_left_interval = LerpPosInterval(nodePath=ball,
                                      duration=2,
                                      startPos=(+4, 17.5, 0),
                                      pos=(-4, 17.5, 0))
move_sequence = Sequence(move_right_interval, move_left_interval)
move_sequence.loop()

jump_up_interval = LerpPosInterval(nodePath=ball,
                                   duration=.75,
                                   startPos=(0, 17.5, -1.5),
                                   pos=(0, 17.5, 3),
                                   blendType='easeOut')
jump_down_interval = LerpPosInterval(nodePath=ball,
                                     duration=.75,
                                     startPos=(0, 17.5, 3),
                                     pos=(0, 17.5, -1.5),
                                     blendType='easeIn')
jump_sequence = Sequence(jump_up_interval, jump_down_interval)
jump_sequence.loop()

base.run()
