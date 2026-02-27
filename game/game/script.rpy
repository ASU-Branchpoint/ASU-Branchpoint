# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("Brendan")
define g = Character("Gary")


# The game starts here.

label start:

    scene bg room
    
    "well, I suppose you've got everything under control, then."

    "Best of luck!"
    
    jump mainLoop

    return

label mainLoop:
    #modal True

    "Idk"

    return




"""
    menu:
        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        "Do you require a tutorial for this game?"

        "I need a tutorial":
            jump tutorial

        "I don't need a tutorial":
            jump continue
"""

label tutorial:

    scene bg main_hq_hall

    "It's your first day on the job..."

    "Despite the fact the keycard in your hand is clearly labeled 'Intern', you're determined to do the job right."

    "The main door to the wing opens, and a somewhat friendly face greets you as you enter."

    scene bg helpdesk_1

    show b_happy

    b "Welcome in! What is it this time, laptop trouble? Authenticator on the fritz? Access permission issues?"

    b "Ohh, a green keycard? So you're the intern they were telling me about."

    b "Well, we're glad to have you! I know this place ain't much, but we hope you'll excel while you're here!"

    b "Personally, I'm about to head to lunch, but I'll hand it off to main-man Gary and he'll show you the ropes."

    hide b_happy
    show g_mad

    g "Yeah we just kinda keep the beeps beepin and the boops boopin"

    g "lmao"

    hide g_mad

    # This ends the game.

    jump start

    return