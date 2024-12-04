label alex_emma_room:
    if freeroom_state == FREEROOM_STATE_DAY:
        scene alex_emma_room_night with dissolve
    # ALEX FREEROOM 1 DAY2
    elif freeroom_state == FREEROOM_STATE_ALEX_FR_1:
        hide screen garden_bar_alex_sfr_1
        hide screen kitchen_alex_sfr_1
        hide screen living_room_alex_sfr_1
        hide screen gym_alex_sfr_1
        $ renpy.music.stop("ambient1", fadeout=2.0)
        scene alex_emma_room_alex_fr_1 with dissolve
        show screen alex_emma_room_alex_sfr_1
    else:
        scene alex_emma_room_night with dissolve
    
    show screen top_right_button
    window hide
    $ renpy.pause(hard=True)
    jump alex_emma_room

##################################### FREEROOM_STATE_ALEX_FR_1
screen alex_emma_room_alex_sfr_1():
    # EMMA
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "talk"
        action Call("alex_fr1_emma")
        xpos 1165
        ypos 391
        xsize 205
        ysize 301

label alex_fr1_emma:
    if alex_fr1_emma_talk:
        hide screen alex_emma_room_alex_sfr_1
        e "Promise me you'll come back safely."
        show screen alex_emma_room_alex_sfr_1
    else:
        hide screen alex_emma_room_alex_sfr_1
        $ alex_fr1_emma_talk = True
        e "Alex, please... be careful."
        e "I don't like this at all."
        e "Promise me you'll come back safely."
        a_ "Emma’s worry is so clear in her eyes, and it hits me harder than I expected."
        a_ "She’s right to be concerned, but I can’t let her fear hold me back. I need to take care of this, for both of us."
        show screen alex_emma_room_alex_sfr_1

    return
