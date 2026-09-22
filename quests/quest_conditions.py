'''contains boolean functions for evaluating quest advancement'''

from game_objects.characters import player

# returns True if the player has the item in their inventory
def item_in_inventory(item):
    return item in player.inventory

# returns True if the player has visited the room
def room_visited(room):
    return room.visited

# returns True if the player has used the item
def item_been_used(item):
    return item.been_used