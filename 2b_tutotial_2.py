from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # W metodzie „__init__”:
        music = self.loader.loadMusic("Vitamins.ogg")
        music.setLoop(True)
        # Ten utwór jest dość głośny,
        # więc ściszmy głośność.
        # Dostosujcie się do swoich ustawień i preferencji!
        music.setVolume(0.75)
        music.play()


app = MyApp()
app.run()