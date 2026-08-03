from enum import Enum

TyreType = Enum('TyreType', [('FL', 1), ('FR', 2), ('BL', 3), ('BR', 4)])

class Car():

    def __init__(self):
        self.front_left_tyre = []
        self.front_right_tyre = []
        self.back_left_tyre = []
        self.back_right_tyre = []

    def add_tyre(self, type, tyre):
        if type == 1:
            self.front_left_tyre.append(tyre)
        elif type == 2:
            self.front_right_tyre.append(tyre)
        elif type == 3:
            self.back_left_tyre.append(tyre)
        elif type == 4:
            self.back_right_tyre.append(tyre)