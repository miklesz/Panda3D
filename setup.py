from setuptools import setup

setup(
    name="Amiga Boing Ball",
    options={
        "build_apps": {
            # Pliki, które chcemy dołączyć. Konkretnie:
            # * Wszystkie nasze pliki graficzne (.png)
            # * Wszystkie nasze pliki dźwiękowe i muzyczne
            #   (.ogg)
            # * Wszystkie nasze pliki tekstowe (.txt)
            # * Wszystkie nasze modele 3D (.egg)
            #    - Zostaną one automatycznie prze-konwertowane
            #      na pliki .bam
            # * Wszystkie nasze modele 3D (.bam)
            # * I wszystkie nasze pliki czcionek
            #   (w folderze „Font”)
            "include_patterns": [
                "**/*.png",
                "**/*.ogg",
                "**/*.txt",
                "**/*.egg",
                "**/*.bam",
                "Fonts/*"
            ],
            # Chcemy mieć aplikację gui, a nasz "główny" plik
            # Pythona to "2a_amiga.py"
            "gui_apps": {
                "Amiga Boing Ball": "2a_amiga.py"
            },
            # Wtyczki, których używamy. W szczególności
            # używamy OpenGL i dźwięku OpenAL
            "plugins": [
                "pandagl",
                "p3openal_audio"
            ],
            # Platformy, dla których budujemy.
            # Usuńcie te, których nie chcecie.
            # "platforms": [
            #     "manylinux2010_x86_64",
            #     "macosx_10_9_x86_64",
            #     "win_amd64"
            # ],
            # Nazwa naszego pliku dziennika. Zachowujemy
            # krótką nazwę katalogu — nasz tytuł jest dość
            # długi — i umieszczamy plik w katalogu
            # „app-data” użytkownika.
            "log_filename":
                "$USER_APPDATA/AmigaBoingBall/output.log",
            # Zamiast zezwalać na gromadzenie danych dziennika,
            # decydujemy się na rozpoczęcie dziennika od nowa
            # przy każdym uruchomieniu.
            "log_append": False
        }
    }
)