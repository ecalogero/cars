from lib.car import *
from lib.tyre import *

fl_tyre = Tyre(120.05,5.1)
fr_tyre = Tyre(119.05,4.1)
bl_tyre = Tyre(118.5,4.8)
br_tyre = Tyre(115.05,3.1)

fl_tyre1 = Tyre(132.05,4.1)
fr_tyre1 = Tyre(128.05,3.1)
bl_tyre1 = Tyre(150.5,3.8)
br_tyre1 = Tyre(136.05,2.1)

def test_creating_a_car_w_tyres_works():

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
    assert tyre2 == fr_tyre
    assert tyre3 == bl_tyre
    assert tyre4 == br_tyre

    assert tyre1.pressure == 120.05
    assert tyre1.tread_depth == 5.1
    assert tyre2.pressure == 119.05
    assert tyre2.tread_depth == 4.1
    assert tyre3.pressure == 118.5
    assert tyre3.tread_depth == 4.8
    assert tyre4.pressure == 115.05
    assert tyre4.tread_depth == 3.1

def test_viewing_the_records_of_tyres_on_the_car():

    car = Car()
    
    car.add_tyre(1, fl_tyre)
    car.add_tyre(2, fr_tyre)
    car.add_tyre(3, bl_tyre)
    car.add_tyre(4, br_tyre)
    car.add_tyre(1, fl_tyre1)
    car.add_tyre(2, fr_tyre1)
    car.add_tyre(3, bl_tyre1)
    car.add_tyre(4, br_tyre1)

    assert car.show_all_tyres() == {
            "front_left_tyre":[
                {
                    "tyre":{
                        "pressure":"120.05",
                        "tread_depth":"5.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                },
                {
                    "tyre":{
                        "pressure":"119.05",
                        "tread_depth":"4.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                }
            ],
            "front_right_tyre":[
                {
                    "tyre":{
                        "pressure":"120.05",
                        "tread_depth":"5.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                },
                {
                    "tyre":{
                        "pressure":"119.05",
                        "tread_depth":"4.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                }
            ],
            "back_left_tyre":[
                {
                    "tyre":{
                        "pressure":"120.05",
                        "tread_depth":"5.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                },
                {
                    "tyre":{
                        "pressure":"119.05",
                        "tread_depth":"4.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                }
            ],
            "back_right_tyre":[
                {
                    "tyre":{
                        "pressure":"120.05",
                        "tread_depth":"5.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                },
                {
                    "tyre":{
                        "pressure":"119.05",
                        "tread_depth":"4.1",
                        "updated":"2026-08-5 11:30:00"
                    }
                }
            ]
    
    }



