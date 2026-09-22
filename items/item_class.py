'''
Class Item is used to create items for the game. 
'''

import time

class Item:
    def __init__(self, name, description, location, static = False, use_func = None):
        self.name = name
        self.description = description
        self.location = location
        self.picked_up = False
        self.use_func = use_func
        self.static = static # static cannot be picked up
        self.been_used = False
        self.looked_at = False

    # use the item if it has a use function, and mark as used
    def use_item(self):
        self.use_func()
        self.been_used = True
        time.sleep(1)

    # look at the item and print its description
    def look_item(self):
        self.looked_at = True
        print("You look closely at the " + self.name)
        time.sleep(1)

        for line in self.description:
            print(line)
            time.sleep(1)