+++ To Dos +++


*** Future Versions and Features ***

2.1.x - functionalize darkcastle into a client-server app
	- 2.1.0 - decice on repo strat: fork?, branch?, new repo?
			- July 13: Reading up on Git branching - sounds like tags will be helpful - more research to do
			- July 14: Read up on app versioning - I need to get more consistent about this
			- Less clear is coding across platforms... it's beginning to look like there's no one simple solution to this
			- I will need to roll my own
			- Maybe start by functionalizing Dark Castle and make that version work at the command line
			- decision = new repo
	- 2.1.1 - move timer, quit, one-time variable assignment, create updated descript dict, and description.csv load to interpreter_text
			- Took the plunge today - just decided that	I needed to get started - copied DC files into dark_castle2 - will use a separate repo
			- Updated docs
			- Moved start-of-game text to interpreter_txt
			- Created descript_updates_dict
			- Added messy_handwriting_read to descript_updates_dict
			- updated read and examine ifel to read first from descript_updates_dict
			- updated "-base" description updates in 'push' and 'trigger'
			- changed description_updates() (hedgehog description updates called from trigger & timer) to write to descript_updates_dict
			- description_dict load and timer moved to interpreter_txt; not fully functional!
			- move quit routine into interpreter_txt
			- solve issues with end() 
			- moved big_red_button success_code variable assignment to interpreter_txt; fixed pull description assignment
			- full playthrough and some minor text tweaks; started stdout redirect research
	-2.1.2 - redirect interpreter_txt stdout to string, return string to dark_castle2, and print string from main routine
			- redirected stdout in printtw; getting repeat prints due to print within function
			- return 'output' from interpet_txt and print from main routine
			- convert all print() commands to printtw()
			- troubleshoot all print spacing
	-2.1.3 - client-server deployment
			- DONE: separated dark-castle into front-end and back-end routines!
			- DONE: successful win play-through test
			- DONE: reduce imports for main where possible
			- DONE: full play-through test
	-2.1.4 - final clean-up pre flaskify
			- DONE: version feature
			- DONE: additional puzzle clues
					- DONE: call the crown 'royal_crown' in Nana's memory
					- DONE: Indicate in the grimy_axe description that it could kill a crocodile
						- 'small_print' = 'ACME AXE: Effective at dispatching small dragons, large crocidiles, and even the most agressive of trees.'
			- improved error messages
				- DONE: drop from hand only (see 'eat' or 'wear')
				- DONE: can only read text - not the item containing text
				- DONE: On attempt to 'wear hedgehog_broach' - "You can't bring yourself to put it on - the memories of seeing your dear Nana wearing it are suddenly too fresh. Perahps there is something else around the castle you could wear?"
					- pre-action trigger not working
					- problem solved - was treating 'hand' as a string when it's actually a list (argh!!)
				- DONE: style check
				- DONE: full play-through test
	-2.2.x - flaskify client-server app
		-2.2.0 - basic 'wiring' for flaskification
			- DONE: Copy static and template directories into repo
			- DONE: Create copies of client & server app in repo
			- DONE: Update import statement in main and pefrom basic functionality test
			- DONE: Copy flash variable assignment into dc22_main.py
			- DONE: 'sessionize' client-server dictionary variables
			- DONE: Added remaining code from flask_test3
			- DONE: Finish updating flask code in main
				- DONE: re-enable the 'restart' variable
				- DONE: Sort out actual function call
				- DONE: 'wire-up' flask and client-server control variables
				- DONE: link variable calls / updates to index.html
				- DONE: internalize implicit while loop of flask in calls
			- DONE: Run and troubleshoot initial run errors
				- I get to the submit routine but but I can't print the submit value??
			- DONE: Run and troubleshoot web errors
				- Primitive functionality achieved!!!
			- DONE: Clean up test comments
			- DONE: Troubleshoot restart functionality
				- Need to review code flow... walk through the ifels on paper... upon restart need to reset variables and play start of game txt
				- Also track end of game through code block flow
			- DONE: clean up troubleshooting comments
			- DONE: return descript_updates_dict back to main
			- DONE: style clean-up
			- DONE: update static_dict and comments version numbers
			- DONE: win game playthrough
		2.2.1
			- DONE: post to pythonanywhere
			- DONE: 'htmlize' my output text
				- Key reference links:
					- How to disable auto-escaping: https://stackoverflow.com/questions/12244057/any-way-to-add-a-new-line-from-a-string-with-the-n-character-in-flask
					- How to manually escape '<' and '>': https://stackoverflow.com/questions/7381974/which-characters-need-to-be-escaped-in-html
					- Overview doc: https://jinja.palletsprojects.com/en/2.11.x/templates/
			- DONE: troubleshoot error on 'examine hedgehog_broach' - convert session['output'] to non-session output variable 
				- Does not need to persist across HTML renders
				- instead, runs in memory for the specific user
				- this avoids issues with the 4 KB client-side cookie limitation when rendering the hedgehog broach text
				- problem solved by JoyEllen!
				- tested on pythonanywhere.com where we both hit server with simultaneous submits at least a dozen times
		- 2.2.2
			- DONE: Write up git for pythonanwhere steps
			- DONE: Someday - moves, score, and version presented continuously in corners of index.htm.		
			- DONE: remove old score / move table
			- DONE: How to get static_dict values to dc22_main ??
			- How to set right margins??
			- Consider implementing word wrap in jinja template wordwrap() rather than hard coded in dc22_interpreter printtw()
		-2.3.y
			- Someday - fresh repo with only the needed code
			- Unify version doc
			- Move completed updates to castle_done
			- flash text blue (this is harder than I thought - requires some deep CSS)
			- Someday - update to nice template
			- Someday - tab for readme and github link
			- Someday - tab for feedback
			- Someday - provide scrolling log of past moves
			- Someday - update doc!

			
Git for pythonanywhere.com
1) New repo
	A. Create new directory (e.g. dark_castle_2)
	B. git clone <repo> <directory>
	C. Go to pythonanywhere web tab
	D. Set 'source code' and 'working directory' and, in WSGI, update the config with the name of the flask script (e.g. dc22_main.py)
	E. click the button to 'Reload tsnellgrove.pythonanywhere.com'
2) Update repo from GitHub Origin
	A. Update code in Pythonista
	B. Commit to Git and Push to GitHub origin via Working Copy commit
	C. Go to pyhonanywhere Bash consonle
	D. From within the repo directory: 'git pull https://github.com/tsnellgrove/dark_castle2' (replace 'dark_castle2' as needed)
	E. From the pythonanywhere.com web tab, click the button to 'Reload tsnellgrove.pythonanywhere.com'


To Dos:

The Zen of Functionalizing - Detailed Notes:

-2.1.1
	DONE: need for description_dict to be called from interpreter_txt (this means description_dict must be *static*)
		- DONE: create independent variable description dictionary
			- DONE: call it descript_updates_dict = {}
		- DONE: Known description change cases
			- DONE: messy_handwriting_read assignment (main routine)
			- DONE: '-base' door and container description cases
			- DONE: push-big_red_button-success trigger
			- DONE: door / container testing
			- DONE: change description_update() routine (hedgehog updates) to write to descript_updates_dict
			- DONE: hedgehog testing
		- DONE: Alter verbs to check descript_updates first
			- DONE: examine
			- DONE: read
			- DONE: look
			- DONE: attack
			- DONE: eat
		- DONE: Move description.csv load to interpreter_txt
			- DONE: load descriptions in interpreter_txt
			- DONE: testing
				- testing discovery: timer() passes description_dict and is called from main... where description_dict is now 'undefined'
				- I need to move timer() to interpreter_txt to fix this
			- DONE: move code to interpreter_txt
				- DONE: increment move count
				- DONE: timer call
			- DONE: testing
				 - testing discovery: upon winning, end() needs description_dict in order to print credits but description_dict is not currently passed..
				 - since end() is also called from the quit rountine in main that means I need to move the quit routine to interpreter_txt...
				 - before I can correctly pass description_dict
			- DONE: move quit routine to interpreter_txt
			- DONE: check move count on pre-action triggers (e.g. 'south' or 'east' from front_gate) - maybe move back to top of interpreter_txt
			- DONE: pass description_dict to end()
			- DONE: win play-through testing
			- DONE: get end_of_game variable passing working
				- DONE: track in state_dict
				- DONE: then return value via main routine statement end_of_game = interpreter_txt()
				- DONE: Worked - had to add return state_dict['end_of_game'] to all interpreter_txt returns - not just the last one!!
			- DONE: delete comments
			- DONE: final play-through testing
	- DONE: move as much code into interpreter_txt as possible
			- DONE: move start of adventure text into interpreter_txt
			- DONE: execute "start game" code based on start_of_game = True
			- DONE: move remaining variable assignments to interpreter - move to top of routine	
			- DONE: first half play-thorugh test (iron_portcullis openned)
			- DONE: second half play-through test (win!)

-2.1.2	
	- DON:E All input and output from main routine
		- DONE: input already gathered there
		- DONE: print to output variable and then actually print buffer variable in main
			- DONE: redirected to output in printtw and appending with each print
				- DONE: used global variable 'output' to avoid passing to printtw a zillion times
				- DONE: still getting repeat prints due to printing within printtw
			- DONE: return 'output' from interpet_txt and print from main routine (as expected, non printtw text is now first)
			- DONE: convert all prints via printtw
			- DONE: troubleshoot print spacing (eliminated "/n" as needed)

- 2.1.3
	- DONE: Break into to 'dark_castle2' and 'interpreter' and call 'interpreter' from 'dark_castle2'
		- DONE: move imports to main routine
		- DONE: move all static lists & dictionaries into interpreter_txt
		- DONE: move all variable lists & dictionaries into main and pass back & forth
		- DONE: testing and troubleshooing - win play-through
			- nb: most of my errors were just long-standing variable passing misses... I guess it was lax in the monolithic form

2.1.4 - Clean-up
	- DONE: Additional Puzzle Clues:
		- DONE: call the crown 'royal_crown' in Nana's memory
		- DONE: Indicate in the grimy_axe description that it could kill a crocodile
			- 'small_print' = 'ACME Axe: Effective at dispatching small dragons, large crocidiles, and even the most agressive of trees.'
	- DONE: Features:
		- DONE: Add a 'version' command (set in static_dict['version'])
		- DONE: Add 'you can't X and object that's not in your hand' error for allowed_verbs; also: 'you can only read text'


	- flaskify main routine
		- decide on how to store data... 
				- maybe first pass is client-side cookies, then server-side JSON then Redis
				- Need to re-apply description updates on load.. or maybe just JSON?? Or maybe special dict just for those?
				- Create dynamic description dict and update descript_dict on load (for update in update_dict descript_dict[update] = update_dict[update])
		- convert interpreter_text to function using print to buffer approach (redirect stdio)	

	- Initial function thinking:
		- dark_castle includes:
			- fask code, dictionaries, imports, while != end_state (input, interpreter_text(), print buffer)
			- pass buffer and end_state in interpeter_text()
		- interpreter_text includes: 
			- imports, check for quit, timer code, std code (all prints to buffer)
			- end() => updates end_state

	- First steps
		- Make interpreter_txt callable from main routine in a stateless fashion
		- print to buffer and do all printing in main routine


	- set a versioning scheme (x.y.z) and official version notes; also create a version command in Dark Castle 
	- Link: https://medium.com/@GabEarnsh/versioning-mobile-app-releases-like-a-pro-25137766150a
	- Web sites
		- get it working on local host website
		- get working on python anywhere or Heroku
		- figure out sessions
	- Functionalize thoughts:
		- What is the value of functionalizing? Maybe just convert output to buffer??	



Some Day:
	- Investigate AWS implemenations
	- Future deployment options: Cloud web, instance, container, Lambda / serverless, mobile, text, echo

3.x Minor Edits:
	Joshua idea: give the player an option to be a boy (Burt) or a girl (Rose); or maybe let them choose their own name
	make synthetic score_keys more consistent (e.g. always '-success'; 'gator-crown' => 'croc-crown-success')
	provide printtw() options for double spacing (add print() to inner for) and also change column width
	use .strip() on input
	Fix trigger so that it no longer sometimes returns a value and sometimes doesn't
	maybe put the throne attop a 'dias' (just to be more purple prose ;-D)
	add guiding error message for unseen verbs
	docstrings for all functions [?]
	map routines graphicaly; consider "flattening" function calls (?)
	normalize variable names (e.g. consistent _dict, _lst, _txt suffixes)
	Consider making state_dict['active_timers'] a list to allow for multiple simultaneous active timers

3.x General
	add 'close' 
	add 'lock'
	consider adding 'put' for containers
	consider implementing 'give' for creatures
	implement 'stow' for backpack
	implement container capacity limits
	consider normalizing pre - and post checks for verbs (??)
		- create a "generalized" verb block with trigger & score for every verb
	'wear' implementation has similar limitations to containers... no limits on how many similar items can be worn
	Create a "repeat" command that lets you put the same text on the command line but then lets you edit it (like 'g' in Zork)

3.x Make silver_sword puzzle more beginner-friendly... consider making stale_biscuts supply 'bottomless'
	Note from Burt's Mom telling him to whistle for more biscuts
	Perhaps have Baker weinner dog Schnitzel come woofing along with more biscuts from entrance... 
	need a state_dict variable to track total world biscut population
	would give time for Baker history and great, great grandmother McVities 
	Never forget Burty... you may not be biscuts and weiner dogs.. but you're from biscuts and weiner dogs.. never forget where ya from
	Maybe somehow also fit in tale of Goblin?? (Bright Castle caretakeer, 'a real goblin of a man.. and that was back in the good days')
	Could use as hedgehog run-away reset as well?

3.x Create a Save routine... what is needed to caputure state?
	Create save_dict with same entries as state_dict, score_dict, and room_dict and any other variable dictionaries
	Save => write state_dict to save_dict
	Restore => write save_dict to state_dict
	Above will work within session but will need to write to file to survive between sessions
	Will need to run description_update() based on state_dict[hedgehog_state] 

3.x Associate Epilogs with Each end game score
	Functionality
		Associate endings with accomplishments from score_dict 
		Provide ending text for accomplishments and whether Burt lived to wander back to the pub or died
	Implementation
		Create epilog_dict to hold text
		Add logic to end() to call and print correct epilog for accomplishment values from epilog_dict


4.x Object Oriented Ideas:
	Classes
	Text Adventure Link: https://inventwithpython.com/blog/2014/12/11/making-a-text-adventure-game-with-the-cmd-and textwrap-python-modules/
	Link score increases to item, room, and door objects
	embed smarts / behavior into switches; create a generic switch model
	idea: embed paths into rooms
	idea: need a more elegant way to handle 'untakable' path (e.g. e, w, s @ entrance) descriptions 
	idea: brief vs. verbose modes
	create "availability" categories - (i.e. viewable, interactable, hand) [??]
	verbs to functions with switcher?? (too much variable passing?)
	concept of the container being _in_ the room - currently contents basically just dumped to room

5.x Additional rooms
	Have portait of Willie revealed in throne room and give player mouse hole and time travel quest
	5th room
		mouse hole - to exercise existing capabilities (e.g. "food" that can be eaten)
		copper key opens cabinet which holds potion
		find a use for 'close' verb; maybe potion refill
		possibly create 'return' verb to put things back (or maybe 'swap')
		potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
		enter mouse hole
		maybe fight mouse?
		silver key in mouse trap; need to swap with copper key
		find a use for close command?
		would be fun to use every verb ;-D
		maybe a guard mouse that only lets you past if you're wearing the hedgehog_broach
		Indiana Jones reference for mouse trap and ball chasing you out ;-D
		make hedgehog_broach wearable
		link puzzle to total number of moves? Or to score?
		repeat option like 'again' / 'g' in Zork (JE request)
	Possibly add a room 6 with time travel??
		find a use for the word "griffonage" (illegible handwriting)
		Opportunity to include princess in game - perhaps have Willie give her the hedgehog_broach to time travel
		Depict future (opportunity but challenges) by painting to portrait
		Also get key from time travel - put in container and then refind 100 years later
		loose brick in dark_alcove - "appears not to have been disturbed for 100 years"
		guard with key_detector in main hall
		trade keys with princess? give her the hedgehog broach? maybe during dance in throne room
		dungeon down stairs from throne room
		in throne room 3 paintings of past and 1 blank space for future
		key to open dungeon?
		keys same colors as ready player 1

5.x Future Ideas:
	fun idea - small creature - like a mouse - as an item
	more directions
	landscape / path changes
	create 'win' test routine with checksum



