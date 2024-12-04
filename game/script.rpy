# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init -1:
    define e = Character(_("Emma"), color="#fa62d4", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define e_ = Character(_("Emma"), color="#fa62d4", what_color="#ce8ebb", what_italic=True, who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define e__ = Character(_("Mystic Emma"), color="#cc05fd", what_color="#db6cf7", what_italic=True, who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define o = Character(_("Octavia"), color="#cc05fd", what_color="#db6cf7", what_italic=True, who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define a = Character(_("Alex"), color="#4248FF", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define a_ = Character(_("Alex"), color="#4248FF", what_color="#299fd6", what_italic=True, who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define d = Character(_("Daniel"), color="#FF6928", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define d_ = Character(_("Daniel"), color="#FF6928", what_color="#f78a5c", what_italic=True, who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define isa = Character(_("Isabella"), color="#FF00FF", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define isa_ = Character(_("Isabella"), color="#FF00FF", what_color="#f371f3", what_italic=True, who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define s = Character(_("Samuel"), color="#3FFF4C", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define arq = Character(_("Arch-enemy"), color="#FF0400", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define ele = Character(_("Eleanor"), color="#b309f7", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define r = Character(_("Ruby"), color="#FF2E16", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define av = Character(_("Ava"), color="#f5164e", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define tr = Character(_("Tristan"), color="#533d7c", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define v = Character(_("Victor"), color="#7ed8ee", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define t = Character(_("Tanya"), color="#f59c69", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define z = Character(_("Zara"), color="#acf5cd", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define h = Character(_("Henry"), color="#526a86", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define dom = Character(_("Dominic"), color="#ebdc5d", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])

    define tmh_ = Character(_("*Hannah*"), color="#d8e709", what_color="#ebf379", what_font="fonts/consolasb.TTF", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])
    define tme_ = Character(_("*Emma*"), color="#fa62d4", what_color="#ce8ebb", what_font="fonts/consolasb.TTF", who_outlines=[(1, "000000", 0, 0)], what_outlines=[(1, "000000", 0, 0)])


######################################################
#################### SANDBOX TEST ####################
######################################################
    default a_name = "Test"
    define mc = Character("Player")
    define a = Character("[a_name]", icon = "icon alice")
    define an = Character("Ann", icon = "icon ann")
######################################################

init python:
    style.say_dialogue.bold = True

    # Set the default basic cursor
    config.mouse = {
        "default": [("images/freeroom/cursor_default.webp", 0, 0)],
        "talk": [("images/freeroom/cursor_talk.webp", 0, 0)],
        "take": [("images/freeroom/cursor_take.webp", 0, 0)]
    }

    # Sound Channels
    renpy.music.register_channel("music1", "music", loop=True)
    renpy.music.register_channel("music2", "music", loop=True)
    renpy.music.register_channel("sfx1", "sound", loop=False)
    renpy.music.register_channel("sfx2", "sound", loop=False)
    renpy.music.register_channel("sfx3", "sound", loop=False)
    renpy.music.register_channel("sfxloop1", "sound", loop=True)
    renpy.music.register_channel("sfxloop2", "sound", loop=True)
    renpy.music.register_channel("ambient1", "sound", loop=True)

    # Alex Power Functions
    def AlexPowerAdd(addPower=1):
        if not ((alex_power + addPower) > 10):
            return alex_power + addPower
        else:
            return 10
        return
    def AlexPowerRemove(removePower=1):
        if not ((alex_power - removePower) < 0):
            return alex_power - removePower
        else:
            return 0
        return

    # Emma Mental Functions
    def EmmaMentalAdd(addMental=1):
        if not ((emma_mental + addMental) > 10):
            return emma_mental + addMental
        else:
            return 10
        return
    def EmmaMentalRemove(removeMental=1):
        if not ((emma_mental - removeMental) < 0):
            return emma_mental - removeMental
        else:
            return 0
        return


label splashscreen:

    $ renpy.movie_cutscene("movies/logo.webm")    
    scene black
    with Pause(1)

    show discl1 with fade
    with Pause(10)
    hide discl1 with fade
    with Pause(2)

    menu:
        "{font=fonts/hatten.ttf} {size=50} Yes, I am 18 years or older{/size}{/font}":
            hide text with dissolve
            with Pause(1)
            show discl3 with fade
            with Pause(6)
            hide discl3 with fade
            with Pause(1)
        "{font=fonts/hatten.ttf} {size=50} No, I'm under 18{/size}{/font}":
            hide text with fade
            with Pause(1)
            show discl2 with fade
            with Pause(10)
            hide discl2 with fade
            with Pause(1)
            $renpy.quit()

    return


# The game starts here.

label start:

    stop music

    default max_emma_mental = 10
    default max_alex_power = 10
    $ emma_mental = 10
    $ alex_power = 0

    ############################### ALEX'S ROUTE VARIABLES
    ###############DAY 1
    $ alexflirtemmaday1 = False
    $ alexflirteleanorday1 = False
    $ alexemmaanddanieljealousday1 = False
    $ alexprotectrubyday1 = False
    $ alexflirtrubyday1 = False
    ###############DAY 2
    $ alexaboutavaboyfriendavaday2 = False
    $ alexspillswineday2 = False
    $ alexsflirtisabelladay2 = False
    $ alexsholdisabelladay2 = False
    $ alex_fr1_emma_talk = False
    $ alexspiesrubyshowerday2 = False
    $ alexkissemmaday2 = False
    ###############DAY 3
    $ alexreceiveblowjobeleanorday3 = False
    $ alexspieseleanortristanday3 = False
    ###############DAY 4
    $ alexrubydanielinterfereday4 = False
    ###############DAY 5
    $ alexfuckzaraday5 = False
    ###############DAY 6
    $ alexspiesisabellavictorday6 = False

    ############################### EMMA'S ROUTE VARIABLES
    ###############DAY 1
    $ emmateasealexday1 = False
    $ emmagetsmadalexday1 = False
    $ emmahugdanielday2 = False
    ###############DAY 3
    $ emma_fr1_ruby_tanya_talk = False
    $ emma_fr1_zara_talk = False
    $ emma_fr1_ava_isabella_talk = False
    $ emmaspysamuelrubyday3 = False
    ###############DAY 4
    $ emmajealouseleanorday4 = False
    

    # jump intro
    jump intro
    
    return

label sandbox:
    return

screen alex_power_screen():

    bar:
        bar_vertical False
        value AnimatedValue(alex_power, max_alex_power, delay=1.0)
        xpos 10
        ypos 10
        xmaximum 350
        ymaximum 55
        left_bar "gui/alex_power_bar_full.webp"
        right_bar "gui/alex_power_bar.webp"

screen emma_mental_screen():

    bar:
        bar_vertical False
        value AnimatedValue(emma_mental, max_emma_mental, delay=1.0)
        xpos 10
        ypos 10
        xmaximum 350
        ymaximum 55
        left_bar "gui/emma_mental_bar_full.webp"
        right_bar "gui/emma_mental_bar.webp"
