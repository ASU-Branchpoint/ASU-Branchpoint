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
            "shorthand": "Stolen Lunch",
            "longhand": "An employee's missing lunch",
            "location": defineCubicle,
            "points": 5,
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

#Assigns cutoffs for:   maximum value of all questions on screen
#                       maximum score that can be accumulated through questions
#                       maximum number of questions until feedback
#                       number of days until the simulation ends
label defineArray:
    if gameScript == "easy":
        $ activeCeiling = 60
        $ scoreTerminate = 30
        $ scriptTerminate = 20
        $ numDays = 4
    elif gameScript == "medium":
        $ activeCeiling = 100
        $ scoreTerminate = 100
        $ scriptTerminate = 25
        $ numDays = 5
    elif gameScript == "hard":
        $ activeCeiling = 150
        $ scoreTerminate = 180
        $ scriptTerminate = 25
        $ numDays = 7
    else:
        $ activeCeiling = 10
        $ scoreTerminate = 1
        $ scriptTerminate = 1
        $ numDays = 1

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
                #Shuffle the array of events to add more randomness and decrease bell curve skew.
                renpy.random.shuffle(fullArrayOfEvents)
            #If the event is a followup event to a trap question, add it to its own array.
            if entry.get('is_followup'):
                followUpDefine.append(entry)
    #Set the original array to blank to save memory. It will not be referenced again.
    $ event_library.clear()
    #See below.
    call addEvents
    return

#label getDynamicSize:
    #KEEP THIS COMMENTED
    #This utilizes an external library not innately packed with Ren'Py and will always fail to compile on anything other than my machine.
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
        global dayEvents
        global scriptTerminate
        global scoreTerminate
        global endDayValid

        #Length of completed events, bar followup events. Traps and followups count for one question answered for multiplier.
        multCounter = 0
        for entry in dayEvents:
            if not entry.get('is_followup'):
                multCounter = multCounter + 1

        #Multipliers for point "ceiling" to restrict event spawning for the first one to three questions, give or take. Needs finer tuning.
        if gameScript == "easy":
            currentMultiplier = 0.2 * multCounter * (currentDay ** 0.4)
        elif gameScript == "medium":
            currentMultiplier = 0.3 * multCounter * (currentDay ** 0.6)
        elif gameScript == "hard":
            currentMultiplier = 0.25 * multCounter**1.2 * (currentDay * 0.5)
        else:
            currentMultiplier = 1

        #Because multipliers scale higher than one, cap it at one to flatted spawn curve.
        if currentMultiplier > 1:
            currentMultiplier = 1
        #For first event, multiplier will always be zero, so add 0.1 to force one single event to spawn.
        #I have no clue how it keeps creating multipliers less than zero but it keeps happening and apparently it's a thing.
        if currentMultiplier <= 0:
            currentMultiplier = 0.1

        #For loop to determine how many points the questions on screen are worth.
        #For instance, if a question's highest value answer is worth 40 points, the question is worth 40.
        #This consecutively adds values for every instance in the queue.
        for event in currentEvents:
            addPoints = event.get('points')
            activePoints = activePoints + addPoints
        #Set the ceiling for "available points" according to the progression multiplier.
        addCeiling = activeCeiling * currentMultiplier
        if addCeiling <= 0:
            addCeiling = 1
        #If called externally, sets the temp event variable to blank to prevent edge case errors.
        addedEvent = {}
        #If the points on screen is less than its cap, spawn another event until it equals or exceeds the cap.
        #   Edge case for trap followup events, which are locked to only allow themselves to exist while active.
        while activePoints < addCeiling and not followUpActive:
            #If the score or number of completed events exceeds cutoff, spawn no new events regardless.
            if dayScore < scoreTerminate and len(dayEvents) < scriptTerminate:
                #Get length of list of every spawnable event.
                index = (len(fullArrayOfEvents) - 1)
                #Grab a random event from the list of spawnable events.
                newRandomEvent = renpy.random.randint(1, index)
                addedEvent = fullArrayOfEvents[newRandomEvent]
                #Shuffle order of answers to make it slightly more difficult to pattern-recognize answers per question.
                renpy.random.shuffle(addedEvent.get('choices'))
                #Add event with shuffled answers to queue.
                currentEvents.append(addedEvent)
                #Add its point value to the cap.
                activePoints = activePoints + fullArrayOfEvents[newRandomEvent].get('points')
                #If/else for repeatable. If repeatable, remove only that copy of the event from the library.
                #   This assumes all repeatable events have at least 1 weight.
                if not addedEvent.get('repeatable'):
                    for event in fullArrayOfEvents:
                        if event.get('id') == addedEvent.get('id'):
                            fullArrayOfEvents.remove(event)
                #Else, search the entire pullee array for all copies of the event and remove them procedurally.
                else:
                    fullArrayOfEvents.remove(addedEvent)
            #If the cap has been reached, set flag to allow early workday endings.
            else:
                endDayValid = True
                break
    #See below.
    call sortEvents
    return

label sortEvents:
    #Simple sort to sort events from easiest first to hardest last.
    #Makes visuals more concise and tidy.
    #   With the removal of difficulty declaration, this is more a QOL thing than anything functional.
    #   But I digress, it's still cool to have I guess.
    python:
        sort = []
        mediumThreshold = 0
        for option in currentEvents:
            if option.get('question_difficulty') == "Easy":
                sort.insert(0, option)
                mediumThreshold = sort.index(option)
            if option.get('question_difficulty') == "Medium":
                sort.insert(mediumThreshold, option)
            if option.get('question_difficulty') == "Hard":
                sort.append(option)
        currentEvents.clear()
        for entry in sort:
            currentEvents.append(entry)
        if [] in currentEvents:
            currentEvents.remove([])
    return

label eventUpdate:
    #Display a notification saying which event was resolved.
    if tutorialMode:
        $ renpy.notify(f"Event resolved!")
    elif dayScore + dynamScore > scoreTerminate:
        $ renpy.notify(f"Workday complete!")
    else:
        $ renpy.notify(f"Event resolved: {tempEvent.get('shorthand')}")
    #Clear the finished event from the active event queue.
    $ arrayOfScores.append(dynamScore)
    $ currentEvents.remove(tempEvent)
    #Add the event to a dummy array of "completed" events.
    $ dayEvents.append(tempEvent)
    #Add the response's score to the total score
    #Edge case for calling from the tutorial cycle, prevents escape and allows the tutorial to complete as intended. Tutorial no longer completely boned!
    if tempEvent.get('id') == "tutorial":
        $ dayScore += dynamScore
        call tutorialConclusion
    python:
        if followUpActive:
            for entry in sideArray:
                currentEvents.append(entry)
            sideArray.clear()
            followUpActive = False
        if tempEvent.get('followup_event').get('allowed') and dynamScore < tempEvent.get('followup_event').get('score_cutoff'):
            for entry in currentEvents:
                sideArray.append(entry)
            currentEvents.clear()
            followUpActive = True
            getEntry = tempEvent.get('followup_event').get('event_id')
            for entry in followUpDefine:
                if entry.get('id') == getEntry:
                    currentEvents.append(entry)
    #TODO: Refactor according to proper scoring system. This is temp and for debug.
    $ dayScore += dynamScore
    #Clears the temporary variable, effectively removing all copies of the event from active memory except in the above completed events.
    $ tempEvent = {}
    #Menu items created through a for loop have disastrous selection highlighting, this variable exists solely to remedy it.
    $ responseSelected = None
    #Calls below cycle to update notification marks on the main screen.
    #This addEvents call seems irrelevant but it is MISSION CRITICAL!!! Removing it bricks the refresh self-sustain, somehow.
    call addEvents
    call evUpdateNotif
    scene bg mainloop with dissolve
    call screen mainGameplayLoop
    


label evUpdateNotif:
    python:
        #Calls the pre-existing array and 8 associated booleans, allows function to alter proper variables
        global eventToView
        global currentEvents

        #Clears the array of departments with events ready.
        eventToView.clear()

        #Iterates through active events for the entire array.
        #If an event's location matches a department, it sets the notification flag.
        #Multiple events in the same department are fine, as it only checks false and refuses true.
        for option in currentEvents:
            if option.get('location') == defineOffice and defineOffice not in eventToView:
                eventToView.append(defineOffice)
            if option.get('location') == defineRD and defineRD not in eventToView:
                eventToView.append(defineRD)
            if option.get('location') == defineCyber and defineCyber not in eventToView:
                eventToView.append(defineCyber)
            if option.get('location') == defineServer and defineServer not in eventToView:
                eventToView.append(defineServer)
            if option.get('location') == defineHelpdesk and defineHelpdesk not in eventToView:
                eventToView.append(defineHelpdesk)
            if option.get('location') == defineStorage and defineStorage not in eventToView:
                eventToView.append(defineStorage)
            if option.get('location') == defineCopier and defineCopier not in eventToView:
                eventToView.append(defineCopier)
            if option.get('location') == defineCubicle and defineCubicle not in eventToView:
                eventToView.append(defineCubicle)
    return

label endDay:
    #End-of-day event closer
    python:
        dayMaxScore = 0
        #Clears the current event queue, if it exists.
        if currentEvents:
            for entry in currentEvents:
                dayEvents.append(entry)
        currentEvents.clear()
        scores = []
        for entry in dayEvents:
            for value in entry.get('choices'):
                maxed = value.get('score')
                scores.append(maxed)
            dayMaxScore += max(scores)
            scores.clear()
        for score in arrayOfScores:
            fullArrayOfScores.append(score)
        sessionMaxPoints += dayMaxScore
        #Adds the score of completed events to the total.
        fullScore = fullScore + dayScore
        #Adds all completed events to the complete queue.
        #Cleared questions from above will be added to complete but will not be counted towards score.
        #Order matters!
        for entry in dayEvents:
            completedEvents.append(entry)
        if currentDay == numDays:
            renpy.call_screen("returnFeedback")
            displayEnd = False
    #See screens.
    call screen returnFeedback
    #Add new events to queue.
    call addEvents
    #Updates notifs
    call evUpdateNotif
    #Resumes normal gameplay, plus one day.
    call screen mainGameplayLoop
    return