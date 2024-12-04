label kitchen:
    #SWITCH BG
    if freeroom_state == FREEROOM_STATE_DAY:
        scene kitchen_night with dissolve
    # ALEX FREEROOM 1 DAY2
    elif freeroom_state == FREEROOM_STATE_ALEX_FR_1:
        hide screen alex_emma_room_alex_sfr_1
        hide screen garden_bar_alex_sfr_1
        hide screen living_room_alex_sfr_1
        hide screen gym_alex_sfr_1
        $ renpy.music.stop("ambient1", fadeout=2.0)
        scene kitchen_night with dissolve
        show screen kitchen_alex_sfr_1
    else:
        scene kitchen_night with dissolve
    
    show screen top_right_button
    window hide
    # Here the menu or other actions can be called in the future
    $ renpy.pause(hard=True)
    jump kitchen

screen kitchen_alex_sfr_1():
    #GLASS DOOR
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "take"
        action Call("alex_fr1_kitchen_glass_door")
        xpos 1538
        ypos 207
        xsize 184
        ysize 194

label alex_fr1_kitchen_glass_door:
    hide screen kitchen_alex_sfr_1
    $ renpy.music.play("audio/sfx/sfx_door_close.opus", channel="sfx1", relative_volume=0.5)
    a_ "The glass doors are locked. I try to turn the handle, but it doesn't budge."
    a_ "The lock is in place. There are no signs of forced entry. The attacker definitely didn't come in through here."
    show screen kitchen_alex_sfr_1

    return
