+++ Documentation +++


*** Preamble ***

- What Exactly is a Text Adventure / Interactive Fiction Game:

	- Wikipedia: "Interactive fiction, often abbreviated IF, is software simulating environments in which players use text commands to control characters and influence the environment."

	- I grew up calling IF "Text Adventures". I was 12 when Infocom released Zork I for the Commodore 64 and it blew my mind. At the time computer graphics were very primative. Fine if you wanted an arcade "twitch" experience like Pac Man or Galaga... but not something that could pull you into a story. Zork changed all that... suddenly there was a detailed fantasy setting where I could be the main character. It was the computer version of reading a "Choose Your Own Adventure" book - but with infinitely more freedome. Like being set down in Middle Earth or Narnia and asked simply "Where do you want to go next?". I was overjoyed.

	- I came to IF for the stories but I stayed for the puzzles. Games like Zork did not rely primarily on roling dice, collecting gear, and gaining levels in the fashion of my other favorite childhood hobby, D&D (though Zork combat does have a minor element of chance to it). Instead, IF was all about solving a series of interlinked logic puzzles. And man could those puzzles be madening! This was back before Google. Back before the World Wide Web. If you got stuck you either had to mail order the Invisclues hint book - which cost about a third the price of the game and took weeks to arrive - or find someone who had solved it already and beg for answers. In my case I had one friend who had solved nearly every Infocom Text Adventure released - but at the time I only saw him at school during lunch period. So I might get stuck on a puzzle over the weekend and not see him till Monday... and then my friend (yes, Im talking about you Geoff!) might well say "That's a really easy puzzle - you don't need a hint - you just need to think about it a bit more". Argh!!

	- The positive side to frustration was engagement and satisfaction. I would wander around the real with the puzzles in my head - replaying the steps I'd tried already again and again and thinking about new things to try in order to make progress. And when I did finally have a breakthrough it was a genuine triumph. I can still vividly recall the thrill of getting the Platinum Bar for the first time in Zork.

	- When I first started learning Python (as part of an AI Coursera course) I marvelled at how well it managed text and lists. So, not unsurprisingly, when I decided to start a Python project to really learn the language, a Text Adventure seemed like a natural fit. That said, it's important to be aware, while writing IF is a great way to *learn* Pyhton, it's certainly not the best way to *write* IF. That would be TADS - which is a purpose built language specifically created for IF and supported by a rich community of amerature IF game writers: https://www.tads.org

	- I also heartily recommend that you try out "real" IF if you haven't already.
		- Here is a link to play Zork I on the web: https://playclassic.games/games/adventure-dos-games-online/play-zork-great-underground-empire-online/
		- Here's a link to IFDB - one of the most widest and most active repositories of IF content: https://ifdb.tads.org
		- Lastly, if you're an Apple iOS user, I recommend the "Frotz" app. It's an older compiler but it still has a rich collection of works for free.

*** Web Updates ***

This is a documentation addendum that covers the updates made to web-enab dark_castle

"Just Put it on the Web"

- I had expected that sharing the app on the web to be pretty simple... because the web is ubiquitous and I assumed anything common would be easy. In the event, this turned out to be one of the hardest parts of writing the app.
- The challenge was that I was fundamentally ignorant of how web apps worked - I really didn't know what I didn't know. I learned PASCAL in highschool on an Apple IIc and that formed the basis for my mental model of how an application runs. It was a single-threaded, single-user, stateful environment. When you were running your program on the IIc that was *all* the IIc was doing. The program owned standard input / output and the user was either interacting with the programming or exiting out of it. And there was only one user. So the program could keep everything in memory in a simple stateful fashion. Also, the program was a bit like a novel... it had a beginning, a middle, and an end. The program did some work and then it finished.. it didn't just hang about waiting for another user interaction all the time. This experience from highschool shaped my mental model of applications for the next 35 years - right up through writing dark_castle.
- By contrast, as I came to learn, a web app is innately stateless, multi-user, and available. Since the program itself is stateless, you need to store the data somewhere (typically a DB but in my very simple case a client-side session cookie). Since any number of users could be using the app simultaneously you need to embrace the concept of session variables... i.e. a separate set of variables for each user. And lastly, the web never just stops. It's always out there. And users interact with it very asynchronously... maybe they use your web app for 5 minutes and then get and email, reply to that, and then come back to your app's browser tab in 5 minutes. Or 5 hours. Or 5 days. So if your program is on the web you always need to be ready for the user to stop using it at any time and come back to it at any time. 
- To a web programmer these decarlations must seem blazingly obvious but to me this was all brand new. YouTube videos were great at teaching me specific tools and frameworks but getting these concepts into my head took a lot of trial and error. On the plus side, I've been supporting web servers at the OS level for 25 years and now finally I have some idea what they're actually doing - so maybe old dogs can learn new tricks ;-D


Functionalizing

Flask and Jinja

CSS




*** Game Overview - Console Version ***

- Program Summary:
	- A simple Zork-like Text Adventure / Interactive Fiction.
	- My primary goal in writing the game is to learn Python. This is my first "written from scratch" Python program.


- Program approach:
	- The coding style (for better or worse) is nearly 'anti-object-oriented'
	- Verbs are the central construct of the code
	- Everything else is a series of loosely connected (at best) dictionaries and lists
	- This is not something I set out to do.. the style arose naturally from beginner programming techniques and a 'figure it out as I go' approach to writing the text adventure
	- The result is code that is challenging to maintain and extend because you need to update so many diseparate lists anytime you want to change anything
	- Although not ideal from a coding standpoint I don't really have any regrets. This has given me a lot of practice with lists and dictionaries and a deep appreciation for object-oriented coding


- Program layout
	- A Main Routine that first imports modules and loads description.csv into description_dict
	- The Main Routine then takes user input and calls interpeter_text() until user input = 'quit'
	- The interpeter_text() function is an if - elif chain of all existing one-word commands and verbs
	- Each verb elif performs a standard action on allowed verbs (e.g. 'take' and item into the players 'hand')
	- Helper Routines assist with common tasks (e.g. print_score)
	- Situational_Logic routines address special puzzle cases where standard actions cause non-standard results (e.g. 'take shiny_sword' in the main_hall is blocked by a hungry hedgehog)
	- There are a collection of smaller static and stateful dictionaries and lists that hold game variables (e.g. room_dict)


- Linguistics (such as they are):
	- The linguistics are extremely primitive
	- All sentences are either one word or 2-word noun-verb pairs
	- There are no articles, adjectives, adverbs, prepositions, or direct objects
	- This means you can 'take' the scroll_of_the_king out of the container but you litterally can't put it back (i.e. a full implementation of 'put' is impossible in a noun-verb pair)
	- One of my main user experience goals for version 2.0 is to enrich the interpreter
	- From a writing standpoint Dark Castle is intentionally a bit "purple prose". This is partly in immitation of Zork. And partly because any game that depends entirely on words should embrace language with sumptuous exuberence.


*** Nouns ***

- Noun types:
	- Items: Nouns that can be taken
	- Features: Nouns that can be interacted with but not taken. Includes doors, containers, creatures, and switches.
	- Vew_only: Nounds that can be examined but not taken or interacted with.

	- Doors: May be locked or unlocked (with the right key). If unlocked a door can be opened. Finding a way to open a door is one of the most basic puzzle elements in the game.

	- Containers: Like doors, containers can be locked or unlocked and open or closed. Also, they can contain things. Once a container i open it's contents are added to the room 'items' and may be taken. Due to linguistic limitations (i.e. only noun verb pairs) items cannot be put back into a container. No concept of container capaicty has been coded yet.

			- Note on Doors and Containers: At present only 'unlock' and 'open' are implemented. I plan to implement 'close' and 'lock' when I write a puzzle that utilizes these. It does irk me that Burt wanders through Dark Castle like some random murder hobo leaving a swath of unclosed doors behind him. I picture his Nana yelling "Burty Baker, for goodness sake, close the door behind you!". I'm also considering implementing 'put' <item> to place something in a container... this would limit the game to one container per room - but that seems like a reasonable tradeoff.

	- Switches: Set values and trigger effects. At present 'levers' are implemented to set values and 'buttons' trigger effects but the reverse is also possible. Also other switch types are possible - e.g. dials, knobs, switches, etc.

	- Creatures: Living entities that Burt can interact with. These may be helpul (like the 'hedgehog' when treated well) or hazardous (like the 'goblin' and 'crocodile'). Finding the right gift or weapon needed to interact with a creature is a common puzzle element in the game.


*** Verbs ***

- Verb overview:
	- For better or worse, verbs are the heart of the program; its primary organizing structure. Nouns come and go from list to list but verbs drive the program and the story forward.
	- Each noun-verb pair verb is an ifel in the interpreter_text loop
	- Each verb ifel has some common features: 
		- Before the verb ifel statements, check for a pre-action tirgger; Escape if one exists
		- At the start of each verb ifel, check for scope to ensure that the command is possible (i.e. the item is 'takeable' or 'wearable' or such).
		- Asign local variables to make dictionary calls shorter and clearer
		- Upon confirming scope and performing action each verb ifel confirms success to the player (e.g. 'Taken', 'Openned', etc)
		- At the end of each verb ifel statement check for post-action triggers
		- At the end of each verb ifel statment check score_key for score changes.


- Verbs-Noun Interactions:
	- examine: Many things can be examined. Scope = room scope + inventory scope + view_special + room name. Probably the most frequently used verb in the game. Check's specially for open containers and lists their contents.

	- take: Items can be taken. Scope = room items + backpack + worn. Possibly the most complicated verb. Upon confirming scope, adds the taken item to 'hand'. Adds the current contents of 'hand' to 'backpack'. Updates the 'backpack' or 'worn' lists or the room or container dictionaries to remove the taken item from its source.  Adds a 'nothing' placeholder to 'backpack' or 'worn' if 'take' leaves them empty.

	- drop: Items in your hand can be dropped. Scope = 'hand'. Dropped items are added to the room dictionary. If 'hand' contains 'nothing' then don't allow 'drop'.
	
	- open: Doors and container features can be opened. Scope = allowed_language['can_be_openned'] and (feature in room) and (not open) and (not locked). There is code to update the door / container description as "open". If the feature is a container and opening reveals contents then the contents are revealed and added to the rooms inventory.

	- unlock: Doors and container features can be unlocked. Scope = allowed_language['can_be_openned'] and (feature in room) and (not open) and (is locked). Upon confirming scope, test to ensure that the player has the correct key in 'hand'. If so, set door state to 'unlocked'.

	- read: Some items or features have text on them. Text can be read. Scope = allowed_language[can_be_read] and (room scope + inventory scope). Check to ensure that the text referenced is written on an item or feature that is in scope. If so, print the text message.

	- attack: Creature features can be attacked. The results of the attack may vary based on whether the player has a weapon (e.g. the shiny_sword or the grimy_axe) or just their fists. Attack results are deterministic based on creature and attack weapon (i.e. there are no die rolls). Ultimately, creatures are more puzzles to solve than they are RPG enemies to defeat. Scope = allowed_language[can_be_attacked] and (creature is in room_features). If attack is in scope, 'hand' is checked to determine attack_weapon (if no weapon in hand, attack_weapon = 'fist'). Based on creature and attack_weapon an attack description is printed. Then, based on attack_weapon, an attack result is looked up in creature_dict. The three possilbe results are 'creature_death', 'creature_runs', and 'player_death'. player_death prints a result description and calls end(). creature_runs prints a result description, removes the creature from room_features, and updates score. creature_death removes creature from room_features and replaces it with dead_creature, prints a result description, updates score, and then adds any 'drops' items (stored in creature_dict) to room_items. Because score is dependent on attack_result, attack is the only verb that does not genericaly check score at the end of the verb ifel.

	- eat: Food can be eaten. This is probably my least implemented verb. You can't actually eat anything in the game but I thought it was only fair to let the player attempt to eat the stale_biscuits. Scope = allowed_language[can_be_eaten] and (in 'hand'). If scope is met, print eat description. There is a food_dict sub-dictionary in static_dict meant to track eating results but this is not currently implemented.

	- pull: Levers can be pulled to change a state as a standard action. Other features may be pulled via trigger. Scope = allowed_lang_dict[can_be_pulled] and in (room_view_only or room_features). If in scope and word2 is in switch_dict, swap switch_state from up to down or vice versa and update switch description. For cases other than levers controlling state, trigger can be used to initiate an action (e.g. 'pull throne').

	- push: Buttons can be pushed to trigger an action as a standard action. Other features may be pushed via trigger. Scope = allowed_lang_dict[can_be_pushed] and in (room_view_only or room_features). If in scope and word2 is in switch_dict check to see is switch success value == current switch value. If it does update trigger_key and score_key (the actual action will be handled via the tirgger routine). If switch success value != current switch value print failure description. I also track button pushes. Non-button push cases (e.g. push throne) can be handeled via trigger.

	- wear: Garments can be worn. Scope = allowed_lang_lst['can_be_worn'] and (item in 'hand'). If scope conditions are met, append garment to 'worn' and clean up "nothing" placeholder if needed ('worn' is tracked in state_dict[worn] so that it can be printed during inventory). Remove garment from 'hand' and add "nothing" placeholder if needed. Print confirmation of command to player along with any effects of donning the garment. At present the only wearable item is the royal_crown. It feels like the hedgehog_broach should also be wearable but I feared that this would be a red herring for the scroll_of_the_king puzzle. I'd like to add one more room that provides a puzzle that is solved by wearing the hedgehog_broach.

	- close: [future] "For the love of God Burt, close the door!". Would like a puzzle that requires 'cloes'
	- lock: [future] Feels like if you can unlock something you should be able to lock it. Again, puzzle needed.
	- put: [future] Place contents of 'hand' in container. Syntax = "put <item>". Assumes one container per room.
	- give: [future] Give contents of 'hand' to a creature. Syntax = "give <item>". Assumes one creature per room.
	- stow: [future] Explicitly put something into your backpack. Syntax = "stow <item>".
	- swap: [future] Swap the contents of 'hand' with a takeable item. Syntax = "swap <takeable item>". Puzzle needed.


*** The Game World ***

- The world and the "laws of physics" within which, and according to which, the game takes place. 
	
- Inventory:
	- Your inventory scope includes the contents of your hand, backpack, and what you are wearing.
	- Hand: Can hold exactly one item. Anything taken goes into your hand. Anything dropped is dropped from your hand. Something must be in your hand in order to drop, wear, or eat it.
	- Backpack: Items can be taken from your backpack. There is no mechanic to intentionally place something in your backpak but any overflow from your hand (i.e. if you are holding the 'rusty_key' and take the 'shiny_sword', the 'rusty_key' is automatically placed in your backpack). Unlike in the game Zork, there is no capacity limit to your backpack.
	- Worn: In theory, multiple items can be worn but at paresent only the 'royal_crown' is wearable. Wearing an item may have an effect (e.g. the 'royal_crown' enables the magic of the 'scroll_of_the_king').
	- The word "nothing" is used as a placeholder for an empty inventory slot. This is a bit of a pain to manage in the code but provides postive confirmation to the player that their hand (for example) is empty.
	- Your inventory is tracked in state_dict and printed to the player by invoking the 'inventory' command.

- Rooms: 
	- Everything in the game happens in a 'room' (the 'room where it happens'). In IF 'room' does not imply "four walls". Here 'room' is defined as any specific setting you can move to. 
	- Every room has: A title (e.g. "*** Main Hall ***"), a description, a collection of nouns (items, features, and view_only), and some available exits.
	- From a noun perspective, room scope = items + features (including creatures) + view_only + the contents of open containers. Each room has its own scope - if a noun is in the scope of one room it is generally not available in another room unless it is an item and the player caries it there.
	- The room layout in Dark Castle is extremely simple - there are only four rooms and each one is north of the next. An innate objective of the game is to gain access to the next unexplored room.
	- The room structure itself is stored in room_dict which tracks the items, features, and view_only that exist in each room. The dictionary is updated as items are picked up and moved around.
	- It's a measure of the list-centric and disjointed nature of my programming strucuture that no information about exits resides in room_dict. Instead, exits live in their own separate dictionary. You would never know that you could travel north from the main_hall just by inspecting room_dict. What can I say... code and learn ;-D

- Movement:
	- After taking and examining, movement is propably the most basic function in IF. Many puzzles are solved in order to be able to move into an unexplored area.
	- I decided to treat rooms and the paths between them as separate entities. In retrospect I think embeding path options into rooms would have been simpler but I was working it out as I went.
	- The four allowed movement directions in the game are north, south, east, and west. These are tracked in allowed_movement
	- If the player inputs a direction in allowed_movement, interpreter_text sets path_key = <current room>_<direction> and checks to see if the path_key exists in path_dict. If it does, an "approaching path" description is printed to the player and room_action() is called. If it doesn't, an error message from invalid_path_lst is printed.
	- [I'm considering geting rid of the "approaching room" description.. I implemented it in the spirit of "always confirm action success - then provide action results" (e.g. 'push button' => 'pushed' followed by <result>). However, in the case of paths this seems like overkill. And the text is quite vague since I can't yet know if they will actually be able to enter the next room (if there's a door).]
	- room_action() checks path_dict for one of three possible actions: 'death', 'door', or 'passage'.
		- 'passage': Means there is no barier to entering the next room. 'room' is updated in state_dict and look() is executed on the next room.
		- 'door': Means there is a door between the current room and the next door. If door_state = 'open' the player proceeds as if the action were 'passage'. If door_state != 'open' a "door closed" message is printed to the player.
		- 'death': game_ending is updated to 'death' and end() is called. This action is intended for cases where the player has moved in a direction that is fatal (e.g. walking off the drawbridge without a weapon). In this case the "you chose poorly" message is in the path_description and then they go straight to the end() routine. In hindsight this is not a very elegant approach to this case... but this was one of the very first outcomes I was coding so I was still sorting out the basic structure of the game.
	- For each path, path_dict stores 'action', 'door' (i.e. "door name", 'none' for no door), and 'next_room' ('none' if no next room exists)

- Switches:
	- Switches are the generic name I give to the levers and button that make up the Antechamber iron_portcullis puzzle. A random value between 0 and 7 is set for the big_red_button['success_value'] in the main routine at the very start of the game. This value is written (somewhat crypticaly) in messy_handwriting on the torn_note that the goblin drops when it dies. The player then needs to set the 3 levers (left, middle, and right) to the same value using binary notation. If the levers match success_value then when you push the big_red_button the iron_portcullis   will open.
	- There are six code components used to enable switching:
		- The switch_dict dictionary holds the state of each lever (they all start 'down'; down = 0) and the success_value, current_value, and press_count of the big red button.
		- The verb 'pull' allows the player to swap the state of the levers from 'down' to 'up' (0 to 1) or vice versa. The descriptions for each lever are updated as well.
		- The verb 'push' enables the player to push the big_red_button. Push calls switch_value() to esatblish the current_value the levers are set to, compares it to success_value, and if they match updates trigger_key and score_key to indicate success. If current_value and success value don't match then a failure message is printed. At the end of 'push' trigger() and score() are called.
		- switch_value calculates the current_value (in binary notation) of the lever settings and returns it to push()
		- trigger() is called at the end of the 'push' verb elif. If the trigger_key has been updated to indicate success, then the door state is toggled (i.e. if currently 'down' now 'up'), a result is printed to the user, and the description is updated.
		- score() is called at the end of the 'push' verb elif. Upon the first successful press of the big_red_button the score is incremented.
	- Although the switch components are implemented in a very puzzle specific way, they are all written to be extensible for additional switches. A core problem here is that there is no "generic" switch capability in the game... each switch scenario has to be hand coded and added to the routines listed above as a special case. In a tiny game like mine this is fine. In a larger game with more switches this would rapidly become cumbersome.
	- It could be argued that the puzzle to get the hedgehog_broach is essentially a switch puzzle and so perhaps it should be implemented as such. Since the results of both are handled by trigger() in some way they are handled the same.
	- Switch is another fine example of the listy nature of my coding. Instead of baking the behavior of the levers and button into the nouns I spread them across a dictionary and three functions. Stepping back and reviewing this from affar it is clearly not ideal - tracking and maintaining switch state would be a nightmare for a game with many switches.


*** Program Mechanics ****

- Most of the game is simply the player interacting with the game world by invoking verbs to move nouns from one list to another and then printing the results. But some of the behind the scenes interactions are a bit more involved. I call these "mechanics". Mecahnics are ultimately an act of "slight of hand" - in the ideal game the there would be no explicit mechanics - all of the interactions would be accounted for already by the nouns, verbs, and game world - but in this case that's a very lofty ideal.

- Triggers: 
	- Each verb has a 'standard action' - e.g. if you 'take' an item the standard action is to add it to your 'hand'. 
	- Standard actions are carried out by verb code. However, in some cases, an action has situation-specific results (e.g. if you attempt to take the shiny_sword in the Great Hall the hedgehog will bar your path). This is where triggers come in. 

	- Triggers come in two flavors: 1) pre-action triggers and 2) post-action triggers. As implied by their name, pre-action triggers execute *before* a verb action (e.g. the hedgehog bars your way before you are able to take the shiny_sword). By contrast, post-action triggers execute *after* you have taken an action (e.g. after you successfully drop the shiny_sword in the Great Hall the hedgehog offers up the silver_key). 

	- Each user input checks for pre-action triggers before invoking any trigger logic and post-action triggers after the standard action code in each verb ifel. Triggers are identified by the 'trigger key' - which by default is 'word1-word2'.

	- Standard actions are generic in nature. Triggers are typically story / situation-specific. Most of the game puzzles depend on triggers because puzzles themselves tend to be situation-specific.

- Timers:
	- Time in the game is measured in 'moves'. The move counter is incremented by one with each user input (with a subsequent decrement by one for "unknown word' cases).
	- Move count is tracked in state_dict and can be incorporated into puzzles.
	- Some situations or opportunities only prevail for a limited number of moves.

	- There is currently only one timer in use in the game - it is linked to the shiny_sword puzzle. When a player drops the stale_biscuits the hedgehog will spend the next 5 moves eating them. If the player does not take the shiny_sword within that time window the hedgehog will return to his vigilant guarding state and the player will never be able to get the shiny_sword or win the game.

	- The existence of an active timer is tracked in state_dict['active_timer'] and the count on a given timer is tracked in state_dict[timer_dict]. The timer duration itself is set outside of the timer rountine (in the case of the shiny_sword puzzile it is set in the drop-stale_biscuits trigger).

	- The main routine check's for an active_timer on each loop and calls the timer() routine if one exists. The code for a specific timer is referenced via its 'timer key' (typically 'word1_word2'). Within the code for a specific timer timer_num is decremented each move and a timer description is printed to the user. The idea behind the timer description is that the player needs some awareness that the situation is changing with passage of time. In the case of the shiny_sword puzzle this is provided by tracking how much of the stale_biscuits the hedgehog has finished eating.

	- Special cases are also handled in the specific timer code. For example, it is possible for the player to grab the shiny_sword on the first timer move and then attack the hedgehog with it on the very next move (which scares the hedgehog away). The timer needs to halt if the hedgehog is not in the room. Likewise, the timer has to keep functioning but the descriptions of the hedgehog eating need to halt if if the player walks out of the Main Hall.

	- Frankly, the timer code is limited and a bit kludgey. Because active_timer takes a single value you can only have one timer running at a time. And many of the functions managed in the timer-specific code could be generalized across multiple timers (e.g. decrementing the timer). Someday if I add more timers to the game I will clean this up a bit. 

- Description Updates:
	- Most noun descriptions are static but some do change over time.
	- Simple cases like doors ('open' or 'closed') or levers ('down' or 'up') are updated in the elif of the verb that changes their state.
	- But some cases are more complex. In particular, the hedgehog's appearance changes depending on the circumstances and that appearance (famished, focussed on eating, looking expectantly) is often an important puzzle clue.
	- Complex description updates are handled by the description_update() function. The function takes the current description_key (e.g. 'hedgehog') and sets it equal t the update_key (e.g. 'hedgehog_eating').
	- This is another aspect of the listy nature of my coding choices. The hedgehog's responses to attacks live in creature_dict, his multiple descriptions live in desctiption_dict, and the logic that determines his current appearnace lives in triggers. It works, and the dictionary key naming is pretty clear, but it's still mighty hard to follow!

- Scoring:
	- Scoring gives the player a feeling of accomplishment and re-enforces when they have made a right choice.
	- As with many other aspects of Dark Casle I am modeling the scoring off of Zork. One departure is that I provide negative scoring for bad choices (e.g. scaring off the hedgehog).
	- When the game ends the player gets a title based on their score.
	- current_score is stored in state_dict and starts at zero. state_dict also contains score_dict which keys off the score_key for scorable events and holds values for the number of times an event has occurred and the score value of the event.
	- At the start of interpeter_text score_key is set to <word1>-<word2>. Than at the end of each verb elif, if score_key is in score_dict score() is called.
	- score() checks the score_event_count and, if it is 0, increments current_score by score_event_value and calls print_score(). Lastly, score() increments score_event_count.
	- print_score() print's the curent_score out of the max_score possible (which is stored in static_dict). print_score() is separate from score() since it is also called in end().
	- end() calculates title_score from current score. title_score = -10 if current_score is negative or title_score = current_score rounded to the nearest 10 if current_score is positive. Then based on title_score, end() looks up and prints the apropriate title from static_dict[titles_dict].
	- In a couple cases the player must not only accomplish an objective in order to score but must accomplish it successfully (e.g. 'push-big_red_button', 'read-scroll_of_the_king'). In these cases, the score_dict key has 'success' or 'win' appended to the end of it and this text is added to score_key in trigger(). In the special cases of the crocodile royal_crown puzzle, score_key is arbitrarily assigned in trigger() (as 'gator_crown' - demonstrating my poor grasp of reptile matters).  
	- As with so many other aspects of the game, the scoring functionality is distributed across multiple lists. Given that most score events are linked to when an item is taken, a door is openned, a room is entered, or a creature is interacted with, it seems like scoring could also be built into these entities.


*** Dictionaries and Lists ***

- Nearly all of the text in the game and much of it's structure live in a series of dictionaries. A database back end might be better in several respects but I wanted to practice using python dictionaries and lists and this appraoch game me plenty of practice. Initially, I just wrote the game with no planning or structure in mind and just created new dictionaries whenever I needed to track a new noun or machanic. this eventually got quite cumbersome from a variable passing standpoint so I started consolidating small "single depth" dictionaries into state_dict and static_dict. My general rule was that no dictionary could be more than two levels deep. I also categorized dictionaries as "static" or "variable" with the notion that if I ever created a game save functionality I would need to write the contents of all stateful dictionaries to files and then import them again during a restore process. I've included a few details about each dictionary below. 

- description_dict: Notable in several respects. For one, it is the only dictionary that is currently loaded from a text file. I did this partly because it is by far the largest dictionary, containing most of the text in the game. And partly because I wanted to learn more about file imports. In theory, description_dict is static in that as part of the restore process you could update all of the variable descriptions based on the states saved in other dictionaries.

- door_dict: Variable. Holds information on doors and containers. Keyed off the name of the door and has values for door_state (open or closed), locked_state, key (i.e. key name), is_container, and, in the special case of containers, 'contains'

- switch_dict: Variable. Tracks the state of all switches (e.g. levers and buttons)
	
- path_dict: Static. Keys have the format <room name>-<direction>. For each path values include 'action', 'door' (i.e. door name), and next_room. 'action' has possible values of 'none' (for paths that can't actually be taken but have some description text when attempted), 'passage' (no obsticle to taking path), 'door' (indicates that door_state must be checked in door_dict), or 'death' (e.g. stepping off the drawbirdge without a weapon into the crocodile-infested moat). In retrospect it seems like path information could have been integrated into rooms.

- room_dict: Variable. Keys are room names. Values include items, features (including creatures), and view_only (things that can be examined but not interacted with). In retrospect, rooms might have been a great place to centralize more information and logic (e.g. paths and descriptions).

- creature_dict: Variable. Keys off creature names. Values include 'drops' (what the creature drops if slain), 'state' (in theory, could be used to reset variable descriptions upon game restore - not currently implemented), and the attack results based on what weapon is used to attack. This approach to attack results doesn't seem to scale very well and would be a real pain if there were more weapons in the game.

- state_dict: Variable. Holds a lot of global values like the player's inventory, score, and move count.

- static_dict: Static. Holds a miscelaneous collection of static dictionaries that used to stand on their own.

- allowed_lang_dict: Static. Holds lists that define what verbs can be performed on which nouns. In retrospect, it would be far easier to code nouns if these capabilities were baked into the noun itself. Instead, every time you create a new noun you need to add it to the appropriate allowed_lang_dict lists. Code and learn ;-D


*** Puzzles ***

- In general the puzzles start very easy and get a bit harder with each room.
	
- Room 1: Very easy puzzles. The basic goal here is for the player to figure out how to play the game. They get points for accessing their inventory and then managing to open the front_gate. They also (probably) learn that Burt can perish if they don't carefully read the descriptions. They also (likely) learn a bit about their quest in the process.

- Room 2: Easy puzzles. The front_gate can be unlocked and opened without looking at anything but item names but players will probably have to examine the hedgehog in order to realize that it's hungry and might be interested in the stale_biscuits. The timer was fun to implement but does not add much additional challenge. The goblin in Room 3 is really part 2 of the Room 2 puzzle. He is effectively a door that cannot be opened without the right key (the shiny_sword).
	
- Room 3: Moderate puzzles. This is a little more tricky. The player must read the code on the torn_note and think to use the levers to match it in binary. I initially intended to make this tougher and have the iron_portcullis jam after 3 button pushes but eventually decided to make the adventure more beginner / kid friendly. A player who knows nothing about binary notation can simply try ever lever combination until they happen upon the right one.
	
- Room 4: More challenging puzzles. The player must get two mcguffins in order to solve the Room 4 puzzles and win the game. I did this because I have two kids and I wanted them each to be able to plan out their own room (containing the mcguffin) if they became inspired. So far they haven't come up with anything but time will tell. As the puzzles stand, they are a bit tricky for two reasons 1) the needed items are not immediately at hand and 2) the actions required are a bit counter-intuitive. The player gained points for getting the shiny_sword and it's already proven quite useful. There are clues to the need to return it to the hedgehog (the hedgehog holds the sword and key in the family_tree, the lock is shiny like the shiny_sword, the hedgehog is looking at the player expectantly) but it's still a wrench to give up. Likewise, the player has probably already died once going into the moat and may have mentally categorized it as a death trap. They need to first figure out from the illuminated_letters that they need a crown and then to read the hedgehog_broach memory carefully in order to realize that the crown is likely in the moat and that a weapon might make the moat safe. And of course they also need to find the hedgehog broach in the first place and to realize that the grimy_axe might serve their weapon needs. With both mcguffins in hand winning the game is a simple matter of wearing the crown and reading the illuminated_letters.
	
- Room 5: [future]. Hard puzzles. I have plans to come up with one grand final room that has multiple puzzles and some fun references. The strategy would be to make the silver_key harder to reach - with the hedgehog handing over some intermediate puzzle solving object instead.


*** Story ***

- Like everything elese in the game the story just sort of happened as I went along. Burt did not start off as a Henry IVth wastrel with a destiny, a career as a baker, and a great-grandmother with little-known connections to royalty -  but here is the tale of how he eventually got there. I rewrote very little of the description text during final editing (the main exception being an update to the hedgehog description to discourage players from attacking it) so you can track the story evolution from room to room.

- Room 1: In the tradition of Zork I introduce Burt as a rough and ready sort not known for his feats of intelect or his sophistication. At this point I had a vague idea of Burt's pub bragging motivations but that was about all. Although the story had little refinement even at this point I was planning for the game to have four rooms with the winning condition being in Room 4.

 - Room 2: This was still early days story-wise. Why a hedgehog? Why not!? That's the unique beauty of the puzzle-centric easthetic of IF - on day you're whomping draggons - the next day you're held at bay by hungry hedgehogs. The stale_biscuits were inspired by my wife's love of British McVitties biscuits. At this point Burt was still a random bloke living in his Mom's basement without any kind of baking career and the game victory vaguely involved him finding a big chest of gold in Room 4.

- Room 3: Making the switches work and fixing some timer bugs took me a while so this is when a lot of the story thinking happened. Also around this time I had a conversation with my young friend Gideon who told me to end the game with a magic scroll that you read to win. Having no better plan I agreed heartily so now the end plan was in sight. The goblin was planned from Room 2 and is still entirely arbitrary but I was starting to think more about the writing and you can begin to see small signs of the eventual narrative. The description of the Antechamber is longer than that of past rooms and hints at a cursed condition. And the description of Burt's shiny_sword attack on the goblin hints at a hitherto unanticipated destiny. It was somewhere around this time that the castle went from just being a random spooky place to "Dark Castle".

- Room 4: The puzzles here are a lot more intricate so I had a lot more time to ponder the story. Also, endings tend to make one think of beginnings. And lastly I didn't have good puzzle ideas / props. My original idea was just that Burt would just get to Room 4 and find a pile of gold. But now that I'd committed to the scroll ending I had to have Burt return to earlier rooms to find the necessary puzzle mcguffins - which led me to want to explain elements which had previously been arbitrary. Why exactly was Burt destined to be king / barron of the castle. What was the castle called before it was Dark Castle? How come Burt is carying biscuits in his backpack? And what on earth is the deal with the hedgehog in the Main Hall? All of these ideas came together in Room 4. Which perhaps explains why nearly all the story elements get pulled together in the description of one item - which I proudly believe the be the most exposition-heavy broach in IF history. 

- Room 5: [future] We'll see if this ever happens but story-wise I do have some loose ends to tie together. Why is there a guard golin in Room 3? I usually picture him as a sour old servent who went dark with the castle but time will tell. And what about Burt's love life. In fantasy tales, (un)promsing lads like Burt usually have some sweetheart they are pining for. In Burt's case I picture it being a no nonsense laday of superior intelect and competence who's attention Burt is desperately trying to gain. Her story has been wholy absent from the tale so far and would be fun to weave in.

+++ Steps for Game Expansion +++

New room creation
	- Outline contents and actions in the room
	- Create room_dict entry: description, features, items
	- Updated allowed_lang_lst as needed
	- Create path_dict entires for viable paths
	- Write description.txt entries for new items, features, view_only, and read entities
	- Update static_dict written_on_dict if needed
	- Create interactions for any doors, creatures, timers, switches, or containers

New verb creation:
	- Add the word to the help() text
	- Add word to allowed_lang_dict 'allowed_verbs' (e.g. [.., 'eat'])
	- If needed, add a verb-specific list to allowed_lang_dict (e.g.: allowed_lang_dict = {'can_be_eaten_lst': ['stale_biscuts']} )
	- If the verb impacts new nouns in a complex way create a new noun dictionary for it (e.g. static_dict food_dict['stale_biscuts'] => eat_results )
		- If you create an entirely new noun dictionary be sure to add it to the passed variables for interpreter_txt()
		- Create verb elif in interpreter_text to call dictionary entries and update lists (e.g. inventory) as needed
		- It can help to start by copying the elif for an existing verb that has similar usage constraints (e.g. 'drop' for 'eat')
	- Test your new verb!

New trigger creation:
	- Determine whether trigger is pre or post action
	- Add trigger text to the correct trigger list (pre_action_trigger_lst and post_action_trigger_lst) (currently skippable for 'push')
	- If trigger is post_action ensure that trigger() is called in the verb elif in text_interpreter() 
	- Add trigger logic to trigger()

New item creation:
	- Determine where the item will 'live' (which room or container it will be found in)
	- Add the item to room_dict or container_dict
	- Add the item's description to description.txt


+++ Limitations & Goals +++

Version 1.0 Major Limitations
- Only 2 word sentences... adjectives are connected to nouns using "_"
- No prepositions
- Only one timer active at a time
- If you attack the hedgehog while it's eating the stale_biscuts simply vanish

Version 2.0 Features
- articles, adjectives, and prepositions
- Save Game capability
- Object oriented code
- Base on examples of efficient code.. focus on pythonic implementation
- Classes
- switcher


*** Coda ***

If You Teach Your Pa Some Python (A Cautionary Tale)

If you teach your Pa some python
He will get excited
And want to start "a project"
He will wander around the house
Saying "hmmm" 
(thinking of an idea)
And before you know it
He will be writing a "text adventure"
(Which is a strange old game with only words)
Then he will get very enthusiastic
And declare that he needs an IDE
(Because someone on YouTube has one)
Then there will be typing
And more typing
And more typing

Next it will get a bit tricky
And he will wander around the house
Saying "hmmm"
(thinking about dictionaries of dictionaries)
Eventually he will want you to try his game
And will be very proud to have created
One door and one key
But there won't actually be a room
Behind the door
Which won't be very interesting
So then there will be typing
And more typing
And more typing

Then one day
There will be some unfortunate language in the house
And he will declare that he needs "version control"
(Which means "Git")
And he will wander around the house
Saying "hmmm"
(thinking about Git clients and respositores)
Then he will proudly tell you
That his code is on "GitHub"
And he will go back to typing
And more typing
And more typing

Eventually
After more "hmmm"s 
And much more typing
the game will be "mostly done"
He will be very proud of it
And want the whole family to play it
To give him "feedback"
(but only Mommy
will actually play the whole thing..
and she'll help him with his spelling too)

So then
He'll want to show it to all his friends
He will declare that he is "just going to put it on the web"
Which will mean
Learning Flask and Jinja2
And I'm sorry to say
There will thne be more unfortunate language in the house
Because client-side programming is "strange and unnatural"
But eventually
After quite a bit of typing
(And delting)
And some wandering around the house
Saying "hmmm"
And more typing
(And more deleting)
And a last bit of typing

There will be "much rejoicing"
And the game will be running
On the local web server
He will declare "now I just need to spruce it up a bit"
Which will mean "CSS"
And more YouTube classes
And also "Exercising aesthetic judgment"
Then there will be
More wandering about the house
Saying "hmmm"
Then it will be time again for typing
And more typing
And a bit of photo editing

Finally
He will be ready to put the game on the "real" web
Which wil mean a "Pythonanywhere"
Which will seem great at first
Until it becomes clear that this means
Using
Bash shell and vi
Then there will be more unforutunate language in the house
And also long stories
About the last time he used vi
30 years ago
But after a bit more typing
and a few more "hmmm"s

At last
The game will be up on the "real" web
He will send everyone he knows a link to it
Then just when the "project"
Is finally finished
he will declare that he needs to do it all over again "right"
Which will mean "object oriented code with a NoSQL DB"
(This is why this a cautionary tale)

