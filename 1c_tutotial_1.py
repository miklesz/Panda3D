from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.filter.CommonFilters import CommonFilters

loadPrcFileData("", "textures-power-2 none")
loadPrcFileData("", "basic-shaders-only #t")
base = ShowBase()
ball = base.loader.loadModel("ball.bam")
ball.reparentTo(base.render)
base.setBackgroundColor(0, 0, 0)
ball.setPos(0, 17.5, 0)
spotlight = Spotlight("spotlight")
spot = base.render.attachNewNode(spotlight)
spot.setPos(-25, -15, 30)
spot.lookAt(ball)
base.render.setLight(spot)
ambient_light = AmbientLight("ambient light")
ambient_light.setColor((0.1, 0.1, 0.1, 1))
ambient = base.render.attachNewNode(ambient_light)
base.render.setLight(ambient)
ball.setHpr(90, -60, 0)
grid = base.loader.loadModel("grid.bam")
grid.reparentTo(base.render)
grid.setScale(0.005)
grid.setPos(grid.getTightBounds()[0][0] / 2, 2, 15)
rotate_interval = LerpHprInterval(nodePath=ball, duration=5, hpr=(90, -60, 360))
rotate_interval.loop()
base.setFrameRateMeter(True)
filters = CommonFilters(base.win, base.cam)
filters.setVolumetricLighting(
    caster=spot,
    numsamples=200,
    density=0.1,
    decay=0.98,
)

grid.setColorScale(1, 1, 1, 0)

base.run()
