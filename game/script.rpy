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
define quickDissolve = Dissolve(0.25)

default gameScript = ""

default departCaller = ""
default fullScore = 0

default eventToView = []

default tutorialMode = False

default fullArrayOfEvents = []
default followUpDefine = []
default currentEvents = []
default completedEvents = []
default dayEvents = []
default sideArray = []
default arrayOfScores = []
default fullArrayOfScores = []
default followUpActive = False
default endDayValid = False
default dayMaxPoints = 0
default sessionMaxPoints = 0

default dynamicRoomArray = []
default shortMenu = []
default dynamScore = 0
default dynamOption = ""
default responseSelected = None
default tempEvent = {}
default activePoints = 0
default activeCeiling = 0
default scoreTerminate = 0
default numDays = 0
default currentDay = 1
default dayScore = 0
default displayEnd = True

default mainOfficeHovered = False
default researchDevHovered = False
default helpDeskHovered = False
default cyberSecHovered = False
default serverRoomHovered = False
default cubicleHovered = False
default deviceStorageHovered = False
default copyRoomHovered = False
default titleScreenHovered = False
default endDayHovered = False
default endDayAvail = False

# The game starts here.

label start:

    show bg cityscape with dissolve
    
    call screen role_select

    scene bg mainloop with dissolve

    call defineFull

    call defineArray

    call evUpdateNotif

    call screen mainGameplayLoop



#Access codes are ordered by rank, 100's slot is EMPLOYEE access, 010's slot is CYBERSEC access, and 001's slot is CISO access.
#Following numbers are the way departments should be ordered on UI.
#All eight switches restrict access based on game difficulty, creating artificial ease of access for low difficulties.
#Refer to 001-1 "mainOfficeSwitch" comments for general switch behavior.

#001
#1
label mainOfficeSwitch:
    #If the game is in tutorial mode, send the player to the equivalent tutorial department.
    #This split was done to keep the departments from getting too messy at the time, and now matters substantially [V]
    #   as the actual gameplay departments were abstracted to one function, which could not be done for tutorial.
    if tutorialMode:
        jump tutorialOfficeGeneral
    #Checks the player's selected difficulty and blocks access to the department if difficulty is too low.
    elif gameScript == "easy" or gameScript == "medium" and defineOffice not in eventToView:
        "The door beeps, and the light blinks red. Your keycard doesn't grant your role access into this department."
        call screen mainGameplayLoop
    #Sets the reference "department" to the corresponding switch, then jumps to the abstract function. See below.
    else:
        $ departCaller = defineOffice
        jump departmentGeneral

#011
#2
label researchDevSwitch:
    if tutorialMode:
        jump tutorialResDevGeneral
    elif gameScript == "easy" and defineRD not in eventToView:
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
    elif gameScript == "easy" and defineCyber not in eventToView:
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
    elif gameScript == "easy" and defineServer not in eventToView:
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
    elif gameScript == "easy" and defineHelpdesk not in eventToView:
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


#The eight departments were originally all their own function, but were abstracted to one function for upkeep and brevity.
#TODO: Make departments more distinct by calling a sub-function to do a different animation or something on click based on department.
label departmentGeneral:
    hide screen mainGameplayLoop
    scene bg eventfocus with quickDissolve
    #Clears pre-existing array of menu items for subsequent entries to departments.
    $ dynamicRoomArray.clear()
    python:
        global currentEvents
        global dynamicRoomArray
        global departCaller
        #Gets every event in the active event queue that matches the referred department.
        for option in currentEvents:
            if option.get('location') == departCaller:
                #Gets the slightly longer description for the question and writes it to the title.
                out = option.get('longhand')
                #For each valid event, add the aforementioned question title to the menu and attach its corresponding event.
                dynamicRoomArray.append((out, option))
        #Hardcoded bail out button to return to previous menu.
        dynamicRoomArray.append(("Never mind...", "home"))
        #Display all events in the "valid" array, with the native tool to track menu response.
        #The way this line works makes no sense logically, but it works nonetheless.
        shortMenu = renpy.display_menu(dynamicRoomArray)
        
        #Get response from the displayed menu. If the bailout was clicked, return to previous menu.
        #   Else, view the full event and all relevant information it contains. See "eventViewer" in screens.
        if shortMenu == "home":
            renpy.show("bg mainloop")
            renpy.with_statement(quickDissolve)
            renpy.call_screen("mainGameplayLoop")
        else:
            renpy.call_screen("eventViewer", event=shortMenu)
