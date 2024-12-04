###########################################RUBY IN THE SHOWER DAY 2
label ruby_in_the_shower_day2:
    $ renpy.music.play("audio/sfx/sfx_shower_hallway.ogg", channel="sfxloop1", fadein=2.0, relative_volume=0.3)
    scene w_328 with dissolve
    a_ "What am I doing? I shouldn't be spying on her like this. But her naked body... it's hard to resist."
    "{i}As I slowly opened the door, I could see Ruby's beautiful form through the steamy glass.{/i}"
    scene w_329 with dissolve
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.play("audio/sfx/sfx_shower.opus", channel="sfxloop1", fadein=2.0, relative_volume=0.3)
    $ renpy.pause()
    "{i}Her skin was glistening with water droplets, and her hair was piled on top of her head in a messy bun.{/i}"
    scene w_330 with dissolve
    $ renpy.pause()
    "{i}My eyes traced the lines of her body, taking in every curve and contour.{/i}"
    scene w_331 with dissolve
    $ renpy.pause()
    "{i}I couldn't help but imagine what it would be like to touch her, to feel her soft skin under my fingertips.{/i}"
    scene w_332 with dissolve
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.play("audio/sfx/sfx_shower_hallway.ogg", channel="sfxloop1", fadein=2.0, relative_volume=0.3)
    a_ "I need to stop this. I shouldn't be thinking like this."
    "{i}Just as I was about to turn around, I heard Ruby's voice.{/i}"
    scene w_333 with dissolve
    r "Mr Alex. What are you doing here?"
    a_ "Shit, she saw me!"
    scene w_334 with dissolve
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    "{i}Panic surged through me, and I reacted on instinct. I pulled the door shut quickly but quietly, my breath coming in shallow gasps{/i}"
    "{i}My heart sank as I realized I had been caught. Trying to come up with an excuse for my behavior.{/i}"
    "{i}With that, I backed away from the bathroom door and headed back to my room, feeling a mix of embarrassment and relief.{/i}"
    scene w_337 with dissolve
    "{i}I took a step back, feeling the cold sweat on my brow. Without thinking, I turned and walked away as fast as I could without running, my mind racing. {/i}"
    a_ "What the hell was I thinking? I need to get a grip. This isn't the time for distractions, especially not ones like that."
    "{i}I knew I had crossed a line, and I needed to be more careful in the future.{/i}"
    "{i}But the image of Ruby in the shower was burned into my mind, and I knew it wouldn't leave me easily.{/i}"
    $ renpy.end_replay()
    $ persistent.day4_ruby_in_the_shower_unlocked = True

    return

###########################################SAMUEL FUCKS RUBY DAY 3
init python:
    labels_list = [
        "label_samuelfucksruby_3",
        "label_samuelfucksruby_1",
        "label_samuelfucksruby_2"
    ]

    current_label_index = 0

    def change_label():
        global current_label_index
        current_label_index += 1
        if current_label_index >= len(labels_list):
            current_label_index = 0
        renpy.jump(labels_list[current_label_index])

screen angle_viewer():
    vbox:
        spacing 10
        xpos 0.96
        ypos 0.02
        anchor (0.0, 0.0)

        imagebutton:
            idle im.Scale("gui/change_views.png", 60, 60)
            hover im.Scale("gui/change_views.png", 60, 60)
            action Function(change_label)
            xalign 0.5
            yalign 0.5
            hover_sound "audio/hover_sound.mp3"
            activate_sound "audio/click_sound.mp3"
            tooltip "Switch to Next"

        imagebutton:
            idle im.Scale("gui/exit_views.png", 60, 60)
            hover im.Scale("gui/exit_views.png", 60, 60)
            action Jump("samuel_fucks_ruby_day3_2")
            xalign 0.5
            yalign 0.5
            hover_sound "audio/hover_sound.mp3"
            activate_sound "audio/click_sound.mp3"
            tooltip "Continue the Story"

label samuel_fucks_ruby_day3_1:
    $ renpy.music.stop("ambient1", fadeout=2.0)
    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    $ renpy.music.stop("music2", fadeout=2.0)
    scene w_653 with dissolve
    "{i}The closer I got, the more I could hear the quiet sounds of rustling hay and a faint, rhythmic creaking from within.{/i}"
    scene w_654 with dissolve
    "{i}My pulse quickened with an uneasy suspicion as I crept up to the door, peering inside.{/i}"
    scene w_655 with dissolve
    "{i}The scene I stumbled upon made me stop cold.{/i}"
    scene w_656 with dissolve
    $ renpy.music.play("audio/musics/sexy_music.mp3", "music1", fadein=2.0, relative_volume=0.2)
    "{i}There, right in the middle of the barn, were Ruby and Samuel—entangled in each other, lost in a heated, intimate moment that caught me completely off guard.{/i}"
    scene w_657 with dissolve
    "{i}Ruby was standing with her arms resting on a pile of hay, her head thrown back in ecstasy.{/i}"
    $ renpy.music.play("audio/adult/ruby_moanpent10.mp3", "sfx1", relative_volume=0.2)
    scene w_659 with dissolve
    "{i}Samuel was behind her, his strong hands gripping her hips as he thrust into her. The sound of their bodies slapping together filled the barn, along with Ruby's moans of pleasure.{/i}"
    $ renpy.music.play(["audio/adult/ruby_moansamuel10.opus" , "audio/adult/ruby_moansamuel11.opus" , "audio/adult/ruby_moansamuel12.opus"], "sfxloop1", fadein=2.0, relative_volume=0.1)
    scene w_660 with dissolve
    e_ "What the hell did I just walk into? Seriously? Of all the people… Ruby and Samuel? Why here? Why now?"
    "{i}I tried to quiet my breathing, suddenly feeling ridiculous for being there, for having seen them.{/i}"
    scene w_661 with dissolve
    "{i}Part of me wanted to laugh at the absurdity of it all, while another part… well, it was complicated.{/i}"
    "{i}Samuel had always been a bit of an enigma, and Ruby, well… she wasn’t exactly who I would have expected him to be with.{/i}"

    $ emmaspysamuelrubyday3 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}I keep spying{/size}{/font}":
            $ emmaspysamuelrubyday3 = True

            scene w_671 with dissolve
            "{i}I knew I shouldn't be here, but the thought of what might be happening inside the barn was too tempting to resist.{/i}"
            scene w_672 with dissolve
            "{i}Tonight, I couldn't help but give in to my curiosity. Peeking through the in the door, I could see them clearly.{/i}"
            $ renpy.music.stop("sfxloop1", fadeout=2.0)
            scene w_673 with dissolve
            r "Fuck, Samuel,"
            $ renpy.music.play("audio/adult/ruby_moanpent10.mp3", "sfx1", relative_volume=0.2)
            scene w_674 with dissolve
            "{i}she gasped, her voice echoing in the rustic space.{/i}"
            r "Harder, please."
            $ renpy.music.play(["audio/adult/ruby_moansamuel10.opus" , "audio/adult/ruby_moansamuel11.opus" , "audio/adult/ruby_moansamuel12.opus"], "sfxloop1", fadein=2.0, relative_volume=0.4)
            scene run_samuelfucksruby1 with fade
            $ renpy.pause()
            "{i}Samuel obliged, his pace quickening.{/i}"
            s "You like that, don't you, Ruby? You like feeling my big cock inside you."
            "{i}Ruby let out a loud moan, her body trembling with each powerful thrust.{/i}"
            r "Yes, yes, I do,"
            $ renpy.music.stop("sfxloop1", fadeout=2.0)
            $ renpy.music.play(["audio/adult/ruby_moansamuel10.opus" , "audio/adult/ruby_moansamuel11.opus" , "audio/adult/ruby_moansamuel12.opus"], "sfxloop2", fadein=2.0, relative_volume=0.2)
            scene w_677 with dissolve
            "{i}I watched, my own body reacting to the scene before me.{/i}"
            scene w_678 with dissolve
            "{i}My pussy began to throb,{/i}"
            $ renpy.music.stop("sfxloop2", fadeout=2.0)
            $ renpy.music.play(["audio/adult/ruby_moansamuel10.opus" , "audio/adult/ruby_moansamuel11.opus" , "audio/adult/ruby_moansamuel12.opus"], "sfxloop1", fadein=2.0, relative_volume=0.1)
            scene w_679 with dissolve
            "{i}and I slid my hand down my jeans, feeling the wetness already building.{/i}"
            $ renpy.music.play("audio/adult/emma_moangentl1.opus", "sfxloop2", fadein=2.0, relative_volume=0.3)
            scene run_emmarubbedgently1 with dissolve
            "{i}I rubbed gently, my fingers moving in time with Samuel's thrusts.{/i}"
            scene run_emmarubbedgently1 with dissolve
            $ renpy.pause()
            $ renpy.music.stop("sfxloop2", fadeout=2.0)
            scene w_666 with dissolve
            $ renpy.music.stop("sfxloop1", fadeout=2.0)
            $ renpy.pause()
            $ renpy.music.play("audio/adult/ruby_moanpent10.mp3", "sfx1", relative_volume=0.4)
            scene w_667 with dissolve
            $ renpy.pause()
            scene w_658 with dissolve
            $ renpy.pause()
            $ renpy.music.play("audio/adult/ruby_moan10.opus", "sfxloop1", fadein=2.0, relative_volume=0.2)
            "{i}Suddenly, Samuel grabbed Ruby by the neck, pulling her upright so her back was pressed against his chest.{/i}"
            s "Look at me,"
            "{i}he commanded, his voice rough with desire. Ruby turned her head, her eyes meeting his as he continued to fuck her, now faster and harder.{/i}"
            s "Watching you take my cock like this, Ruby, it drives me crazy,"
            $ renpy.music.stop("sfxloop1", fadeout=2.0)
            $ renpy.music.play("audio/adult/ruby_moan10.opus", "sfxloop2", fadein=2.0, relative_volume=0.4)
            "{i}Ruby's moans grew louder, her body convulsing with each forceful thrust.{/i}"
            scene w_682 with dissolve
            "{i}I watched, my breath coming in ragged gasps as I brought myself to orgasm, the sound of their pleasure echoing in my ears.{/i}"
            scene w_682 with dissolve
            $ renpy.pause()

            jump view_samuel_fucks_ruby
        "{font=fonts/hatten.ttf} {size=50}I go to the room{/size}{/font}":
            $ emmaspysamuelrubyday3 = False

            scene w_662 with dissolve
            e_ "Okay, Emma, pull it together. Just sneak away, and pretend you didn’t see anything. Don’t be that person. But seriously, Ruby?"
            scene w_666 with dissolve
            "{i}I peeked around the corner again just to make sure they hadn’t noticed my moment of voyeurism.{/i}"
            scene w_663 with dissolve
            e_ "How long have they been sneaking around like this? And in the barn? Come on. Get a room at least."
            scene w_664 with dissolve
            "{i}I shook my head to myself, then carefully backed away from the barn’s entrance, trying not to make any noise.{/i}"
            "{i}The last thing I needed was for them to catch me here, lurking like some kind of creep. I quickly slipped behind the doorway, hidden in the shadows again.{/i}"
            scene w_665 with dissolve
            e_ "Still… now I know. And maybe I wish I didn’t."
            "{i}My brain was still buzzing with the implications of what I had seen, though I kept telling myself it was none of my business.{/i}"

            jump samuel_fucks_ruby_day3_3

label label_samuelfucksruby_1:
    scene samuelfucksruby1_2 with fade
    s "You're so beautiful, Ruby"
    r "You feel so good,"
    s "You’re taking it so well, Ruby… thought you’d be begging me to slow down by now."
    r "You wish… I can take everything you've got."
    s "Let’s see how long you last."
    window hide
    $ renpy.pause(hard=True)
    jump label_samuelfucksruby_1

label label_samuelfucksruby_2:
    scene samuelfucksruby1_1 with fade
    r "Samuel… fuck… don't stop…"
    s "You think I’m stopping now? No chance…"
    r "Harder… I want more…"
    s "Greedy, aren't you?"
    s "This what you wanted?"
    r "Yes… yes, fuck… just like that…"
    window hide
    $ renpy.pause(hard=True)
    jump label_samuelfucksruby_2

label label_samuelfucksruby_3:
    scene samuelfucksruby1_3 with fade
    r "Harder, Fuck me harder, Samuel."
    r "Fuck me harder,."
    r "Yes, yes, right there,"
    s "Fuck, you're so tight,"
    r "Yes, yes, more,"
    window hide
    $ renpy.pause(hard=True)
    jump label_samuelfucksruby_3

label view_samuel_fucks_ruby:
    show screen angle_viewer
    $ renpy.pause(hard=True)
    jump view_samuel_fucks_ruby

label samuel_fucks_ruby_day3_2:
    hide screen angle_viewer
    s "You're so fucking tight, Ruby,"
    s "I can't get enough of you."
    r "You feel so good, Samuel. So fucking good."
    s "Your pussy is so wet. You like it rough, don't you?"
    r "I love it when you fuck me rough."
    $ renpy.music.stop("sfxloop2", fadeout=2.0)
    $ renpy.music.play("audio/adult/ruby_moan10.opus", "sfxloop1", fadein=2.0, relative_volume=0.2)
    scene w_683 with fade
    $ renpy.music.play("audio/adult/emma_moangentl1.opus", "sfxloop2", fadein=2.0, relative_volume=0.4)
    $ renpy.pause()
    "{i}I mirrored their movements, my hand moving faster against my pussy.{/i}"
    scene w_684 with dissolve
    "{i}I could feel the wetness soaking through my shorts, my clit aching with need.{/i}"
    "{i}My own breath was coming in gasps now, my body tensing as I neared the edge.{/i}"
    scene w_685 with dissolve
    "{i}I began to finger myself, my movements matching the rhythm of Samuel's thrusts.{/i}"
    $ renpy.music.stop("sfxloop2", fadeout=2.0)
    scene w_673 with dissolve
    "{i}Inside the barn, Ruby was crying out, her body trembling as Samuel fucked her harder and harder.{/i}"
    r "I'm going to come, Samuel. I'm going to come all over your cock."
    scene w_674 with dissolve
    r "Samuel... I'm... I'm going to come,"
    s "Come for me, Ruby,"
    s "Come all over my cock."
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.play("audio/adult/ruby_orgasm1.opus", "sfx1", fadein=2.0, relative_volume=1.0)
    scene w_667
    with Dissolve(0.1)
    scene white
    with Dissolve(0.1)
    scene w_667
    with Dissolve(0.1)
    scene w_667
    with Dissolve(0.2)
    scene white
    with Dissolve(0.2)
    scene w_667
    with Dissolve(0.2)
    scene w_667
    with Dissolve(0.3)
    scene white
    with Dissolve(0.3)
    scene w_667
    with Dissolve(0.3)
    scene w_667
    with Dissolve(0.4)
    scene white
    with Dissolve(0.4)
    scene w_667
    with Dissolve(0.4)
    scene w_667
    with Dissolve(0.5)
    scene white
    with Dissolve(0.5)
    scene w_667
    with Dissolve(0.5)
    $ renpy.pause()
    "{i}Her body tensed, and a loud cry escaped her lips as she climaxed. Samuel held her tightly, his own body shaking as he found his release.{/i}"
    $ renpy.music.play("audio/adult/emma_orgasm1.opus", "sfx2", fadein=2.0, relative_volume=1.0)
    scene w_686
    with Dissolve(0.1)
    scene white
    with Dissolve(0.1)
    scene w_686
    with Dissolve(0.1)
    scene w_686
    with Dissolve(0.2)
    scene white
    with Dissolve(0.2)
    scene w_686
    with Dissolve(0.2)
    scene w_686
    with Dissolve(0.3)
    scene white
    with Dissolve(0.3)
    scene w_686
    with Dissolve(0.3)
    scene w_686
    with Dissolve(0.4)
    scene white
    with Dissolve(0.4)
    scene w_686
    with Dissolve(0.4)
    scene w_686
    with Dissolve(0.5)
    scene white
    with Dissolve(0.5)
    scene w_686
    with Dissolve(0.5)
    $ renpy.pause()
    "{i}The sound of their pleasure pushed me over the edge. I bit down on my lip, my body convulsing as an orgasm ripped through me.{/i}"
    "{i}I rode out the waves of pleasure, my body shaking as I came down from the high.{/i}"
    scene w_687 with dissolve
    "{i}As I caught my breath, I slipped my hand out of my shorts, my fingers still trembling from the aftershocks of my orgasm.{/i}"
    "{i}I knew I shouldn't have been here, but I was glad I had.{/i}"
    "{i}I slipped away, my body still tingling from the intense encounter.{/i}"

    jump samuel_fucks_ruby_day3_3

label samuel_fucks_ruby_day3_3:
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.stop("sfxloop2", fadeout=2.0)
    $ renpy.music.stop("music1", fadeout=2.0)
    scene w_669 with dissolve
    $ renpy.pause()
    scene w_670 with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    $ persistent.day5_samuel_fucks_ruby_unlocked = True

    return
