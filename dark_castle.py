"""Castle Adventure 2.1.2 (candidate)

This is a simple Zork-like text adventure game.
I am creating it in order to learn how to program in Python.

Written and programmed by Tom Snellgrove

Last update = July 30, 2020
"""

# *** Imports ***
import random
import math
import textwrap
import csv
import io
from contextlib import redirect_stdout

# *********************
# --- SITUATIONAL LOGIC
# *********************


def switch_value(switch_key, switch_dict):
    # *** Upon pressing the big_red_button returns binary lever value ***

    if switch_key == 'push-big_red_button':
        temp_value = 0
        if switch_dict['left_lever']['state'] == 'up':
            temp_value += 4
        if switch_dict['middle_lever']['state'] == 'up':
            temp_value += 2
        if switch_dict['right_lever']['state'] == 'up':
            temp_value += 1
    return(temp_value)


def trigger(trigger_key, room_dict, description_dict,
            state_dict, static_dict, door_dict, creature_dict,
            descript_updates_dict):
    # *** Situational triggers and switch results ***

    room = state_dict['room']
    features = room_dict[room]['features']
    view_only = room_dict[room]['view_only']
    items = room_dict[room]['items']
    hand = state_dict['hand']
    if trigger_key in description_dict:
        trigger_descript = description_dict[trigger_key]

    # *** pre-action triggers - return value used ***
    if trigger_key == 'take-shiny_sword':
        if room == 'main_hall' and ('hedgehog' in features) \
                and ('stale_biscuits' not in view_only) \
                and ('shiny_sword' in items):
            printtw(trigger_descript)
            return(True)
        else:
            return(False)

    elif (trigger_key == 'east-blank') or (trigger_key == 'west-blank'):
        if room == 'entrance' and ('grimy_axe' in hand
                    or 'shiny_sword' in hand):
            if state_dict['score_dict']['gator-crown'][0] == 0:
                printtw(description_dict['east-blank-crown'])
                state_dict['backpack'].append('royal_crown')
                score('gator-crown', state_dict, static_dict)
                return(True)
            else:
                printtw(description_dict['east-blank-no_crown'])
                return(True)
        else:
            return(False)

    elif trigger_key in [
            'examine-control_panel', 'open-iron_portcullis',
            'examine-iron_portcullis', 'examine-grimy_axe', 'north-blank']:
        if room == 'antechamber' and 'goblin' in features \
                and 'shiny_sword' in state_dict['hand']:
            printtw(description_dict['goblin_attacks-parry'])
            return(True)
        elif room == 'antechamber' and 'goblin' in features \
                and 'shiny_sword' 'shiny_sword' not in hand:
            printtw(description_dict['goblin_attacks-death'])
            end(state_dict, static_dict, description_dict)
        else:
            return(False)

    # *** post-action triggers - return value discarded ***
    elif trigger_key == 'drop-stale_biscuits':
        if room == 'main_hall' and 'hedgehog' in features:
            room_dict[room]['items'].remove('stale_biscuits')
            room_dict[room]['view_only'].append('stale_biscuits')
            state_dict['active_timer'] = 'drop-stale_biscuits'
            state_dict['timer_dict']['drop-stale_biscuits'] = 5
            creature_dict['hedgehog']['state'] = 'hedgehog_eating'
            description_update(
                'hedgehog', 'hedgehog_eating', description_dict,
                descript_updates_dict)

    elif trigger_key == 'drop-shiny_sword':
        if room == 'main_hall' and 'hedgehog' in features \
                and state_dict['active_timer'] != 'drop-stale_biscuits':
            creature_dict['hedgehog']['state'] = 'hedgehog_fed_sword_returned'
            description_update(
                'hedgehog', 'hedgehog_fed_sword_returned', description_dict,
                descript_updates_dict)
            printtw(trigger_descript)
            room_dict[room]['items'].append('silver_key')

    elif trigger_key == 'attack-goblin':
        if room == 'antechamber' \
                and 'dead_goblin' in features:
            room_dict[room]['view_only'].extend(
                ['left_lever', 'middle_lever', 'right_lever', 'big_red_button']
                )

    elif trigger_key == 'pull-throne':
        if state_dict['max_count']['broach_found'] > 0:
            printtw(trigger_descript)
            room_dict[room]['items'].append('hedgehog_broach')
            state_dict['max_count']['broach_found'] -= 1

    elif trigger_key == 'push-throne':
        if state_dict['max_count']['broach_found'] > 0:
            printtw(trigger_descript)

    elif trigger_key == 'read-illuminated_letters':
        if room != 'throne_room':
            printtw(description_dict['read-illuminated_letters-wrong_room'])
        elif 'hedgehog' not in room_dict['main_hall']['features']:
            printtw(description_dict['read-illuminated_letters-no_hedgehog'])
        elif 'royal_crown' not in state_dict['worn']:
            printtw(description_dict['read-illuminated_letters-no_crown'])
        else:
            trigger_key = trigger_key + "-win"
            printtw(description_dict['read-illuminated_letters-win'])
            score(trigger_key, state_dict, static_dict)
            state_dict['game_ending'] = 'won'
            end(state_dict, static_dict, description_dict)


    elif trigger_key == 'push-big_red_button-success':
        if door_dict['iron_portcullis']['door_state'] == 'closed':
            door_dict['iron_portcullis']['door_state'] = 'open'
            printtw(description_dict['push-big_red_button-open'])
            descript_updates_dict['iron_portcullis'] = \
                description_dict['iron_portcullis-base'] + "open.\n"
        else:
            door_dict['iron_portcullis']['door_state'] = 'closed'
            printtw(description_dict['push-big_red_button-close'])
            descript_updates_dict['iron_portcullis'] = \
                description_dict['iron_portcullis-base'] + "closed.\n"

    return(False)


def timer(room_dict, state_dict, description_dict, descript_updates_dict):
    # *** Timer conditionals ***

    timer_key = state_dict['active_timer']
    room = state_dict['room']

    if timer_key == 'drop-stale_biscuits':

        features = room_dict['main_hall']['features']
        items = room_dict['main_hall']['items']
        timer_num = state_dict['timer_dict']['drop-stale_biscuits']

        # *** If the hedgehog no longer exists (i.e. attacked by player), ***
        # *** reset timer_value to 0 and set active_timer to none ***
        # *** and remove 'stale_biscuits' from 'view_only' ***
        if 'hedgehog' not in features:
            state_dict['timer_dict']['drop-stale_biscuits'] = 0
            state_dict['active_timer'] = 'none'
            room_dict['main_hall']['view_only'].remove('stale_biscuits')
            return

        # *** If hedgehog exist and room == main_hall print description ***
        if room == 'main_hall':
            printtw(description_dict[timer_key + "-timer_" + str(timer_num)])

        # *** decrement timer ***
        timer_num -= 1
        state_dict['timer_dict']['drop-stale_biscuits'] = timer_num

        # *** if timer == 0 reset 'active_timer' & remove 'stale_biscuits' ***
        if timer_num == 0:
            state_dict['active_timer'] = 'none'
            room_dict['main_hall']['view_only'].remove('stale_biscuits')

            # *** update hedgehog state & description based on shiny_sword ***
            if 'shiny_sword' in items:
                creature_dict['hedgehog']['state'] = 'fed_sword_returned'
                description_update(
                    'hedgehog', 'hedgehog_fed_sword_not_taken',
                    description_dict, descript_updates_dict)
            else:
                creature_dict['hedgehog']['state'] = 'fed_sword_taken'
                description_update(
                    'hedgehog', 'hedgehog_fed_sword_taken',
                    description_dict, descript_updates_dict)

        return

# *******************
# --- HELPER ROUTINES
# *******************

def printtw(txt_str):

    global output

    txt_lst = []
    txt_lst = txt_str.split("\n")

    for paragraph in txt_lst:
        wrapper = textwrap.TextWrapper(width=80,break_long_words=False)
        word_list = wrapper.wrap(text=paragraph) 

        with io.StringIO() as buffer, redirect_stdout(buffer):
            for element in word_list:
                print(element)
            print()
            output = output + buffer.getvalue()
#    print(output)

    return


def unknown_word():
    response = random.randint(0, 4)
    printtw(static_dict['unknown_word_lst'][response])
    state_dict['move_counter'] -= 1
    return


def look(room_dict, state_dict, description_dict, static_dict):

    room = state_dict['room']
    features = room_dict[room]['features']
    items = room_dict[room]['items']
    score_key = room

    if room in descript_updates_dict:
        printtw(descript_updates_dict[room])
    else:
        printtw(description_dict[room])
    if len(features) > 0:
        for feature in features:
            printtw("There is a " + feature + " here.\n")
    if len(items) > 0:
        printtw("The following items are here: " + ", ".join(items))
    if score_key in state_dict['score_dict']:
        score(score_key, state_dict, static_dict)
    return


def str_to_lst(user_input):
    lst = []
    lst.append(user_input)
    return(lst[0].split())


def description_update(description_key, update_key, description_dict, descript_updates_dict):
    descript_updates_dict[description_key] = description_dict[update_key]
#    description_dict[description_key] = description_dict[update_key]
    return


def print_score(state_dict, static_dict):

    current_score = state_dict['current_score']
    max_score = static_dict['global_dict']['max_score']

    printtw("Your score is now " + str(current_score)
        + " out of " + str(max_score) + "\n")	
    return


def end(state_dict, static_dict, description_dict):

    score = state_dict['current_score']
    moves = state_dict['move_counter']
    game_ending = state_dict['game_ending']

    if score < 0:
        title_score = -10
    elif score == 0:
        title_score = 0
    else:
        title_score = math.ceil(score / 10) * 10
    title = static_dict['titles_dict'][title_score]

    if game_ending == 'death':
        printtw("You have died.\n")
    elif game_ending == 'quit':
        printtw("You have quit.\n")
    elif game_ending == 'won':
        printtw("You have won!\n")
    printtw("Your adventure ended after " + str(moves) + " moves.\n")
    print_score(state_dict, static_dict)
    printtw("Your title is: " + title + "\n")
    if game_ending == 'won':
        printtw(description_dict['credits'])
    state_dict['end_of_game'] = True
    return


def room_action(
        path_key, state_dict, static_dict, path_dict, room_dict,
        description_dict):

    action = path_dict[path_key]['action']
    door_name = path_dict[path_key]['door']
    next_room = path_dict[path_key]['next_room']

    if action == "death":
        state_dict['game_ending'] = 'death'
        end(state_dict, static_dict, description_dict)
    elif action == "door":
        door_state = door_dict[door_name]['door_state']
        if door_state == 'open':
            state_dict['room'] = next_room
            look(room_dict, state_dict, description_dict, static_dict)
        else:
            printtw("The " + door_name + " is closed.\n")
    elif action == "passage":
        state_dict['room'] = next_room
        look(room_dict, state_dict, description_dict, static_dict)
    return


# *** Score is called from look(), 'take', 'attack', and a few other spots ***
def score(score_key, state_dict, static_dict):

    score_event_count = state_dict['score_dict'][score_key][0]
    score_event_value = state_dict['score_dict'][score_key][1]

    if score_event_count == 0:
        state_dict['current_score'] += score_event_value
        print_score(state_dict, static_dict)
    score_event_count += 1
    state_dict['score_dict'][score_key][0] = score_event_count
    return


# ********************
# --- TEXT INTERPRETER
# ********************


def interpreter_text(
        user_input, path_dict, room_dict,
        door_dict, state_dict, allowed_lang_dict, creature_dict,
        switch_dict, static_dict, descript_updates_dict):


### Stack Overflow 1
#old_stdout = sys.stdout
#sys.stdout = mystdout = StringIO()

### blah blah lots of code ...

#sys.stdout = old_stdout

### Stack Overflow 2
#import io
#from contextlib import redirect_stdout

#with io.StringIO() as buf, redirect_stdout(buf):
#    print('redirected')
#    output = buf.getvalue()


### Stack Overflow 3
#import io
#import sys

#real_stdout = sys.stdout
#fake_stdout = io.BytesIO()   # or perhaps io.StringIO()
#try:
    #sys.stdout = fake_stdout
    ### do what you have to do to create some output
#finally:
    #sys.stdout = real_stdout
    #output_string = fake_stdout.getvalue()
    #fake_stdout.close()
    ### do what you want with the output_string


# *** Global Variable Declaration ***
    global output
    output = ""

# *** Load Description Dictionary ***
    file = open('description.csv', 'r', newline='')
    description_dict = {}
    with file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            val = row[1].replace('\\n', '\n')
            description_dict[key] = val

    # *** local variables ***
    allowed_verbs = allowed_lang_dict['allowed_verbs']
    allowed_movement = allowed_lang_dict['allowed_movement']
    room = state_dict['room']
    room_items = room_dict[room]['items']
    room_features = room_dict[room]['features']
    room_view_only = room_dict[room]['view_only']
    view_special = state_dict['view_special']
    hand = state_dict['hand']
    backpack = state_dict['backpack']
    worn = state_dict['worn']
    post_action_trigger = static_dict['post_action_trigger_lst']

# *** Start of Game Welcome Text and Variable Assignment ***
    if user_input == 'start of game':
        printtw(description_dict['intro'])
        printtw(description_dict['help'])
        look(room_dict, state_dict, description_dict, static_dict)
        portcullis_code = random.randint(0, 7)
        switch_dict['big_red_button']['success_value'] = portcullis_code
        port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
        descript_updates_dict['messy_handwriting-read'] = port_code_txt
        return state_dict['end_of_game'], output

# *** Convert User Input to single word strings ***

    user_input_lst = str_to_lst(user_input)

    word1 = user_input_lst[0]
    if len(user_input_lst) > 1:
        word2 = user_input_lst[1]
    else:
        word2 = "blank"

    print("")

    if (word1 in allowed_verbs) and (len(user_input_lst) == 1):
        printtw(word1 + " what Burt?")
        return state_dict['end_of_game'], output

    score_key = word1 + "-" + word2
    trigger_key = score_key
    switch_key = score_key
    path_key = room + "-" + word1
    state_dict['move_counter'] += 1

    if trigger_key in static_dict['pre_action_trigger_lst']:
        if trigger(
                trigger_key, room_dict, description_dict,
                state_dict, static_dict, door_dict, creature_dict,
                descript_updates_dict):
            return state_dict['end_of_game'], output


# --- Handle One Word Commands

    if word1 == "help":
        printtw(description_dict['help'])

    elif word1 == "look":
        look(room_dict, state_dict, description_dict, static_dict)

    elif word1 == "score":
        print_score(state_dict, static_dict)


    elif word1 == "inventory":
        printtw("In your hand you have: " + hand[0])
        backpack_inv = ', '.join(backpack)
        printtw("In your backpack you have: " + backpack_inv)
        worn_inv = ', '.join(worn)
        printtw("You are wearing: " + worn_inv)

    elif word1 == "credits":
        printtw(description_dict['credits'])

    elif user_input == "quit":
        printtw("Goodbye Burt!\n")
        state_dict['game_ending'] = 'quit'
        state_dict['move_counter'] -= 1
        end(state_dict, static_dict, description_dict)

    elif word1 in allowed_movement:
        if (path_key) in path_dict:
            printtw(description_dict[path_key])
            room_action(
                path_key, state_dict, static_dict, path_dict, room_dict,
                description_dict)
        else:
            response = random.randint(0, 4)
            printtw(static_dict['invalid_path_lst'][response])

# *** Handle Two Word Commands ***

# --- Examine verb

    elif word1 == "examine":
        visible_items = (hand + backpack + room_items + room_features
            + room_view_only + worn + view_special)
        visible_items.append(room)

        if word2 not in visible_items:
            printtw("Burt you can't " + word1 + " that!\n")
        else:
            if word2 in descript_updates_dict:
                printtw(descript_updates_dict[word2])
            else:
                printtw(description_dict[word2])
            if word2 in allowed_lang_dict['is_container']:
                if door_dict[word2]['door_state'] == 'open':
                    contain_inv = ', '.join(door_dict[word2]['contains'])
                    printtw("The " + word2 + " contains a "
                        + contain_inv + ".\n")

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- Take verb

    elif word1 == "take":
        takeable_items = backpack + room_items + worn

        if word2 not in takeable_items or word2 == "nothing":
            printtw("Burt you can't " + word1 + " that!\n")
        else:
            # *** new item=>hand; old hand item=>backpack (except 'nothing')***
            temp_swap = hand[0]
            del hand[0]
            hand.append(word2)
            state_dict['hand'] = hand
            if temp_swap != "nothing":
                backpack.append(temp_swap)

            # *** remove taken item from source lst (backpack, room, worn) ***
            if word2 in backpack:
                backpack.remove(word2)
            elif word2 in worn:
                worn.remove(word2)
            else:
                room_items.remove(word2)
                room_dict[room]['room_items'] = room_items
                # *** Container Cases (open containers dump into room_items)***
                if word2 in state_dict['item_containers']:
                    container = state_dict['item_containers'][word2]
                    door_dict[container]['contains'].remove(word2)
                    if len(door_dict[container]['contains']) == 0:
                        door_dict[container]['contains'].append('nothing')
                    del state_dict['item_containers'][word2]
            printtw("Taken\n") # confirm to play that item has been taken

            # *** if the backpack is now empty add placeholder "nothing" ***
            if len(backpack) == 0:
                backpack.append("nothing")
            # *** ensure we don't get multiple "nothing" in backpack ***
            if len(backpack) > 1 and "nothing" in backpack:
                backpack.remove("nothing")
            # *** if worn is now empty add the placeholder "nothing" to it ***
            if len(worn) == 0:
                worn.append("nothing")
                printtw(description_dict[score_key + '-worn']) # worn removal txt
            # *** ensure we don't get multiple "nothing" in worn ***
            if len(worn) > 1 and "nothing" in backpack:
                worn.remove("nothing")
            
            state_dict['backpack'] = backpack
            state_dict['worn'] = worn

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- Drop verb

    elif word1 == "drop":
        droppable_items = hand
        
        if word2 not in droppable_items or word2 == "nothing":
            printtw("Burt you can't " + word1 + " that!\n")
        else:
            temp_swap = hand[0]
            del hand[0]
            hand.append("nothing")
            state_dict['hand'] = hand
            room_items.append(temp_swap)
            room_dict[room]['room_items'] = room_items
            printtw("Dropped\n")

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- Open verb

    elif word1 == "open":
        if word2 not in allowed_lang_dict['can_be_opened']:
            printtw("Burt you can't " + word1 + " that!\n")
        else:
            door_state = door_dict[word2]['door_state']
            lock_state = door_dict[word2]['lock_state']

            if word2 not in room_features:
                printtw("Burt, you can't see a " + word2 + " here!\n")
            elif door_state == 'open':
                printtw("Burt, the " + word2 + " is already open!\n")
            elif lock_state == 'locked':
                printtw("The " + word2 + " is locked.\n")
            else:
                printtw("Opened\n")
                door_state = 'open'
                door_dict[word2]['door_state'] = door_state
                descript_updates_dict[word2] = description_dict[word2 + '-base'] \
                    + door_state + ".\n"
                if door_dict[word2]['is_container']:
                    contain_inv = ', '.join(door_dict[word2]['contains'])
                    printtw("The " + word2 + " contains a "
                        + contain_inv + ".\n")
                    room_dict[room]['items'].extend(
                        door_dict[word2]['contains'])

                if trigger_key in post_action_trigger:
                    trigger(
                        trigger_key, room_dict, description_dict,
                        state_dict, static_dict, door_dict, creature_dict,
                        descript_updates_dict)

                if score_key in state_dict['score_dict']:
                    score(score_key, state_dict, static_dict)

# --- Unlock verb

    elif word1 == "unlock":
        if word2 not in allowed_lang_dict['can_be_opened']:
            printtw("Burt you can't " + word1 + " that!")
        else:
            door_state = door_dict[word2]['door_state']
            lock_state = door_dict[word2]['lock_state']

            if word2 not in room_features:
                printtw("Burt, you can't see a " + word2 + " here!\n")
            elif door_state == 'open':
                printtw("Burt, the " + word2 + " is already open!\n")
            elif lock_state == 'unlocked':
                printtw("The " + word2 + " is already unlocked.\n")
            elif hand[0] != door_dict[word2]['key']:
                printtw("Burt, you don't have the key in your hand!\n")
            else:
                printtw("Unlocked\n")
                door_dict[word2]['lock_state'] = 'unlocked'

                if trigger_key in post_action_trigger:
                    trigger(
                        trigger_key, room_dict, description_dict,
                        state_dict, static_dict, door_dict, creature_dict,
                        descript_updates_dict)

                if score_key in state_dict['score_dict']:
                    score(score_key, state_dict, static_dict)

# --- read verb

    elif word1 == "read":
        visible_items = (hand + backpack + worn + room_items + room_features
            + room_view_only)

        if word2 not in allowed_lang_dict['can_be_read']:
            printtw("Burt you can't " + word1 + " that!\n")
        elif static_dict['written_on_dict'][word2] not in visible_items:
            printtw("Burt, you can't read what you can't see!\n")
        else:
            if (word2 + "-read") in descript_updates_dict:
                printtw(descript_updates_dict[word2 + "-read"])
            else:
                printtw(description_dict[word2 + "-read"])

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- attack verb

    elif word1 == "attack":
        if word2 not in allowed_lang_dict['can_be_attacked'] \
                or word2 not in room_features:
            printtw("Burt you can't " + word1 + " that!\n")
        else:
            if hand[0] not in allowed_lang_dict['weapons']:
                weapon = 'fist'
            else:
                weapon = hand[0]

            attack_weapon = word1 + "-" + weapon
            attack_result = attack_weapon + "-" + 'result'
            attack_description = word2 + "-" + attack_weapon
            if attack_description in descript_updates_dict:
                printtw(descript_updates_dict[attack_description])
            else:
                printtw(description_dict[attack_description])

            if creature_dict[word2][attack_result] == 'creature_death':
                room_dict[room]['features'].remove(word2)
                room_dict[room]['features'].append('dead_' + word2)
                printtw("the " + word2 + " has died.\n")
                if score_key in state_dict['score_dict']:
                    score(score_key, state_dict, static_dict)
                room_dict[room]['items'].extend(creature_dict[word2]['drops'])

            elif creature_dict[word2][attack_result] == 'creature_runs':
                room_dict[room]['features'].remove(word2)
                printtw("the " + word2 + " has run away.\n")
                if score_key in state_dict['score_dict']:
                    score(score_key, state_dict, static_dict)

            elif creature_dict[word2][attack_result] == 'player_death':
                state_dict['game_ending'] = 'death'
                end(state_dict, static_dict, description_dict)  # print_score() called by end()

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

# --- eat verb

    elif word1 == "eat":
        if word2 not in allowed_lang_dict['can_be_eaten_lst']:
            printtw("Burt you can't " + word1 + " that!\n")
        elif word2 not in hand:
            printtw("Burt you can't eat something that's not in your hand!")
        else:
            if word2 in descript_updates_dict:
                printtw(descript_updates_dict[word2 + "-eat"])
            else:
                printtw(description_dict[word2 + "-eat"])

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- Pull verb

    elif word1 == 'pull':
        if word2 not in allowed_lang_dict['can_be_pulled_lst']:
            printtw("Burt you can't " + word1 + " that!\n")
        elif (word2 not in room_view_only) and (word2 not in room_features):
            printtw("Burt, you can't pull what you can't see!")
        else:
            printtw("Pulled.\n")

            if word2 in switch_dict:
                switch_state = switch_dict[word2]['state']
                if switch_state == 'down':
                    switch_state = 'up'
                else:
                    switch_state = 'down'
                descript_updates_dict[word2] = "The " + word2 + " is " \
                    + switch_state + ".\n"
                switch_dict[word2]['state'] = switch_state

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- Push verb

    elif word1 == 'push':
        if word2 not in allowed_lang_dict['can_be_pushed_lst']:
            printtw("Burt you can't " + word1 + " that!\n")
        elif (word2 not in room_view_only) and (word2 not in room_features):
            printtw("Burt, you can't push what you can't see!")
        else:
            printtw("Pushed.\n")

            if word2 in switch_dict:
                success_num = switch_dict[word2]['success_value']
                switch_num = switch_value(switch_key, switch_dict)
                switch_dict[word2]['press_count'] += 1
                if success_num == switch_num:
                    trigger_key = trigger_key + '-success'
                    score_key = trigger_key
                else:
                    printtw(description_dict[word1 + "-" + word2 + '-fail'])

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

# --- Wear verb

    elif word1 == "wear":
        if word2 == "nothing" or word2 not in allowed_lang_dict['can_be_worn']:
            printtw("Burt you can't " + word1 + " that!\n")
        elif word2 not in hand:
            printtw("Burt, you're not holding the " + word2 + "!\n")
        else:
            # *** wear the taken item ***
            worn.append(word2)
            if len(worn) > 1 and "nothing" in worn:
                worn.remove("nothing")
            state_dict['worn'] = worn

            # *** clean up hand ***
            if word2 in hand:
                hand.remove(word2)
            if len(hand) == 0:
                hand.append("nothing")
            state_dict['hand'] = hand

            # *** confirm worn and print effect ***
            printtw("Worn\n")
            printtw(description_dict[score_key])

            if trigger_key in post_action_trigger:
                trigger(
                    trigger_key, room_dict, description_dict,
                    state_dict, static_dict, door_dict, creature_dict,
                    descript_updates_dict)

            if score_key in state_dict['score_dict']:
                score(score_key, state_dict, static_dict)

    else:
        unknown_word()

    if state_dict['active_timer'] != 'none':
        timer(room_dict, state_dict, description_dict, descript_updates_dict)

    return state_dict['end_of_game'], output


# ************************
# --- DICTIONARIES & LISTS
# ************************

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

# --- Path Description Dictionary [STATIC]
path_dict = {
    'entrance-north': {
        'action': 'door',
        'door': 'front_gate',
        'next_room': 'main_hall'
    },
    'entrance-south': {
        'action': 'none',
        'door': 'none',
        'next_room': 'none'
    },
    'entrance-east': {
        'action': 'death',
        'door': 'none',
        'next_room': 'none'
    },
    'entrance-west': {
        'action': 'death',
        'door': 'none',
        'next_room': 'none'
    },
    'main_hall-north': {
        'action': 'passage',
        'door': 'none',
        'next_room': 'antechamber'
    },
    'main_hall-south': {
        'action': 'door',
        'door': 'front_gate',
        'next_room': 'entrance'
    },
    'antechamber-north': {
        'action': 'door',
        'door': 'iron_portcullis',
        'next_room': 'throne_room'
    },
    'antechamber-south': {
        'action': 'passage',
        'door': 'none',
        'next_room': 'main_hall'
    },
    'throne_room-south': {
        'action': 'door',
        'door': 'iron_portcullis',
        'next_room': 'antechamber'
    },
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

# --- Static Dictionary [STATIC]
static_dict = {
    'global_dict': {
        'max_score': 75
    },
    'invalid_path_lst': [
        "Ouch! You have walked into a wall.\n",
        "Ouch! Burt, stop walking into walls!\n",
        "You can't go that way.\n",
        "And exactly how do you propose to do that?\n",
        "There's no exit that way.\n"
    ],
    'pre_action_trigger_lst': [
        'take-shiny_sword',
        'examine-control_panel',
        'open-iron_portcullis',
        'examine-iron_portcullis',
        'examine-grimy_axe',
        'north-blank',
        'east-blank',
        'west-blank'
    ],
    'post_action_trigger_lst': [
        'drop-stale_biscuits',
        'attack-goblin',
        'drop-shiny_sword',
        'push-big_red_button-success',
        'pull-throne',
        'push-throne',
        'read-illuminated_letters'
    ],
    'written_on_dict': {
        'rusty_lettering': 'front_gate',
        'trademark': "stale_biscuits",
        'dwarven_runes': 'shiny_sword',
        'messy_handwriting': 'torn_note',
        'calligraphy': 'crystal_box',
        'illuminated_letters': 'scroll_of_the_king'
    },
    'unknown_word_lst': [
        "Burt, I have no idea what you're talking about!\n",
        "Burt, are you babbling again?\n",
        "Burt, I'm just going to pretend I didn't hear that\n",
        "Burt, you've said some strange things over the years but "
        "that was a doosey!\n",
        "Burt! What would your mother say if she heard you speaking like that!?\n"
    ],
    'food_dict': {
        'stale_biscuits': 'none'
    }, #  to be used to track food results
    'titles_dict': {
        -10: 'Burt the Best Forgotten',
        0: 'Burt the Boneheaded',
        10: 'Burt the Beginner',
        20: 'Burt the Better Than Average',
        30: 'Burt the Brawny',
        40: 'Burt the Brainy',
        50: 'Burt the Benevolent',
        60: 'Burt the Breathtaking',
        70: 'Burt the Bodacious',
        80: 'Burt the Bold, Barron of Bright Castle'
    }
}

# --- Allowed Language Dictionary [STATIC]
allowed_lang_dict = {
    'allowed_movement': ["north", "south", "east", "west"],
    'allowed_verbs': [
        "examine", "take", "attack", "drop", "open", "unlock",
        'read', 'eat', 'pull', 'push', 'wear'],  # 2-word verbs
    'can_be_opened': ['front_gate', 'iron_portcullis', 'crystal_box'],
    'can_be_read': [
        'rusty_lettering', 'trademark', 'dwarven_runes',
        'messy_handwriting', 'calligraphy', 'illuminated_letters'],
    'can_be_attacked': ['hedgehog', 'goblin'],
    'weapons': ['shiny_sword', 'grimy_axe'],
    'can_be_eaten_lst': ['stale_biscuits'],
    'can_be_pulled_lst': [
        'left_lever', 'middle_lever', 'right_lever', 'throne'],
    'can_be_pushed_lst': ['big_red_button', 'throne'],
    'is_container': ['crystal_box'],
    'can_be_worn': ['royal_crown']   # not broach; causes player confusion
}

# ****************
# --- Main Routine
# ****************

# *** Variable Assignment ***
descript_updates_dict = {}
start_of_game = True
end_of_game = False

# *** Get User Input ***
print("WELCOME TO DARK CASTLE!\n")
while end_of_game == False:
    if start_of_game:
        user_input = 'start of game'
        start_of_game = False
    else:
        user_input = input("> ").lower()
    end_of_game, output = interpreter_text(
        user_input, path_dict, room_dict,
        door_dict, state_dict, allowed_lang_dict, creature_dict,
        switch_dict, static_dict, descript_updates_dict)
    print(output)
print("THANKS FOR PLAYING!")
exit()

