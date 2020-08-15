"""Dark Castle 2.2.0 (candidate)

This is a simple Zork-like text adventure game.
I am creating it in order to learn how to program in Python.

This is the front-end code

Written and programmed by Tom Snellgrove

Last update = August 15, 2020
"""

# *** Imports ***
from dc22_interpreter import interpreter_text

# *** Flask Header ***
from flask import Flask, render_template, request, session, url_for, redirect, flash
from datetime import datetime, timedelta
#from processing import do_calculation

app = Flask(__name__)
app.config["SECRET_KEY"] = "qpueuwrhuqjfn;nWOREJsdf"
app.permanent_session_lifetime = timedelta(minutes = 120)

@app.route('/', methods=["GET", "POST"])

# ************************
# --- VARIABLE ASSIGNMENT
# ************************

# *** Flash Code ***
def index():

    # Initial falsh variable assignment
    if 'id' not in session:

        # *** Client-Sever Dictionary Variable Assignment ***

        session['descript_updates_dict'] = {}

        # --- Door Dictionary [Variable]
        session['door_dict'] = {
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
        session['switch_dict'] = {
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
        session['room_dict'] = {
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
        session['creature_dict'] = {
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
        session['state_dict'] = {
            'room': 'entrance',
            'hand': ["nothing"],
            'worn': ['nothing'],
            'backpack': ['rusty_key', 'stale_biscuits'],
            'view_special': ['fist', 'burt', 'conscience'],
            'item_containers': {'scroll_of_the_king': 'crystal_box'},
            'max_count': {'broach_found': 1},
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

        session['id'] = 'active'
#        session["game_over"] = False
#        session['player_command'] = "blank"
#        session['buffer_txt'] = ""
##        session['test_lst'] = []
#        session['restart'] = False
##        session["count"] = 0

        # *** Client-Sever Control Variable Assignment ***
        session['user_input'] = ""
#        session['user_input'] = "start of game"
        session['start_of_game'] = True
        session['end_of_game'] = False
        session['output'] = ""

        session.permanent = True

# ****************
# --- Main Routine
# ****************

        # post variable aissignment flask flash message for new session
#        flash(f"WELCOME TO DARK CASTLE - PLEASE ENTER A COMMAND", "info")

#    print(session['start_of_game'])


    if not session['start_of_game']:


#    elif request.method == "POST":
        if request.method == "POST":

            if request.form['submit_button'] == 'Submit':
                session['user_input'] = str(request.form['user_input']).lower()

            if request.form['submit_button'] == 'Restart':
#                session['restart'] = True
                session['start_of_game'] = True
#                session['user_input'] = "start of game"
                session.pop('id', None)
#            flash(f"WELCOME TO DARK CASTLE - PLEASE ENTER A COMMAND", "info")

            elif not session['end_of_game']:
                session['end_of_game'], session['output'], session['room_dict'], session['door_dict'], session['switch_dict'], session['creature_dict'], session['state_dict'] = interpreter_text(session['user_input'], session['room_dict'], session['door_dict'], session['state_dict'], session['creature_dict'], session['switch_dict'], session['descript_updates_dict'])
                session.modified = True

            else: # if session['game_over'] == True
                flash(f"THANKS FOR PLAYING! YOUR GAME HAS ENDED - PRESS 'RESTART' TO PLAY AGAIN", "info")

#    else:  # (if not POST must be GET)
#        if session['start_of_game']:
#                session['end_of_game'], session['output'], session['room_dict'], session['door_dict'], session['switch_dict'], session['creature_dict'], session['state_dict'] = interpreter_text(session['user_input'], session['room_dict'], session['door_dict'], session['state_dict'], session['creature_dict'], session['switch_dict'], session['descript_updates_dict'])
#                session['start_of_game'] = False
#                session.modified = True


    if session['start_of_game']:
        session['user_input'] = "start of game"
        session['end_of_game'], session['output'], session['room_dict'], session['door_dict'], session['switch_dict'], session['creature_dict'], session['state_dict'] = interpreter_text(session['user_input'], session['room_dict'], session['door_dict'], session['state_dict'], session['creature_dict'], session['switch_dict'], session['descript_updates_dict'])
        session['start_of_game'] = False
        session.modified = True
        flash(f"WELCOME TO DARK CASTLE - PLEASE ENTER A COMMAND", "info")
#            return render_template('index.html', output = session['output'])

#    if not session['restart']:
    return render_template('index.html', output = session['output'])

if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)



# *** Get User Input ***
#print("WELCOME TO DARK CASTLE!\n")
#while end_of_game is False:
#    if start_of_game:
#        user_input = 'start of game'
#        start_of_game = False
#    else:
#        user_input = input("> ").lower()
#    end_of_game, output, room_dict, door_dict, switch_dict, \
#        creature_dict, state_dict \
#        = interpreter_text(
#            user_input, room_dict, door_dict, state_dict,
#            creature_dict, switch_dict, descript_updates_dict)
#    print(output, end='')
#print("THANKS FOR PLAYING!")
#exit()


