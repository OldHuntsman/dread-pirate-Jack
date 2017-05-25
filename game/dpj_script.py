# -*- coding: <UTF-8> -*-
# Main script for MER Origins: Dread Pirate Jack
from random import *
import renpy.store as store
import renpy.exports as renpy


class Ship(object):

    def __init__(self, name='Unknown'):
        self.name = name
        self.hull_max_durability = 10000
        self.hull_durability = self.hull_max_durability
        self.hull_capacity = 112000     # in pounds
        self.hull_speed = 100           # in 0.1 knots

    @property
    def condition(self):
        percent = str(self.hull_durability / (self.hull_max_durability / 100))
        return percent + "%"

passphrase = ""