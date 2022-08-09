from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
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

base.run()