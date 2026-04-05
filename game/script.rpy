# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#RESERVED CHARACTERS: C/Charlie as CISO for lower roles, G/Giovanni for CISO and general.
define j = Character("John") #CEO
define c = Character("Charlie") #CISO
define m = Character("Matt") #Storage head
define e = Character("Eleanor") #Cubicle head
define b = Character("Brendan") #Helpdesk head
define g = Character("Giovanni") #Cybersec head
define p = Character("Peter") #R&D head
define a = Character("Abigail") #Server head
define n = Character("Norman") #Copier head

default fullArrayOfEvents = []
default compactArrayLoop = []
default eventsLength = 0
default eventsToAdd = 0

default gameScript = "Level1"
default gameScriptInit = ""
default tutorialMode = False
default currentEvents = []
default event = ""
default eventText = ""
default eventResponses = 1
default dynamScore = 0
default shortMenu = []
default dynamicRoomArray = []

default choice = "1"

default score = 0
default weight = 1

default mainOfficeHovered = False
default researchDevHovered = False
default helpDeskHovered = False
default cyberSecHovered = False
default serverRoomHovered = False
default cubicleHovered = False
default deviceStorageHovered = False
default copyRoomHovered = False
default titleScreenHovered = False

default officeEventToView = False
default rdEventToView = False
default deskEventToView = False
default cyberEventToView = False
default serverEventToView = False
default cubicleEventToView = False
default storageEventToView = False
default copyEventToView = False

# The game starts here.

label start:

    show bg cityscape

    call defineArray

    "The Almighty CEO" "Whoa now, I thought we told you that you didn't start for another few weeks."

    "The Almighty CEO" "I get that you're eager to get started... but we've got a fiscal quarter to round out and we don't have the wiggle room to take chances."

    "The Almighty CEO" "It's nothing personal. Just hang tight for a little bit and we'll welcome you to your new role with open arms."

    #scene bg room
    
    #"well, I suppose you've got everything under control, then."

    #"Best of luck!"
    
    call screen role_select

    call screen mainGameplayLoop

#000 is access code, 100 is Level 1 access, 10 is Level 2 access, 1 is CISO access.
#Makes gameplay less complicated on lower difficulties by gating accessible departments.

#001
#1
label mainOfficeSwitch:
    if tutorialMode:
        jump tutorialOfficeGeneral
    elif gameScript == "Level1" or gameScript == "Level2":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        jump mainOfficeGeneral

#011
#2
label researchDevSwitch:
    if tutorialMode:
        jump tutorialResDevGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        jump resDevGeneral

#011
#3
label cyberSecSwitch:
    if tutorialMode:
        jump tutorialCyberSecGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        jump cyberSecGeneral

#011
#4
label serverRoomSwitch:
    if tutorialMode:
        jump tutorialServersGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        jump serverRoomGeneral

#011
#5
label helpDeskSwitch:
    if tutorialMode:
        jump tutorialHelpDeskGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        jump helpDeskGeneral

#111
#6
label deviceStorageSwitch:
    if tutorialMode:
        jump tutorialStorageGeneral
    else:
        jump deviceStorageGeneral

#111
#7
label copyRoomSwitch:
    if tutorialMode:
        jump tutorialCopierGeneral
    else:
        jump copyRoomGeneral

#111
#8
label cubicleSwitch:
    if tutorialMode:
        jump tutorialCubicleGeneral
    else:
        jump cubicleGeneral


#Label to handle event trees for CISO Office.
label mainOfficeGeneral:
    menu:
        #If event to view, use the name of the event and display it as a button. Does not support multiple events for the same department. Ditto for all other departments.
        #TODO: Abstract number of events per department to allow multiple at once. REPEAT THIS TO-DO AD INFINITUM FOR ALL DEPARTMENTS.
        #"[line[0]]" for line in compactArrayLoop if officeEventToView:
            #for line in compactArrayLoop if officeEventToView:
            #"[line[0]]":
        "[event]" if officeEventToView:
                call eventLookup
                call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for R&D Department.
label resDevGeneral:
    menu:
        "[event]" if copyEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Helpdesk.
label helpDeskGeneral:
    $ dynamicRoomArray.clear()
    python:
        global currentEvents
        global dynamicRoomArray
        for option in currentEvents:
            if option.get('location') == "helpdesk":
                dynamicRoomArray.append((option.get('id'), option))
        dynamicRoomArray.append(("Never mind...", "home"))
        shortMenu = renpy.display_menu(dynamicRoomArray)
        
        if shortMenu == "home":
            renpy.call_screen("mainGameplayLoop")
        else:
            renpy.call_screen("eventViewer", event=option)

#Label to handle event trees for Cybersecurity.
label cyberSecGeneral:
    menu:
        "[event]" if cyberEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Server Room.
label serverRoomGeneral:
    menu:
        "[event]" if serverEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Cubicles.
label cubicleGeneral:
    menu:
        "[event]" if cubicleEventToView:
            "When handling an event, a list of 2 to 5 options will appear. What response you choose can and will affect your score at the end of the game, and may even end your game early."
            "Much like the real world, there is, more often than not, no truly correct or incorrect answer."
            "Most importantly, these events are chosen randomly from a pool. You may see the same event four times, not at all, or face impossible tasks. How you handle it is, once again, up to you."
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Device Storage.
label deviceStorageGeneral:
    menu:
        "[event]" if storageEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Copy Room.
label copyRoomGeneral:
    $ dynamicRoomArray.clear()
    python:
        global currentEvents
        global dynamicRoomArray
        for option in currentEvents:
            if option.get('location') == "copier":
                dynamicRoomArray.append((option.get('id'), option))
        dynamicRoomArray.append(("Never mind...", "home"))
        shortMenu = renpy.display_menu(dynamicRoomArray)
        
        if shortMenu == "home":
            renpy.call_screen("mainGameplayLoop")
        else:
            renpy.call_screen("eventViewer", event=option)