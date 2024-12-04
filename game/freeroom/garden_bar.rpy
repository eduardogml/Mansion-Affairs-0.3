label garden_bar:
    if freeroom_state == FREEROOM_STATE_DAY:
        scene garden_bar_fr_1 with dissolve
    # ALEX FREEROOM 1 DAY2
    elif freeroom_state == FREEROOM_STATE_ALEX_FR_1:
        hide screen alex_emma_room_alex_sfr_1
        hide screen kitchen_alex_sfr_1
        hide screen living_room_alex_sfr_1
        hide screen gym_alex_sfr_1
        $ renpy.music.stop("ambient1", fadeout=2.0)
        $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
        scene garden_bar_fr_1 with dissolve
        show screen garden_bar_alex_sfr_1
    else:
        scene garden_bar_fr_1 with dissolve
    
    show screen top_right_button
    window hide
    $ renpy.pause(hard=True)
    jump garden_bar

##################################### FREEROOM_STATE_ALEX_FR_1
screen garden_bar_alex_sfr_1():
    # KNIFER
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "take"
        action Jump("alex_fr1_knifer")
        xpos 780
        ypos 357
        xsize 55
        ysize 50
    
    # GLASS
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "take"
        action Call("alex_fr1_glass")
        xpos 1287
        ypos 101
        xsize 102
        ysize 74

label alex_fr1_glass:
    if alexspillswineday2:
        if alexsholdisabelladay2:
            hide screen garden_bar_alex_sfr_1
            a_ "The glasses Isabella and I were drinking wine from earlier today."
            show screen garden_bar_alex_sfr_1
        else:
            hide screen garden_bar_alex_sfr_1
            a_ "The glass I was drinking wine from earlier today."
            show screen garden_bar_alex_sfr_1
    else:
        hide screen garden_bar_alex_sfr_1
        a_ "The glasses Emma and I were drinking wine from earlier today."
        show screen garden_bar_alex_sfr_1
    
    return

label alex_fr1_knifer:
    hide screen alex_emma_room_alex_sfr_1
    hide screen garden_bar_alex_sfr_1
    hide screen kitchen_alex_sfr_1
    hide screen living_room_alex_sfr_1
    hide screen gym_alex_sfr_1
    hide screen top_right_button
    scene w_251 with dissolve
    a_ "There it is..."
    a_ "the knife that bastard used. He must have dropped it when I landed that punch. Who the hell is behind this?"
    scene w_320 with dissolve
    a_ "Who would want me dead? Was it someone from my past, or did I step on the wrong toes recently?"
    a_ "This isn’t just some random attack; this was personal."
    scene w_321 with dissolve
    a_ "But whoever it was, they made a mistake, and I won’t let them get away with it."
    scene w_322 with dissolve
    a_ "I need to find them before they can try something like this again. I need answers, and I won’t stop until I get them."
    scene w_323 with dissolve
    a_ "Time to keep searching. I’ll find the son of a bitch, no matter where they’re hiding in this mansion."

    jump day2_alex_2
