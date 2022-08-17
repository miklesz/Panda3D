from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)
        self.scene = \
            self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.disableMouse()

        self.accept("escape", exit)


app = MyApp()
app.run()