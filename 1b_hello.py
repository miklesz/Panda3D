from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Wyłącz sterowanie kamery myszką.
        self.disableMouse()

        # Załaduj model środowiska.
        self.scene = \
            self.loader.loadModel("models/environment")
        # Zmień model do renderowania.
        self.scene.reparentTo(self.render)
        # Zastosuj przekształcenia skali i pozycji w modelu.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Dodaj procedurę spinCameraTask do menedżera zadań.
        self.taskMgr.add(
            self.spinCameraTask,
            "SpinCameraTask"
        )

        # Załaduj i przekształć aktora pandy.
        self.pandaActor = Actor(
            "models/panda-model",
            {"walk": "models/panda-walk4"}
        )
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Zapętl jego animację.
        self.pandaActor.loop("walk")

        # Stwórz cztery interwały dla lerpów potrzebne pandzie
        # do chodzenia tam i z powrotem.
        posInterval1 = self.pandaActor.posInterval(
            13,
            Point3(0, -10, 0),
            startPos=Point3(0, 10, 0)
        )
        posInterval2 = self.pandaActor.posInterval(
            13,
            Point3(0, 10, 0),
            startPos=Point3(0, -10, 0)
        )
        hprInterval1 = self.pandaActor.hprInterval(
            3,
            Point3(180, 0, 0),
            startHpr=Point3(0, 0, 0)
        )
        hprInterval2 = self.pandaActor.hprInterval(
            3,
            Point3(0, 0, 0),
            startHpr=Point3(180, 0, 0)
        )

        # Utwórz i odtwórz sekwencję, która koordynuje
        # interwały.
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

    # Zdefiniuj procedurę poruszania kamerą.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(
            20 * sin(angleRadians),
            -20 * cos(angleRadians),
            3
        )
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()