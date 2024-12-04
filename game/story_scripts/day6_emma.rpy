label day6_emma_1:

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 8rd_day with fade
    $ renpy.pause()
    hide 8rd_day with dissolve

    scene w_326 with fade
    "{i}As I leaned back against the studio wall, catching my breath, I could still feel the lingering rush of adrenaline from our dance session.{/i}"
    "{i}There was something liberating about letting go like that, moving without overthinking, allowing the music to pull me along.{/i}"
    scene w_933 with fade
    "{i}For the past hour, everything outside this room—the tension, the worries, the weight I’d been carrying—had faded. Here, with Tanya, it was easy to lose myself in the rhythm, to just be in the moment.{/i}"
    "{i}There was something grounding in the way she smiled back at me, as tired and exhilarated as I felt.{/i}"
    "{i}Somehow, she always knew when to push me and when to let me catch my breath, both in dance and in life.{/i}"
    scene w_934 with dissolve
    e "I don’t know if I’m getting better or if you’re just making it look easy."
    t "A little bit of both, maybe? I mean, you’re definitely getting better. You just need to relax a bit more, feel the rhythm."
    e "That’s easy for you to say. You make every move look effortless. I swear you must have been born dancing."
    scene w_935 with dissolve
    t "Well, I did grow up with a lot of it around me."
    t "But trust me, I had my fair share of awkward moments and tripping over my own feet. You’re actually picking it up pretty fast."
    e "Thanks. I really needed this, though… just something to get my mind off things."
    t "Yeah, sometimes life can get heavy. Dancing, for me, it’s like... a way to escape all that, even if just for a little while."
    e "Exactly. Even if it’s just an hour, it feels like I can leave everything outside the studio doors."
    t "You know, you don’t have to deal with it all alone, right? I’m here if you need someone to talk to."
    e "Thanks, Tanya. It really means a lot."
    scene w_936 with dissolve
    t "You know,"
    t "we should probably hit the showers before we collapse right here. Why don’t we take one together?"
    t "Saves time, and... honestly, I think I’m too tired to make it through on my own."
    "{i}I laughed, brushing a stray lock of hair out of my face. The idea felt natural—after all, we were both sweaty from the workout, and the thought of a cool, refreshing shower sounded amazing.{/i}"
    e "Good idea,"
    scene w_937 with dissolve
    "{i}Besides, there was a comfortable ease between us that made me feel at home in her company.{/i}"
    e "After all that, I think a shower is exactly what I need."

    call emma_tanya_shower_day6

    scene w_326 with fade
    "{i}As I stepped out of the shower and wrapped myself in the towel, I couldn’t help but feel like something had shifted.{/i}"
    "{i}Walking down the hallway, I found myself reflecting on everything that had just happened.{/i}"
    o "So, did you enjoy yourself?"
    "{i}I rolled my eyes, though I knew she couldn’t see it.{/i}"
    e__ "Can you just… not?"
    "{i}Whatever this was, it was something I wasn’t ready to let go of just yet.{/i}"
    $ renpy.pause()

    jump day10_emma_1
