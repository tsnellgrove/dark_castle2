"""Castle Adventure 2.1.3 (complete)

This is a simple Zork-like text adventure game.
I am creating it in order to learn how to program in Python.

This is the front-end code

Written and programmed by Tom Snellgrove

Last update = August 1, 2020
"""

# *** Imports ***
# import random
# import math
# import textwrap
# import csv
# import io
# from contextlib import redirect_stdout
from dc2_interpreter import interpreter_text

# ************************
# --- DICTIONARIES & LISTS
# ************************

descript_updates_dict = {}

# --- Door Dictionary [Variable]
door_dict = {
    'front_gate': {
        'door_state': 'closed',
        'lock_state': 'locked',
        'key': 'rusty_key',
        'is_container': False
    },
    'iron_portcullis': {
        'door_state': 'closed',
        'lock_state': 'locked',
        'key': 'none',
        'is_container': False
    },
    'crystal_box': {
        'door_state': 'closed',
        'lock_state': 'locked',
        'key': 'silver_key',
        'is_container': True,
        'contains': ['scroll_of_the_king']
    }
}

# --- Switch Dictionary [Variable]
switch_dict = {

    # *** Control Panel ***

    'left_lever': {
        'state': 'down'
    },
    'middle_lever': {
        'state': 'down'
    },
    'right_lever': {
        'state': 'down'
    },
    'big_red_button': {
        'success_value': 0,
        'current_value': 0,
        'press_count': 0,
    }
}

# --- Room Dictionary [VARIABLE]
room_dict = {
    'entrance': {
        'features': ["front_gate"],
        'items': [],
        'view_only': ['dark_castle']
    },
    'main_hall': {
        'features': ['hedgehog', 'front_gate'],
        'items': ['shiny_sword'],
        'view_only': ['tapestries']
    },
    'antechamber': {
        'features': ['iron_portcullis', 'goblin', 'control_panel'],
        'items': [],
        'view_only': ['alcove', 'grimy_axe']
    },
    'throne_room': {
        'features': ['iron_portcullis', 'throne', 'crystal_box'],
        'items': [],
        'view_only': ['family_tree', 'stone_coffer']
    }
}

# --- Creature Dictionary [VARIABLE]
creature_dict = {
    'hedgehog': {
        'drops': [],
        'state': 'hungry_has_sword',
        'attack-fist-result': 'none',
        'attack-shiny_sword-result': 'creature_runs',
        'attack-grimy_axe-result': 'creature_runs'
    },
    'goblin': {
        'drops': ['grimy_axe', 'torn_note'],
        'state': 'guarding',
        'attack-fist-result': 'player_death',
        'attack-shiny_sword-result': 'creature_death'
    }
}

# --- State Dictionary [VARIABLE]
state_dict = {
    'room': 'entrance',
    'hand': ["nothing"],
    'worn': ['nothing'],
    'backpack': ['rusty_key', 'stale_biscuits'],
    'view_special': ['fist', 'burt', 'conscious'],
    'item_containers': {'scroll_of_the_king': 'crystal_box'},
    'max_count': {'broach_found': 1,},
    'move_counter': 0,
    'current_score': 0,
    'active_timer': 'none',
    'game_ending': 'unknown',
    'end_of_game': False,
    'score_dict': {
        'take-rusty_key': [0, 5],
        'main_hall': [0, 5],
        'take-shiny_sword': [0, 10],
        'attack-hedgehog': [0, -20],
        'attack-goblin': [0, 5],
        'push-big_red_button-success': [0, 10],
        'take-silver_key': [0, 5],
        'take-scroll_of_the_king': [0, 5],
        'examine-hedgehog_broach': [0, 5],
        'gator-crown': [0, 5],
        'wear-royal_crown': [0, 5],
        'read-illuminated_letters-win': [0, 15]
    },
    'timer_dict': {
        'drop-stale_biscuits': 0
    }
}

# *** Control Variable Assignment ***
start_of_game = True
end_of_game = False
output = ""

# ****************
# --- Main Routine
# ****************

# *** Get User Input ***
print("WELCOME TO DARK CASTLE!\n")
while end_of_game == False:
    if start_of_game:
        user_input = 'start of game'
        start_of_game = False
    else:
        user_input = input("> ").lower()
    end_of_game, output, room_dict, door_dict, switch_dict, \
        creature_dict, state_dict = interpreter_text(
        user_input, room_dict, door_dict, state_dict,
        creature_dict, switch_dict, descript_updates_dict)
    print(output, end = '')
print("THANKS FOR PLAYING!")
exit()


