label gym:
    #SWITCH BG
    if freeroom_state == FREEROOM_STATE_DAY:
        scene gym_night with dissolve
    # ALEX FREEROOM 1 DAY2
    elif freeroom_state == FREEROOM_STATE_ALEX_FR_1:
        hide screen alex_emma_room_alex_sfr_1
        hide screen garden_bar_alex_sfr_1
        hide screen kitchen_alex_sfr_1
        hide screen living_room_alex_sfr_1
        $ renpy.music.stop("ambient1", fadeout=2.0)
        scene gym_night with dissolve
        show screen gym_alex_sfr_1
    else:
        scene gym_night with dissolve
    
    show screen top_right_button
    window hide
    # Here the menu or other actions can be called in the future
    $ renpy.pause(hard=True)
    jump gym

screen gym_alex_sfr_1():
    #GLASS DOOR
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "take"
        action Call("alex_fr1_gym_glass_door")
        xpos 533
        ypos 144
        xsize 312
        ysize 442

label alex_fr1_gym_glass_door:
    hide screen gym_alex_sfr_1
    $ renpy.music.play("audio/sfx/sfx_door_close.opus", channel="sfx1", relative_volume=0.5)
    a_ "It doesn't budge."
    a_ "There are no signs of forced entry."
    show screen gym_alex_sfr_1

    return
