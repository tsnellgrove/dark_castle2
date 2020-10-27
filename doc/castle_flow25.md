*** Flask Flow Pseudo-Code Analysis ***
 
Note: For the sake of clarity many variables (e.g. 'version', 'max_score', dictionaries) are not tracked here

- RUNX=(<template>) [<variable assignment>]
	- define local variables => flask_output="" # these values should never be used; guard against undefined errors
	- if 'id' in session:
		- if POST:
			- if 'Submit': => user_input="<value>"
			- if 'Restart': pop 'id'
	- if 'id' not in session:
		- define session dictionary variables
		- define session non-dictionary variables
		- flash("WELCOME")
- if end_of_game == end_of_game:
	- set local variables => flask_output="GAME OVER"
	- flash("PRESS REPLAY")
- else call interpreter_text(): => flask_output="<value>"
- return render_template [<variable assignment>]

- RUN1=(Start Game) [id=<undefined>, user_input=<undefined>, end_of_game=<undefined>, flask_output=<undefined>]
	- define local variables => flask_output=""
	- if 'id' in session: SKIP
	- if 'id' not in session:
		- define session dictionary variables
		- define session non-dictionary variables => id="active", user_input="start of game", end_of_game=False
		- flash("WELCOME")
- if end_of_game == end_of_game: SKIP
- else call interpreter_text(): => flask_output="<intro text>"
- return render_template [id='active', user_input="start of game", end_of_game=False, flask_output="<intro text>"]

- RUN2=(First Move = "south") [id='active', user_input="start of game", end_of_game=False, flask_output=undefined]
	- define local variables => flask_output=""
	- if 'id' in session:
		- if POST:
			- if 'Submit': => user_input="south"
			- if 'Restart': SKIP
	- if 'id' not in session: SKIP
- if end_of_game == end_of_game: SKIP
- else call interpreter_text(): => flask_output="<south text>"
- return render_template [id='active', user_input="south", end_of_game=False, flask_output="<south text>"]

- RUN3=(Quit) [id='active', user_input="south", end_of_game=False, flask_output=<undefined>]
	- define local variables => flask_output="" # these values should never be used; guard against undefined errors
	- if 'id' in session:
		- if POST:
			- if 'Submit': => user_input="quit"
			- if 'Restart': SKIP
	- if 'id' not in session: SKIP
- if end_of_game == end_of_game: SKIP
- else call interpreter_text(): => flask_output="<quit text>"
- return render_template [id='active', user_input="quit", end_of_game=True, flask_output="<quit text>"]

- RUN4=(attempt post-quit move) [id='active', user_input="quit", end_of_game=True, flask_output=<undefined>]
	- define local variables => flask_output="" # these values should never be used; guard against undefined errors
	- if 'id' in session:
		- if POST:
			- if 'Submit': => user_input="north"
			- if 'Restart': SKIP
	- if 'id' not in session: SKIP
- if end_of_game == end_of_game:
	- set local variables => flask_output="GAME OVER"
	- flash("PRESS REPLAY")
- else call interpreter_text(): SKIP
- return render_template [id='active', user_input="north", end_of_game=True, flask_output="GAME OVER"]

- RUN5=(Restart) [id='active', user_input="north", end_of_game=True, flask_output=<undefined>]
	- define local variables => flask_output="" # these values should never be used; guard against undefined errors
	- if 'id' in session:
		- if POST:
			- if 'Submit': SKIP
			- if 'Restart': pop 'id'
	- if 'id' not in session:
		- define session dictionary variables
		- define session non-dictionary variables => id="active", user_input="start of game", end_of_game=False
		- flash("WELCOME")
- if end_of_game == end_of_game: SKIP
- else call interpreter_text(): => flask_output="<intro text>"
- return render_template [id='active', user_input="start of game", end_of_game=False, flask_output="<intro text>"]

