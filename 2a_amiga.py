from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.interval.IntervalGlobal import *
base = ShowBase()
ball = base.loader.loadModel('ball.bam')
ball.reparentTo(base.render)
base.setBackgroundColor(0, 0, 0)
ball.setPos(0, 17.5, 0)
spotlight = Spotlight('spotlight')
spot = base.render.attachNewNode(spotlight)
spot.setPos(-25, -15, 30)
spot.lookAt(ball)
base.render.setLight(spot)
ambient_light = AmbientLight('ambient light')
ambient_light.setColor((0.1, 0.1, 0.1, 1))
ambient = base.render.attachNewNode(ambient_light)
base.render.setLight(ambient)
ball.setHpr(90, -60, 0)
grid = base.loader.loadModel('grid.bam')
grid.reparentTo(base.render)
grid.setScale(0.005)
grid.setPos(grid.getTightBounds()[0][0]/2, 2, 15)
spot.node().setShadowCaster(True)
base.render.setShaderAuto()
base.render.setDepthOffset(-3)
spot.node().setShadowCaster(True, 8192, 8192)
rotate_interval = LerpHprInterval(
    nodePath=ball,
    duration=5,
    hpr=(90, -60, 360)
)
rotate_interval.loop()
ball_handle = base.render.attachNewNode('ball_handle')
ball.reparentTo(ball_handle)
ball_handle.reparentTo(base.render)
move_right_interval = LerpPosInterval(
    nodePath=ball_handle,
    duration=2,
    startPos=(-4, 0, 0),
    pos=(+4, 0, 0)
)
move_left_interval = LerpPosInterval(
    nodePath=ball_handle,
    duration=2,
    startPos=(+4, 0, 0),
    pos=(-4, 0, 0)
)
move_sequence = Sequence(move_right_interval, move_left_interval)
move_sequence.loop()
jump_up_interval = LerpPosInterval(
    nodePath=ball,
    duration=.75,
    startPos=(0, 17.5, -1.5),
    pos=(0, 17.5, 3),
    blendType='easeOut'
)
jump_down_interval = LerpPosInterval(
    nodePath=ball,
    duration=.75,
    startPos=(0, 17.5, 3),
    pos=(0, 17.5, -1.5),
    blendType='easeIn'
)
jump_sequence = Sequence(jump_up_interval, jump_down_interval)
jump_sequence.loop()

base.setFrameRateMeter(True)

base.run()
