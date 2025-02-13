screen wait_button(small = False):
    imagebutton:
        idle nqtr_menu_icon_wait
        focus_mask True
        action [
            Call("after_return_from_room_navigation", label_name_to_call = "wait"),
        ]
        if renpy.variant("pc"):
            tooltip _("Wait")
        if small:
            at nqtr_button_location_transform
        else:
            at nqtr_button_action_transform

screen character_icon_screen(icon, my_action = []):
    if icon:
        imagebutton:
            idle icon
            focus_mask True
            action my_action
            at dr_small_face_transform

screen time_text(tm, show_wait_button = False):
    hbox:
        align (0.5, 0.01)
        vbox:
            align (0.5, 0.01)
            text "[tm.hour]:00":
                xalign (0.5)
                size gui.nqtr_hour_text_size
                drop_shadow [(2, 2)]
            text tm.weekday_name:
                xalign (0.5)
                size gui.dr_normal_text_size
                drop_shadow [(2, 2)]
                line_leading -16

        if (show_wait_button):
            # Fixed button to wait
            use wait_button(small = True)

screen button_picture_in_background(button, my_actions = []):
    imagebutton:
        align (button.xalign, button.yalign)
        idle button.picture_in_background
        hover button.picture_in_background_selected
        focus_mask True
        action my_actions
        if renpy.variant("pc"):
            tooltip button.name
        if button.picture_in_background_selected == button.picture_in_background:
            at nqtr_button_picture_transform

screen action_button(act):
    imagebutton:
        idle act.button_icon
        hover act.button_icon_selected
        focus_mask True
        action [
            Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
        ]
        if renpy.variant("pc"):
            tooltip act.name
        at nqtr_button_action_transform

screen action_picture_in_background(act):
    use button_picture_in_background(act, [
        Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
    ])

screen conversation_button(conversation, background):
    python:
        my_action = [
            SetVariable('current_conversation_character', conversation.character),
            SetVariable('conversation_image', background),
            Call("after_return_from_room_navigation", label_name_to_call = conversation.label_name),
        ]
    if not conversation.is_hidden(flags = flags, check_if_has_icon = False):
        frame:
            xysize (gui.nqtr_button_action_size, gui.nqtr_button_action_size + gui.nqtr_button_action_size_error)
            background None

            imagebutton:
                align (0.5, 0.0)
                if conversation.is_button:
                    idle conversation.button_icon
                    hover conversation.button_icon_selected
                else:
                    idle nqtr_menu_icon_talk
                focus_mask True
                action my_action
                at nqtr_button_action_transform
                if renpy.variant("pc"):
                    tooltip _("Talk")

            use character_icon_screen(conversation.character_icon, my_action)

screen conversation_picture_in_background(conversation):
    use button_picture_in_background(conversation, [
        SetVariable('current_conversation_character', conversation.character),
        SetVariable('conversation_image', background),
        Call("after_return_from_room_navigation", label_name_to_call = conversation.label_name),
    ])

screen location_button(location):
    if (location.map_id == cur_map_id and not location.is_hidden(flags = flags)):
        vbox:
            align (location.yalign, location.xalign)
            imagebutton:
                if location.is_picture_in_background:
                    idle location.picture_in_background
                    selected_idle location.picture_in_background_selected
                    selected_hover location.picture_in_background_selected
                selected location == cur_location
                sensitive not location.is_hidden(flags)
                focus_mask True
                action [
                    SetVariable('cur_location', location),
                    Call("after_return_from_room_navigation", label_name_to_call = "change_location"),
                ]
                at nqtr_button_location_transform

            # Locations name
            text location.name:
                size gui.dr_little_text_size
                drop_shadow [(2, 2)]
                xalign 0.5
                text_align 0.5
                line_leading 0
                line_spacing -2

screen map_button(map_id, map, align_value, rotation):
    if not map.is_hidden(flags = flags, check_if_has_icon = False):
        hbox:
            align align_value
            imagebutton:
                idle "gui triangular_button"
                focus_mask True
                sensitive not map.is_disabled(flags)
                action [
                    SetVariable('cur_map_id', map_id), 
                    Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                ]
                if renpy.variant("pc"):
                    tooltip map.name
                at nqtr_button_map_transform(rotation)

screen map(maps, cur_map_id):
    $ map_id_north = maps[cur_map_id].map_id_north
    $ map_id_south = maps[cur_map_id].map_id_south
    $ map_id_east = maps[cur_map_id].map_id_east
    $ map_id_west = maps[cur_map_id].map_id_west

    # North map
    if not isNullOrEmpty(map_id_north):
        use map_button(map_id = map_id_north, map = maps[map_id_north], align_value = (0.5, 0.1), rotation = 270)
    # South map
    if not isNullOrEmpty(map_id_south):
        use map_button(map_id = map_id_south, map = maps[map_id_south], align_value = (0.5, 0.99), rotation = 90)
    # West map
    if not isNullOrEmpty(map_id_west):
        use map_button(map_id = map_id_west, map = maps[map_id_west], align_value = (0.001, 0.5), rotation = 180)
    # East map
    if not isNullOrEmpty(map_id_east):
        use map_button(map_id = map_id_east, map = maps[map_id_east], align_value = (0.999, 0.5), rotation = 0)

screen room_button_list(rooms, commitments_in_cur_location):
        $ key_room = 0
        # Rooms
        hbox:
            yalign 0.99
            xalign 0.01
            spacing 2

            for room in rooms:
                # Check the presence of ch in that room
                $ there_are_ch = False
                for comm in commitments_in_cur_location.values():
                    # If it is the selected room
                    if comm != None and room.id == comm.room_id:
                        # I insert hbox only if they are sure that someone is there
                        $ there_are_ch = True

                # If the Locations where I am is the same as the Locations where the room is located
                if (room.location_id == cur_location.id and room.is_button and not room.is_hidden(flags)):
                    $ key_room += 1
                    use room_button(room, cur_room, key_room, there_are_ch)

screen room_button(room, cur_room, key_room, find_ch = False):
    python:
        room_action = [
                SetVariable('prev_room', cur_room),
                SetVariable('cur_room', room),
                Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
            ]
    vbox:
        frame:
            xysize (gui.nqtr_button_room_size, gui.nqtr_button_room_size + gui.dr_little_text_size)
            background None

            # Room icon
            imagebutton:
                align (0.5, - 0.15)
                if room.is_button:
                    idle room.button_icon
                selected_idle room.button_icon_selected
                selected_hover room.button_icon_selected
                selected (True if cur_room and cur_room.id == room.id else False)
                sensitive not room.is_disabled(flags)
                focus_mask True
                action room_action
                at nqtr_button_room_transform

            # Character icon
            if find_ch:
                hbox:
                    align (0.5, 0.6)
                    for comm in commitments_in_cur_location.values():
                        # If it is the selected room
                        if room.id == comm.room_id:
                            use character_icon_screen(comm.character_icon, room_action)

            # Room name
            text room.name:
                align (0.5, 0.99)
                size gui.dr_little_text_size
                drop_shadow [(2, 2)]
                text_align 0.5
                line_leading 0
                line_spacing -2

        if key_room < 10:
            key str(key_room) action room_action
        elif key_room == 10:
            key str(0) action room_action

screen room_picture_in_background(room):
    use button_picture_in_background(room, [
        SetVariable('prev_room', cur_room),
        SetVariable('cur_room', room),
        Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
    ])
