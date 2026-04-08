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

label defineTutorial:
    #Leave this as it is, it makes it much easier to debug and work on when the single event it needs to load is hardcoded in.
    #It's also completely gutted outside of the essentials, given that it doesn't need half the keys of a regular event in this limited format.
    init python:
        tutorial = {
            "id": "tutorial",
            "location": "cubicles",
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
label defineArray:
    #Debug events to temporarily skip full implementation; will be replaced later
    init python: 
        global defineHelpdesk
        event1 = {
        "id": "example_001",
        "difficulty": "medium",
        "spawn_rules": {
        "easy": {"allow": True, "weight": 2},
        "medium": {"allow": False, "weight": 0},
        "hard": {"allow": True, "weight": 10}
        },
        "location": defineCubicle,
        "points": 20,
        "question": "Question text here",
        "choices": [
            {
                "answerText": "This is a really long answer that may or may not be necessarily correct",
                "score": 10
            },
            {
                "answerText": "This is a slightly longer answer that could be correct but it could also be entirely wrong, not like you'd know at the moment",
                "score": 6
            },
            {
                "answerText": "This is a comically short answer. Maybe.",
                "score": 2
            }
        ],
        "feedback": "Answers feedback",
        "allowed_days": [],
        "followup_event": {
        "enabled": False,
        "event_id": ""
        },
        "repeatable": False
        }

        event2 = {
        "id": "example_002",
        "difficulty": "medium",
        "spawn_rules": {
        "easy": {"allow": True, "weight": 2},
        "medium": {"allow": False, "weight": 0},
        "hard": {"allow": True, "weight": 10}
        },
        "location": defineCubicle,
        "points": 20,
        "question": "Question text here",
        "choices": [
            {
                "answerText": "We got water",
                "score": 10
            },
            {
                "answerText": "We got Coke products",
                "score": 6
            },
            {
                "answerText": "We got nothin'",
                "score": 2
            }
        ],
        "feedback": "Answers feedback",
        "allowed_days": [],
        "followup_event": {
        "enabled": False,
        "event_id": ""
        },
        "repeatable": False
        }
    
    #Array should append to FULL array not CURRENT array: debug.
    $ currentEvents.append(event2)
    $ currentEvents.append(event1)
    $ gameScript = "medium"
    return

    #call eventUpdate

label getDynamicSize:
    #KEEP THIS COMMENTED
    #This utilizes an external library not innately packed with Ren'Py and will always fail to compile on anything other than my end.
    #This prints the byte-size of the event (and hopefully later the event library) to the console.
    #Other than my own overhead predictions, it also lets me check to see how efficient I need to be to iterate and process all of this code.
    #init python:
    #    from pympler import asizeof
    #    storage = asizeof.asizeof(tempEvent)
    #    print(storage)

label eventUpdate:
    #Display a notification saying which event was resolved.
    $ renpy.notify(f"Event resolved: {tempEvent.get('id')}")
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
                    
