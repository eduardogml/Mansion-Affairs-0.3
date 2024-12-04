label day5_alex_1:
    $ alexfuckzaraday5 = False

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 7rd_day with fade
    $ renpy.pause()
    hide 7rd_day with dissolve
    
    scene w_326 with fade
    "{i}I woke up with the remnants of last night’s conversation still rattling in my mind. The tension, the subtle accusations, the uneasy alliances.{/i}"
    "{i}Deciding I needed some fresh air, I got dressed and made my way outside, heading toward the stables. As I walked, the cool morning air helped to clear my head.{/i}"
    "{i}Emma’s defense of me, Daniel’s unsettling ease, Isabella’s measured gaze… The more I thought about it, the more I felt I was still missing something crucial.{/i}"
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    scene w_892 with fade
    "{i}As I neared the stables, I noticed someone already hard at work by the barn entrance.{/i}"
    "{i}t was Zara, focused and methodical as she moved through her tasks.{/i}"
    scene w_893 with dissolve
    "{i}I wondered how early she must have woken up to be out here this soon, immersed in the routine of the morning chores.{/i}"
    "{i}Oddly enough, there was no sign of Samuel anywhere. Usually, he’d be nearby, keeping an eye on things or overseeing the work around the grounds.{/i}"
    "{i}But today, it was just Zara, alone and intent on her work.{/i}"
    scene w_894 with dissolve
    a "Early start, huh? Didn't think anyone else would be up this early, let alone hard at work."
    "{i}Zara jolted slightly, glancing over her shoulder. A look of surprise quickly turned into a small, relaxed smile.{/i}"
    scene w_895 with dissolve
    z "Oh, Alex. Didn't hear you coming,"
    z "Guess I got caught up in the job. Someone’s got to keep this place running, after all."
    z "Someone has to make sure the horses are comfortable."
    scene w_896 with dissolve
    a "I guess so. I didn’t expect anyone to be out here this early. You always this dedicated, or just trying to impress?"
    a "Fair enough. Those guys don't wait for anyone, do they?"
    z "You wouldn't believe how demanding they can be."
    scene w_895 with dissolve
    z "Besides, I doubt anyone here is really noticing the work I’m putting in."
    a "Hey, I’m noticing,"
    a "Not everyone here is oblivious. Plus, I know hard work when I see it."
    "{i}She raised an eyebrow, looking at him thoughtfully.{/i}"
    z "Well, glad to know someone appreciates it. Though I have to admit, I’m surprised you’re out here. Not your usual hangout, is it?"
    scene w_896 with dissolve
    a "Just needed some fresh air... and a bit of perspective. Figured a walk might clear my head after everything that’s been happening."
    z "Yeah, I get that. This place can feel... suffocating sometimes. And with everything going on, I can’t blame you for needing some space."
    "{i}There was a pause, comfortable but laden with unspoken thoughts.{/i}"
    scene w_895 with dissolve
    a "You ever feel like you’re trapped here, Zara? Like… all the routines, the expectations—they just start closing in?"
    z "Sometimes,"
    z "But it’s a job, and it’s a place to stay. I don’t have the luxury of feeling ‘trapped’ too often."
    z "It’s just the way things are, you know?"
    scene w_896 with dissolve
    a "Yeah. Guess we all have our reasons for sticking around."
    "{i}Zara looked at me with curious eyes.{/i}"
    z "So, what’s yours? Why are you here, Alex?"
    a "Maybe a book with a few missing pages."
    scene w_895 with dissolve
    z "You know, Alex, you’re full of surprises. Didn't peg you as someone who’d be up early, let alone hanging around the stables."
    a "Guess I’ve got a few tricks up my sleeve. Besides, I’m enjoying the view down here."
    z "Oh, really? Is that so?"
    a "Yeah. You know how to make this place seem... different. Not many people can do that."
    scene w_896 with dissolve
    z "Well, if I knew I’d have company like this, I might’ve worn something a little more... appropriate."
    a "I’m not complaining."
    z "You know, Alex, you have this way about you... It’s like you don’t even realize how much attention you get around here. Or maybe you do?"
    a "I try not to overthink it. But coming from you, I’ll take that as a compliment."
    z "It is. I’ve... noticed you. Probably more than I should admit."
    a "Oh? And here I thought you were just here for the horses."
    scene w_895 with dissolve
    z "I was. Until you started showing up more often."
    a "I didn’t mean to make things... complicated."
    z "Complicated isn’t always a bad thing. Sometimes it’s just what keeps life interesting."
    "{i}She hesitates, looking at me more intensely{/i}"
    z "You’ve got this... confidence, Alex. I think you know exactly what I’m talking about."
    scene w_896 with dissolve
    "{i}Zara’s expression shift as she gathers her thoughts.{/i}"
    a "So, you ever get tired of being out here on your own, handling all the hard work without any backup?"
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    "{i}Zara gives a playful scoff, rolling her eyes.{/i}"
    z "Are you offering to help, Alex? Or just here to critique my technique?"
    a "Maybe both. Or maybe I just wanted an excuse to spend a little more time out here with you."
    "{i}Zara’s eyes widen briefly, but she quickly regains her composure, a small smile tugging at the corner of her mouth.{/i}"
    z "Careful, Alex. Don’t say things you don’t mean."
    a "Who says I don’t mean it?"
    "{i}She glances away for a moment, almost bashful.{/i}"
    z "I… well, let’s just say I’m not used to people sticking around. Out here, it’s usually just me, the horses, and a lot of quiet."
    a "Quiet isn’t always a bad thing. Sometimes it gives you the chance to see what’s really there."
    "{i}She’s clearly intrigued but cautious, her posture tense yet open to the moment.{/i}"
    z "Maybe I could… show you around, if you’re not in a hurry to get back."
    "{i}I catches her subtle invitation, the hint of uncertainty in her voice.{/i}"
    a "I’m not going anywhere. Lead the way."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_897 with dissolve
    "{i}Zara turns, glancing over her shoulder with a playful smirk as she motions toward the entrance of the stable.{/i}"
    z "Alright, but don’t say I didn’t warn you. It can get pretty dusty in here."
    scene w_898 with dissolve
    a_ "Looking from behind... Her body is not one to throw away."
    scene w_899 with dissolve
    z "So… it's just you and me now. Guess the horses have some competition for my attention."
    a "I don’t know if I’d want to compete with a few thousand pounds of muscle."
    z "You know, it’s not every day I let someone distract me while I’m working this hard,"
    a "Oh, I wouldn’t want to get in the way of all this hard work,"
    scene w_900 with dissolve
    "{i}Zara chuckled, leaning back against a haystack, her arms resting casually on either side.{/i}"
    z "Well, maybe... you could make it worth my while,"
    scene w_901 with dissolve
    "{i}She murmured, her fingers tracing lightly over her lips in a way that left little to the imagination.{/i}"
    scene w_902 with dissolve
    "{i}Alex felt the invitation in her manager, the barn suddenly seemed smaller, more intimate.{/i}"
    scene w_903 with dissolve
    $ renpy.pause()
    z "Mmm-mmm"
    scene w_904 with dissolve
    z "Maybe you’re the one who’ll need to keep up."
    a "Oh, is that a challenge?"
    "{i}Zara tilted her head, eyes glinting with both mischief and a hint of nervous excitement.{/i}"
    z "Only if you’re up for it,"
    scene w_905 with dissolve
    a "Well, I’m not one to back down. You’ll find I can be pretty persistent."
    a "And what about you, Zara? Do you know what you want?"
    z "Maybe… but it’s been a while since I’ve had the chance to go after it. I think I might need a little… encouragement."
    "{i}Zara looks away and then back at me, visibly regaining her confidence.{/i}"
    scene w_906 with dissolve
    "{i}For a moment, I hesitated, weighing the situation and the tension that hung in the air.{/i}"
    "{i}The barn was quiet, and Zara’s invitation was clear, but there was a hint of uncertainty in her posture—a momentary hesitation.{/i}"

    $ alexfuckzaraday5 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Fuck Zara{/size}{/font}":
            $ alexfuckzaraday5 = True
            a "Well, I’m here to help with that."

            call alex_fuck_zara_day5
        "{font=fonts/hatten.ttf} {size=50}Back{/size}{/font}":
            $ alexfuckzaraday5 = False
            "{i}I feel the tug, the tension thick in the air between us, but something inside me makes me stop. I take a deep breath, stepping back a little.{/i}"
            a "Zara… I… this probably isn’t the right time."
            "{i}Zara’s smile fades a little, her brows knitting in confusion.{/i}"
            z "Oh… did I… did I say something wrong?"
            scene w_907 with dissolve
            a "No, not at all. You’re… amazing. Really. I just… have a lot going on in my head right now. It wouldn’t be fair to you."
            "{i}She watches him, processing his words. Her expression softens, though there’s a hint of disappointment.{/i}"
            z "I… understand. I mean, I think I do."
            a "Thank you, Zara. I just… I don’t want to rush into anything I’m not ready for. You deserve more than that."
            z "Okay. Well… if you ever feel like talking, or just… need company, I’m around."
            a "That means a lot. Really. I’ll… see you around, Zara."

    scene w_326 with dissolve
    $ renpy.pause()

    jump day6_alex_1
