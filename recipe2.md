# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a game player
I want to create a character with a cool name
So that other players recognise my character

As a game player
I want to see my characters health
So that I know when I might need to drink a health potion

As a game player
I want my character to be able to pick up items (potions/weapons) that they find in the game
So that they can use them when they need

As a game player
I want to be able to use my health potion item
So that my character's health goes back to 100

As a game player
I want to attack another character
So that they lose the health points associated with an attack by that weapon

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────────────────────────────┐
│ Character:                                         │
│   - name                                           │
│   - health: float                                  │
│   - inventory: Inventory                           │
│   Methods:                                         │
│   - add_item(item: Potion | Weapon)                │
│   - use_potion(potion: Potion)                     │
│   - attack(player: Character, weapon: Weapon)      │
│   - show_inventory()                               │
└───────────────────────┬────────────────────────────┘
                        │                             
┌───────────────────────▼────────────────────────────┐
│ Inventory:                                         │
│                                                    │
│                                                    │
│  - potions: [Potion]                               │
│  - weapons: [Weapon]                               │
│                                                    │
│                                                    │
│                                                    │
│                                                    │
└───┬──────────────────────────────┬─────────────────┘
    │                              │                  
┌───▼▼──────────────────┐    ┌─────▼─────────────────┐
│ Potion:               │    │ Weapon:               │
│                       │    │                       │
│   - name: str         │    │  - name: str          │
│   - healing_power:    │    │  - damage: float      │
│     float             │    │                       │
│                       │    │                       │
│                       │    │                       │
│                       │    │                       │
└───────────────────────┘    └───────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Character:
    # User-facing properties:
    #   inventory: object with items posessed by player
    #   name: name of character
    #   health: health of the player

    def __init__(self, name):
        pass # No code here yet

    def add_item(self, item: Potion | Weapon):
        # Parameters:
        #   item: an instance of either Potion or Weapon
        # Side-effects:
        #   Adds the item to the inventory object of the self object
        pass # No code here yet

    def use_potion(self, potion: Potion):
        # Parameters:
        #   potion: Potion
        # Returns:
        #   Nothing
        # Side-effects:
        #   Takes the value healing_power of the given potion and adds it to the self's health value.
        pass # No code here yet

    def attack(self, player: Character, weapon: Weapon):
        # Parameters:
        #   player: Character
        # Returns:
        #   Nothing
        # Side-effects:
        #   Takes the value: damage of the given weapon and subtracts it from the player's health value.
        pass

    def show_inventory(self):
        pass


class Potion:
    # User-facing properties:
    #   name: string
    #   healing_power: float

    def __init__(self, name, healing_power):
        # Parameters:
        #   name: string
        #   healing_power: float
        # Side-effects:
        #   Sets the name and healing_power of the self object
        pass # No code here yet

class Weapon:
    # User-facing properties:
    #   name: string
    #   damage: float

    def __init__(self, name, damage):
        # Parameters:
        #   name: string
        #   damage: float
        # Side-effects:
        #   Sets the name and damage of the self object
        pass # No code here yet


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a character
When we add an item
We see that item reflected in the inventory of the character
"""
player_1 = Character("Princess Leia")
player_2 = Character("Darth Vader")
weapon = Weapon("Light Saber", damage = 70.0)
potion = Potion("Leaf of Life", healing_power = 20.0)
player1.add_item(weapon)
player1.add_item(potion)
player1.show_inventory() =>

{
    weapons:[
        weapon1:{
            name: "Light Saber"
            damage: 70.0
        }
    ]
    potions:[
        potion1:{
            name: "Leaf of Life"
            healing_power: 20.0
        }
    ]
}


"""
Given a character has a health potion, and less than perfect health
When we use the potion after player1 gets wounded/damaged by other character/player2
We see the character's health improve by the healing_power amount
"""
player_1.health = 80
player_1.use_potion() #health starts at 100, potion helps go up by 20
assert player1.healthing_power == 100

"""
Given a character
When we make that character attack another with a weapon that they have,
We see that health decine of the attacked character by the damage amount
"""

player_1.attack(player_2, sword)
assert player_2.health == 80 #player1 would attack another character/player2 so their health will drop
assert player_1.health == 100 # player1 health starts at 100 after potion used


"""
Given a character with many items in their inventory
When we want to see all the items,
We see them all on calling show_invetory
"""
player_1.add_item(weapon)
player_1.add_item(potion)
assert len(player_1.inventory) == 2 #inventory which includes both weapon + potion
player1.inventory = player_1.show_inventory()
assert len(player_1.inventory) == 2 #inventory starts 



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a character
When we create a character 
We see the name and health and item inventory of the character
"""
player_1 = Character("Princess Leia")
player_1.name => #will return character's name
player_1.health =>  #will return 

"""
Given a potion
When we create a potion 
We see the name and healing_power of the potion in the object created
"""

"""
Given a weapon
When we create a weapon 
We see the name and damage of the weapon in the object created
"""

"""
Given an inventory
When we add items an inventory 
We see the list of potions and weapons in the inventory created
"""
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
