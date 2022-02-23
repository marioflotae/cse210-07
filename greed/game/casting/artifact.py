from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    #Move artifact
    def advance(self):
        self._position._y += 1
        return self._position

    #Wrap artifacts
    def move_next(self, max_x, max_y):
        super().move_next(max_x, max_y)

    