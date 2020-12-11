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

Updates for v 2.0.x
	- DONE: Change version naming to x.y.z notation
	- DONE: Read about Flask functions
	- DONE: re-read number input / output example
	- 2.0.1 Learn Flask basics: 
		- https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/
	- 2.0.2 Basic test local site with input
	- 2.0.3 Basic test local site with input box; prints a locally asigned variable
	- 2.0.4 Created a very basic processing.py script to enable input / output testing
	- 2.0.5 Good updates - have input and output linked to web site & sub function calling working
	- 2.0.6 Sessions working (?) but still can't retain text_lst values
	- 2.0.7 Finally got session variable to be persistent!!
	- 2.0.8 Sorted out the KeyError issue and got session.pop() working (well, most of the time)
	- 2.0.9 Wrote pseudo code for how flask wrapper would work if all stateful data was stored in session dictionaries 	
	- 2.0.10 get flask test into git
	- 2.0.11 got git branching working (I think)
	- 2.0.12 working through a really frustrating working copy / pythonista remote file call bug :(
	- 2.0.13 After much adventure got flask_test3.py running smoothly on pythonanywhere with git integration

2.1.x - The Zen of Functionalizing - Early Thoughts:
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
-2.1.1 (Detail)
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
	-2.1.2 - redirect interpreter_txt stdout to string, return string to dark_castle2, and print string from main routine
			- redirected stdout in printtw; getting repeat prints due to print within function
			- return 'output' from interpet_txt and print from main routine
			- convert all print() commands to printtw()
			- troubleshoot all print spacing
-2.1.2 (detail)
	- DONE: All input and output from main routine
		- DONE: input already gathered there
		- DONE: print to output variable and then actually print buffer variable in main
			- DONE: redirected to output in printtw and appending with each print
				- DONE: used global variable 'output' to avoid passing to printtw a zillion times
				- DONE: still getting repeat prints due to printing within printtw
			- DONE: return 'output' from interpet_txt and print from main routine (as expected, non printtw text is now first)
			- DONE: convert all prints via printtw
			- DONE: troubleshoot print spacing (eliminated "/n" as needed)
	-2.1.3 - client-server deployment
			- DONE: separated dark-castle into front-end and back-end routines!
			- DONE: successful win play-through test
			- DONE: reduce imports for main where possible
			- DONE: full play-through test
- 2.1.3 (detail)
	- DONE: Break into to 'dark_castle2' and 'interpreter' and call 'interpreter' from 'dark_castle2'
		- DONE: move imports to main routine
		- DONE: move all static lists & dictionaries into interpreter_txt
		- DONE: move all variable lists & dictionaries into main and pass back & forth
		- DONE: testing and troubleshooing - win play-through
			- nb: most of my errors were just long-standing variable passing misses... I guess it was lax in the monolithic form
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
2.1.4 - Clean-up
	- DONE: Additional Puzzle Clues:
		- DONE: call the crown 'royal_crown' in Nana's memory
		- DONE: Indicate in the grimy_axe description that it could kill a crocodile
			- 'small_print' = 'ACME Axe: Effective at dispatching small dragons, large crocidiles, and even the most agressive of trees.'
	- DONE: Features:
		- DONE: Add a 'version' command (set in static_dict['version'])
		- DONE: Add 'you can't X and object that's not in your hand' error for allowed_verbs; also: 'you can only read text'
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

- 2.2.x
		- 2.2.2
			- DONE: Write up git for pythonanwhere steps
			- DONE: Someday - moves, score, and version presented continuously in corners of index.htm.		
			- DONE: remove old score / move table
			- DONE: How to get static_dict values to dc22_main ??
			- DONE: Unify version doc
			- DONE: Move completed updates to castle_done
			- DONE: Commit and tag as 2.2.2 Complete
			- DONE: Reset moves and score to zero in flask restart code
		-2.2.3
			- Learn how CSS and HTML relate to jinja and flask
				- DONE: Started watching "CSS Crash Course for Absolute Beginners" on YouTube
				- DONE: Watch Jinja tutorial: https://youtu.be/7M1MaAPWnYg
				- DONE: Better understand web server role vs. flask
				- DONE: Update overview diagram
				- DONE: Vital next step - Sept 19, 2020 - Download and play some Infocome games ;-D 
				- DONE: Plan out web site - What tabs and content to include
					- tabs:
						- Adventure
						- About
					- page layout:
						- Header: dark gray
						- NavBar: black
						- Showcase:
							- Art: https://www.canstockphoto.com/twelve-angle-stone-43317519.html
							- Text: Have Fun Storming the Castle
							- Matches Zork font: https://en.wikipedia.org/wiki/Zork#/media/File:Zork_I_box_art.jpg
						- Content: light gray
						- Footer: black
					- Content
						- Adventure:
							- Alerts
							- Response
							- Form fields
						- About:
							- Black: sidebar (Zork quote?), What is IF?, Git links

- 2.3.x - Update existing environment and polish existing flask code
	- DONE!!: troubleshoot existing game issues
		- undefined erro on output when called for index.html render; same error local & on PA
		- seems to be a global vs. local variables - renamed flask 'output' => 'flask_output'; maybe helped??
		- Site seems to be working again? 
	- DONE!!: create base_new.html
		- initial draft created but can't test due to game error
		- when I try swapping in base_new.html I get a global undefined error on flask_output... and keep getting it even when I switch base_new => base again?? Even after restarting?!?
	- DONE: Dig into Flask code and really understand it and get it running right
		- I'm now convinced that the problem is "time" or "run itteration" based... every morning the program runs fine but then I work on other things and by the time I get back to it I get the same 'flask_output undefined' error
		- to test this, today I referenced base_new.html in index... we'll see if tomorrow it runs fine
		- I suspect that what I need to do is formally pass 'output' within interpreter.py but this is a pain because I call printtw() so many times from so many places... perhaps 'output' becomes a value in state_dict[] ? NO!! - that won't work - because then it will blow up my cookie 4 KB space limit :() 
		- Confirmed: base_new.html worked fine until I got to quit
		- Tested my suspicions about the problem being 'output' as a global in dc22_interpreter.py... created static_dict['global_dict']['output'] and stored output value here... still got 'flask_output' undefined but possibly this is a temporarily persistent state issue? We'll see if this change fixes the problem tomorrow (I doubt it); If not, time to drill down deeper into the flask code itself... problem seems to happen after quiting - need to walk through what happens to flask_output after user_input = 'quit' 
		- Confirmed, flask app looses its mind right after 'quit' - need to figure this out
		- Had an unexpected result of moving 'output' to 'static_dict' => output did not reset! instead it kept building up the output history between user inputs! Did not expect this. Also don't think it will work in multi-user mode. not sure why the variable definition isn't working but need to investigate
		- Set static_dict 'output' to "" at start of interpreter_text
		- Need to carefully observe output on quit tomorrow morning; Are flash alerts and end of game score and title printed on 'quit'?
	- DONE: Fix need for double entry post restart
		- Now I understande why we get the intro screen twice upon restart... we need to show something once restart is pressed - but all variables will be reset on next run of 'main'... maybe need an interstitial flask_output of "PRESS ANY KEY TO RESTART"
	- DONE: Address restart interstitial
	- DONE: Simplify flask code - eliminate start_of_game (see flow notes below)
	- DONE: Simplify flask code - eliminate double interpreter_text call (see flow notes below)
	- DONE: Clean up code comments
	- DONE: Updte version number to 2.3.0
	- DONE: Clean up redundant flask variable assignments
	- DONE: Fully understand Flask code and comment all use cases
	- DONE: Update pythonanywhere code and test / troubleshoot
	- Address flow notes:
		- DONE: Why not 'else' instead of 'if not start_of_game' ???
		- DONE: flask_output is not a session variable... does it persist? Presumably not? So flask_output is undefined until interpreter_text assignment; Fixed this; flask_output, max_score, and version now all set to "" at start of code
		- DONE: found the problem I think!! If quit but not yet Restart then python code never runs and flask output is undefined!!
		- DONE: Immedite fix is to set flask_output in this case (ditto for max_score and version) and set "" value at start of code
		- DONE: no longer need flask_output defined in first 'if id exist'; create separate section for local variables in main routine
		- DONE: improve on 'press any key to restart' interstitial? Maybe move pwd reset to near bottom? (i.e. if 'id' exist: <...> else:)
		- DONE: moved 'if id is in session' to just above 'if start_of_game == True'... now I'm wondering... do I really need start of game?? Is there ever a case where it's not start of game and fresh variable assignment?? Can I just make the "start of game run" a continuatio of the variable assignment "if"?
		- DONE: Wondering if I can consolidate the 2 interpreter_text calls just before the 'return rneder_template'... at the end of the day there really only seem to be 2 choices... either game_over == True, in which case we flash "Hit Restart"... or game_over == False... in which case we need to call interpreter_text...
- DONE: update flow model with any changes!! Keep this accurate!!

- 2.4.x update CSS and jinja
	- DONE: Start by applying "my website" CSS to Dark Castle
		- DONE: Figured out CSS has to live in Static for jinja!!! (had forgotten that the directory structure is fixed)
		- LESSON LEARNED: NEED TO RESTART PYTHONISTA FOR CSS CHANGES (VS. BASE OR INDEX CHANGES) TO TAKE EFFECT!!!
		- DONE: Customize CSS to match Dark Castle theme
			- DONE: Reset my_website CSS (rename current to style_old.css and start over with fresh css file)
			- DONE: Next change elements in CSS one by one with Pythonista restarts in-between and tune to my liking
	- DONE: Design of game page
		- WRONG: Struggling to reference image - figure out url_for : https://pythonise.com/series/learning-flask/serving-static-files-with-flask
		- DONE: css is static - so don't use url_for... key is that the image must be in ROOT of STATIC
		- DONE: Tune stone.jpg image for showcase
		- DONE: Used my own photo of a stone wall for showcase
		- DONE: How to set right margins??
		- DONE: Stone background similar to zork for showcase?		
- IN-PROC: Rest of web site
	- IN-PROC: Create Read Me page for Nav Bar
		- DONE: Create initial readme.html
		- DONE: Link readme.html in navbar and flask
	- DONE: Create What is IF page
	- DONE: Create "If you taach a Dad some Python" page
	- DONE: Make flash text blue (this is harder than I thought - requires some flask + CSS)
	- DONE: Consider implementing word wrap in jinja template wordwrap() rather than hard coded in dc22_interpreter printtw()
	- DONE: Clean-up game page
		- DONE: Game text box
		- DONE: Align text box and buttons on same line (just remove </p> ?)
		- DONE: Align "version" on same line as buttons
	- DONE: Update version code (in code and in static_dict)
	- DONE: Full "new player" test play

-2.5.x
	- DONE: Doc organize
		- DONE: Move "dones" from castle_to_do2.md to castle_done2
		- DONE: Move pseudo-code flow from castle_to_do2.md to castle_flow25
		- DONE: Move doc files to /doc
	- DONE: Clean up repo with only the needed code
		- DONE: Move old code to /legacy
		- DONE: Delete unused css and image files
	- IN-PROC: Write doc updates for Flask
		- DONE: "Just put it on the web"
		- DONE: Functionalizing
		- DONE: Flask and Jinja
		- DONE: Storing the Data
		- DONE: CSS
		- DONE: Overview Diagram
			- DONE: Study Good Links:
				- https://docs.python-guide.org/scenarios/web/
				- nginx gunicorn jinja2 flask python
				- jinja2 flask architecture diagram
				- https://machinesaredigging.com/2013/10/29/how-does-a-web-session-work/
				- https://programmer.help/blogs/getting-started-with-flask.html#一、架构简介
				- https://sidsbits.com/Serving-Flask/
				- https://atlasbioinfo.github.io/生物信息/2019/06/12/Flask搭建生物学数据库全流程/
			- DONE: Create new 3-tier diagram
				- DONE: Define Elements: browser, web server, WSGI, Flask, Jinja2, static content, Python, seesion cookie, dev workstation, Git
				- DONE: Hand draw framework
				- DONE: Narrative of dev flow
					- A. Files live in Working Copy iPad Git client
					- B. Pythonista IDE and Textastic text editor update documents in Working Copy
					- C. Working Copy updates are committed locally 
					- C. Working Copy updates are pushed to GitHub origin via Git protocol (port 9418; similar to ssh but no auth)
					- E. From bash console, pull GitHub updates to pythonanywhere.com via Git protocol 
				- DONE: Narrative of browser flow
					- 1. Based on the URL entered, the Client Browser hits the Web Server hosted on pythonanywhere.com. At present, NGiNX is the most popular dedicated Web Server but I have no knowledge of what Web Server pythonanywhere.com uses.
					- 2. Web Server communicates with WSGI (Web Server Gateway Interface). The WSGI is middleware that allows any WSGI-compliant Web Server to interface with any WSGI-compliant app framework. gUnicorn (Green Unicorn) is presently the most popluar dedicated WSGI but I have no knowledge of what WSGI pythonanaywhere uses.
					- 3. WSGI interfaces with Flask Micro-Framework
					- 4. Flask pulls (or creates) sessision variables stored in client side cookies; Usually just User ID but in my code all persistent variables. Also, based on the url address requested, Flask routes to the correct html generation sequence.
					- 5. Flask Micro-Framework calls Python Function. Each instance of the Python Function runs in its own memory space.
					- 6. Typically the Python Function would use a DB key stored in session variables to read & write session-specific data from a Database (e.g. SQLAlchemy) but in my code it's all in cookies
					- 7. The Python function returns varables to Flask
					- 8. Flask updates persistent session variables and stores them in the browser cookie 
					- 9. Flask passes the data returned by thge Python Function to the Jinja2 Template Engine
					- 10. Jinja2 merges the Python Function data with the HTML Templates in /templates (e.g. base.html, index.html) to produce the Custom HTML Web Page (Note: the /templates location is defined by Flask which is tightly integrated with Jinja2)
					- 11. Jinja2 returns the Custom HTML Web Page to Flask
					- 12. The Custom HTML Web Page is sent by Flask to the WSGI 
					- 13. The WSGI passes the Custom HTML Web Page to the Web Server
					- 14. The Web Server applies static content (e.g. CSS styling and images) to the Custom HTML Web Page (Note: the /static location is defined by Flask but I believe it is applied to the Custome HTML Page by the Web Server)
					- 15. The Web Server returns the Fully Formatted Web Page to the Client Browser
				- DONE: Review / validate Browser Flow Narrative
				- DONE: Label what is passed between each element
					- DONE: Left half of diagram
					- DONE: Right half of diagram
				- DONE: Move to draw.io
					- DONE: Client Side
					- DONE: Web
					- DONE: App & DB
					- DONE: Web Connectors
					- DONE: Dev Connectors & Labels
					- DONE: Review and update Web Flow label text
					- DONE: Update cookie in diagram and add Web Labels
				- DONE: Final review of diagram and Flow text
				- IN-PROC: Create "How (I think) It Works" (howit.html) html page containing diagram (w/ github link) and description; req feedback
					- DONE: raw page created
					- DONE: Intro and deve text
					- DONE: Image
					- DONE: Web flow text
					- DONE: Update Flask code
					- DONE: Update base.html with new nav bar link
					- DONE: Scale image
					- DONE: Convert uls to links
	- DONE: Update version code (in code and in static_dict)
  - DONE: Create Dedicated feedback email
  	- DONE: Create new email and link to personal email
  	- DONE: Create email image and add to web pages - version 1
  	- DONE: version 2 of email email image (email11 looks good on iPad in IDE browser)
  	- DONE: Push to pythonanywhere and then test on different screens
  	- DONE: Clean up old email images and put final image at bottom of readme page
	- IN_PROC: "publish" to friends and ask for feedback
		- DONE: List of usual suspects:
		- DONE: Final decision on BCC: vs. CC: vs. FB (neither - small groups)
		- IN-PROC: Send!
			- DONE: Tara S, Ben F, Franco B, Geoff T, Mickey & Bonie S, Jon S, Matt C, Andy E-O, Karl D, Ken T, Facebook
