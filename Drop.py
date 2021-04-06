# std libs
import random
# kivy libs
from kivy.core.window import Window
# packages
from Character import Character


class Drop():
    """Manage a column of characters"""
    def __init__(self, x):
        self.x = x
        self.reset()

    def update(self, canvas):
        self.y -= self.velocity
        y = self.y
        for i in self.chars[::-1]:
            y -= i.height
            i.update(canvas, y)
            if i.y < 0:
                y -= i.height
                self.chars.remove(i)
                self.length -= 1

        # if all the character are out of the screen
        # recreate a list at the top
        if self.length == 0:
            self.reset()

    def reset(self):
        self.length = random.randrange(1, 20)
        self.chars = [Character(self.x) for i in range(self.length)]
        self.chars[0].is_first = True
        # make them appear outside the window
        self.y = self.chars[0].height * self.length + Window.size[1]
        self.velocity = random.randrange(3., 10.)


    def __str__(self):
        return f"Drop --> Len: {self.length}, X: {self.x}"
