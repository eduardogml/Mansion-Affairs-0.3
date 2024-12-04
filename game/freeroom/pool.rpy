label pool:
    #SWITCH BG
    if freeroom_state == FREEROOM_STATE_DAY:
        scene pool_night with dissolve
    # ALEX FREEROOM 1 DAY2
    elif freeroom_state == FREEROOM_STATE_ALEX_FR_1:
        hide screen alex_emma_room_alex_sfr_1
        hide screen garden_bar_alex_sfr_1
        hide screen kitchen_alex_sfr_1
        hide screen living_room_alex_sfr_1
        hide screen gym_alex_sfr_1
        $ renpy.music.stop("ambient1", fadeout=2.0)
        $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
        scene pool_night with dissolve
    else:
        scene pool_night with dissolve
    
    show screen top_right_button
    window hide
    # Here the menu or other actions can be called in the future
    $ renpy.pause(hard=True)
    jump pool
    