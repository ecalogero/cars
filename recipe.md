# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
 Car             │
│ - init      
 - CarID                     │
│ - fLTyre: Tyre                     │
│ - fRTyre: Tyre
 - bLTyre: Tyre
  - bRTyre: Tyre
  -TyreRecords
  -getTyreRecords()
    returns tyreRecords      
     │        │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Tyre   │
│             
 - TyreID            │
│ - currentPressure                 │
│ - currentTread_depth
 - updated date                
└─────────────────────────┘

TyreRecords

 - RecordID
 - TyreID
 - Updated_Date
 - pressure
 - tread-depth
```

_Also design the interface of each class in more detail._

```python

from enum import Enum

TyreType = Enum('TyreType', [('FL', 1), ('FR', 2), ('BL', 3), ('BR', 4)])

class Car:
    # User-facing properties:
    #   front_left_tyre: [instance of Tyre]
    #   front_right_tyre: [instance of Tyre]
    #   back_left_tyre: [instance of Tyre]
    #   back_right_tyre: instance of Tyre
    #   car_id

    def __init__(self, flTyre: Tyre, frTyre: Tyre, blTyre: Tyre, brTyre: Tyre):
        pass # No code here yet


    def add_tyre(self, type: TyreType, tyre: Tyre):
        # Parameters:
        #   type: TyreType
        #   tyre: Tyre
        #   Side-effects:
        #   Sets the tyre for each TyreType on the Car
        # Returns:
        #   Nothing
        pass # No code here yet

    def get_current_tyres(self)
        # Parameters: None
        # Side-effects: None
        # Returns:
        #   List of current tyres
        pass


class Tyre:
    # User-facing properties:
    #   pressure: float
    #   tread_depth: float
    #   tyre_id: int
    #   updated_date: datetime

    def __init__(self, pressure, tread_depth):
        # Parameters:
        #   pressure: float
        #   tread_depth: float
        # Side-effects:
        #   Sets the pressure and tread_depth properties
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a car
When we add tyres, they are set at 4 distinct positions
We see those tyres reflected in the tyre member variables
"""

fl_tyre = Tyre(120.05,5.1)
fr_tyre = Tyre(119.05,4.1)
bl_tyre = Tyre(118.5,4.8)
br_tyre = Tyre(115.05,3.1)

car = Car(fl_tyre, fr_tyre, bl_tyre, br_tyre)
tyre1 = car.front_left_tyre()
tyre2 = car.front_right_tyre()
tyre3 = car.back_left_tyre()
tyre4 = car.back_right_tyre()

assert tyre1[0] == fl_tyre


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

