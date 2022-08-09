from direct.showbase.ShowBase import ShowBase
base = ShowBase()
ball = base.loader.loadModel('ball.bam')
ball.reparentTo(base.render)
ball.setPos(0, 17.5, 0)

spotlight = Spotlight('spotlight')
spot = base.render.attach_new_node(spotlight)
spot.set_pos(-25, -15, 30)
spot.look_at(ball)
base.render.set_light(spot)

base.run()
