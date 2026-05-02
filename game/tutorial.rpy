default cubicleEvent = False
default cisoEventTrigger = False
default tutorialComplete = False
default officeWarning = True
default tutorialSection = 0
default reviewTerms = False
default tutorial_event_library = []

#TODO: REWRITE THE DEPARTMENT DEFINITIONS! If the events are as simple as we're making them, we need to change how the departments are 
#described to be more accurate. For instance, changing the helpdesk department to be about tech troubleshooting questions would be
#MUCH more accurate than "it spreads to other departments."
label tutorial:
    #Set opening flag to true to allow catch cases and prevent scenario escape.
    $ tutorialMode = True
    $ eventToView = [defineOffice, defineRD, defineCyber, defineServer, defineHelpdesk, defineStorage, defineCopier, defineCubicle]
    $ gameScript = "Tutorial"
    scene bg main_hq_hall with dissolve
    "It's your first day on the job..."
    "Despite the fact the keycard in your hand is clearly labeled 'Intern', you're determined to do the job right."
    "You walk in the front door at 1:00 PM sharp, as instructed, and with the direction of some helpful receptionists, make your way to the IT department."
    "The main door to the wing opens, and a somewhat friendly face greets you as you enter."
    scene bg helpdesk_1 with quickDissolve
    b "Welcome in! What is it this time, laptop trouble? Authenticator on the fritz? Access permission issues?"
    b "Actually... I don't think I recognize you."
    b "Ohh, the green keycard? So you're the intern they were telling me about!"
    b "Well, we're glad to have you! I know this place ain't much, but we hope you'll excel and learn some tricks of the trade while you're here!"
    b "Actually, I'm a bit tied down behind the desk right now. Someone got locked out of their entire company account! Now it's my job to fix it... I suppose."
    g "You must be the intern, then."
    g "Well, seems like you found your way into the building just fine. Better than some, I'll admit."
    g "Welcome in. As you may or may not know, one of our primary focuses is to keep our customers' information secure. Hence the part of your role: \"Information Security\""
    g "If you stay with us full time, you'd be handling a lot of sensitive information, payment activity, core systems, and daily interactions with customers."
    g "Not to mention, the reputation of our business as a whole."
    g "On that note, as I'm sure you know, our goal at Branchpoint is to protect customers, our coworkers, our assets, and our reputation."
    g "Very original, I know. If you want to complain, go to someone more important than me."
    g "Before we get going on our tour of the place, you should know that if you ever find yourself in doubt of what you're doing..."
    b "You should slow down, follow the defined processes, and report anything you find unusual."
    g "Glad to see you haven't forgotten, at least."
    g "Let's set off, then."

    call defineTutorialSample

    scene bg mainloop with dissolve

    call screen mainGameplayLoop

    return

label tutorialConclusion:
    g "Hmm... I suppose that's not a half bad option. Certainly worse ways to go about it."
    g "Based on your response, the employees down there have awarded you... [dayScore] out of 5 points."
    g "Betcha didn't think we were keeping score, did you?"
    g "Given that you actually responded with something sensible, it seems like you're a natural at this."
    g "Well, looks like you're really getting the hang of things. I think we'd do well to keep you around even after your time as an intern here is up."
    g "That said... I've still got work to do, and this little \"tour\" of yours has started creeping into my break."
    g "I'll let someone else run you through some advanced employee filtering."
    g "Assuming you do well, you'll start actually working tomorrow. In which case, show up at 9 on the dot."
    "You will now face some simple stylized events."
    "Good luck!"
    $ cubicleEvent = False
    $ eventToView.clear()
    $ tutorialComplete = True
    $ cisoEventTrigger = False
    if not tutorial_event_library:
        call defineTutorial
    scene bg mainloop with quickDissolve
    call screen mainGameplayLoop

label spawnTutorialEvents:
    if tutorialComplete:
        python:
            for entry in tutorial_event_library:
                if entry.get('spawn_rules').get('section') == tutorialSection:
                    currentEvents.append(entry)
        call evUpdateNotif
    return
        

    
label finishTutorial:
    scene bg eventfocus with quickDissolve
    "You have now completed the tutorial. When you wish to play the full game, return to the title screen."
    $ eventToView.clear()
    $ cubicleEvent = False
    $ tutorialComplete = True
    $ cisoEventTrigger = False
    $ tutorialComplete = False
    $ endDayValid = False
    scene bg mainloop with quickDissolve
    call screen mainGameplayLoop

#Tutorial label to handle the event tree for CISO Office.
#When cycling through the department explanations, a string of the department's name is added to an array.
#If the name is in the array, skip the introduction on future clicks and prevent the name being added multiple times.
#If the array is long enough to contain all departments, proceed to the next phase of the tutorial.
label tutorialOfficeGeneral:
    scene bg eventfocus with quickDissolve
    if defineOffice in eventToView:
        c "Welcome to my office, intern. We hope you'll stay a while and consider us as a more permanent employer."
        "A large number of high-grade managerial decision happen within the CISO's office."
        "As such, it won't see many events. However, events that show up within the office have high scores for correct responses and dire consequences for incorrect responses."
        "Handle these events appropriately."
        c "See you around, then."
        $ eventToView.remove(defineOffice)
    menu:
        "Could you repeat the department's function?":
            "This is where a large number of managerial decisions happen."
            "Events in this location are high-priority with high risk to high reward."
            "Additionally, events in this location tend to be rarer."
            jump tutorialOfficeGeneral
        "... An \"event\"\?" if len(eventToView) < 1:
            if tutorialComplete:
                "Events will be marked by an exclamation mark next to their respective department."
                "The bottom option will always take you back to the department list, no strings attached."
                "However, to reach new events and progress the game, decisions will have to be made."
            else:
                g "There's always something to do around here."
                g "We have a patented system that allows us to easily throw up flags for our department when we can't fix something ourselves."
                g "You've been using it this whole time to find your way around. Just... without the permissions you'd need to see the flags."
                "An event in a department is denoted by the orange exclamation mark next to its name."
                "The bottom option will always take you back to the department list, no strings attached."
                "However, to reach new events and progress the game, decisions will have to be made."
                "Events can range in difficulty, regardless of the role and difficulty selected during gameplay."
                "Some events, if mishandled, can force the user into handling an event that would otherwise never happen."
                "As the day progresses, the number of events to handle will increase, and events left in queue when the day ends will be counted for no points."
                g "On that note, my dashboard seems to have slid a rather silly proposition my way."
                g "Let's go investigate the Cubicles."
                $ officeWarning = False
                $ cisoEventTrigger = False
                if tutorial not in currentEvents:
                    $ currentEvents.append(tutorial)
                $ eventToView.append(defineCubicle)
                $ cubicleEvent = True
            jump tutorialOfficeGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop

#Tutorial label to handle event trees for R&D Department.
label tutorialResDevGeneral:
    scene bg eventfocus with quickDissolve
    if defineRD in eventToView:
        p "Welcome to the R&D department."
        p "We handle a lot of our company's future-facing projects..."
        p "..."
        p "Uh... I forgot the rest of my spiel."
        p "Just let us do our thing and you'll be pleasantly surprised. I prefer action over words, anyway."
        "The R&D department hosts events that will have less short-term impacts and more long-term impacts."
        "These will often feature critical operations that could shape the company's future."
        $ eventToView.remove(defineRD)
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The R&D department hosts events that will have less short-term impacts and more long-term impacts."
            "These will often feature critical operations that could shape the company's future."
            jump tutorialResDevGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Helpdesk.
label tutorialHelpDeskGeneral:
    scene bg eventfocus with quickDissolve
    if defineHelpdesk in eventToView:
        b "Welcome back!"
        b "Guess they've got you walking around like we're animals in a zoo, eh?"
        b "Well, this is the Help Desk. You've got a problem, we're the first people you turn to."
        "The Help Desk will be critical in keeping day-to-day functions in tip-top shape."
        "Events in this location will frequently feature employee-side problems unrelated to public-facing operations."
        $ eventToView.remove(defineHelpdesk)
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Help Desk will be critical in keeping day-to-day functions in tip-top shape."
            "Events in this location will frequently feature employee-side problems unrelated to public-facing operations."
            jump tutorialHelpDeskGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Cybersecurity.
label tutorialCyberSecGeneral:
    scene bg eventfocus with quickDissolve
    if defineCyber in eventToView:
        g "Here's my department. I know it ain't all that pretty..."
        g "But, we keep things safe and secure and that's what counts."
        "The Cybersecurity department frequently features events that relate to external threats."
        "Mishandling these events will often have dire consequences, but handling them correctly will almost always net you a large sum of points."
        g "Let's keep moving."
        $ eventToView.remove(defineCyber)
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Cybersecurity department frequently features events that relate to external threats."
            "Mishandling these events will often have dire consequences, but handling them correctly will almost always net you a large sum of points."
            jump tutorialCyberSecGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Server Room.
label tutorialServersGeneral:
    scene bg eventfocus with quickDissolve
    if defineServer in eventToView:
        a "Well, you're a new face."
        a "Hope you don't mind the background noise. These servers get pretty noisy when things get going."
        "Server room events usually focus on customer-facing problems relating to web servers and web sites."
        "While they are not mission critical, these events should not be ignored."
        a "See you around, rookie."
        $ eventToView.remove(defineServer)
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "Server room events usually focus on customer-facing problems relating to web servers and web sites."
            "While they are not mission critical, these events should not be ignored."
            jump tutorialServersGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Cubicles.
label tutorialCubicleGeneral:
    scene bg eventfocus with quickDissolve
    if defineCubicle in eventToView and not cubicleEvent:
        e "You look a little lost. I'm assuming you're new here?"
        e "Green card... It's been a few weeks since we last had an intern."
        e "Well, welcome to our cubicles. Majority of where the grunt work gets done."
        "Cubicle events are very often events that happen employee-to-employee, or employee-to-customer."
        "These will be the majority of the easy events, although they are the most numerous."
        e "See you around."
        $ eventToView.remove(defineCubicle)
        #Fascinatingly, this is the only department to require manual hiding of the text box following the introduction.
        #Probably something to do with the python code lurking below, but as it's a non-issue and fixed bug it's not of much note.
        window hide
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    #Bastardized copy of pre-existing dropdown event code, starting here.
    $ dynamicRoomArray.clear()
    #Clears array of loaded answers for redundancy.
    python:
        global currentEvents
        global dynamicRoomArray
        global eventToView
        #Loads relevant variables from renpy instead of using its own blank ones (why does it behave that way)
        #Even though the only event that can possibly spawn in tutorial is in cubicles and is tutorial, better safe than sorry.
        #I'd rather have the game not function properly than break in half when something unexpected happens.
        for option in currentEvents:
            if option.get('location') == defineCubicle:
                dynamicRoomArray.append((option.get('longhand'), option))
        #If there is no event to resolve, allow display and function of button allowing repeats of the department explanation.
        if defineCubicle not in eventToView and not cubicleEvent:
            dynamicRoomArray.append(("Could you repeat the department's function?", "redefine"))
        #If no event is active and there is an event in completed events, allow explanation of how events play out and resolve.
        if defineCubicle not in eventToView and len(dayEvents) == 1:
            dynamicRoomArray.append(("Repeat how the events play out.", "repeat"))
        #Bail out button to just return to main screen.
        dynamicRoomArray.append(("Never mind...", "home"))
        #Display all buttons defined above.
        shortMenu = renpy.display_menu(dynamicRoomArray)
        
        if shortMenu == "home":
            renpy.show("bg mainloop")
            renpy.with_statement(quickDissolve)
            renpy.call_screen("mainGameplayLoop")
        elif shortMenu == "redefine":
            renpy.say(None, "Cubicle events are very often events that happen employee-to-employee, or employee-to-customer.")
            renpy.say(None, "These will be the majority of the easy events, although they are the most numerous.")
            renpy.jump("tutorialCubicleGeneral")
        elif shortMenu == "repeat":
            renpy.say(None, "When handling an event, a list of 2 to 5 options will appear. What response you choose can and will affect your score at the end of the game, and may even end your game early.")
            renpy.say(None, "Much like the real world, there is, more often than not, no truly correct or incorrect answer.")
            renpy.say(None, "Most importantly, these events are chosen randomly from a pool. You may see the same event four times, not at all, or face nearly impossible tasks. How you handle it is, once again, up to you.")
            renpy.jump("tutorialCubicleGeneral")
        #Assuming the console was not used and things function as intended, this allows us to open the tutorial event without catching
        #the exact name, id, or any other identifier of the tutorial event with 100% accuracy. Simple is as simple does.
        else:
            renpy.say(None, "When handling an event, a list of 2 to 5 options will appear. What response you choose can and will affect your score at the end of the game, and may even end your game early.")
            renpy.say(None, "Much like the real world, there is, more often than not, no truly correct or incorrect answer.")
            renpy.say(None, "Most importantly, these events are chosen randomly from a pool. You may see the same event four times, not at all, or face nearly impossible tasks. How you handle it is, once again, up to you.")
            renpy.call_screen("eventViewer", event=option)

#Tutorial label to handle event trees for Device Storage.
label tutorialStorageGeneral:
    scene bg eventfocus with quickDissolve
    if defineStorage in eventToView:
        m "Oh, look at you with your fancy green keycard."
        m "Stick around long enough, you'll get upgraded to a yellow one like the rest of us."
        "Device Storage events typically relate to employee devices and company property."
        m "Peace out."
        $ eventToView.remove(defineStorage)
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "Device Storage events typically relate to employee devices and company property."
            jump tutorialStorageGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Copy Room.
label tutorialCopierGeneral:
    scene bg eventfocus with quickDissolve
    if defineCopier in eventToView:
        n "You aren't here to color print anything, are ya?"
        n "Ah, intern. Welcome to the copy room... Not counting color printing."
        "Copy room issues will typically involve employe permission issues and internal networking."
        "Additionally, unattended internal documents will be a pervasive issue."
        n "Go warn the rest of the departments for me, they don't seem to see what I'm saying."
        
        $ eventToView.remove(defineCopier)
    if len(eventToView) < 1 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "Copy room issues will typically involve employe permission issues and internal networking."
            "Additionally, unattended internal documents will be a pervasive issue."
            jump tutorialCopierGeneral
        "Never mind.":
                scene bg mainloop with quickDissolve
                call screen mainGameplayLoop