#Split from screens.rpy for ease of merging.
screen role_select():
    key "K_ESCAPE" action MainMenu()
    modal True
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            text "Select the difficulty"
            #Set difficulty of game
            textbutton "Easy" action [SetVariable("gameScript", "easy"), Notify("Helpdesk Role")]
            textbutton "Medium" action [SetVariable("gameScript", "medium"), Notify("Cybersecurity Role")]
            textbutton "Hard" action [SetVariable("gameScript", "hard"), Notify("CISO Role")]
            #Catch to prevent entering the game without selecting a difficulty
            if gameScript:
                textbutton "Confirm" action [Return(), Hide("role_select")]

#Defines fade_in transition. -c
transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0

#Main hub screen. All departments are handled here as imagebuttons.
#TODO organize the buttons by importance; add a better office building and text background to make these buttons better.
screen mainGameplayLoop():
    key "K_ESCAPE" action MainMenu()
    modal True
    #CISO Office button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 88
        hovered SetVariable("mainOfficeHovered", True)
        unhovered SetVariable("mainOfficeHovered", False)
        action [SetVariable("mainOfficeHovered", False), Jump ("mainOfficeSwitch")]
    #Research and Development button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 150
        hovered SetVariable("researchDevHovered", True)
        unhovered SetVariable("researchDevHovered", False)
        action [SetVariable("researchDevHovered", False), Jump ("researchDevSwitch")]
    #Employee Helpdesk button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 212
        hovered SetVariable("helpDeskHovered", True)
        unhovered SetVariable("helpDeskHovered", False)
        action [SetVariable("helpDeskHovered", False), Jump ("helpDeskSwitch")]
    #Cybersecurity Dept. button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 274
        hovered SetVariable("cyberSecHovered", True)
        unhovered SetVariable("cyberSecHovered", False)
        action [SetVariable("cyberSecHovered", False), Jump ("cyberSecSwitch")]
    #Server Room button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 336
        hovered SetVariable("serverRoomHovered", True)
        unhovered SetVariable("serverRoomHovered", False)
        action [SetVariable("serverRoomHovered", False), Jump("serverRoomSwitch")]
    #Cubicles button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 400
        hovered SetVariable("cubicleHovered", True)
        unhovered SetVariable("cubicleHovered", False)
        action [SetVariable("cubicleHovered", False), Jump ("cubicleSwitch")]
    #Device Storage button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 462
        hovered SetVariable("deviceStorageHovered", True)
        unhovered SetVariable("deviceStorageHovered", False)
        action [SetVariable("deviceStorageHovered", False), Jump ("deviceStorageSwitch")]
    #Copy Room button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1265
        ypos 523
        hovered SetVariable("copyRoomHovered", True)
        unhovered SetVariable("copyRoomHovered", False)
        action [SetVariable("copyRoomHovered", False), Jump ("copyRoomSwitch")]
    #End workday button
    imagebutton idle "loop_hitbox":
        anchor (1.0, 0.5)
        xpos 1265
        ypos 620
        if endDayValid:
            hovered SetVariable("endDayHovered", True)
            unhovered SetVariable("endDayHovered", False)
            action [SetVariable("endDayHovered", False), Jump ("endDay")]
        elif tutorialComplete:
            action MainMenu()
        else:
            action None
    #Return to Title button
    imagebutton idle "loop_hitbox":
        anchor (1.0, 0.5)
        xpos 1265
        ypos 690
        hovered SetVariable("titleScreenHovered", True)
        unhovered SetVariable("titleScreenHovered", False)
        action [SetVariable("titleScreenHovered", False), MainMenu(),]
    #Box for displaying what day the user is on
    if not tutorialMode:
        frame:
            xalign 0 yalign 1.0
            vbox:
                text "Day [currentDay] of [numDays]"


    #This entire block basically adds the floor-by-floor glow when a button is hovered over. Also adds fun effects for "return to title".
    if mainOfficeHovered:
        add "lights/OfficeLights.png"
    elif researchDevHovered:
        add "lights/RDLights.png"
    elif helpDeskHovered:
        add "lights/HelpdeskLights.png"
    elif cyberSecHovered:
        add "lights/CyberLights.png"
    elif serverRoomHovered:
        add "lights/ServerLights.png"
    elif cubicleHovered:
        add "lights/CubicleLights.png"
    elif deviceStorageHovered:
        add "lights/StorageLights.png"
    elif copyRoomHovered:
        add "lights/CopierLights.png"
    elif titleScreenHovered:
        add "lights/ReturnToTitleLights.png"
    elif endDayHovered:
        add "lights/EndDayLights.png"
    if endDayValid and not endDayHovered:
        add "lights/endDayAvail.png"

    #Blocks add event notifications when events are in departments.
    if defineOffice in eventToView or cisoEventTrigger:
        add "eventmark.png":
            xpos 924
            ypos 62
    #Properly ordered
    if defineRD in eventToView:
        add "eventmark.png":
            xpos 943
            ypos 125
    if defineHelpdesk in eventToView:
        add "eventmark.png":
            xpos 941
            ypos 187
    if defineCyber in eventToView:
        add "eventmark.png":
            xpos 890
            ypos 249
    if defineServer in eventToView:
        add "eventmark.png":
            xpos 908
            ypos 312
    if defineCubicle in eventToView:
        add "eventmark.png":
            xpos 902
            ypos 374
    if defineStorage in eventToView:
        add "eventmark.png":
            xpos 879
            ypos 437
    if defineCopier in eventToView:
        add "eventmark.png":
            xpos 928
            ypos 499

#Procedural menu generator that loads options and associated scores when given a valid event.
screen eventViewer(event):
    key "K_ESCAPE" action MainMenu()
    modal True
    frame:
        #Centers the event box
        #TODO: Make this look better, these long winded events make this box way bigger than it needs to be and it looks horrible.
        xalign 0.5 yalign 0.5
        vbox:
            #Gets and prints question text at the top of the box
            text "[event.get('question')]"
            #For every choice available, get its text, and associate each response with a unique button for score tracking.
            for option in event['choices']:
                #Button sets score to add to the response's score, and a dummy variable to the response to allow highlighting.
                #The default highlighting does not work on menus generated through for loops.
                textbutton "[option['answerText']]" action [
                    SetVariable("dynamScore", option['score']), 
                    SetVariable("responseSelected", option)
                    ] selected responseSelected == option

            #Hardcoded bailout button to allow user to return to previous screen.
            #Added if block to catch an edge case where tutorial event was unviewable after backing out.
            textbutton "Return" action [
                SetVariable("dynamScore", 0),
                SetVariable("responseSelected", None),
                Function (renpy.restart_interaction),
                If(tutorialMode, Jump("tutorialCubicleGeneral"), Jump("departmentGeneral"))]
            
            #Blank line to split confirm button from the rest of the text.
            textbutton "-------------------------" action None

            #Checks if a response was clicked, then allows the user to proceed to score evaluation.
            #See "eventUpdate" in events.
            if not responseSelected == None:
                textbutton "Confirm selection" action SetVariable("tempEvent", event), Jump("eventUpdate")
        
screen returnFeedback():
    key "K_ESCAPE" action MainMenu()
    modal True
    add "VOID.jpg"
    #TODO CHANGE!!! This black screen exists to make it easier for me to program in the screens.
    frame:
        background None
        xalign 0.045 yalign 0.2
        vbox:
            #If end day display, show workday and day's score, otherwise
            #Show full session's score
            if tutorialMode:
                text "Summary of Events:":
                    xalign 0.5
                text "[dayScore] / [dayMaxScore]":
                    xalign 0.5
            elif displayEnd:
                text "Workday Summary: Day [currentDay]":
                    xalign 0.5
                text "[dayScore] / [dayMaxScore]":
                    xalign 0.5
            else:
                text "Full Work Session Summary:":
                    xalign 0.5
                text "[fullScore] / [sessionMaxPoints]":
                    xalign 0.5
    frame:
        #Box to display all events within criteria.
        area (22, 243, 350, 400)
        side ("c"):
            viewport:
                draggable False
                mousewheel True
                scrollbars "vertical"
                #If end of day display, show all events in end of day array;
                #Else, display all events from compiled end of day arrays.
                vbox:
                    if displayEnd:
                        for element in dayEvents:
                            textbutton "[element.get('longhand')]" action [
                                SetVariable("responseSelected", element) 
                                ] selected responseSelected == element
                    else:
                        for element in completedEvents:
                            textbutton "[element.get('longhand')]" action [
                                SetVariable("responseSelected", element)
                                ] selected responseSelected == element
    frame:
        #Box to display feedback, gets feedback to show from above box's selected element.
        #Author's note: Good god what on earth is this layering
        area (381, 80, 613, 570)
        side("c"):
            viewport:
                draggable False
                #If a "completed" event is selected, active the below block.
                if responseSelected:
                    vbox:
                        python:
                            #Use two unrelated variables for temp values for efficiency. Will be cleared on exit.
                            global activePoints
                            global departCaller
                            global dynamOption
                            scores = []
                            #Find the answer with the highest score for the selected event
                            #Use the found score to get the associated text for the "best" answer.
                            for item in responseSelected.get("choices"):
                                scores.append(item.get("score"))
                                activePoints = max(scores)
                            for item in responseSelected.get("choices"):
                                if item.get("score") == activePoints:
                                    departCaller = item.get("answerText")

                            #Run this block if end day variant of screen.
                            if displayEnd:
                                #Get index of the selected event.
                                index = dayEvents.index(responseSelected)
                                #Try Except to catch out of bounds errors caused by skipped events.
                                try:
                                    #Use the found index to look up the user's response to the event.
                                    dynamScore = arrayOfScores[index]
                                    #Get the user's selected response by reverse looking up the score given.
                                    for item in responseSelected.get("choices"):
                                        if item.get("score") == dynamScore:
                                            dynamOption = item.get("answerText")
                                #If out of range of responses, no response was given. Thus, tell user as much.
                                except IndexError:
                                    dynamOption = "No answer selected."

                            #Run this block if full session display.
                            #Functionally identical to the above block, but using the "full" arrays instead.
                            else:
                                index = completedEvents.index(responseSelected)
                                try:
                                    dynamScore = fullArrayOfScores[index]
                                    for item in responseSelected.get("choices"):
                                        if item.get("score") == dynamScore:
                                            dynamOption = item.get("answerText")
                                except IndexError:
                                    dynamOption = "No answer selected."

                        text "Correct answer: [departCaller]\n"
                        text "Selected answer: [dynamOption]\n"
                        text "[responseSelected.get('feedback')]"
    frame:
        #Box for continuing gameplay cycle.
        xalign 0.97 yalign 0.5
        vbox:
            #If screen is an end of day screen, show 
            if displayEnd:
                #Edge case for if final day. Instead of showing "next day" it shows "full session feedback."
                if currentDay == numDays or tutorialSection == 3:
                    #As the core function calls this screen a second time if the condition is met, return is sufficient to go to full session.
                    textbutton " Continue to full  \nsession feedback":
                        action [
                            Return()
                        ]

                elif tutorialMode and tutorialSection < 3:
                    textbutton "Continue to \n next section":
                        action [ 
                            SetVariable("dayScore", 0),
                            SetVariable("dayEvents", []),
                            SetVariable("endDayValid", False),
                            SetVariable("arrayOfScores", []),
                            SetVariable("departCaller", ""),
                            SetVariable("dynamOption", ""),
                            SetVariable("dynamScore", 0),
                            SetVariable("responseSelected", None),
                            SetVariable("tutorialSection", tutorialSection + 1),
                            SetVariable("tutorialComplete", True),
                            SetVariable("reviewTerms", False),
                            Return()
                        ]
                    if reviewTerms:
                        textbutton "Review functions":
                            action [
                                SetVariable("tutorialComplete", False),
                                Return()
                            ]            

                else:
                    #Set all day-specific variables and miscellaneous used variables to default states on day continue.
                    textbutton "Continue to\n   next day": 
                        action [
                            SetVariable("dayScore", 0),
                            SetVariable("dayEvents", []),
                            SetVariable("currentDay", currentDay + 1),
                            SetVariable("endDayValid", False),
                            SetVariable("arrayOfScores", []),
                            SetVariable("departCaller", ""),
                            SetVariable("dynamOption", ""),
                            SetVariable("dynamScore", 0),
                            SetVariable("responseSelected", None),
                            Notify(f"Entering Day {currentDay + 1}"),
                            Return()]
            else:
                if tutorialMode:
                    textbutton "Conclude \n Tutorial":
                        action Jump("finishTutorial")
                #If day was the final day, gameplay is complete; prompt user to return to title.
                else:
                    textbutton "Return to Title":
                        action [MainMenu()]
