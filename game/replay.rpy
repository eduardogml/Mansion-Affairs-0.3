#Gallery code


init python:

    import math 

    def add_gallery_scene(scene_label, gallery_scene_name, gallery_image_path ):
        """
        All arguments must be string.
        """
        if [scene_label, gallery_scene_name, im.Scale(gallery_image_path,640,360)] not in persistent.gallery_b_list:
            persistent.gallery_b_list.append([scene_label, gallery_scene_name, im.Scale(gallery_image_path,640,360)])




screen gallery_navigation():

    ## Change with your image
    add "gui/ireplay.webp"

    viewport id ("gallery_scroll"):
        mousewheel True
        ypos 140
        xpos 30
        ymaximum 800
        has vbox
        style_prefix "gallery_nav"

        ## Gallery Navigation going with alphabet wise.
        textbutton _("") action Show("gallery_a") background "images/alex_name_back.webp" xsize 150 ysize 50 hover_background "images/alex_name_back_over.webp"
        textbutton _("") action Show("gallery_b") background "images/emma_name_back.webp" xsize 150 ysize 50 hover_background "images/emma_name_back_over.webp"
        textbutton _("") action Show("gallery_c") background "images/daniel_name_back.webp" xsize 150 ysize 50 hover_background "images/daniel_name_back_over.webp"
        textbutton _("") action Show("gallery_e") background "images/isabella_name_back.webp" xsize 150 ysize 50 hover_background "images/isabella_name_back_over.webp"
        textbutton _("") action Show("gallery_f") background "images/ava_name_back.webp" xsize 150 ysize 50 hover_background "images/ava_name_back_over.webp"
        textbutton _("") action Show("gallery_g") background "images/ruby_name_back.webp" xsize 150 ysize 50 hover_background "images/ruby_name_back_over.webp"
        textbutton _("") action Show("gallery_h") background "images/natalie_name_back.webp" xsize 150 ysize 50 hover_background "images/natalie_name_back_over.webp"
        textbutton _("") action Show("gallery_i") background "images/eleanor_name_back.webp" xsize 150 ysize 50 hover_background "images/eleanor_name_back_over.webp"
        textbutton _("") action Show("gallery_j") background "images/samuel_name_back.webp" xsize 150 ysize 50 hover_background "images/samuel_name_back_over.webp"
        textbutton _("") action Show("gallery_k") background "images/victor_name_back.webp" xsize 150 ysize 50 hover_background "images/victor_name_back_over.webp"
        textbutton _("") action Show("gallery_l") background "images/dominic_name_back.webp" xsize 150 ysize 50 hover_background "images/dominic_name_back_over.webp"
    
    vbar value YScrollValue("gallery_scroll") xpos 210 ypos 140 ymaximum 800

    # textbutton _("Return") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]

## The position of the vertical box containing the gallery navigation buttons
style gallery_nav_vbox:
    xalign 0.03
    yalign 0.5
    spacing 40


python:
        """


        """




screen gallery_a():
    default gallery_a_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["alex_fuck_zara_day5","{color=#ababab}Zara gives Alex a blowjob{/color}", im.Scale("images/gallery/day7_alex_fuck_zara_off.webp", 640, 360), im.Scale("images/gallery/day7_alex_fuck_zara.webp", 640, 360), persistent.day7_alex_fuck_zara_unlocked]

            
            

        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_a_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_a_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_a_list[i][0], scope={ }, locked=not  gallery_a_list[i][4]) #or master_unlock))
                            idle Transform(gallery_a_list[i][2], zoom=1)
                            hover gallery_a_list[i][3]   #Composite((640, 360), (0, 0), gallery_a_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                            hover_sound "audio/hover_sound.mp3"
                            activate_sound "audio/click_sound.mp3"
                        
                        # font styling on image here
                        text str(gallery_a_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_b():
    default gallery_b_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["girls_in_the_jacuzzi_day3","{color=#ababab}Jacuzzi{/color}", im.Scale("images/gallery/day4_girls_in_the_jacuzzi_off.webp", 640, 360), im.Scale("images/gallery/day4_girls_in_the_jacuzzi.webp", 640, 360), persistent.day4_girls_in_the_jacuzzi_unlocked],
            ["emma_blowjob_alex_day3","{color=#ababab}Octavia's Blowjob{/color}", im.Scale("images/gallery/day5_emma_blowjob_alex_off.webp", 640, 360), im.Scale("images/gallery/day5_emma_blowjob_alex.webp", 640, 360), persistent.day5_emma_blowjob_alex_unlocked],
            ["emma_tanya_shower_day6","{color=#ababab}Emma and Tanya shower{/color}", im.Scale("images/gallery/day8_emma_tanya_shower_off.webp", 640, 360), im.Scale("images/gallery/day8_emma_tanya_shower.webp", 640, 360), persistent.day8_emma_tanya_shower_unlocked]


        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_b_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_b_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_b_list[i][0], scope={ }, locked=not  gallery_b_list[i][4]) #or master_unlock))
                            idle Transform(gallery_b_list[i][2], zoom=1)
                            hover gallery_b_list[i][3]           #Composite((640, 360), (0, 0), gallery_b_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                            hover_sound "audio/hover_sound.mp3"
                            activate_sound "audio/click_sound.mp3"
                        
                        # font styling on image here
                        text str(gallery_b_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_c():
    default gallery_c_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["turan_fucks_aydan","{color=#ababab}Daniel{/color}", im.Scale("images/gallery_lock.webp", 640, 360), im.Scale("images/gallery_lock.webp", 640, 360), persistent.turan_fucks_aydan_unlocked]

            

        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_c_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_c_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_c_list[i][0], scope={ }, locked=not  gallery_c_list[i][4]) #or master_unlock))
                            idle Transform(gallery_c_list[i][2], zoom=1)
                            hover gallery_c_list[i][3]      #Composite((640, 360), (0, 0), gallery_c_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                        
                        # font styling on image here
                        text str(gallery_c_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_e():
    default gallery_e_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["isabella_victor_fucks_day6","{color=#ababab}Isabella & Victor{/color}", im.Scale("images/gallery/day8_isabella_victor_fucks_off.webp", 640, 360), im.Scale("images/gallery/day8_isabella_victor_fucks.webp", 640, 360), persistent.day8_isabella_victor_fucks_unlocked]


        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_e_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_e_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_e_list[i][0], scope={ }, locked=not  gallery_e_list[i][4]) #or master_unlock))
                            idle Transform(gallery_e_list[i][2], zoom=1)
                            hover gallery_e_list[i][3]  #Composite((640, 360), (0, 0), gallery_e_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                            hover_sound "audio/hover_sound.mp3"
                            activate_sound "audio/click_sound.mp3"
                        
                        # font styling on image here
                        text str(gallery_e_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_f():
    default gallery_f_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["ruslan_whore_scene","{color=#ababab}Ava{/color}", im.Scale("images/gallery_lock.webp", 640, 360),im.Scale("images/gallery_lock.webp", 640, 360), persistent.ruslan_whore_scene_unlocked_1]


        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_f_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_f_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_f_list[i][0], scope={ }, locked=not  gallery_f_list[i][4]) #or master_unlock))
                            idle Transform(gallery_f_list[i][2], zoom=1)
                            hover gallery_f_list[i][3]  #Composite((640, 360), (0, 0), gallery_f_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/ruslanhasfunwithhiswhoregrey.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                        
                        # font styling on image here
                        text str(gallery_f_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_g():
    default gallery_g_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["ruby_in_the_shower_day2","{color=#ababab}Ruby in the shower{/color}", im.Scale("images/gallery/day4_ruby_in_the_shower_off.webp", 640, 360), im.Scale("images/gallery/day4_ruby_in_the_shower.webp", 640, 360), persistent.day4_ruby_in_the_shower_unlocked],
            ["samuel_fucks_ruby_day3_1","{color=#ababab}Samuel fucks Ruby{/color}", im.Scale("images/gallery/day5_samuel_fucks_ruby_off.webp", 640, 360), im.Scale("images/gallery/day5_samuel_fucks_ruby.webp", 640, 360), persistent.day5_samuel_fucks_ruby_unlocked],


        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_g_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_g_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_g_list[i][0], scope={ }, locked=not  gallery_g_list[i][4]) #or master_unlock))
                            idle Transform(gallery_g_list[i][2], zoom=1)
                            hover gallery_g_list[i][3]     #Composite((640, 360), (0, 0), gallery_g_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                            hover_sound "audio/hover_sound.mp3"
                            activate_sound "audio/click_sound.mp3"
                        
                        # font styling on image here
                        text str(gallery_g_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_h():

    default gallery_h_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["leyla_threesome","{color=#ababab}Tanya{/color}", im.Scale("images/gallery_lock.webp", 640, 360), im.Scale("images/gallery_lock.webp", 640, 360), persistent.leyla_threesome_1]

        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_h_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_h_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_h_list[i][0], scope={ }, locked=not  gallery_h_list[i][4]) #or master_unlock))
                            idle Transform(gallery_h_list[i][2], zoom=1)
                            hover gallery_h_list[i][3]    #Composite((640, 360), (0, 0), gallery_h_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                        
                        # font styling on image here
                        text str(gallery_h_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_i():
    default gallery_i_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["eleanor_bj1_day3","{color=#ababab}Eleanor's blowjob{/color}", im.Scale("images/gallery/day5_blowjob_eleanor_off.webp", 640, 360), im.Scale("images/gallery/day5_blowjob_eleanor.webp", 640, 360), persistent.day5_blowjob_eleanor_unlocked],
            ["tristan_f_eleanor_day3","{color=#ababab}Tristan fucks Eleanor{/color}", im.Scale("images/gallery/day5_tristan_fuck_eleanor_off.webp", 640, 360), im.Scale("images/gallery/day5_tristan_fuck_eleanor.webp", 640, 360), persistent.day5_tristan_fuck_eleanor_unlocked],
        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_i_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_i_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_i_list[i][0], scope={ }, locked=not  gallery_i_list[i][4]) #or master_unlock))
                            idle Transform(gallery_i_list[i][2], zoom=1)
                            hover gallery_i_list[i][3]   #Composite((640, 360), (0, 0), gallery_i_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                            hover_sound "audio/hover_sound.mp3"
                            activate_sound "audio/click_sound.mp3"
                        
                        # font styling on image here
                        text str(gallery_i_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]


screen gallery_j():
    default gallery_j_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["banuteaseinterninhishome","{color=#ababab}Samuel{/color}", im.Scale("images/gallery_lock.webp", 640, 360), im.Scale("images/gallery_lock.webp", 640, 360), persistent.banu_tease_samir_unlocked]

        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_j_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_j_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_j_list[i][0], scope={ }, locked=not  gallery_j_list[i][4]) #or master_unlock))
                            idle Transform(gallery_j_list[i][2], zoom=1)
                            hover gallery_j_list[i][3]   #Composite((640, 360), (0, 0), gallery_j_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                        
                        # font styling on image here
                        text str(gallery_j_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]

 
screen gallery_k():
    default gallery_k_list = [
            # [Scene Label, Image, Persistent True or False ]
            # ["label_name", im.Scale("images/sample_img.jpg", 640, 360), persistent.mia_hotel_scene_1],
            ["murat_fucks_banu","{color=#ababab}Victor{/color}", im.Scale("images/gallery_lock.webp", 640, 360), im.Scale("images/gallery_lock.webp", 640, 360), persistent.murat_fucks_banu_unlocked],


        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_k_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_k_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_k_list[i][0], scope={ }, locked=not  gallery_k_list[i][4]) #or master_unlock))
                            idle Transform(gallery_k_list[i][2], zoom=1)
                            hover gallery_k_list[i][3]   #Composite((640, 360), (0, 0), gallery_k_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                        
                        # font styling on image here
                        text str(gallery_k_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]

    
screen gallery_l():
    default gallery_l_list = [
            #                                                                                            Size of image,  unlock variable 
            # ["label_name", "Name os the scene that will show in gallery",im.Scale("images/sample_img.jpg", 640, 360), persistent.unlock],
            ["hicran_soaps_banu","{color=#ababab}Dominic{/color}", im.Scale("images/gallery_lock.webp", 640, 360), im.Scale("images/gallery_lock.webp", 640, 360), persistent.hicran_soaps_banu_unlocked]


        ]

    style_prefix "navigation"
    
    
    
    default total_scenes = len(gallery_l_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    # Displays number of pages in the scene
    # text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#ffa237" size gui.interface_text_size
    # displays number of scenes present in the gallery
    # text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_l_list):
                    vbox:
                        imagebutton:                                    #in scope "mc_name": mc or "Main Character"
                            action Replay(gallery_l_list[i][0], scope={ }, locked=not  gallery_l_list[i][4]) #or master_unlock))
                            idle Transform(gallery_l_list[i][2], zoom=1)
                            hover gallery_l_list[i][3]    #Composite((640, 360), (0, 0), gallery_l_list[i][2], (0, 0), "images/backgroundruslanleyladoggy1.png")
                            #insensitive Transform("images/backgroundruslanleyladoggy.png", zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                        
                        # font styling on image here
                        text str(gallery_l_list[i][1]):
                            color "#262626"
                            bold True
                            xalign 0.5
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_back_replay.png" hover_background "gui/button_back_over_replay.png" xsize 200 ysize 50

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#ffa237}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] xsize 100 ysize 50

        textbutton _("") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] background "gui/button_next_replay.png" hover_background "gui/button_next_over_replay.png" xsize 200 ysize 50

    #Gallery exit
    textbutton _("") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95 background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]
