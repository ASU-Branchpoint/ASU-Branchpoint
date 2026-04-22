#Split from screens.rpy for ease of merging.
screen role_select():
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

#Main hub screen. All departments are handled here as imagebuttons.
#TODO organize the buttons by importance; add a better office building and text background to make these buttons better.
screen mainGameplayLoop():
    add "bg mainloop.png"
    modal True
    #CISO Office button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 75
        hovered SetVariable("mainOfficeHovered", True)
        unhovered SetVariable("mainOfficeHovered", False)
        action [SetVariable("mainOfficeHovered", False), Jump ("mainOfficeSwitch")]
    #Research and Development button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 134
        hovered SetVariable("researchDevHovered", True)
        unhovered SetVariable("researchDevHovered", False)
        action [SetVariable("researchDevHovered", False), Jump ("researchDevSwitch")]
    #Employee Helpdesk button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 193
        hovered SetVariable("helpDeskHovered", True)
        unhovered SetVariable("helpDeskHovered", False)
        action [SetVariable("helpDeskHovered", False), Jump ("helpDeskSwitch")]
    #Cybersecurity Dept. button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 252
        hovered SetVariable("cyberSecHovered", True)
        unhovered SetVariable("cyberSecHovered", False)
        action [SetVariable("cyberSecHovered", False), Jump ("cyberSecSwitch")]
    #Server Room button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 311
        hovered SetVariable("serverRoomHovered", True)
        unhovered SetVariable("serverRoomHovered", False)
        action [SetVariable("serverRoomHovered", False), Jump("serverRoomSwitch")]
    #Cubicles button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 370
        hovered SetVariable("cubicleHovered", True)
        unhovered SetVariable("cubicleHovered", False)
        action [SetVariable("cubicleHovered", False), Jump ("cubicleSwitch")]
    #Device Storage button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 429
        hovered SetVariable("deviceStorageHovered", True)
        unhovered SetVariable("deviceStorageHovered", False)
        action [SetVariable("deviceStorageHovered", False), Jump ("deviceStorageSwitch")]
    #Copy Room button
    imagebutton idle "loop_hitbox":
        anchor(1.0, 0.5)
        xpos 1210
        ypos 488
        hovered SetVariable("copyRoomHovered", True)
        unhovered SetVariable("copyRoomHovered", False)
        action [SetVariable("copyRoomHovered", False), Jump ("copyRoomSwitch")]
    #End workday button
    imagebutton idle "hitbox_border":
        anchor (1.0, 0.5)
        xpos 1210
        ypos 590
        if endDayValid:
            action Jump ("endDay")
        elif tutorialComplete:
            action MainMenu()
        else:
            action None
    #Return to Title button
    imagebutton idle "loop_hitbox":
        anchor (1.0, 0.5)
        xpos 1210
        ypos 690
        hovered SetVariable("titleScreenHovered", True)
        unhovered SetVariable("titleScreenHovered", False)
        action [SetVariable("titleScreenHovered", False), MainMenu(),]
    #Box for displaying what day the user is on
    frame:
        xalign 0 yalign 1.0
        vbox:
            text "Day [currentDay] of [numDays]"


    #This entire block basically adds the floor-by-floor glow when a button is hovered over. Also adds fun effects for "return to title".
    if titleScreenHovered == False:
        add "titleScreenButton.png"
    if mainOfficeHovered:
        add "lights/mainOfficeLights.png"
    elif researchDevHovered:
        add "lights/researchDevLights.png"
    elif helpDeskHovered:
        add "lights/helpDeskLights.png"
    elif cyberSecHovered:
        add "lights/cyberSecLights.png"
    elif serverRoomHovered:
        add "lights/serverRoomLights.png"
    elif cubicleHovered:
        add "lights/cubicleLights.png"
    elif deviceStorageHovered:
        add "lights/deviceStorageLights.png"
    elif copyRoomHovered:
        add "lights/copyRoomLights.png"
    elif titleScreenHovered:
        add "lights/titleScreenLights.png"
    if endDayValid:
        add None

    #Properly ordered
    if defineOffice in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 50
    #Properly ordered
    if defineRD in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 108
    #When ordered correctly, this becomes cybersecurity.
    if defineHelpdesk in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 166
    #When ordered correctly, this becomes server room.
    if defineCyber in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 224
    #When ordered correctly, this becomes helpdesk.
    if defineServer in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 282
    #When ordered correctly, this becomes device storage.
    if defineCubicle in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 340
    #When ordered correctly, this becomes copy room.
    if defineStorage in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 398
    #When ordered correctly this becomes cubicles.
    if defineCopier in eventToView:
        add "eventmark.png":
            xpos 1222
            ypos 456
    
    if cisoEventTrigger:
        add "eventmark.png":
            xpos 1222
            ypos 50

#Procedural menu generator that loads options and associated scores when given a valid event.
screen eventViewer(event):
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
                textbutton "[option['answerText']] [option['score']]" action [
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
    modal True
    add "VOID.jpg"
    #TODO CHANGE!!! This black screen exists to make it easier for me to program in the screens.
    frame:
        background None
        xalign 0.075 yalign 0.2
        vbox:
            #If end day display, show workday and day's score, otherwise
            #Show full session's score
            if displayEnd:
                text "Workday Summary: Day [currentDay]":
                    xalign 0.5
                text "[dayScore] / [dayMaxScore]":
                    xalign 0.5
            else:
                text "Work Session Summary: All Days":
                    xalign 0.5
                text "[score] / [sessionMaxPoints]":
                    xalign 0.5
    frame:
        #Box to display all events within criteria.
        area (62, 243, 350, 400)
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
        area (427, 80, 500, 570)
        side("c"):
            viewport:
                draggable False
                if responseSelected:
                    vbox:
                        text "[responseSelected.get('feedback')]"
    frame:
        #Box for continuing gameplay cycle.
        xalign 0.93 yalign 0.5
        vbox:
            #If day end screen, reset all day-specific variables, increment day, and notify user of what day.
            #Else, prompt user to return to title screen.
            if displayEnd:
                textbutton "Continue to\n   next day": 
                    action [
                        SetVariable("dayScore", 0),
                        SetVariable("dayEvents", []),
                        SetVariable("currentDay", currentDay + 1),
                        SetVariable("endDayValid", False),
                        Notify(f"Entering Day {currentDay + 1}"),
                        Return()]
            else:
                textbutton "Return to Title":
                    action [MainMenu()]