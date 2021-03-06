*** GIT CONSOLE NOTES ***
			
Git for pythonanywhere.com
1) New repo on pythonanywhere server
	A. Create new directory (e.g. dark_castle_2)
	B. git clone <repo> <directory>
	C. Go to pythonanywhere web tab
	D. Set 'source code' and 'working directory' and, in WSGI, update the config with the name of the flask script (e.g. dc22_main.py)
	E. click the button to 'Reload tsnellgrove.pythonanywhere.com'
2) Update repo on PythonAnywhere from GitHub Origin
	A. Update code in Pythonista
	B. Commit to Git and Push to GitHub origin via Working Copy commit
	C. Go to pyhonanywhere Bash consonle
	D. From within the repo directory: 'git pull https://github.com/tsnellgrove/dark_castle2' (replace 'dark_castle2' as needed)
	E. From the pythonanywhere.com web tab, click the button to 'Reload tsnellgrove.pythonanywhere.com'
3) Create new repo on GitHub
	A. Create repo and files in Working Copy
	B. Navigate to "folder" within pythonista (this can be a bit tweaky)
	C. Perform initial local commits in Working Copy
	D. Create repo with same name in GitHub
	E. Copy full repo url from GitHub (e.g. "https://github.com/tsnellgrove/css_cheat_sheet.git")
	F. In working copy, within repo, "Add remotes"; Accept "origin" default and use coppied GitHub repo url; Save
	G. working Copy repo Commits will now push to both local and origin git repos


+++ Playtest Feedback +++

"Great idea.
My 2 cents on this is....
The command box should gain focus so the user doesn't have to click into it to type a command.
Maybe not in scope but how about 2 drop down lists populated with only the possible actions and items for those actions once selected. (The game for me was constantly typing 'help' and going back and forth to remember the item names.)
Maybe have a side <table> populated with the 'in hand', backpack contents, and wearing info.
-Andy""

Feedback requests:
- From Andy, Ken, and Karl D: Add focus to the input form [IN-PROC]
	- Try adding autofocus="autofocus" to input line in index.html [DONE]
	- Seems to half work in Pythonista browser so trying on public [DONE]
	- Yes! It appears to work in both iPad Safari and Chrome! I will ask Karl D to test [NEXT]


+++ To Dos +++
- READ: https://inventwithpython.com/blog/2014/12/02/why-is-object-oriented-programming-useful-with-a-role-playing-game-example/
- IN-PROC: Make a plan to learn object oriented programming (YouTube?)
	- DONE: Tech w Tim - Python OOP
	- DONE: Tech w Tim - Software Design
	- IN-PROC: Tech w Tim - Classes & Objects
	- TBD: Plan out creating Nouns (items, doors, containers, switches) in OOP
	- TBD: Plan out createing Game World (rooms, inventory, movement, switches) in OOP
	- TBD: Plan out creating Game Mechanics (triggers, timers, description_updates) in OOP
	- TBD: Plan out creating interpreter in OOP


- Read https://inventwithpython.com/blog/2014/12/11/making-a-text-adventure-game-with-the-cmd-and textwrap-python-modules/
- Post "OOP for Dark Castle", learn to use Python to get work done: https://nostarch.com/automatestuff2
- Watch advanced Text Adventure with Python: https://youtu.be/8CDePunJlck


List of Next Version Requirements:
- Functional
	- Player name as variable
	- Short version of noun names (i.e. gate vs. front_gate; "n" for "north")
	- Support articles (e.g. a, an, the)
	- Support adjectives (i.e. "shiny sword" vs "shiny_shword")
	- Support propositions (e.g. in, on, under, to, from)
	- Support direct objects (e.g. "put the hedgehog broach into the crystal box")
	- Support game saves and restores
	- Give command box focus on web page startup
	- cmd line ability to "arrow up" to past commands
	- Either implement scrolling interaction or provide side table of inventory and room contents
	- Add shrink into mouse hole room
	- Add time travel room
	- Auto testing routine (?)
	- Introduce a puzzle where waiting is key
- Non-Functional
	- Object-Oriented code
	- DB back end (SQLAlchemy ?)
	

*** Future Versions and Features ***

Some Day:
	- Investigate AWS implemenations
	- Future deployment options: Cloud web, instance, container, Lambda / serverless, mobile, text, echo

-3.0.x Web / Flask / Python Minor Updates:
	- Change index.html inline styling to syle.css based
	- Someday - provide scrolling log of past moves	
	- What is the preferred response to an entry after 'Quit' but before 'Restart'? Maybe cache quit output?? Or don't bother?
		- Could hid form and 'Submit' in this case?
		- Or, perhaps better, could pop 'id' upon end_of_game == True
	- end_of_game is sort of strange... it is a local session variable in main(); but it is also a key-value pair in state_dict, which is also a session variable, and which I pass to interpreter_text... and in interpreter() is only exists in state_dict... strange
	- Return to use of output as global?
	- Someday - tab for feedback
	- Custom google email for feedback?
	- Maybe - update to nice bootstrap template??


3.1.x Minor Python Edits:
	Joshua idea: give the player an option to be a boy (Burt) or a girl (Rose? Betty?); or maybe let them choose their own name
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
  enable shorthand item references (e.g. "gate" instead of "front_gate" when in Entrance)
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



