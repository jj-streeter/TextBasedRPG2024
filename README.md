# Project Overview:
This project is a command-line adventure RPG (Role-playing-game) set in an abandoned museum. It was created from August to December of 2024 for CSCI 3320 Data Structures at Univeristy of Nebraska at Omaha. The player explores connected rooms, examines the environment, talks with non-player characters, collects and uses items, and progresses through a questline by discovering how the museum's objects and secrets are connected. The objective was to design an interactive game while practicing object-oriented programming and implementing data structures such as graphs, binary trees, lists, and sets. While the project was considered completed as per the course's requirements, it is more accurate to call it a game demo rather than a full game, which would require futher development.

# Instructions for running:
1. Download or clone the TextBasedRPG2024 project
2. Run `main.py` in a terminal from the project folder
3. Enter a player name and confirm it when prompted
4. Enter `y` when asked if you want to venture forth
5. Enter commands when prompted to explore the museum
6. Enter `q` at any point to quit

# Commands:
- `talk <character>` or `t <character>`: Talk to a character in the current room
- `look room` or `l room`: Inspect the current room and reveal its items
- `look <object>` or `l <object>`: Examine a character or an item
- `move <direction>` or `m <direction>`: Move north, south, east, or west; the first letter of a direction can also be used
- `get <item>` or `g <item>`: Pick up an item from the current room
- `use <item>` or `u <item>`: Use an item in the inventory or current room
- `inventory` or `i`: Display the player's inventory
- `commands` or `c`: Display the command instructions in the game
- `quit` or `q`: Exit the game

Commands and arguments are not case sensitive. Items in a room must be revealed with `look room` before they can be examined or picked up.

# Topics and skills developed:
### Object-oriented programming
Created classes for rooms, characters, players, items, quests, and dialogue trees, then used objects to represent the game's changing state.
### Graph-based room navigation
Represented the museum as a graph of connected room objects. Each room stores its available exits and connections are created in both directions for movement through the map.
### Binary trees and recursive traversal
Implemented dialogue as a binary tree. Player choices select the left or right branch, while recursive methods add, remove, and update dialogue nodes as conversations progress.
### Lists, dictionaries, and sets
Used lists to store rooms, characters, items, and inventory contents; dictionaries to map commands and room connections; and a set to track rooms visited by the player.
### Item actions and state management
Created item actions that can change the game state, such as repairing the broken clock, opening the lock box, reading the old tome, and using the map.
### Quest conditions and progression
Implemented quest checkpoints with condition functions that check whether the player has visited a room, used an item, or obtained an item. Dialogue can trigger actions and advance the main questline.
