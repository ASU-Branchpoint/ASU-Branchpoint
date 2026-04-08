#Game by:
#Jim Heisler
#Chris Camilleri
#Javier Diaz
#Josh Kim
#A whole host of pre-initialized variables.

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

default departCaller = ""
default score = 0

default officeEventToView = False
default rdEventToView = False
default deskEventToView = False
default cyberEventToView = False
default serverEventToView = False
default cubicleEventToView = False
default storageEventToView = False
default copyEventToView = False

default tutorialMode = False
default gameScript = ""

default fullArrayOfEvents = []
default compactArrayLoop = []
default currentEvents = []
default completedEvents = []

default dynamicRoomArray = []
default shortMenu = []
default dynamScore = 0
default dynamOption = ""
default responseSelected = None
default tempEvent = {}

default mainOfficeHovered = False
default researchDevHovered = False
default helpDeskHovered = False
default cyberSecHovered = False
default serverRoomHovered = False
default cubicleHovered = False
default deviceStorageHovered = False
default copyRoomHovered = False
default titleScreenHovered = False

# The game starts here.

label start:

    show bg cityscape

    call defineArray

    call evUpdateNotif

    "The Almighty CEO" "Whoa now, I thought we told you that you didn't start for another few weeks."

    "The Almighty CEO" "I get that you're eager to get started... but we've got a fiscal quarter to round out and we don't have the wiggle room to take chances."

    "The Almighty CEO" "It's nothing personal. Just hang tight for a little bit and we'll welcome you to your new role with open arms."

    #scene bg room
    
    #"well, I suppose you've got everything under control, then."

    #"Best of luck!"
    
    call screen role_select

    call screen mainGameplayLoop

#000 is access code, 100 is Level 1 access, 010 is Level 2 access, 001 is CISO access.
#Makes gameplay less complicated on lower difficulties by gating accessible departments.
#Also lets our main gameplay screen link directly into tutorial functions without just having two copies.

#001
#1
label mainOfficeSwitch:
    if tutorialMode:
        jump tutorialOfficeGeneral
    elif gameScript == "Level1" or gameScript == "Level2":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        $ departCaller = defineOffice
        jump departmentGeneral

#011
#2
label researchDevSwitch:
    if tutorialMode:
        jump tutorialResDevGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        $ departCaller = defineRD
        jump departmentGeneral

#011
#3
label cyberSecSwitch:
    if tutorialMode:
        jump tutorialCyberSecGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        $ departCaller = defineCyber
        jump departmentGeneral

#011
#4
label serverRoomSwitch:
    if tutorialMode:
        jump tutorialServersGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        $ departCaller = defineServer
        jump departmentGeneral

#011
#5
label helpDeskSwitch:
    if tutorialMode:
        jump tutorialHelpDeskGeneral
    elif gameScript == "Level1":
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    else:
        $ departCaller = defineHelpdesk
        jump departmentGeneral

#111
#6
label deviceStorageSwitch:
    if tutorialMode:
        jump tutorialStorageGeneral
    else:
        $ departCaller = defineStorage
        jump departmentGeneral

#111
#7
label copyRoomSwitch:
    if tutorialMode:
        jump tutorialCopierGeneral
    else:
        $ departCaller = defineCopier
        jump departmentGeneral

#111
#8
label cubicleSwitch:
    if tutorialMode:
        jump tutorialCubicleGeneral
    else:
        $ departCaller = defineCubicle
        jump departmentGeneral


#ALL DEPARTMENTS HAVE BEEN ABSTRACTED TO ONE FUNCTION FOR BREVITY AND UPKEEP
#This label is passed the argument for which department called it based on the switches above, then filters events accordingly.
#TODO: Make departments more distinct by calling a sub-function to do a different animation or something on click based on department.
label departmentGeneral:
    scene bg eventfocus
    #Clears pre-existing array of menu items for subsequent entries to departments.
    $ dynamicRoomArray.clear()
    python:
        global currentEvents
        global dynamicRoomArray
        global departCaller
        for option in currentEvents:
            if option.get('location') == departCaller:
                #If event in active events is in [location], add it to the menu. Works dynamically so multiple events can be in one place.
                    #Hey uhh it actually doesn't work if the events are in the same department, ffs
                dynamicRoomArray.append((option.get('id'), option))
        #Hardcode bail out button
        dynamicRoomArray.append(("Never mind...", "home"))
        shortMenu = renpy.display_menu(dynamicRoomArray)
        
        if shortMenu == "home":
            renpy.call_screen("mainGameplayLoop")
        else:
            renpy.call_screen("eventViewer", event=shortMenu)