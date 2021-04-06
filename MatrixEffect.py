# std libs
import random
import argparse
# kivy libs
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
# packages
from Character import Character
from Drop import Drop


class Animation(Widget):
    """Widget of the animation"""
    def __init__(self, speed):
        super().__init__()
        self.y = 0
        x = Window.size[0]
        self.drops = list()
        while x > 0:
            self.drops.append(Drop(x))
            x -= self.drops[-1].chars[-1].height
        Clock.schedule_interval(lambda x: self.update(), speed)

    def update(self):
        self.canvas.clear()
        for i in self.drops:
            i.update(self.canvas)


class Main(App):
    def __init__(self, debug=False):
        super().__init__()
        self.conf(debug)

    def build(self):
        return Animation(self.speed)

    def conf(self, debug):
        if debug:
            Window.size = [1440//2, 900//2]
            self.speed = 0.05
        else:
            Window.size = [1440, 900]
            Window.fullscreen = True
            Window.show_cursor = False
            self.speed = 0.01
        Window.left = 0
        Window.top = 0
        Window.borderless = True
        self.title = "Animation"


if __name__ == "__main__":
    Main().run()
