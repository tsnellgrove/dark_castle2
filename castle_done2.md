*** Early Game Outline ***

Simple Castle Adventure Overview
	1. Entrance (front_gate): unlock front_gate with rusty_key and open front_gate to go north; has door
	2. Main Hall (hedgehog, shiny_sword): drop stale_biscuts to distract hedgehog to get to shiny_sword); has creature, trigger, timer
	3. Antechamber (goblin; defeat goblin with sword and pull lever to open portculus to next room); 
	4. Throne Room (treasure chest; open chest to get gold); scroll in chest to open (Gideon)
	5. Upon victory Burt becomes known as 'Burt the Bold'


*** Version History ***
v 1.0: Base functionality for all four rooms
v 1.1: PEP-8 Styel Compliance
v 1.2 - 1.4: Spell checking, re-writing, puzzle tuning, centralize trigger text => description_dict
v 1.5: Migrate files to Working Copy git client
v 1.6 - 1.8: Tune Git workflow, consolidate dictionaries, code review
v 1.9: Consolidate text => description.csv and import file to dict, Document application
v 2.0: Final tweaks, updates, and documentation 


*** Program Change Log / Relese Notes ***

Note: I originally kept my coding to-do list in comments at the end of my code and deleted items as I completed them. This is a chronological list strating from when I retained completed to-dos for historic review.

Entrance:
	DONE Change examine of non available item to "Burt, you can't examine that!"
	DONE Change & universalize the response to one-word "examine" => "examine what Burt?" (works for taake & attack & drop too)
	DONE Consider eliminating "store" and implementing "drop" instead
	DONE Optimize unknonwn word: list with randint index
	DONE Create Path Dictionary ("entranc-south": "..") "you apprach the mighty gate"; Path_Action Dict; 
	DONE Take Key
	DONE Drop Key
	DONE dictionary of functions to replace long interpreter elif 
	DONE Clear up comments
	DONE Test drop / inv / take with multiple objects
	DONE paths in dictionary of dictionaries	
	DONE Door / container State dictionary of dictionaries
	DONE Bundle vital info into state_dict 
	DONE Return to elif word routine to handle variable passing
	DONE Add room description and feaature text to room_dict`
	DONE Check for room_feature on "look" text
	DONE Unlock Door & Open Door;
	DONE room feature text in look: for i in [lst] Print("there is an " + i + " here\n")  

main_hall
	DONE Describe paths
	DONE Add stale_biscuts to backpack
	DONE Add writing_dict
	DONE Describe items & features: shiny_sword, hedgehog, tapestries, biscuts 
	DONE Add 'view_only' key to room_dict
	DONE Incorporate special view_only cases into room_dict
	DONE Describe tapastries in main_hall; disconcerting ref to Zork; pillaging GUE; makes you question the very nature of your being
	DONE Add 'read' command for 'rusty_lettering', 'dwarven_runes', 'trademark'
	DONE need a move counter (don't count un-recognized words); show count at end and 
	DONE Also inscription Sword 'Foehammer' (which, when translated from Dwarven means 'Goblin Wolloper')
	DONE Add the "read" verb for the front_gate lettering "Abandon Hope All Ye Who Even Think About It"
	DONE hedgehog is territorial and hungry; will not let Burt get the sword unless fed
	DONE If burt tries to attack the hedgehog it dodges and he gets mocked; 
	DONE Add stale_biscut (examine: "McVities") to backpack; If burt drops biscut hedgehog will be distracted for 3 turns
	DONE While hedgehog eating remind Burt that time is passing; after 3 moves the hedgehog goes back to guarding the shiny_sword
	DONE Implementation: add trigger_lst to room_dict; check for trigger in 'take' routine
	DONE Pehaps 'trigger_lst' is in room_dict? This links the trigger to the room; trigger_key = 'take-shiny_sword-main_hall'
	DONE In trigger() if 'hedgehog' in room_dict[room]['features'] and 'stale_biscuts' not in room_dict[room]['items']
		DONE => trigger_txt "The moment you approach the sword the teritorial hedghog blocks your path and bares it's teeth"
		DONE introduce "attack" command and attack_results_dict (??) 
		DONE Add trigger with timer for trigger_key == 'drop-stale_biscuts-main_hall'
		DONE dropped biscuts picked up by hedgehog go to view_only_lst ?
		DONE Need a timer_dict and a routine in the main program to enable timed text when 'timer_on' = True ??
		DONE Create 'timer_action' that will remove 'stale_biscuts' from room_dict['main_hall']['view_only']
		DONE Reset state_dict['room'] to 'entrance'
		DONE Attack hedgehog with weapon => hedgehog dies; "you know in your heart that you will come to regret this unkingly deed"
	DONE: Create "eat" command but don't let burt eat the biscut
		Add  allowed_lang_dict['eatable_lst']: 'stale_biscuts' 
		Create food_dict['stale_biscuts'] => eat_txt and eat_action
		Create eat elif in interpreter_text to call dictionary entries and update lists as needed
	DONE: Create end() function
		create an end() function that prints moves
		call end() from quit and also room_action() 'action' == 'death'
   DONE Gideon suggests adding a scoring system; 'score' command to show score; print score on each increase; 
		DONE Functionality
		DONE Your score is now x out of a maximum of y in z moves
		DONE 5 pt for taking key, 5 pts for entering main_hall, 5 pts for getting shiny_sword, 5 pts for opening iron_portculus, etc
		DONE negative scores possible for truly ignomious endings
		DONE Implementation
			DONE Track current_score and max_score in state_dict
			DONE Create a 'score' verb following the usual new verb process
			DONE Create a score_dict to hold 'score_key', and score_value
			DONE create a score() function similar to trigger() that increments and prints current_score when score_key in score_dict
	DONE: Associate Titles with Each end game score
		Functionality
			Associate titles ("Burt the Brave") with scores; 
			Provide ending text for each score
		Implementation
			Create title_dict to hold text and min score values for each titel
			Add logic to end() to call and print correct title for score value from title_dict
			< 0 : 'Burt the Best Forgotten'
			== 0 : 'Burt the Boneheaded'
			10 <= x < 20 : 'Burt the Beginner'
			20 <= x < 30 : 'Burt the Better Than Average'
			30 <= x < 40 : 'Burt the Brainy'
			40 <= x < 50 : 'Burt the Breathtaking'
			50 : "Burt the Bold, Baron of Bright Castle"
			Need a python roundup funciton => title_score = roundup(score / 10) * 10
			math.ceil(score / 10) * 10
	DONE: Trigger improvements
		Need to create a separate list for triggers separate from rooms
		Rooms are just a criteria to be tested in trigger()
		Actually, there are really 2 kinds of triggers... pre-action and post-action
		"take-shiny_sword" is a pre-action trigger... before the action can be performmed it is interupted by the hedgehog
		"drop-stale_biscuts" is a post-action trigger... it takes effect immediately after the action (dropping) is completed
		So 2 trigger lists - one pre and one post
		Pre=action keys are tested in the main interpeter_txt routine above all verb elifs
		Post-action keys are tested for in each verb elif and performed after the main body of the elif
	DONE: Improve Timer Routine
		Functionality:
			Need a dedicated timer function
			Several problems... timer continues if player leaves room... 
			also need work-around to prevent player from killing hedgehog during timer
			Timer bug if you leave the room because timer is embeded in room_dict
			Timer should continue but not print when player leaves room
			Timer should stop when feature is removed
		Implementation:
			state_dict[active_timer] = 'drop-stale_biscuts'
			timer_dict holds attributes of each timer
			Attributes include curent_timer_value, timer_visible_room, timer_dependency, timer_txt_<timer_value>, timer_event
			state_dict['active_timer'] is set within trigger(); timer_dict[current_timer_value]
			Check state_dict[active_timer] in main routine and call timer() if != 'none'
			timer() checks for timer_dependency ('hedgehog' in room_dict['main_hall']['features'] and resets current_timer_value to 0 if gone
			timer() checks current room vs. timer_visible_room and prints timer_txt_<num> if in room
			timer() performs timer_event upon count down (e.g. remove stale_biscuts from room_dict['main_hall']['view_only']) 
			don't forget to pass timer_dict to functions
			key limitation here is that you can only have one timer running in the game at a time
			Move timer_dict['timer_current_value'] to minimize variable dictionaries; could just name state_dict[stale_biscuts_timer]
	Description Updates
		Functionality
			hedgehog replaced by dead_hedgehog if attacked with weapon
			Need to update hedgehog "hungry" state in examine description after hedgehog has eaten
			Need to update examine status to "The hedgehog looks at you hopefully" once player has shiny_sword
			Update "examine hedgehot" status to "deligthed" once fed and has sword
		Implementation
			2 different feature nouns each with their own description: 'hedgehog' and 'dead_dedgehog'
			Create multiple descriptions for hedgehog in creatures_dict
				Update value of 'hedgehog' in descrptions_dict based on events
				3 options... 
					1) could track hedgehog state and use as key to description txt.. not needed but could be useful for other interactions
						Makes creature_dict a variable dictionary (and description_dict too unless there is additional logic in 'restore')
					2) could just swap text in description at time of state change
						Makes description_dict a variable dictionary
					3) Maybe hedgehog state lives in state_dict ; call description_update() to update description_dict?
						'hedgehog_state' == 'hungry_has_sword', 'eating', 'fed_sword_not_taken', 'fed_sword_taken', 'fed_sword_returned'
				Leaning towards option 3
Antechamber
	Functionality
		for path actions create "passage" for no door
		Must attack goblin in alcove with shiny_sword to get by to closed portculus
			If player has no weapon then dies
			If play has shiny_sword they parry
			If player attacks with shiny_sword goblin is killed 
		Behind goblin are 3 levers on the wall (left_lever, middle_lever, right_lever) and a big red button
			Dead Goblin has a note with a number (0 - 7) randomly set at start of game; "Pwd = #"; levers must match number in binary to open
			Allow infinite button push tries
		Implementation
			DONE: 1) Descriptions for new room, iron_portculus, goblin, dead_goblin, grimy_axe
				Also for : torn_note, messy_handwriting, alcove, control_pannel
			DONE 2) Update path descriptions and logic to allow palyer to enter and exit antechamber
				DONE Follow new room directions and test travel and examine
			DONE 3) With the benefit of hindsight it is now clear that I should stop scattering descriptions all over (rooms, creatures, etc)
				Instead I should centralize all descriptions into 'actve decsriptions' (i.e. descriptions_dict)
				And stateful_descriptions_dict
				And then track description state for stateful descriptions in state_dict 
				And consistently update description_dict via stateful_descriptions_dict using description_update()
			DONE: 4) Create goblin attack trigger for:
				'examine' control_pannel, iron_portculus, grimy_axe; 'open-iron_portculus', 'north' via pre-action trigger
				Add a drops: [] element to creature_dict to track what a creature drops on death ? (e.g. grimy_ax and torn_note)
				Create iron_portculus in doors_dict
				'attack goblin' (without a weapon or with shiny_sword) based on attack()
				On goblin dead: features.remove(goblin);  features.append(dead_goblin); goblin['drops'] == grimy_axe and torn_note => items
			5) Control pannel
				DONE: Create switch_dict
					track each lever state in switch_dict; all levers start 'down' (0)
					button tracks success value, success text, failure text, success event
						maybe track number of button pushes just for fun?
				DONE: Creat code value
					Randomly assign value to torn_note in main routine and track in switch_dict
					Print note number based on random value
					IN TROUBLE SHOOTING - KEEPS PRINTING initial value instead of updated value
					Figured out - once assigned wasn't reacalculating because of str() conversion
				DONE: Add Levers and Button to Room
					button and levers to be added to room['view_only'] upon goblin death via post-action trigger
				DONE: Descriptions:
					create descriptions for levers and button
					test examine
				DONE: Need to solve dictionary update issue..
					Problem exists for torn_note, all doors, and all levers
					Thinking maybe create a "base" and "variable" portion to each variable decitionary description
					Update "base" with variable at top of main routine
					Then re-update in each verb that changes value (e.g. read, open, pull)
					Keep "base" text in stateful_description_dict`	
					Or is there a better way??
					Fix works for front_gate!!
				DONE: Create Pull Verb
					Create pull verb for levers (swap up vs down)
					Note: Will likely need to update the description_dict key, not just the swtich_dict variable!!
					Maybe recalculate 'current_value' on each lever pull?
					Use front_gate fix to update value
				DONE: update lever entries in switch_dict to switch_dict['left_lever']['state']
					Allow for levers that cause actions
				DONE: Create push verb for button	
					update button push count
					compare 'success_value' to 'current_value'
					Create success_event in swicth_dict: "door_dict['iron_portculus']['door_state'] = 'open'"
						 => find a way to execute code
					Where to execute specific antechamber control panel logic??
					if lever state == random number open portculus and print success description from switch_dict
					if lever state != random number print (print fail description from switch_dict)
				DONE: Increment score on iron_portculus open for first time (+10)
					Test!!!
	DONE: Update initial hedgehog description "for some reason you feel an innate fondness for the hedgehog"
 	DONE: Idea: Have hedgehog run away on weapon attack; 
	DONE: Need to capture how the game was ended (i.e. 'quit', 'death', or 'win') in state_dict and use this in end()

Old throne room ideas
	marble_torch (brazer?), eternal flame of kingship on dias in middle of room; On north end of room is the throne;
	Description on plaque
	Player must return to main_hall and drop (give) shiny_sword to hedgehog to get matches (from hidden pouch)
	re-light torch with matches (provides light and hope and also opens crystal_box
	read scroll while sitting on throne to win game, fill coffers with gold and deed to castle
		 ("can you think of somewhere more kingly to read the scroll?")
	If you burn the scroll with the torch, castle crumbles, player dies, score = -100
	If you kill the hedgehog after getting the matches a draft blows out your match when attempting to light the torch

Throne Room
	DONE: Features
		Just left of throne is an empty treasury coffer; 
		just right of throne on a pedistal is a crystal box with silver lock holding a scroll
		crystal_box has etching script on it: "scroll of the king"
		Player must return to main_hall and drop (give) shiny_sword to hedgehog to get silver key (from hidden pouch)
		have hedgehog supply silver_key; 
		have crown hidden in crocodile tummy at entrance; 
		need to read scroll in throne room while wearing crown; scroll sepcifies need for hedgehog to be in castle
		read scroll while wearing crown in throne room to win game, fill coffers with gold and deed to castle
		Hence forth known as Burt the Bold; Crest with a hedgehog holding up a sword
		Family tree on wall - with 'Willy the Wanderer' as the last of the Flatheads
		Also 'read scroll' from chest to open secret compartment in throne with bag of gold and deed to Dark Castle
		Maybe examining throne triggers an old memory of Burts great grandmother on death bed telling Burt about
			Hedgehog broach under throne - brings back memories of great grandmother on death bed - engraving "To B."
			She sends rest of family off on errands and then, with bright eyes, tells "Burty" his desitiny to be king
			Warns him not to go wandering off drawbridges without a weapon handy and breaking young girl's hearts
			Willy, the eccentric old king who died while doddering about with newspaper and pipe on drawbridge and fell in moat in bath robe
			And was eaten by crocodile (should have a cute name for croc - maybe tick-tock after peter pan?)
			Turns out Burts middle name - Burt William Baker - was named after "the old dear"
			A bit blarmy in the head but he did know how to romance an young girl
			"When you're king Burty, don't go wandering off the edge of the drawbridge without a good weapon handy"
			Of course grammy was well out of her gourd by this time and convinced that her own grandson was hamster but...
			(could mention 'old goblin of a caretaker')
 		Upon reading scroll castle is scourgeified and gleaming; tapastries depect Burt's adventures'
		Credits at end: Toby, Joshua, Gideon, Franco
	DONE: Pseudo Code:
		Throne Room Contents:
			features: throne, coffers, crystal_box (on pedestal; containing scroll_of_the_king; calligraphy_etching)
			view_only: family_tree
			items: upon examining the throne, the hedgehog_broach is added to items
		Puzzle Solution:
			1) Player enters Throne room for first time
				Descriptions for room, throne, coffers, crystal_box on pedestal, familiy tree
				Description of crystal box highlights shiny silver key hole; maybe hint?
				Examining throne reveals hedgehog_broach under it
					upon taking first time trigger long memory of great grandmother recounting Willy's death
			2)Getting the silver_key
				When player returns ('drop') shiny_sword to hedgehog it retrieves the silver_key from a hidden fold of its fur
				and gratefully places it at Burts feet with a bow
			3)Getting scroll_of_the_king
				Player unlocks crystl_box with the sliver_key in hand and then opens it
				the scroll_of_the_king can now be taken
				I will need to create a containers_dict
				'look' and 'examine' will show the open / closed state of the container and its contents
				a full implementaiton would required a 'put' or 'deposit' command to put things in - as well as a capcacity metric
					But I think I can get away in v 1.0 with just hooks into unlock, open, take, examine, and look  
			4) Reading the scroll_of_the_king
				'read scroll_of_the_king'... specifies that if read by true king, in throne room, with crown worn, and hedgehog in castle
				new king of Bright Castle shall be proclaimed
				test for all conditions and give a mild hint upon missing conditions
			5) Get crown
				east or west off of entrance drawbridge with shiny_sword or grimy_axe in hand
				trigger one time event: crocodile lunges - sees weapon - belches up crown in terror - and flees; 
					burt puts crown in backpack and clambers back up onto drawbridge
				All future entrances into the moat either lead to death (no weapon) or no encounter (weapon)
			6) Wear crown
				new 'wear' verb
				need to update 'inventory' to show worn state
				probably also need to update 'take'
			7) Winning
				with all conditions met the castle becomes gloriously bright, the coffers are filled, and Burt becomes King (per family tree)
	DONE: Implementation:
		1) New Room & Descriptions
			room_dict, allowed_lang_lst, path_dict, room & feature descriptions
		2) Create trigger based on 'drop shiny_sword' to provide text and silver_key
			Also need to update hedgehog description after return of key
			Create description of silver_key (include clue about crystal_box)
			Add 5 pts to score upon take-silver_key
		3) Create crystal_box
			Treat containers as doors (i.e. add to door_dict); create is_container door_dict value to be tested
			Add crystal_box to allowed_lang[can_be_openned]
			Add '-base' description for crystal box
			code to 'open' to display contents when openned and add to room_dict items
			5 points to score for taking scroll_of_the_king
			Add code to 'examine' to display contents when openned; in allowed_lang create [is_container] list
			Need to remove item from container if taken; create dictionary of contained_in in state_dict and check during 'take' ??
		4) Scroll of the King
			Description
			Read text
		5) Get hedgehog_broach
			add 'throne' to 'can_be_pulled' & 'pull_throne' to post action triggers
			add triggers() 'pull_throne' action and inject hedgehog_broach
		6) Trigger hedgehog broach memory
			If examine hedgehog broach while holding it in hand...
			Trigger memory of great grandmother on death bed... provides clue about crown
			Score + 5
		7) Get crown
			trigger on east / west from entrance with axe or sword in hand
			Description of croc approaching then belching up crown in fear and swimming away
				burt jumps back up on drawbridge, crown in pack
			Add crown to pack
			Score + 5
			Description of subsequent jumps into moat with weapon
			Description of Crown
			**** Test ****
		8) Wear crown
			Verb pre work
			add worn list to state_dict
			add worn to examine items
			update inventory
			Verb elif
			Updeate score_dict
			update take
			Alert player on attempt to wear wearable item that it must be in their hand
			Test, test, test!!!
		9) Check for win state on reading scroll_of_the_king
			Trigger on read to check for conditions
				add 'read-scroll_of_the_king' to post trigger actions list
				add 'read-scroll_of_the_king' elif to triggers()
				check for 1) room , 2) hedgehog, 3) crown
		10) Win text
*** Base Game Complete!! ***


DONE: Updates for v 1.1
	PEP-8 compliant style
 		DONE: Excess spaces removed
 		DONE: 79 char line max
		Code Examples:
			https://web.archive.org/web/20120709112020/http://wwd.ca/blog/2009/07/09/pep-8-cheatsheet/
			https://gist.github.com/RichardBronosky/454964087739a449da04

DONE: Updates for v 1.2
	DONE: Trigger text to dict
	DONE: Generalize 'push' verb (use 'word 2')
		Reconsider where push *button* logic should live
		If push will be used for things other than buttons (it's a pretty general verb)
		Then need to keep all logic in trigger... or possibly a dedicated function
		Also, where should switch push result text live? description_dict? switch_dict?
		Certainly not in def push!
		Perhaps I need a special button push routine? 
		is there anything i could push that wouldn't act like a button?

DONE: Updates for v 1.3
	DONE: Full Spell check
	DONE: spelling: biscuts, celinged, publ, distrection, 'is ever' vs. 'if ever'
	DONE: spelling: gaurds, bsicut-baking, broach (?), portculus (?)
	DONE: more spelling: recipie, there-after, gloary, incomplete, ligth, indstinct
	DONE: JE Feedback
		DONE: Need better hints for silver key... possiblities include
			DONE: Hedgehog with sword and silver key on family tree
			DONE: describe silver lock as shining like shiny_sword
			DONE: describe hedghog as 'loves that sword' or 'partial to shiny things'
		DONE: Make it easier to examine broach... eliminate 'hand' requirement

Updates for v 1.4
	DONE: Add trigger for "push throne" - mention unevenness
	DONE: Fix case where pulling throne multiple times produces multiple broaches
	DONE: Make timer routine more efficient
	DONE: Inhibit return of shiny_sword response (silver_key) while hedgehog is eating
	DONE: Full writing review
	DONE: Re-Run Style Check

Updates for v1.5
	Add to Working Copy

Updates for v1.6
	Sort out Working Copy
		DONE: Get live connection working (Open from Pythonista file manger - use app chooser)
		DONE: Test an Undo / Revert (pre remote push, left swipe on commit to undo then "revert" at top)
	Centralize lists and dictionaries
		DONE: worn_dict => description_dict
		DONE: room_dict descriptions => description_dict
		DONE: writing_dict text => description_dict [remove commented txt]
		DONE: consolidate writing_dict into single level dictionary
		DONE: creature_dict descriptions => description_dict
		DONE: understand and the update_dict and migrate to description_dict (crystal box testing needed)
		DONE: food_dict txt => description_dict
		DONE: remove creature_dict from timer, trigger, and update routines
		DONE: state_dict['hedgehog_state] => creature_dict
		DONE: Move timer from state_dict to timer_dict
		DONE: Move timer descriptions to description_dict and make timer_dict single level
		DONE: use '-base' to isolate logic from text descriptions (switch descriptions => door descriptions)
		DONE: move broach_found => generalized max_count dict

Updates for v 1.7 & 1.8
		DONE: More testing - Offer the boys $1.00 to finish the game and report bugs
		DONE: reduce path_dict to only valid paths and create random text for banging into wall
		DONE: intro => description_dict
		DONE: move 'invalid_path' to static_dict
		DONE: help text => description_dict
		DONE: credits => description_dict & valid 1-word command
		DONE: pre_action_trigger_lst => static_dict
		DONE: post_action_trigger_lst => static_dict
		DONE: written_on_dict => static_dict
		DONE: unknown_word_lst => static_dict
		DONE: food_dict => static_dict
		DONE: titles_dict => static_dict
		DONE: max_score => static_dict
		DONE: score_dict => state_dict
		DONE: timer_dict => state_dict
		DONE: use .lower() on input
		DONE: Implement 'import textwrap'
			DONE: Create printtw() function (see: https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/)
			DONE: Test printtw() on opening text in Main Routine
			DONE: Extend to all other existing print() commands
			DONE: Full test of game with examine all
		DONE: Post to GitHub using working Copy
		DONE: sort out score printing - currently have score printed in 3 different locations: score(), end(), look()
		DONE: Code Revew - local variable usage, simplify code, clean up variable passing
			DONE: triger() - Improve local variable usage
			DONE: trigger() - Full test post local variable update
			DONE: trigger() - clean up variable passing
			DONE: timer() - cleaned up variable passing, implemented local variables, tested
			DONE: look() - cleaned up variable passing, local vars, testing (NEEDED IT!)
			DONE: end() - cleaned up local vars; tested
			DONE: room_action() - cleaned up variable passing & local vars; tested
			DONE: One word commands & existing Interpreter local variables
			DONE: clean up examine() and take()
			DONE: clean up drop() and open()
			DONE: clean up unlock()
			DONE: clean up read(); introduce post_action_trigger local variable; re-arrange if-elif-else
			DONE: re-arrange if-elif-else for examine(), take(), drop(), open(), and unlock()
			DONE: clean up attack(); add print_score() to end() [back to dual score print on win]
			DONE: clean up eat()
			DONE: clean up pull() and push()
			DONE: clean up wear()
			DONE: if-else alteration
			DONE: standardize attack trigger / score
			DONE: normalize each "if verb"
		DONE: apply local variables to push in switch case
		DONE: optimize function calls
			DONE: figure out a way to only print score once end end when game is won
			TRIED: "interpreter()=> score(), interpeter => print_score()" vs. "interpeter() => score() => print_score()"
				TRIED: (doesn't work - need score() to ensure only printing on first score_event)
			DONE: move print(credits) to end() and follow with exit()
				DONE: allows removal of post end() exit() calls; Use "if" to ensure credits only on end = win
		DECIDED AGAINST: try switcher routine for end()
		
Updates for v 1.9
		DONE: create view_special containing 'fist', 'burt', 'concious'
		DONE: standardize return on trigger()
		DONE: separate descriptions into text file and import at start of game
			DONE: doors, non-door features, items
			DONE: newline issue solved
			DONE: special
			DONE: creatures, rooms, all keys in double quotes
			DONE: triggers
			DONE: worn, paths, read
			DONE: attack results, stateful updates
			DONE: eat, timer
			DONE: dictionary cut-over with win-path test
			DONE: full walk-through test with text edits (and read illuminated_letters score fix)
			DONE: remove description_dict_old and all unneeded comments
		DONE: fix for read verb scoring... in trigger append "-win" to score key; update score dict
		DONE: Find a more efficient way to tell the player "you can't go that way" 
			- unique path descriptins won't scale well to 10 cardinal directions for 10+ rooms
		DONE: document the terms of art (e.g. items vs. features vs. view_only)
			DONE: update existing doc
			DONE: outline documentation section, document program approach and layout
			DONE: document linguistics
			DONE: document nouns
			DONE: document verbs
			DONE: doc IF, Zork, TADS, IF sites, Frotz app
			DONE: triggers and timers doc
			DONE: game world doc inventory & rooms
			DONE: game world movement
			DONE: game world switches
			DONE: mechanics - description updates
			DONE: mechanics - scoring
			DONE: dictionaries and puzzles
			DONE: story
			
Final Updates for Version 2.0
	DONE: Organize castle_done notes
	DONE: Organize castle_to_do notes
	DONE: Organize Flask Notes
	DONE: Create dark_castle description for entrance view_only
		Dark_castle looms over you. Its facade of blackened turrets and cracked walls dour and singlularly univiting. It's hard to imagine but your great grandma Nana used to tell wonderous stories of the old days when the castle gleamed brightly on its hill and brought order and goodness to the land. Maybe it's because of the stories but you've always had a bit of an itch to venture inside - and now that a round of beer and your alehouse repuation as a fearless ruffian are on the line you certainly don't intend to back down now! 


