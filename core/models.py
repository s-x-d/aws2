from django.db import models
from typing import NamedTuple

class RainbowColor(NamedTuple):
    name: str
    hex_code: str
    order: int

class Rainbow:
    RED = RainbowColor('Red', '#FF0000', 1)
    ORANGE = RainbowColor('Orange', '#FF7F00', 2)
    YELLOW = RainbowColor('Yellow', '#FFFF00', 3)
    GREEN = RainbowColor('Green', '#00FF00', 4)
    BLUE = RainbowColor('Blue', '#0000FF', 5)
    INDIGO = RainbowColor('Indigo', '#4B0082', 6)
    VIOLET = RainbowColor('Violet', '#9400D3', 7)

    COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

    @classmethod
    def get_all_colors(cls):
        return cls.COLORS

    @classmethod
    def get_color_by_name(cls, name):
        return next((color for color in cls.COLORS if color.name.lower() == name.lower()), None)

    @classmethod
    def get_color_by_order(cls, order):
        return next((color for color in cls.COLORS if color.order == order), None)
