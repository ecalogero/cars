from lib.car import *
from lib.tyre import *

def test_creating_a_car_w_tyres_works():

    fl_tyre = Tyre(120.05,5.1)
    fr_tyre = Tyre(119.05,4.1)
    bl_tyre = Tyre(118.5,4.8)
    br_tyre = Tyre(115.05,3.1)

    car = Car()
    car.add_tyre(1, fl_tyre)
    car.add_tyre(2, fr_tyre)
    car.add_tyre(3, bl_tyre)
    car.add_tyre(4, br_tyre)
    tyre1 = car.front_left_tyre[0]
    tyre2 = car.front_right_tyre[0]
    tyre3 = car.back_left_tyre[0]
    tyre4 = car.back_right_tyre[0]

    assert tyre1 == fl_tyre

    assert tyre1.pressure == 120.05
    assert tyre1.tread_depth == 5.1
    