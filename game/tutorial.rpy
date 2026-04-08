default departmentsViewed = []
default tutorialOfficeBypass = False
default cisoEventTrigger = False
default tutorialComplete = False
default officeWarning = True

#TODO: REWRITE THE DEPARTMENT DEFINITIONS! If the events are as simple as we're making them, we need to change how the departments are 
#described to be more accurate. For instance, changing the helpdesk department to be about tech troubleshooting questions would be
#MUCH more accurate than "it spreads to other departments."
label tutorial:
    #Set opening flag to true to allow catch cases and prevent scenario escape.
    $ tutorialMode = True

    $ officeEventToView = True
    $ rdEventToView = True
    $ deskEventToView = True
    $ cyberEventToView = True
    $ serverEventToView = True
    $ cubicleEventToView = True
    $ storageEventToView = True 
    $ copyEventToView = True

    scene bg main_hq_hall

    "It's your first day on the job..."

    "Despite the fact the keycard in your hand is clearly labeled 'Intern', you're determined to do the job right."

    "You walk in the front door at 1:00 PM sharp, as instructed, and with the direction of some helpful receptionists, make your way to the IT department."

    "The main door to the wing opens, and a somewhat friendly face greets you as you enter."

    scene bg helpdesk_1

    #show b_happy

    b "Welcome in! What is it this time, laptop trouble? Authenticator on the fritz? Access permission issues?"

    b "Actually... I don't think I recognize you."

    b "Ohh, the green keycard? So you're the intern they were telling me about!"

    b "Well, we're glad to have you! I know this place ain't much, but we hope you'll excel and learn some tricks of the trade while you're here!"

    b "Actually, I'm a bit tied down behind the desk right now. Someone got locked out of their entire company account! Now it's my job to fix it... I suppose."

    "Brendan picks up a hard-line phone behind the desk and pushes a button."
    
    b "Hey, Giovanni? Yeah. The intern's here. No... No, it's YOUR intern. Who else?"

    b "Great. Thanks."

    b "Just sit down over there for a couple minutes."
    
    b "Hardly the warm welcome we had planned, but things have a funny way of going wrong precisely when you need them to behave."
    
    b "There he is."

    "A man in a surprisingly casual outfit opens the door, calmly walking in."

    g "Pleasure to meet you face-to-face. My apologies for everything that's happened so far."

    #hide b_happy
    #show g_mad

    g "I'm Giovanni, the head of the Cybersecurity department. Doesn't mean a lot since there's only three of us in the department, but still."

    g "I suppose that makes it easier for you to get to know everyone and how to do the job."

    g "With that said, talking about things only gets you so far."

    g "I'll be accompanying you on your first-day-tour, so you can get the lay of the land and know who your colleagues are."

    g "Let's get moving. Just tell me where you want to go first."

    call defineTutorial

    hide g_mad

    scene bg eventfocus

    call screen mainGameplayLoop

    return

label tutorialConclusion:
    g "Hmm... I suppose that's not a half bad option. Certainly worse ways to go about it."
    g "Based on your response, the employees down there have awarded you... [score] out of 5 points."
    g "Betcha didn't think we were keeping score, did you?"
    g "Given that you actually responded with something sensible, it seems like you're a natural at this."
    g "Well, looks like you're really getting the hang of things. I think we'd do well to keep you around even after your time as an intern here is up."
    g "That said... I've still got work to do, and this little \"tour\" of yours has started creeping into my break."
    g "Come swing by my department if you need a hand."
    g "Otherwise, I think you're on your own. You'll start actually working tomorrow. Show up at 9 on the dot."
    "You have now completed the tutorial. When you wish to play the full game, return to the title screen."
    $ tutorialComplete = True
    $ cisoEventTrigger = False
    return

#Tutorial label to handle the event tree for CISO Office.
#When cycling through the department explanations, a string of the department's name is added to an array.
#If the name is in the array, skip the introduction on future clicks and prevent the name being added multiple times.
#If the array is long enough to contain all departments, proceed to the next phase of the tutorial.
label tutorialOfficeGeneral:
    if "CISO" not in departmentsViewed:
        g "I believe I'll leave you on your own for this. It'd be rude for me to sit in with you."
        c "This is my office, the CISO's office."
        c "Easy now... We're a small department. You don't have to be afraid of me."
        c "People know each other on a first-name basis around here, after all."
        c "Maybe you'll end up here one day, when my 30 years is up."
        c "... Assuming no one else steps up to take my place."
        g "Afternoon, Charlie."
        c "Ah, perfect. We just finished our introductions."
        g "We'll be leaving, now."
        "This is where a large number of managerial decisions happen."
        "Events in this location are high-priority with high risk to high reward."
        "Additionally, events in this location tend to be rarer, and persist for longer."
        $ officeEventToView = False
        $ departmentsViewed.append("CISO")
    menu:
        "Could you repeat the department's function?":
            "This is where a large number of managerial decisions happen."
            "Events in this location are high-priority with high risk to high reward."
            "Additionally, events in this location tend to be rarer, and persist for longer."
            jump tutorialOfficeGeneral
        "... An \"event\"\?" if len(departmentsViewed) > 7:
            if tutorialComplete:
                "Events will be marked by an exclamation mark next to their respective department."
                "The bottom option will always take you back to the department list, no strings attached."
                "However, to reach new events and progress the game, decisions will have to be made."
            else:
                g "There's always something to do around here."
                g "As much as I know ol' Charlie isn't a fan of the system, it makes my job a lot easier."
                g "Seeing as I'm head of Cybersecurity, I get notifications from R&D, the Servers, the Helpdesk, Storage, the Copy Room, and the Cubicles."
                g "Our system works by popping up a little mark next to the Department's directory when there's something to do."
                "There are multiple types of events in this simulator, each represented by an exclamation mark."
                "Yellow marks are basic, standard events. Orange marks means there's more than one yellow event to view."
                "Red marks are extreme events. Only one can appear at a time, have a cooldown before another can appear, and put all other event timers on pause when they appear."
                g "On the topic of the Cubicles, looks like something's going on down there for us to resolve. Let's go have a look."
                $ officeWarning = False
                $ cisoEventTrigger = False
                if tutorial not in currentEvents:
                    $ currentEvents.append(tutorial)
                $ cubicleEventToView = True
            jump tutorialOfficeGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for R&D Department.
label tutorialResDevGeneral:
    if "R&D" not in departmentsViewed:
        p "Welcome to the R&D department."
        p "We handle a lot of our company's future-facing projects..."
        p "..."
        p "Uh... I forgot the rest of my spiel."
        p "Well, just stick around a while and watch us work. I prefer action over words, anyway."
        g "He's not good with words, but he's a great boss."
        g "Notably, I don't think any of his employees hate working under him."
        "The R&D department hosts events that will have less short-term impacts and more long-term impacts."
        "However, they should not necessarily be passed up for other departments when time is low."
        $ rdEventToView = False
        $ departmentsViewed.append("R&D")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The R&D department hosts events that will have less short-term impacts and more long-term impacts."
            "However, they should not necessarily be passed up for other departments when time is low."
            jump tutorialResDevGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Helpdesk.
label tutorialHelpDeskGeneral:
    if "Helpdesk" not in departmentsViewed:
        b "Welcome back!"
        b "Guess they've got you walking around like we're animals in a zoo, eh?"
        b "Well, this is the Help Desk. You've got a problem, we're the first people you turn to."
        b "Like, for instance... This! Big hunk of crap here. And..."
        "..."
        g "He's someone with a lot to say. Don't mind him, he does his job and does it well."
        g "Let's get a move on."
        "The Help Desk will be critical in keeping day-to-day functions in tip-top shape."
        "This serves as a middle ground between the Cubicles, the Device Storage, and the Cybersecurity departments."
        "Events here can often be handled easily, but may be overwhelming in comparison to other departments."
        "If neglected, problems here can escalate to other departments, and bring more pressuring decisions with them."
        $ deskEventToView = False
        $ departmentsViewed.append("Helpdesk")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Help Desk will be critical in keeping day-to-day functions in tip-top shape."
            "This serves as a middle ground between the Cubicles, the Device Storage, and the Cybersecurity departments."
            "Events here can often be handled easily, but may be overwhelming in comparison to other departments."
            "If neglected, problems here can escalate to other departments, and bring more pressuring decisions with them."
            jump tutorialHelpDeskGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Cybersecurity.
label tutorialCyberSecGeneral:
    if "Cybersecurity" not in departmentsViewed:
        g "Here's my department. I know it ain't all that pretty..."
        g "But, we keep things safe and secure and that's what counts."
        g "Also, don't touch the light switch."
        g "No, you don't want to find out what happens if you do. Trust me."
        g "Ahem... Regardless, do what we say and there won't be problems between you, me, or the company as a whole."
        "The Cybersecurity Department tends to be extremely self-sufficient, and won't raise issues all that often."
        "When they happen, Cybersecurity events often are high caliber threats."
        "These events can critically affect everything, both short and long-term."
        g "Let's keep moving."
        $ cyberEventToView = False
        $ departmentsViewed.append("Cybersecurity")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Cybersecurity Department tends to be extremely self-sufficient, and won't raise issues all that often."
            "When they happen, Cybersecurity events often are high caliber threats."
            "These events can critically affect everything, both short and long-term."
            jump tutorialCyberSecGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Server Room.
label tutorialServersGeneral:
    if "Servers" not in departmentsViewed:
        a "Who are you? I don't recall opening access..."
        a "Oh, hey, Giovanni. I assume the intern is with you."
        g "Didn't mean to surprise you."
        a "It's just not often that I get visitors while I'm tinkering around back here."
        a "This is the Server Room, obviously. It's a room, full of servers. What more do I need to say."
        a "Oh, yeah. It also holds everything we need to function, documents, employee information, customer data, the whole nine yards."
        a "I tend to forget that, with how much these things give me headaches and throw fits."
        "The Server Room is a mission-critical department with a wide breadth of event severity."
        "While minor events can sometimes be resolved on their own, high-tier events can bring every other department to a screeching halt if left unchecked."
        g "I'll let you get back to it, then. We'll be taking our leave."
        $ serverEventToView = False
        $ departmentsViewed.append("Servers")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Server Room is a mission-critical department with a wide breadth of event severity."
            "While minor events can sometimes be resolved on their own, high-tier events can bring every other department to a screeching halt if left unchecked."
            jump tutorialServersGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Cubicles.
label tutorialCubicleGeneral:
    if "Cubicles" not in departmentsViewed:
        g "Sounds like they're on their best behavior for the intern."
        g "That's rare."
        e "You look a little lost. I'm assuming you're new here?"
        e "Green card... It's been a few weeks since we last had an intern."
        e "Welcome to our lovely little office area. This is where the bulk of our workforce is, and they all report back to me."
        e "I'm always one to welcome new ideas, and letting those ideas flourish and make our department better is always so lovely to watch."
        g "More of an \"if\" than a \"when\". Remember when someone found out a way to circumvent the BYOD ban?"
        e "We don't talk about that."
        "Cubicle events are very often low-grade, common threats with easy answers."
        "They accumulate quickly and can be an easy way to raise your score if nothing else is plausible."
        "If neglected, they can find their own way to resolve their issues, for better or for worse."
        g "Best not get involved in the political environment down here."
        g "Eleanor props it up to be real nice, but it's a warzone when things get going."
        $ cubicleEventToView = False
        $ departmentsViewed.append("Cubicles")
        #Fascinatingly, this is the only department to require manual hiding of the text box following the introduction.
        #Probably something to do with the python code lurking below, but as it's a non-issue and fixed bug it's not of much note.
        window hide
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    #Bastardized copy of pre-existing dropdown event code, starting here.
    $ dynamicRoomArray.clear()
    #Clears array of loaded answers for redundancy.
    python:
        global currentEvents
        global dynamicRoomArray
        global cubicleEventToView
        #Loads relevant variables from renpy instead of using its own blank ones (why does it behave that way)
        #Even though the only event that can possibly spawn in tutorial is in cubicles and is tutorial, better safe than sorry.
        #I'd rather have the game not function properly than break in half when something unexpected happens.
        for option in currentEvents:
            if option.get('location') == defineCubicle:
                dynamicRoomArray.append((option.get('id'), option))
        #If there is no event to resolve, allow display and function of button allowing repeats of the department explanation.
        if not cubicleEventToView:
            dynamicRoomArray.append(("Could you repeat the department's function?", "redefine"))
        #If no event is active and there is an event in completed events, allow explanation of how events play out and resolve.
        if not cubicleEventToView and len(completedEvents) == 1:
            dynamicRoomArray.append(("Repeat how the events play out.", "repeat"))
        #Bail out button to just return to main screen.
        dynamicRoomArray.append(("Never mind...", "home"))
        #Display all buttons defined above.
        shortMenu = renpy.display_menu(dynamicRoomArray)
        
        if shortMenu == "home":
            renpy.call_screen("mainGameplayLoop")
        elif shortMenu == "redefine":
            renpy.say(None, "Cubicle events are very often low-grade, common threats with easy answers.")
            renpy.say(None, "They accumulate quickly and can be an easy way to raise your score if nothing else is plausible.")
            renpy.say(None, "If neglected, they can find their own way to resolve their issues, for better or for worse.")
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
    if "Storage" not in departmentsViewed:
        m "Look, I've told you already... you lot have run me out of Authenticator Cards, I can't activate more until..."
        m "Ah. You're not one of the Cubicle employees."
        m "I apologize for my outburst, those idiots lose those cards like their pockets have holes in them."
        g "And I'm the one who has to keep track of them all once they leave your hands."
        m "Yep. Thanks again, by the way."
        m "Welcome to our humble Device Storage locker. Loaner laptops, dummy ID lanyards, company phones, and once the week rolls over, Authenticator Cards."
        m "And some other, less common things in that closet there."
        m "Now that BYOD is done and gone, if you need something given to you for company use, you're going through us."
        "The Device Storage department is typically extremely self-sufficient, given how few devices need to be handed out in a stable staff."
        "If an event here occurs, it typically means that something is running short."
        "This can drastically drive down the effectiveness and self-sufficiency of other departments as a result."
        g "Unfortunately, I don't think we'll be any help here."
        $ storageEventToView = False
        $ departmentsViewed.append("Storage")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Device Storage department is typically extremely self-sufficient, given how few devices need to be handed out in a stable staff."
            "If an event here occurs, it typically means that something is running short."
            "This can drastically drive down the effectiveness and self-sufficiency of other departments as a result."
            jump tutorialStorageGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Copy Room.
label tutorialCopierGeneral:
    if "Copier" not in departmentsViewed:
        n "The one time the print queue isn't clogged to high heaven..."
        n "Sorry, I've just been monitoring and fixing these things all day."
        n "You'd be astounded how often these things clog up and need things unblocked."
        n "Welcome to the Copy Room. All our paperwork originates here, is duplicated here, and often ultimately meets its end here."
        n "We've got black and white printers, color printers, copiers, shredders, everything in between."
        g "And a cybersecurity black box that even I struggle to wrap my head around."
        n "Yep. For both our sakes, I wish we could have this place run simpler."
        "The Copy Room functions quite simply. The more the other departments operate, the harder it has to work."
        "Events from this department focus primarily on security, and between cybersecurity loopholes that can't be closed..."
        "And paperwork finding its way into trash cans without being properly shredded and disposed of..."
        "Its importance should not be understated when it comes to keeping the company as a whole afloat."
        g "Alright, Norm. I'll be back in a couple days to get that new photocopier set up."
        g "With or without my trusty intern here."
        $ copyEventToView = False
        $ departmentsViewed.append("Copier")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "Could you repeat the department's function?":
            "The Copy Room functions quite simply. The more the other departments operate, the harder it has to work."
            "Events from this department focus primarily on security, and between cybersecurity loopholes that can't be closed..."
            "And paperwork finding its way into trash cans without being properly shredded and disposed of..."
            "Its importance should not be understated when it comes to keeping the company as a whole afloat."
            jump tutorialCopierGeneral
        "Never mind.":
                call screen mainGameplayLoop