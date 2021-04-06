# std libs
import random
# kivy libs
from kivy.core.text import Label as CoreLabel
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window


class Character(Label):
    """Handle character creation and animation"""
    def __init__(self, x, *args, **kwargs):
        super().__init__()
        self.x = x
        self.y = Window.size[1]
        # Georgian font on Linux
        self.font_name = "NotoSerifGeorgian-Regular.ttf"
        self.font_size = 24
        self.text = self.pick()
        self.texture_update()
        self.height = int(self.texture.size[1])
        self.is_first = False

    def pick(self):
        """Returns a random unicode character selected in the Georgian script scope.
        From ani (10D0) to hae (10F0)"""
        # Georgian script range as integers
        self.letters = [ord("\u10D0"), ord("\u10F0")]
        # randomly select one and cast it as unicode char
        return chr(random.randrange(self.letters[0], self.letters[1]))

    def update(self, canvas, y, *args):
        self.y = y
        # randomize changing the character
        if not self.text or random.random() > 0.995:
            self.text = self.pick()
            self.texture_update()
        txt = self.texture
        # set the character color
        # if it is first, it can have a different color
        try:
            self.__getattribute__('r')
        except AttributeError:
            if self.is_first and random.random() > 0.66:
                self.r = 1
                self.g = 1
                self.b = 1
            else:
                self.r = 1
                self.g = 0
                self.b = 0
        canvas.add(Color(self.r, self.g, self.b, 1))
        canvas.add(Rectangle(size=txt.size, pos=[self.x, y], texture=txt))

    def __str__(self):
        return f"Character --> txt: {self.text}, height: {self.height}"
