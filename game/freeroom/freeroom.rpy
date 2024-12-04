#FREEROOM_STATE_
default FREEROOM_STATE_DAY = 0
default FREEROOM_STATE_AFTERNOON = 1
default FREEROOM_STATE_NIGHT = 3
default FREEROOM_STATE_ALEX_FR_1 = 4
default FREEROOM_STATE_EMMA_FR_1 = 5

default freeroom_state = FREEROOM_STATE_DAY

screen top_right_button():
    
    hbox:
        xpos 1920
        ypos 0
        xanchor 1.0
        spacing 10

        imagebutton:
            idle im.Scale("gui/freeroom/mansion_icon.webp", 150, 150)
            hover im.Scale("gui/freeroom/mansion_icon_hover.webp", 150, 150)
            action ToggleScreen("free_room_menu")
            hover_sound "audio/hover_sound.mp3"
            activate_sound "audio/click_sound.mp3"

screen free_room_menu():
    
    frame:
        xpos 1.0
        ypos 0.12
        anchor (1.0, 0.0)
        
        if freeroom_state == FREEROOM_STATE_EMMA_FR_1:
            vbox:
                spacing 20
                textbutton _("Hydromassage") action [Hide("free_room_menu"), Jump("jacuzzi_bath")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Massage") action [Hide("free_room_menu"), Jump("jacuzzi_massage")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Sofa") action [Hide("free_room_menu"), Jump("jacuzzi_sofa")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
        else:
            vbox:
                spacing 20
                textbutton _("My Room") action [Hide("free_room_menu"), Jump("alex_emma_room")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Living Room") action [Hide("free_room_menu"), Jump("living_room")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Kitchen") action [Hide("free_room_menu"), Jump("kitchen")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Gym") action [Hide("free_room_menu"), Jump("gym")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Mansion Entrance") action [Hide("free_room_menu"), Jump("mansion_entrance")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Pool") action [Hide("free_room_menu"), Jump("pool")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Garden") action [Hide("free_room_menu"), Jump("garden_side1")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
                textbutton _("Garden Bar") action [Hide("free_room_menu"), Jump("garden_bar")]:
                    hover_sound "audio/hover_sound.mp3"
                    activate_sound "audio/click_sound.mp3"
