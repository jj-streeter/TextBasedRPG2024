'''
game.py holds the gameloop
'''

import time
from game_objects import rooms, characters, items
from main.commands import talk, look, move, use, inventory, get, commands

def run_game():

    # library mapping valid command strings to command
    valid_commands = {"talk": talk,
                      "t": talk,
                      "look": look,
                      "l": look,
                      "move": move,
                      "m": move,
                      "quit": quit,
                      "q": quit,
                      "inventory": inventory,
                      "i": inventory,
                      "use": use,
                      "u": use,
                      "get": get,
                      "g": get,
                      "commands": commands,
                      "c": commands
                    }

    # Print game intro text
    start_game = input("Venture forth? (y/n) ").strip().casefold()
    while start_game not in ['y', 'n']:
        start_game = input("Venture forth? (y/n) ").strip().casefold()
    if start_game == "n":
        print("You decide to turn back, yet can't help but wonder what mysteries could be found inside...")
        time.sleep(0.5)
        quit_game = True
    elif start_game == "y":
        quit_game = False
        print("You open the door and step inside...")
        time.sleep(1)
    
    # game loop
    quit_game = False
    while quit_game == False:

        # description of the current room
        print(characters.player.location.main_description)
        time.sleep(1)

        # characters in the current room
        characters.player.location.print_all_characters() 
        time.sleep(1)

        # valid exits in current room
        characters.player.location.print_viable_moves()
        time.sleep(1)
        
        # prompts user for an action
        print("Valid commands: talk (t), look (l), move (m), use (u), get (g), inventory (i), commands (c), quit (q)")
        time.sleep(1)
        player_action = input("What would you like to do? ").strip().casefold()

        # split compound commands (ex "move north" into ["move", "north"])
        # make at most one split
        command_parts = player_action.split(maxsplit=1)
        main_command = command_parts[0]

        # if player action is not a valid command, continue asking for a command
        while main_command not in valid_commands:
            print("'" + player_action + "' is not a recognized command.")
            time.sleep(1)
            print("Valid commands: talk (t), look (l), move (m), use (u), get (g), inventory (i), commands (c), quit (q)")
            time.sleep(1)
            player_action = input("What would you like to do? ").strip().casefold()

            command_parts = player_action.split(maxsplit=1)
            main_command = command_parts[0]
        
        # set command argument if compound
        argument = command_parts[1] if len(command_parts) > 1 else None

        # handle commands
        if main_command in ["quit", "q"]:
            quit_game = True

        else:
            # MOVE
            if main_command in ["move", "m"]:
                if not argument:
                    argument = input("Which direction do you want to move? ").strip().casefold()
                valid_commands[main_command](characters.player, characters.player.location, argument)

            # TALK    
            elif main_command in ["talk", "t"]:
                if len(characters.player.location.characters) > 0:
                    if not argument:
                        argument = input("Who do you want to talk to? ").strip().casefold()
                    valid_commands[main_command](characters.player.location, argument)

                else:
                    print("There is no one here to talk to.")
                    time.sleep(1)

            # LOOK
            elif main_command in ["look", "l"]:
                if not argument:
                    argument = input("What do you want to look at? ").strip().casefold()
                valid_commands[main_command](characters.player, characters.player.location, argument)

            # USE (ITEM)
            elif main_command in ["use", "u"]:
                if not argument:
                    argument = input("What do you want to use? ").strip().casefold()
                valid_commands[main_command](characters.player, characters.player.location, argument)
            
            # GET (ITEM)
            elif main_command in ["get", "g"]:
                if not argument:
                    argument = input("What do you want to pick up? ").strip().casefold()
                valid_commands[main_command](characters.player, characters.player.location, argument)

            # COMMANDS (HOW-TO)
            elif main_command in ["commands", "c"]:
                valid_commands[main_command]()

            # INVENTORY
            else:
                valid_commands[main_command](characters.player)