from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.interval.IntervalGlobal import *
base = ShowBase()
ball = base.loader.loadModel('ball.bam')
ball.reparentTo(base.render)
base.setBackgroundColor(0, 0, 0)
ball.setPos(0, 17.5, 0)

# ball.setTransparency(TransparencyAttrib.M_alpha)
# ball.setTransparency(TransparencyAttrib.M_dual)
# ball.setAlphaScale(.5)

spotlight = Spotlight('spotlight')
spotlight.setColor((1, 1, 0.5, 1))
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

move_right_interval = LerpPosInterval(
    nodePath=ball,
    duration=2,
    startPos=(-4, 17.5, 0),
    pos=(+4, 17.5, 0)
)
move_left_interval = LerpPosInterval(
    nodePath=ball,
    duration=2,
    startPos=(+4, 17.5, 0),
    pos=(-4, 17.5, 0)
)
move_sequence = Sequence(move_right_interval, move_left_interval)
# move_sequence.loop()

base.render.setRenderMode(RenderModeAttrib.M_filled_wireframe, 10)

base.run()