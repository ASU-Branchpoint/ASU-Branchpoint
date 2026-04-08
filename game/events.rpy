#TODO: Events that do the same thing in different departments will likely just need multiple copies for the same event

#Hard defined variables for referencing departments, to prevent typo mismatches and grammatical semantics.
define defineOffice = "ciso"
define defineRD = "resdev"
define defineHelpdesk = "helpdesk"
define defineCyber = "cyber"
define defineServer = "server"
define defineStorage = "storage"
define defineCubicle = "cubicle"
define defineCopier = "copier" 
default eventLibrary = []

label defineTutorial:
    #Leave this as it is, it makes it much easier to debug and work on when the single event it needs to load is hardcoded in.
    #It's also completely gutted outside of the essentials, given that it doesn't need half the keys of a regular event in this limited format.
    init python:
        tutorial = {
            "id": "tutorial",
            "location": defineCubicle,
            "points": 9,
            "question": "Someone's lunch got stolen out of the break room fridge! As the new resident problem-solver, what's your plan of action?",
            "choices": [
                {
                    "answerText": "Let bygones be bygones, the employees will figure it out between themselves.",
                    "score": 3
                },
                {
                    "answerText": "Go through the camera footage from the hallway and see who was acting strangely, and confront them.",
                    "score": 5
                },
                {
                    "answerText": "Reimburse them for their troubles and hope it never happens again.",
                    "score": 1
                }
            ],
            }
    $ fullArrayOfEvents.append(tutorial)
    return


#TO: FUNCTION AND EVENT LIBRARY WRITER;
#   USE THE HARDCODED DEFINITIONS FOR EACH DEPARTMENT IN LOCATION ARGUMENT
#   IT'LL MAKE THINGS MUCH EASIER FOR DEBUGGING AND CODE STABILITY

#Assigns maximums for: how many events can be done in a single run
#                      how much score can be accumulated in a single run (as a fallback)
#                      how much maximum score all events on screen can total to (for adding events)
label defineArray:
    if gameScript == "easy":
        $ activeCeiling = 90
        $ scoreTerminate = 500
        $ scriptTerminate = 15
    elif gameScript == "medium":
        $ activeCeiling = 120
        $ scoreTerminate = 800
        $ scriptTerminate = 25
    elif gameScript == "hard":
        $ activeCeiling = 180
        $ scoreTerminate = 1500
        $ scriptTerminate = 40
    else:
        $ activeCeiling = 100
        $ scoreTerminate = 1
        $ scriptTerminate = 1

#   See: event_library.
    call defineFull
    #call getDynamicSize
    python: 
        global currentEvents
        global gameScript
        #Loops through all entries in the library, and checks for events that can "spawn" on the player's chosen difficulty.
        for entry in event_library:
            eventLowLayer = entry.get('spawn_rules').get(gameScript)
            if eventLowLayer.get('allowed'):
                #If the event can spawn on the difficulty, add copies to the secondary library equal to weight.
                #This creates artificial rarity and frequency of events.
                for i in range(eventLowLayer.get('weight')):
                    fullArrayOfEvents.append(entry)
    #See below.
    call addEvents
    #Set the original array to blank to save memory. It will not be referenced again.
    $ event_library = []
    return

    #call eventUpdate

#label getDynamicSize:
    #KEEP THIS COMMENTED
    #This utilizes an external library not innately packed with Ren'Py and will always fail to compile on anything other than my end.
    #This prints the byte-size of the event (and hopefully later the event library) to the console.
    #Other than my own overhead predictions, it also lets me check to see how efficient I need to be to iterate and process all of this code.
    #python:
    #    from pympler import asizeof
    #    storage = asizeof.asizeof(event_library)
    #    print(storage)
    #return

label addEvents:
    #Tracker variable to see how many potential points are in the queue.
    $ activePoints = 0
    python:
        global gameScript
        global activePoints
        global activeCeiling        
        global fullArrayOfEvents
        global currentEvents
        global completedEvents
        global scriptTerminate
        global score
        global scoreTerminate

        #Multipliers for point "ceiling" to restrict event spawning for the first one to three questions, give or take.
        if gameScript == "easy":
            currentMultiplier = 0.5 * len(completedEvents)
        elif gameScript == "medium":
            currentMultiplier = 0.3 * (len(completedEvents))
        elif gameScript == "hard":
            currentMultiplier = 0.4 * (len(completedEvents))**1.2
        else:
            currentMultiplier = 1

        #Because multipliers scale higher than one, cap it at one to flatted spawn curve.
        if currentMultiplier > 1:
            currentMultiplier = 1
        #For first event, multiplier will always be zero, so add 0.1 to force one single event to spawn.
        if currentMultiplier == 0:
            currentMultiplier = 0.1

        #For loop to determine how many points the questions on screen are worth.
        #For instance, if a question's highest value answer is worth 40 points, the question is worth 40.
        #This consecutively adds values for every instance in the queue.
        for event in currentEvents:
            addPoints = event.get('points')
            activePoints = activePoints + addPoints
        #Set the ceiling for "available points" according to the progression multiplier.
        addCeiling = activeCeiling * currentMultiplier
        #Get length of list of every spawnable event.
        index = len(fullArrayOfEvents)
        #If the points on screen is less than its cap, spawn another event until it equals or exceeds the cap.
        while activePoints < addCeiling:
            #If the score or number of completed events exceeds cutoff, spawn no new events regardless.
            if score < scoreTerminate and len(completedEvents) < scriptTerminate:
                #Grab a random event from the list of spawnable events and add it to queue.
                #Add its point value to the number of points in queue, repeat until condition met.
                newRandomEvent = renpy.random.randint(1, index)
                currentEvents.append(fullArrayOfEvents[newRandomEvent])
                activePoints = activePoints + fullArrayOfEvents[newRandomEvent].get('points')
            else:
                break
    #See below.
    call sortEvents
    return

label sortEvents:
    #Simple sort to sort events from easiest first to hardest last.
    #Makes visuals more concise and tidy.
    python:
        sort = []
        global currentEvents
        for option in currentEvents:
            if option.get('question_difficulty') == "easy":
                sort.append(option)
                currentEvents.remove(option)
        for option in currentEvents:
            if option.get("question_difficulty") == "medium":
                sort.append(option)
                currentEvents.remove(option)
        for option in currentEvents:
            if option.get("question_difficulty") == "hard":
                sort.append(option)
                currentEvents.remove(option)
        currentEvents.append(sort)
        if [] in currentEvents:
            currentEvents.remove([])
    return

label eventUpdate:
    #Display a notification saying which event was resolved.
    $ renpy.notify(f"Event resolved: {tempEvent.get('shorthand')}")
    #Clear the finished event from the active event queue.
    $ currentEvents.remove(tempEvent)
    #Add the event to a dummy array of "completed" events.
    $ completedEvents.append(tempEvent)
    #Add the response's score to the total score
    #TODO: Refactor according to proper scoring system. This is temp and for debug.
    $ score += dynamScore
    #Edge case for calling from the tutorial cycle, prevents escape and allows the tutorial to complete as intended. Tutorial no longer completely boned!
    if tempEvent.get('id') == "tutorial":
        call tutorialConclusion
    #Clears the temporary variable, effectively removing all copies of the event from active memory except in the above completed events.
    $ tempEvent = {}
    #Menu items created through a for loop have disastrous selection highlighting, this variable exists solely to remedy it.
    $ responseSelected = None
    #Calls below cycle to update notification marks on the main screen.

    call addEvents

    call evUpdateNotif
    call screen mainGameplayLoop
    


label evUpdateNotif:
    python:
        #Calls the pre-existing array and 8 associated booleans, allows function to alter proper variables
        global currentEvents
        global officeEventToView
        global rdEventToView
        global cyberEventToView
        global serverEventToView
        global deskEventToView
        global storageEventToView
        global copyEventToView
        global cubicleEventToView

        #Sets all booleans to false to prevent false positives
        officeEventToView = False
        rdEventToView = False
        cyberEventToView = False
        serverEventToView = False
        deskEventToView = False
        storageEventToView = False
        copyEventToView = False
        cubicleEventToView = False

        #Iterates through active events for the entire array.
        #If an event's location matches a department, it sets the notification flag.
        #Multiple events in the same department are fine, as it only needs to set it once.
        for option in currentEvents:
            if option.get('location') == defineOffice:
                officeEventToView = True
            if option.get('location') == defineRD:
                rdEventToView = True
            if option.get('location') == defineCyber:
                cyberEventToView = True
            if option.get('location') == defineServer:
                serverEventToView = True
            if option.get('location') == defineHelpdesk:
                deskEventToView = True
            if option.get('location') == defineStorage:
                storageEventToView = True
            if option.get('location') == defineCopier:
                copyEventToView = True
            if option.get('location') == defineCubicle:
                cubicleEventToView = True
                    
