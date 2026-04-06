#TF/TF/TF 1/2/3
#0 - CISO, ... 7 - Cubicles
#TODO: Events that do the same thing in different departments will likely just need multiple copies for the same event

# Event Name, Diff 1, Diff 2, Diff 3, Dept., [Responses], [Score], Persistence, Copies in "Event Deck" (manipulates rarity)

label defineTutorial:
    init python:
        tutorial = {
            "id": "tutorial",
            "location": "cubicles",
            "points": 10,
            "question": "Someone's lunch got stolen out of the break room fridge! As the resident problem-solver, what's your plan of action?",
            "choices": [
                {
                    "answerText": "Let bygones be bygones, the employees will figure it out between themselves.",
                    "score": 3
                },
                {
                    "answerText": "Go through the camera footage from the hallway and see who was acting strangely, and confront them.",
                    "score": 6
                },
                {
                    "answerText": "Reimburse them for their troubles and hope it never happens again.",
                    "score": 1
                }
            ],
            "feedback": "Hmm... Well, I suppose none of those were a perfect answer after all.",
            }
    $ fullArrayOfEvents.append(tutorial)
    return


label defineArray:        
    init python: 
        event1 = {
        "id": "example_001",
        "difficulty": "medium",
        "spawn_rules": {
        "easy": {"allow": True, "weight": 2},
        "medium": {"allow": False, "weight": 0},
        "hard": {"allow": True, "weight": 10}
        },
        "location": "helpdesk",
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
        "location": "copier",
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
    
    $ currentEvents.append(event2)
    $ currentEvents.append(event1)
    $ gameScript = "medium"

    #call eventUpdate

label debugEvents:
    $ score += dynamScore
    return


label eventUpdate:
    
    #KEEP THIS COMMENTED
    #This utilizes an external library not innately packed with Ren'Py and will always fail to compile.
    #This prints the byte-size of the event (and later the event library) to the console.
    #init python:
    #    from pympler import asizeof
    #    storage = asizeof.asizeof(event1)
    #    print(storage)
    $ score += dynamScore
    call screen mainGameplayLoop
    


label evUpdateNotif:

    python:
        global currentEvents
        global officeEventToView
        global rdEventToView
        global cyberEventToView
        global serverEventToView
        global deskEventToView
        global storageEventToView
        global copyEventToView
        global cubicleEventToView
        def cycleEventUpdate(currentEvents): 
            #officeEventToView = False
            #rdEventToView = False
            #serverEventToView = False
            #cyberEventToView = False
            #deskEventToView = False
            #storageEventToView = False
            #copyEventToView = False
            #cubicleEventToView = False
            for event in currentEvents:
                if event[4] == 0:
                    officeEventToView = True
                if event[4] == 1:
                    rdEventToView = True
                if event[4] == 3:
                    cyberEventToView = True
                if event[4] == 4:
                    serverEventToView = True
                if event[4] == 5:
                    deskEventToView = True
                if event[4] == 6:
                    storageEventToView = True
                if event[4] == 7:
                    copyEventToView = True
                if event[4] == 8:
                    cubicleEventToView = True
