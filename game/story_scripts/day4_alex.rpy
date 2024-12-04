label day4_alex_1:
    $ alexrubydanielinterfereday4 = False

    scene black with fade

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 6rd_day with fade
    $ renpy.pause()
    hide 6rd_day with dissolve

    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    scene w_763 with fade
    "{i}I woke up that morning still feeling the heat of last night with Emma. She had been cold all day, angry at me for... well, for being me, I guess.{/i}"
    "{i}And then, out of nowhere, she pulls that surprise in the middle of the night. It was like she became a different person.{/i}"
    scene w_764 with dissolve
    a_ "Why did she do that? Guilt? Anger masked as desire?"
    "{i}I couldn’t quite shake the feeling that something was off. But hell, I wasn’t complaining in the moment.{/i}"
    scene w_765 with dissolve
    "{i}As I move through the mansion, the quiet feels heavy, broken only by the soft creak of the floor under my feet.{/i}"
    "{i}I get closer to the entrance, and that’s when I see them.{/i}"
    scene w_766 with dissolve
    "{i}Daniel—of all people—and Eleanor.{/i}"
    a_ "What the hell are they doing together?"
    "{i}I slow my steps, watching them talk near the grand double doors.{/i}"
    "{i}She’s leaning in, her body language all too familiar—just like yesterday morning. And Daniel, looking too damn comfortable, too smug for my liking.{/i}"
    a_ "What's she playing at now?"
    "{i}I wonder, not even sure if I want to interrupt them or just keep walking. But I can already feel the tension crawling up my spine, knowing full well I can't avoid whatever's coming next.{/i}"
    scene w_767 with dissolve
    ele"Alex! Good morning, handsome."
    "{i}She gave me that smile, the one that said more than it should. I could feel her eyes sweeping over me.{/i}"
    a "Morning, Eleanor."
    "{i}I smiled back, but my eyes were already on Daniel.{/i}"
    a "Daniel"
    d "Alex"
    "{i}His voice was stiff, cold—exactly how I expected it. He barely nodded in my direction, making it clear that, for him, I might as well not exist. The feeling was mutual.{/i}"
    a_ "Ah, here we go. Let's see what smartass thing he's going to say this time."
    a "Didn't know you two were already acquainted."
    d "We met not too long ago. Surprised she never mentioned me?"
    a_ "Eleanor? With him? What the hell is going on here?"
    ele "It just never came up, I guess. Daniel and I were catching up on a few things."
    "{i}She didn’t seem to notice the undercurrents between us, her voice soft and cheerful.{/i}"
    a_ "Right, 'catching up.' That sounds like code for something else."
    a "Interesting."
    a "Well, as long as you’re catching up and not causing trouble, Daniel."
    scene w_768 with dissolve
    d "Trouble? You know me, Alex. I keep everything above board."
    "{i}His words sounded innocent, but there was a glint in his eyes. He knew exactly what he was doing—pushing buttons, like he always did.{/i}"
    d "I should get going. I have some business to attend to."
    ele "Oh, already? Well, don’t be a stranger, Daniel."
    d "Alex, take care."
    "{i}I watched him leave, my jaw clenched.{/i}"
    a_ "What the hell is he doing here with Eleanor?"
    scene w_772 with dissolve
    "{i}As soon as he was out of sight, I turned back to Eleanor, who was now watching me with that familiar mischievous glint in her eyes.{/i}"
    a_ "And here we go again."
    scene w_770 with dissolve
    ele "So, Alex... about yesterday..."
    "{i}she began, her voice low and suggestive.{/i}"

    if alexreceiveblowjobeleanorday3 == False and alexspieseleanortristanday3 == True:
        ele "Did you like looking?"
        a_ "shit... yeah... but I wish I was fucking you"
        ele "I was thinking... what it would be like if it were you."
    elif alexreceiveblowjobeleanorday3 == False and alexspieseleanortristanday3 == False:
        a "Don't you think we almost reached the limit yesterday?"
        scene w_769 with dissolve
        ele "What limit? Nothing happened yesterday."
        a_ "Seriously? She's dangerous... Seductive... a temptation... yes... but... Shit, focus Alex."
        if alexflirteleanorday1:
            a "Yesterday..."
            ele "..."
            ele "You know..."
            ele "It was... pretty unusual... I wonder what it'll be like next time."
            a_ "Holy shit... what's on her mind? and I don't even..."
        else:
            scene w_769 with dissolve
            ele "I want to help you, Alex. Whenever we talk, you're so tense... you never relax."
            ele "I want to help you, because you seem like a good friend..."
            a_ "Okay... I know what that means..."
    else:
        a_ "I know what it is... we will have more opportunities..."
        ele "You know, right? I sleep thinking about our promise."
    
    scene w_772 with dissolve
    "{i}I raised an eyebrow, acting more composed than I felt.{/i}"
    a "Yesterday was... something, wasn’t it?"
    $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx1", relative_volume=0.3)
    "{i}She let out a soft laugh, her fingers lightly brushing my arm as she spoke.{/i}"
    scene w_770 with dissolve
    ele "It certainly was. We almost got caught. You’re not still worried about that, are you?"
    a_ "How could I not be?"
    scene w_772 with dissolve
    a "It’s hard to forget, Eleanor. Your husband could’ve walked in any second,"
    ele "But he didn’t. And isn’t that all that matters?"
    a_ "She’s unbelievable."
    "{i}We stood there for a moment, the air between us thick with the memory of what almost happened the other day.{/i}"
    scene w_769 with dissolve
    ele "So, how are you feeling after..."
    ele "you know, everything with the attack?"
    "{i}Her tone shifted slightly, and I could see the concern behind her playful demeanor.{/i}"
    "{i}I shrugged, trying to push the tension away.{/i}"
    a "I’ve been better. But I’m managing. It’s just... one of those things you don’t expect, you know?"
    scene w_771 with dissolve
    "{i}She nodded, stepping even closer.{/i}"
    ele "Well, I’m just glad you’re okay."
    ele "We wouldn’t want anything to happen to you..."
    "{i}She left the sentence hanging, the meaning as clear as day.{/i}"
    "{i}Her laughter rang through the hall as we spoke, filling the quiet morning air.{/i}"

    if alexkissemmaday2:
        $ renpy.music.stop("music1", fadeout=2.0)
        scene w_777 with dissolve
        "{i}I watched Emma descend the stairs, her movements calm, yet I could sense the tension simmering beneath her composed expression.{/i}"
        "{i}Her eyes were fixed on me and Eleanor, narrowing slightly as she got closer. It was clear that she was already on alert, and I braced myself.{/i}"
        a_ "Oh boy... she’s picking up on something. Probably way more than I’d like."
        $ renpy.music.play("audio/musics/filaments1.mp3", "music2", fadein=2.0, relative_volume=0.2)
        scene w_778 with dissolve
        e "Well, who’s our visitor here, Alex?"
        "{i}Her tone was clipped, a sharp edge cutting through her words. I cleared my throat, scrambling to find the right explanation.{/i}"
        scene w_779 with dissolve
        a "Oh, Emma, this is Eleanor. She...uh, stopped by for a visit."
        "{i}Emma’s gaze flicked to Eleanor, sizing her up.{/i}"
        scene w_780 with dissolve
        "{i}Eleanor, however, didn’t miss a beat, her smile steady as she extended a hand with effortless grace.{/i}"
        ele "Pleasure to meet you, Emma."
        scene w_782 with dissolve
        "{i}I held my breath as Emma glanced down at Eleanor’s hand without making any move to shake it.{/i}"
        "{i}An uncomfortable silence lingered until she finally spoke, her voice cool and direct.{/i}"
        scene w_783 with dissolve
        e "Emma. Alex's wife."
        a_ "Oh, that’s not good. She’s staking her claim."
        "{i}Eleanor merely chuckled softly, withdrawing her hand with a subtle nod, completely unruffled.{/i}"
        scene w_784 with dissolve
        ele "Ah, of course. I've heard so much about you. It’s always nice to put a face to the name."
        a_ "Heard so much about her? Did I even mention Emma? No, Eleanor must mean... the usual small talk. Hopefully."
        "{i}I saw a flicker of something in Emma’s eyes, a hint of doubt that she didn’t bother to hide.{/i}"
        scene w_783 with dissolve
        e "Is that so?"
        "{i}She looked at me pointedly, one eyebrow raised in question.{/i}"
        e "I didn’t realize we had...friends dropping by unannounced."
        "{i}I could feel my face twitch, and I tried to keep my expression neutral.{/i}"
        a_ "She’s definitely not letting this go easily."
        scene w_785 with dissolve
        ele "Oh, I’m sorry if my visit seems abrupt. Alex was just being a good host."
        "{i}Eleanor’s voice was smooth, every word carefully chosen. She looked at Emma with a charming smile, her tone sweetly casual.{/i}"
        ele "I’m sure you know how charming he can be."
        a_ "Charming? Is that supposed to sound innocent?"
        "{i}Emma shot her a tight smile in response, her tone dripping with a slight sarcasm.{/i}"
        e "Charming, yes, that’s one word for it."
        scene w_784 with dissolve
        a_ "This is going downhill fast. I need to shift gears."
        a "Um, actually, Eleanor had an idea."
        "{i}I looked between the two of them, trying to dispel the charged atmosphere.{/i}"
        a "She suggested we...do a double date. Us with her and her husband, Tristan."
        "{i}Emma’s eyes narrowed slightly, but she didn’t say anything immediately. She just watched Eleanor, her expression unreadable.{/i}"
        scene w_786 with dissolve
        ele "Yes, Tristan loves wine. I thought it would be a lovely evening, just the four of us."
        a_ "Emma’s not going to be easy to convince. But she does love wine…"
        "{i}After a brief pause, Emma finally responded, her tone measured.{/i}"
        e "A dinner with your husband, huh? And where exactly did you two plan this little gathering?"
        ele "Oh, it would be at our place. Tristan has an extensive wine collection, and he’s rather eager to share it. I’m sure you’d appreciate it, Emma."
        "{i}Emma crossed her arms, assessing Eleanor, her lips curving into a faint, skeptical smile.{/i}"
        e "Well, I do love a good wine. I suppose...it might be interesting."
        "{i}Eleanor’s eyes brightened, and she looked from Emma to me, her enthusiasm almost infectious.{/i}"
        ele "Wonderful. I’ll have Tristan set everything up, and we’ll let you know the date."
        "{i}She then turned to me with a warm expression.{/i}"
        ele "I appreciate you both being so open to this. It’s refreshing to find good company these days."
        e "Isn’t it just."
        "{i}Emma’s tone was polite but clipped, her eyes never leaving Eleanor.{/i}"
        "{i}She watched intently as Eleanor took a step back, clearly preparing to leave, her gaze lingering on me for just a fraction longer than necessary.{/i}"
        ele "I should go now. I look forward to our evening together."
        scene w_787 with dissolve
        "{i}With one last glance over her shoulder, Eleanor walked toward the door, her heels clicking against the floor, leaving us in silence.{/i}"
        "{i}As the door closed, I exhaled, feeling the tension settle in my chest, bracing myself for whatever Emma might say next.{/i}"        
        $ renpy.music.stop("music2", fadeout=2.0)
        $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)
        scene w_788 with fade
        "{i}As soon as Eleanor left, the silence between us felt heavier, almost awkward. I glanced at her, catching a look in her eyes that I couldn’t quite read—was it irritation? Jealousy? Hard to tell.{/i}"
        scene w_789 with dissolve
        e "So... were you really talking about me to Eleanor?"
        a "What? Of course, I was."
        e "Really? Because from where I was standing, it looked more like you were just... enjoying her attention."
        "{i}I sigh, feeling the familiar frustration building up. Emma’s tone has that edge again—the one she uses when she’s trying to poke holes in my story.{/i}"
        scene w_791 with dissolve
        a "Come on, Emma."
        a "She was being polite. I was just answering her questions. She asked about my ‘wife’—and last time I checked, that’s you."
        scene w_789 with dissolve
        e "Uh-huh. But you never actually answered my question."
        a "Which question is that?"
        e "Where exactly did you meet Eleanor?"
        a_ "She eyebrows raised, waiting. I know that look; she’s already made up her mind that I’m guilty of something."
        scene w_792 with dissolve
        a "We met the other day. I told you, she's a neighbor. She and her husband."
        e "And I’m supposed to just believe that?"
        a "Yes, you’re supposed to just believe that. Do you honestly think I’d lie about something so trivial?"
        scene w_789 with dissolve
        e "Trivial? Alex, you know your history with... women isn’t exactly reassuring."
        "{i}I take a deep breath, resisting the urge to snap back. She always knows how to hit the sore spots.{/i}"
        a "Emma, you think I’m incapable of a normal conversation with another woman without it meaning something?"
        e "I don’t know, Alex. Can you blame me for wondering?"
        scene w_792 with dissolve
        a "I’m here, aren’t I? With you. If I wanted something with Eleanor, do you really think I’d be wasting my time standing here, arguing with you?"
        e "You know, sometimes I wonder if you even realize how things look from my side."
        scene w_791 with dissolve
        a "What’s that supposed to mean?"
        scene w_789 with dissolve
        e "It means that you’re... you."
        e "Charming, overconfident, and way too comfortable around women like Eleanor. You don’t see what I see when she looks at you."
        "{i}I pause, letting out a short laugh, but there’s no humor in it. She’s always quick to jump to conclusions.{/i}"
        scene w_791 with dissolve
        a "Emma, it’s not like I’m flirting with her in the middle of the lobby. I was just being polite. Do you really think every interaction has to be some performance for the neighbors?"
        e "You know we have to keep up appearances here."
        scene w_789 with dissolve
        e "Eleanor, her husband, this whole place—they’re all watching us, whether you see it or not. And they already have their own assumptions."
        a "You’re right, they probably do. But if we walk around like we’re ready to tear each other apart, that’s not going to help, is it?"
        e "So, what? I’m just supposed to smile and act like everything’s fine?"
        scene w_791 with dissolve
        a "Isn’t that what you want?"
        a "You keep saying we need to look like a ‘happy couple,’ for whatever inheritance game we’re playing here. Isn’t that what you signed up for?"
        scene w_789 with dissolve
        e "I didn’t sign up to be a bystander in my own life, Alex."
        e "I agreed to this because we had... plans. But I can’t keep pretending forever."
        scene w_793 with dissolve
        "{i}I take a step closer, lowering my voice, trying to soften the edges in my tone.{/i}"
        a "Emma, listen. I know this whole setup is... complicated. But it’s just one dinner. If we go in there, put on a united front, it’ll make everything easier."
        e "Easier for who?"
        a "For both of us. Look, we don’t have to be best friends, or even agree on most things, but we both want this to work. Right?"
        "{i}She’s silent for a moment, looking away, and I can tell she’s holding back. It’s always been like this—layers of walls that I can never fully get past.{/i}"
        e "Sometimes I just... wonder if you even care about any of it."
        a "I do care, Emma. I know it may not seem like it, but I do. Why do you think I’m still here, dealing with all of this?"
        e "Because you don’t want to lose. That’s always been your thing—winning."
        a "Maybe. But I don’t want to lose you, either."
        "{i}She looks back at me, surprised, as if she didn’t expect me to say that. And for a brief moment, there’s a softening in her expression, a hint of something vulnerable.{/i}"
        $ renpy.music.play("audio/sfx/sfx_kissing_lip_to_lip.opus", channel="sfxloop1", fadein=2.0, relative_volume=0.2)
        scene w_794 with dissolve
        $ renpy.pause()
        $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
        scene w_795 with dissolve
        e "I don’t know if I can believe that."
        a "Then give me a chance to prove it. Just... let’s get through this dinner, together. That’s all I’m asking."
        "{i}She sighs, but I can see her walls coming down just a bit.{/i}"
        scene w_797 with dissolve
        e "Fine. But don’t make me regret it."
        a "I won’t."
        scene w_798 with dissolve
        a_ "It hasn't been easy. But maybe all is not lost yet."
    else:
        scene w_778 with dissolve
        "{i}But when I heard footsteps behind me, I turned and was met with Emma’s steady gaze as she approached, her expression unreadable, guarded.{/i}"
        a_ "Okay, Emma’s up early... not quite what I expected."
        e "Good morning."
        "{i}The suddenness of her voice startled me, and I blinked, trying to gather myself.{/i}"
        "{i}Eleanor, on the other hand, seemed completely at ease, smiling warmly as she turned to greet Emma.{/i}"
        a "Emma? Have you woken up yet?"
        e "Yes. Who is our guest, Alex?"
        scene w_779 with dissolve
        a_ "Here we go."
        a "Emma, this is Eleanor. She and her husband are our neighbors."
        "{i}Emma’s gaze shifted to Eleanor, assessing her quietly.{/i}"
        "{i}She didn’t look pleased or annoyed—just... interested.{/i}"
        scene w_780 with dissolve
        "{i}Eleanor extended her hand with an easy smile.{/i}"
        ele "Oh! You must be Emma. I’m Eleanor. It’s a pleasure to finally meet you."
        scene w_781 with dissolve
        "{i}Emma glanced at Eleanor’s hand, hesitating for just a beat before reaching out and shaking it with a firm grip.{/i}"
        "{i}I could see her eyes studying Eleanor, not quite as relaxed as usual.{/i}"
        e "Emma, yes. Alex’s wife."
        a_ "I can tell she wants to make it clear who she is. It’s subtle, but it’s there."
        "{i}The brief pause between the two was growing awkward, so I cleared my throat, hoping to cut through the tension.{/i}"
        a "Uh, Eleanor and her husband Tristan have lived in the neighborhood for a while. We were talking about... uh, getting together someday."
        scene w_785 with dissolve
        ele "Yes, actually! That’s why I stopped by,"
        "{i}she said, her voice bright and cheerful, as if completely unaware of the undercurrent between Emma and me.{/i}"
        ele "I was hoping to invite both of you over for dinner."
        ele "My husband and I love hosting, and we thought it might be a nice way to get to know you both better."
        "{i}I could feel Emma’s gaze flick back to me, gauging my reaction as much as Eleanor’s.{/i}"
        "{i}I offered her a reassuring smile, though I could sense she was still on edge.{/i}"
        scene w_786 with dissolve
        e "A dinner? That sounds lovely."
        ele "Wonderful! Tristan has a passion for wines. He’s something of a collector, actually."
        ele "I know it sounds cliché, but he could go on for hours about each bottle in his collection."
        "{i}She chuckled, glancing over at me.{/i}"
        ele "Do you like wine, Emma?"
        a_ "Oh, now she’s speaking Emma’s language."
        e "Yes, guilty as charged. I’m always up for a wine night."
        "{i}Emma let out a small laugh, and for a moment, some of the tension seemed to dissipate.{/i}"
        "{i}I let out a breath I hadn’t realized I’d been holding, relieved that things were lightening up.{/i}"
        e "It sounds perfect."
        a_ "Okay, maybe this will go smoothly after all."
        scene w_785 with dissolve
        ele "How about this Saturday, then?"
        "{i}She turned back to us, her eyes bright with excitement.{/i}"
        ele "I’ll speak with Tristan, but I think he’d love the chance to share some of his collection."
        scene w_786 with dissolve
        "{i}Eleanor’s gaze turned to me with a playful smile.{/i}"
        ele "And don’t worry, we won’t bore you with wine talk the entire night!"
        a "Hey, as long as Emma’s happy, I’m happy."
        "{i}I grinned and reached for Emma’s hand, giving it a small squeeze, hoping to reassure her.{/i}"
        e "We’d be delighted."
        ele "Perfect! I’ll let you know the exact time once Tristan finalizes everything,"
        "{i}Eleanor said, her eyes twinkling as she looked between the two of us.{/i}"
        ele "I think this is going to be a lot of fun."
        a_ "There’s something genuine in her smile, though I can’t quite shake the feeling that Emma’s still uneasy."
        e "Thank you for the invitation, Eleanor. It sounds like a wonderful evening."
        scene w_787 with dissolve
        ele "The pleasure’s all mine. I’ll make sure it’s a night to remember."
        "{i}Eleanor gave us one last warm smile before turning to leave, her heels echoing softly as she walked away.{/i}"
        "{i}I watched her go, feeling the tension fade, though I could tell Emma’s thoughts were still simmering beneath the surface.{/i}"
        scene w_788 with fade
        "{i}The soft echo of Eleanor's footsteps faded down the hallway, and for a moment, the grand entryway felt emptier than usual.{/i}"
        "{i}Alex glanced sideways at Emma, catching the flicker of something unreadable in her eyes.{/i}"
        a "Not a single spark of jealousy, huh? Wow, Emma, I thought you’d be more... possessive."
        scene w_789 with dissolve
        e "Possessive? That’s a bit of a stretch, don’t you think?"
        a "Just seems like the old you would’ve had a thing or two to say about Eleanor, that’s all."
        e "The ‘old me’?"
        e "Alex, it’s not like you gave me a reason to worry. Besides, we’re both here to keep up appearances, right?"
        scene w_791 with dissolve
        a_ "I can’t tell if she’s genuinely unaffected or just putting up a front."
        a_ "Either way, the calm in her voice is unsettling, like she’s rehearsed this in her head."
        a "Right... appearances. Because we have to play the perfect couple for the neighbors, huh?"
        scene w_790 with dissolve
        e "Exactly. Which means a little ‘friendly’ chat with Eleanor won’t break the illusion."
        scene w_791 with dissolve
        a "So you’re saying you don’t care who I talk to, as long as it fits our little act?"
        e "Why would I care? If I remember correctly, you’re the one who insisted on this... arrangement."
        scene w_792 with dissolve
        a "Hey, I didn’t exactly twist your arm. You agreed, didn’t you?"
        e "We both have our reasons. Let’s not pretend it was some fairytale decision."
        a "Fair enough. But you’re not even curious about Eleanor? Not one question about where I know her from?"
        scene w_789 with dissolve
        e "Fine. If it matters to you so much, enlighten me. Where did you meet her?"
        a_ "She tilts her head slightly, looking at me with a mix of casual interest and subtle challenge."
        a_ "There’s something unreadable in her eyes, but if she’s hiding anything, she’s doing a damn good job."
        scene w_791 with dissolve
        a "She’s just a neighbor, alright? We met the other day. Her and her husband live nearby."
        e "Convenient. She seems... interested."
        a "Interested? She’s married, Emma. I thought you didn’t care."
        scene w_789 with dissolve
        e "I don’t. I’m just pointing out that your... charm works on more than just your wife."
        a_ "Her tone is light, but there’s something underneath it that feels like a test. It’s like she’s daring me to react."
        a "And here I thought you’d be the one charming everyone. It’s not exactly easy keeping up the image of a ‘happy couple’ on my own, you know."
        scene w_790 with dissolve
        e "Oh, don’t worry, Alex. I’m more than capable of playing my part. I’ve had plenty of practice."
        a "Practice, huh? So this is all just one big show for you?"
        e "Isn’t that what you wanted? Smile for the neighbors, play nice for the inheritance... wasn’t that the plan?"
        scene w_791 with dissolve
        a "Look, I know things haven’t exactly... gone the way we planned."
        e "That’s putting it lightly."
        a "Yeah, well... maybe some things are worth trying for again."
        scene w_789 with dissolve
        e "Trying for... or winning back? Because those are two very different things, Alex."
        a_ "She looks at me, not with anger, but with that guarded expression that keeps me at arm’s length."
        a_ "I can tell she’s testing me, even if she won’t say it out loud."
        a "What’s the difference? I’m here, aren’t I? Maybe I’m not perfect, but... I’m still here."
        e "..."
        e "Being here isn’t the same as being trustworthy, Alex."
        scene w_791 with dissolve
        a "You think I don’t know that?"
        e "I just... don’t know if you’re capable of proving it. Not after everything."
        a_ "There it is. She won’t say it outright, but the doubt is still there. She’s practically daring me to prove her wrong, but her walls are as high as ever."
        a "Maybe I am. Maybe I’m just waiting for you to give me a reason to try."
        scene w_790 with dissolve
        e "And maybe I’m waiting to see if you’re worth the risk."
        a_ "She’s calm, controlled, but there’s something else there too. A flash in her eyes, a hesitation. It’s almost... jealousy, but she hides it well. I take a small step forward, testing the waters."
        scene w_793 with dissolve
        a "So... if I told you that I wanted to change things between us, you’d just stand there with that look? That look that says you don’t believe a word I’m saying?"
        e "Alex, change isn’t a promise. It’s just... words until you actually do something."
        a_ "I can feel the frustration in her voice softening, almost like she’s letting down her guard just a little."
        a "Maybe I’m tired of pretending, too."
        e "Pretending... or trying to fix things?"
        a_ "She meets my eyes, her expression unreadable, but she isn’t pulling away. There’s a warmth there, something we haven’t shared in a long time."
        "{i}I take a chance, leaning in slowly, testing the waters as I move closer to her.{/i}"
        scene w_796 with dissolve
        e "Alex..."
        a "What?"
        e "This doesn’t change anything. I still don’t know if I can... if I can trust you."
        scene w_797 with dissolve
        e "Good morning, Alex."
        "{i}She turns away, leaving me with the lingering sense of what could have been.{/i}"
        scene w_799 with dissolve
        a "..."
        "{i}She walks up the stairs, leaving me standing there, feeling both closer and further away from her than ever before.{/i}"

    scene w_326 with fade
    $ renpy.pause()
    "{i}I approached the hallway leading to the kitchen, hearing voices.{/i}"
    scene w_846 with fade
    "{i}I slowed down as I recognized Daniel's soft tone and Ruby's hesitant responses.{/i}"
    d "You know, Ruby, I don’t think I’ve ever really noticed just how… diligent you are around here."
    a_ "This doesn't smell right to me."
    d "Always making sure everything’s perfect. Isabella couldn’t ask for a better employee."
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/villain-entry.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_847 with dissolve
    r "Thank you, Mr. Daniel. I… I just try to do my job the best I can."
    a_ "She looks nervous."
    d "Oh, come on, drop the ‘Mr. Daniel’ stuff."
    d "We’re not strangers, are we?"
    scene w_848 with dissolve
    r "I... I suppose not, but it’s just… well, you are my employer. I wouldn’t want to be… disrespectful."
    d "Respect is overrated sometimes, don’t you think?"
    d "Besides, I don’t bite. Unless, of course, you’d want me to."
    r "Mr. Daniel, please… this isn’t… appropriate. Mrs. Isabella is around, and… I really don’t want any misunderstandings."
    scene w_849 with dissolve
    d "Isabella? Oh, she’s busy with her own affairs. Believe me, she’s not paying attention to what happens in the kitchen."
    r "Still… I’m just here to work, sir. I… I wouldn’t want to cross any lines."
    d "Ruby, you’re too tense. Relax. I’d say a woman as beautiful as you deserves a little attention, don’t you agree?"
    r "I... I really appreciate the compliment, but... I think it’s best I keep my focus on my duties."
    scene w_850 with dissolve
    d "You’re always so focused. Sometimes I wonder if you’re just looking for an excuse to avoid me."
    r "No, no, it’s not that. It’s just… I respect you, Mr. Daniel. And I respect Mrs. Isabella. I wouldn’t want anything… misinterpreted."
    d "You’re worried about what she might think?"
    d "Ruby, you have nothing to worry about. Like I said… Isabella is occupied elsewhere."
    d "You know, Ruby, there’s no need to be so formal. I’d much rather you called me Daniel… or maybe something even more… personal?"
    r "I… I’m sorry, sir, but I really think it’s best to keep things… professional. It’s important to me."
    d "Professional, hm? Sometimes, being too professional can make things feel so… distant. Don’t you ever get tired of always keeping your guard up?"
    a_ "From where I’m standing, I can see Ruby’s unease. She’s cornered, trying to stay polite, but Daniel isn’t letting up."
    a_ "There’s a part of me that wants to barge in and put an end to this, but… is it really my place?"
    r "I… I just want to make sure I’m doing my job well, Mr. Daniel. I wouldn’t want to overstep any boundaries."
    d "Boundaries are all in our heads, Ruby. Sometimes, you just have to let them go… to really enjoy life."
    "{i}His hand lingers a moment too long. I can feel my fists clench, a surge of irritation rising.{/i}"
    a_ "This isn’t just harmless flirting; he’s taking advantage of his position, and Ruby looks like she’s on the verge of panicking."
    r "I… I think I should get back to work now, sir. There are still a few things Mrs. Isabella wanted me to handle before the evening."
    d "Isabella? Honestly, Ruby, you don’t have to mention her every other sentence. Isabella’s not here. Right now, it’s just you… and me."
    r "I’m sorry, but I… I really need to go. I don’t want to… upset anyone."
    scene w_851 with dissolve
    "{i}I feel a familiar frustration building in my chest. This has gone too far, but part of me hesitates.{/i}"
    "{i}Daniel’s a powerful man, and Ruby’s the one who would have to deal with the fallout if this escalates. Still, seeing her like this… trapped, practically pleading… it doesn’t sit right with me.{/i}"
    d "Why are you in such a hurry, Ruby? I was just hoping we could… enjoy each other’s company a little longer."
    r "Please, Mr. Daniel… I really should get back to work."
    a_ "I take a deep breath, feeling the weight of the decision pressing down on me. Do I step in and risk making things worse for her? Or do I walk away and pretend I didn’t see any of this?"
    a_ "It’s clear she’s not interested, but Daniel doesn’t seem to care. Part of me wants to punch him for how smug he looks… but what would Ruby want me to do?"

    $ alexrubydanielinterfereday4 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}I will intervene.{/size}{/font}":
            $ alexrubydanielinterfereday4 = True
            "{i}I’ve been watching Daniel and Ruby’s tense conversation from a distance.{/i}"
            $ alex_power = AlexPowerAdd()
            "{i}Seeing Daniel’s expression change, suggesting he’s about to make a physical move toward Ruby, I make my decision.{/i}"
            "{i}I step forward, speaking before Daniel can close the distance.{/i}"
            scene w_859 with dissolve
            a "Daniel, I thought I’d find you here. I was hoping to have a word."
            scene w_860 with dissolve
            "{i}Daniel pauses, surprised by my sudden presence.{/i}"
            "{i}He straightens, visibly irritated by the interruption, while Ruby lets out a small sigh of relief when she sees me step into the space between her and him.{/i}"
            scene w_861 with dissolve
            d "Alex. Always a surprise, isn’t it? Didn’t expect to see you down here."
            scene w_860 with dissolve
            a "Well, you know, sometimes you find yourself in the right place at the right time."
            a "I figured it was as good a moment as any to check in."
            "{i}Ruby, still visibly uncomfortable, gives me a grateful look, subtly stepping back to put a little more distance between herself and Daniel.{/i}"
            scene w_861 with dissolve
            d "Right place, right time, huh? I don’t recall needing a supervisor for a simple chat."
            scene w_860 with dissolve
            a "Didn’t seem like a ‘simple chat’ to me. Looked more like Ruby was uncomfortable."
            a "Thought I’d just… make sure things were okay here."
            scene w_861 with dissolve
            "{i}Daniel’s expression tightens. He forces a chuckle, trying to mask his annoyance.{/i}"
            d "You’ve got a funny way of interpreting things, Alex. Ruby and I were just… getting to know each other better. Isn’t that right, Ruby?"
            scene w_860 with dissolve
            r "I… um… I really should get back to work. I don’t want to cause any trouble."
            a "No trouble, Ruby. You’re just doing your job. That’s all anyone should expect of you."
            scene w_861 with dissolve
            "{i}Daniel raises an eyebrow, his irritation slipping further into his expression when he realizes I'm not backing down.{/i}"
            d "Alex, I think you’re misunderstanding the dynamics here."
            d "I’d appreciate if you didn’t involve yourself in… matters that don’t concern you."
            d "Men who get involved in matters that do not concern them end up creating problems for themselves."
            scene w_860 with dissolve
            a_ "What the hell is this?! This bastard is threatening me to my face?!"
            "{i}I feel my blood boil. But somehow... something tells me to control myself.{/i}"
            a "Forgive me if I disagree, Daniel. I’d say anyone being put in an uncomfortable situation is everyone’s concern."
            a "We’re all adults here; respect shouldn’t be optional."
            scene w_862 with dissolve
            d "You know, Alex, some people don’t know when to stay out of things. But, for your sake, I’ll let this slide. This time."
            "{i}With one last look, Daniel turns, leaving the kitchen. I watch him leave, a slight smile on my face.{/i}"
            "{i}As he leaves, I feel like I've managed to defuse the situation. Ruby lets out a shaky breath as Daniel walks out of sight.{/i}"
            r "Thank you, Mr. Alex. I… I didn’t know how to… I mean, I didn’t want to upset him."
            scene w_863 with dissolve
            a "You don’t owe him anything, Ruby. Just focus on your work, and don’t let anyone make you feel like you’re in the wrong."
            scene w_864 with dissolve
            $ renpy.pause()
            "{i}As I watch her compose herself, a part of me feels a lingering frustration.{/i}"
            "{i}I’ve dealt with guys like Daniel before—men who think they can have anything, anyone they want, without consequences.{/i}"
        "{font=fonts/hatten.ttf} {size=50}I will observe, for now.{/size}{/font}":
            $ alexrubydanielinterfereday4 = False
            scene w_852 with dissolve
            "{i}At first, I tried to ignore them, but my curiosity got the better of me, and I silently watched the two of them.{/i}"
            $ alex_power = AlexPowerRemove()
            scene run_danielruby with dissolve
            $ renpy.pause()
            "{i}Daniel stood behind Ruby, his hands on her hips, pulling her close.{/i}"
            $ renpy.pause()
            "{i}Ruby's head was thrown forward, her eyes closed, as she rubbed her ass against Daniel's crotch.{/i}"
            scene w_855 with dissolve
            "{i}After a moment of hesitation, decides he can’t stand by any longer. I steps into the kitchen, making my presence known.{/i}"
            a "Am I interrupting something?"
            "{i}Ruby’s eyes widen as she sees me enter the room. She instinctively takes a small step back from Daniel, her face flushed with embarrassment.{/i}"
            scene w_856 with dissolve
            r "Oh… Mr. Alex, I… I didn’t realize you were… I mean…"
            d "Alex. Didn’t see you there. This is… quite the unexpected visit to the kitchen, don’t you think?"
            a "Just happened to be passing by. Sounded like an interesting conversation, so I thought I’d stop in."
            d "I was just having a friendly chat with Ruby here. You know, making sure she’s feeling… appreciated in her role."    
            a "Funny. It didn’t exactly sound like she was enjoying the conversation."
            d "Oh, come on, Alex. Don’t be so dramatic. I was just being… hospitable. Ruby doesn’t seem to have any complaints, do you, Ruby?"
            r "I… I really should get back to my duties. I didn’t mean to cause any trouble…"
            a "You’re not causing any trouble, Ruby. If anyone here is out of line, it’s not you."
            d "Alex, with all due respect, I don’t think you understand how things work around here."
            d "I don’t remember needing your permission to have a private conversation in my own home."
            scene w_857 with dissolve
            a "No one needs permission for a conversation, Daniel. But when that ‘conversation’ makes someone uncomfortable, it stops being harmless."
            r "Please, I… I really don’t want to cause any issues. I just… need to get back to work."
            scene w_858 with dissolve
            d "See what you’ve done, Alex? Now Ruby thinks there’s some sort of… problem here. When really, there wasn’t one until you decided to barge in."
            scene w_857 with dissolve
            a "Funny. From where I was standing, the problem was pretty clear."
            scene w_858 with dissolve
            d "You know, Alex, you’re awfully protective for someone who’s… just a guest in this house. Don’t you think you’re overstepping your bounds?"
            scene w_857 with dissolve
            a "Maybe. But sometimes you have to step up when no one else will."
            scene w_858 with dissolve
            d "Careful, Alex. You might start giving people the wrong impression. It wouldn’t be wise to turn a harmless situation into something… unnecessarily complicated."
            scene w_857 with dissolve
            a "Funny, I was thinking the same thing. But if ‘harmless’ is what you were aiming for, you’re not doing a great job."
            scene w_856 with dissolve
            r "Um… thank you, Mr. Alex, but really, I… I’ll be fine. I think I just need to… finish my work."
            a "Of course, Ruby. I’m sorry if this made you uncomfortable. You shouldn’t have to deal with this kind of… ‘attention.’"
            d "Satisfied, Alex? You’ve saved the day, and all is right in the world. Now maybe you can get back to… whatever it is you actually do around here."

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)
    
    scene w_326 with fade
    "{i}By the time I make it to the hall, I realize my hands are clenched into fists.{/i}"
    a_ "I don’t know what bothers me more: his behavior or the fact that he seems to think he can get away with it."
    "{i}After a few moments of walking, I decide I need some air. There’s no sense in letting this ruin my day, but I need a way to shake off the frustration.{/i}"
    "{i}So, I head out to the garden, hoping a little time outside will help me cool down. The last thing I need is another confrontation.{/i}"

    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    scene w_327 with fade
    "{i}As the day winds down, I’m still running over the events of the day in my mind, trying to make sense of the underlying tension that seems to linger in every corner of this mansion.{/i}"
    "{i}Suddenly, Isabella appears with her usual calm elegance, although there is a touch of urgency in her eyes.{/i}"
    "{i}She gets straight to the point—tonight, she, Daniel, Emma, and I will sit down together to discuss the attack I went through and to address the broader issue of security around the estate.{/i}"
    "{i}It’s clear she wants answers and a plan, and for a brief moment, I sense that she might be just as uneasy as I am in this place.{/i}"
    "{i}As we gather in the living room, I can feel the weight of everyone’s eyes on me.{/i}"
    $ renpy.music.stop("ambient1", fadeout=2.0)
    $ renpy.music.stop("music1", fadeout=2.0)
    scene w_867 with fade
    "{i}Daniel, standing with his usual self-assured stance, has a glass of whiskey in hand, his expression unreadable but intent.{/i}"
    "{i}Isabella stands beside him, poised and elegant, though her gaze betrays a hint of genuine concern. Emma stands slightly behind me, her face a mix of worry and frustration.{/i}"
    "{i}I take a deep breath, recounting every detail of the attack—the sudden ambush, the shadows that appeared out of nowhere, and how quickly it all escalated.{/i}"
    "{i}They listen in silence, each with their own reaction.{/i}"
    $ renpy.music.play("audio/musics/tension_mystery.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_866 with dissolve
    d "I have to admit, Alex, when I first saw that bandage, I thought maybe it was just a little… embellishment."
    d "A tactic to gain sympathy, perhaps. But now… seems like the attack was real enough after all."
    scene w_869 with dissolve
    "{i}Emma interrupts Daniel, her voice sharp.{/i}"
    e "I did the bandage myself. If there’s one thing I wouldn’t do, it’s lie about something like that."
    scene w_866 with dissolve
    "{i}Daniel raises an eyebrow, considering Emma’s words, and then nods in agreement.{/i}"
    d "Fair enough, Emma. I suppose I’ll take your word for it."
    "{i}Jealousy flares up in my chest, quick and irrational. The way Daniel’s gaze shifts to Emma, how easily he accepts her assurance over mine—it rubs me the wrong way.{/i}"
    "{i}Isabella steps in, her tone calm but serious, drawing everyone’s attention back to the issue at hand.{/i}"
    scene w_865 with dissolve
    isa "Regardless of anyone’s initial thoughts, the fact is, we have a problem."
    isa "This isn’t just about a single attack—it’s about the security of everyone in this mansion."
    isa "If someone could get close enough to harm Alex, then we’re all potentially at risk."
    scene w_868 with dissolve
    a "You know, for a moment there, I almost thought it was you who decided to pay me a little late-night visit, Daniel."
    "{i}Emma interrupts me with her irritated tone.{/i}"
    scene w_869 with dissolve
    e "That’s absurd, Alex. Daniel and Isabella were in their rooms when it happened. I saw them myself."
    a_ "How does she know where they were that night?"
    scene w_865 with dissolve
    isa "She’s right, Alex. Emma came to our room that night—she checked on us when she heard the noise. We were both there."
    a_ "Why did she feel the need to go there? Was it just concern, or is there something I’m missing here?"
    "{i}I catch a brief, icy look in Daniel's eyes before he speaks, his tone as sharp as his gaze.{/i}"
    scene w_866 with dissolve
    d "Perhaps the real issue here, Alex, is you. It seems to me that this attack might have more to do with… choices you’ve made."
    "{i}Minha frustração aumenta instantaneamente, meu rosto se contrai de raiva enquanto eu abro a boca para responder, mas Daniel continua, interrompendo antes que eu possa falar.{/i}"
    d "Think about it. Nothing was stolen, no valuables taken. Whoever did this wasn’t here for the mansion or anything in it."
    d "They were here for you. Which suggests, of course, that it’s personal. Maybe a grudge? Some… unresolved history?"
    scene w_867 with dissolve
    "{i}I clench my fists, feeling the weight of Daniel’s accusation settle heavily on me.{/i}"
    "{i}The implication is unnerving, and I can barely keep myself from reacting.{/i}"
    "{i}As I glance around, I catch a flash of fear in Emma’s eyes, her face paler than usual as she absorbs Daniel’s words.{/i}"
    scene w_869 with dissolve
    e "That’s not true, Daniel. You’re wrong."
    e "Alex is a good man. Flawed, yes—we all are—but he’s never been the kind of person to stir up enemies."
    e "No matter what anyone says about him, he’s always tried to do the right thing for the people around him."
    e "If someone attacked him, it wasn’t because he deserved it."
    "{i}Her words hit me harder than I expected, stirring something deep within me.{/i}"
    a_ "I can see the sincerity in her eyes, the unguarded honesty in her voice."
    a_ "Despite everything between us, despite the fact that we’re keeping the reality of our separation a secret, Emma’s words feel genuine."
    a_ "There’s a softness there, an echo of something we once shared."
    "{i}For the first time in a long time, I feel a glimmer of hope—hope that maybe, just maybe, she still cares for me, even if she won’t admit it.{/i}"
    scene w_867 with dissolve
    "{i}The anger I felt moments ago begins to ease, fading under the weight of her words. Instead of the frustration and jealousy that clouded my mind, I feel a strange sense of calm settle over me.{/i}"
    "{i}But as I study her face, I notice a trace of frustration in her expression, almost hidden. I can’t quite place it.{/i}"
    a_ "Why would she look that way now, when she just stood up for me?"
    "{i}Isabella, sensing the tension between them all, interrupts, her voice calm but insistent.{/i}"
    scene w_865 with dissolve
    isa "Alright, let’s get back on track. The focus here needs to be on security, not on personal theories."
    scene w_866 with dissolve
    d "Agreed. Up until now, we haven’t been locking the mansion gates. Given what’s happened, that needs to change. From now on, the gates stay locked."
    scene w_869 with dissolve
    e "And what about the staff? They’ll need access if they’re coming and going. Won’t that just complicate things?"
    scene w_866 with dissolve
    d "They can be given a key, but only select staff."
    d "If there’s another incident, it narrows down who might be involved. Everyone with access becomes a potential suspect."
    scene w_868 with dissolve
    a "Alright… that means we’re talking about Samuel, Ruby, Zara, Ava, and Tanya."
    scene w_865 with dissolve
    isa "And Victor, my stylist. He’s often here for fittings and consultations."
    scene w_868 with dissolve
    a "Who’s Victor?"
    scene w_869 with dissolve
    e "Oh, I’ve met him before. He’s Isabella’s stylist—handles all her fashion needs."
    scene w_866 with dissolve
    d "Victor isn’t a member of the household staff. He’s not a permanent employee here; he shouldn’t have a key."
    "{i}Isabella’s expression hardens, her gaze locking onto Daniel.{/i}"
    scene w_865 with dissolve
    isa "Excuse me? Victor may not be full-time staff, but he’s here frequently enough to need access."
    isa "He has every right to have a key for convenience."
    scene w_866 with dissolve
    d "Convenience isn’t the point here, Isabella. We’re talking about security, not fashion. The fewer people with access, the better."
    "{i}Isabella crosses her arms, her eyes narrowing as the tension between her and Daniel escalates.{/i}"
    scene w_865 with dissolve
    isa "And I’m telling you, Victor’s presence here is essential to my work."
    isa "I’m not going to leave him standing at the gate every time he arrives just to appease your sudden obsession with security."
    scene w_866 with dissolve
    "{i}Daniel's tone getting higher.{/i}"
    d "Maybe it’s time to prioritize what’s actually important here, rather than indulging every whim."
    d "The man doesn’t need constant access to the mansion—he’s a stylist, Isabella."
    "{i}Isabella’s jaw tightens, clearly preparing to push back as the argument threatens to boil over.{/i}"
    "{i}Emma breaks into the heated exchange between Isabella and Daniel, her voice calm but firm.{/i}"
    scene w_869 with dissolve
    e "Victor doesn’t seem like a threat to anyone. I really don’t see the harm in him having a key if he’s here regularly."
    a_ "Who is this Victor, anyway? It’s strange… both Emma and Isabella seem quick to defend him. Why does he matter so much to them?"
    "{i}Daniel pauses, considering Emma’s words. He finally nods, albeit reluctantly.{/i}"
    scene w_866 with dissolve
    d "Fine. Victor can have a key, but let’s be clear—if anything happens, he’ll be under as much scrutiny as anyone else with access. He’s not above suspicion."
    a_ "I have to agree with this bastard."
    d "Alright, that settles it. I’ll handle the rest of the security details—locks, key assignments, the works. We don’t need to overcomplicate this with too much input."
    scene w_867 with dissolve
    "{i}There’s something unsettling about the way Daniel is wrapping things up.{/i}"
    "{i}It’s subtle, but there’s an edge to him, a darkness just beneath the surface that I can’t quite ignore.{/i}"
    "{i}I open my mouth, ready to press him further, but before I can speak, Emma beats me to it.{/i}"
    scene w_869 with dissolve
    e "One more thing, Daniel. Do we have any kind of camera system around the mansion? Security cameras?"
    scene w_866 with dissolve
    d "There are security cameras, but they’re only installed on the exterior of the mansion."
    d "We don’t have anything monitoring the interior. The recordings are handled by an outside security company, and as far as I know, my mother’s lawyer has access to that company’s records."
    d "I’ll get in touch with the lawyer. I’ll make sure we get those recordings and see if they show anything unusual."
    scene w_869 with dissolve
    e "That’s a good start, but I think we should go beyond that. We should notify the local authorities about the attack. Let them investigate—it’s their job, after all."
    "{i}I notice a flash of discomfort on Daniel's face at the mention of involving the authorities.{/i}"
    scene w_866 with dissolve
    d "I don’t see why that’s necessary. This is a private matter, and I’d rather not involve anyone outside. We can handle this ourselves."
    scene w_868 with dissolve
    a "Actually, I think Emma’s right. If there’s someone targeting people in this house, it could be more serious than we think."
    a "The authorities might be able to find out more than we can."
    scene w_865 with dissolve
    isa "Daniel has a point. The last thing we need is the police swarming around the estate, asking questions and disrupting everything."
    isa "We’re capable of handling this internally."
    scene w_867 with dissolve
    "{i}Tension fills the room as a debate breaks out, the four of them divided.{/i}"
    e "But if we don’t involve them, we might miss something critical. We’re not trained to handle investigations, and this isn’t just about personal pride—it’s about safety."
    d "I understand the concern, Emma, but we’re not helpless."
    d " And frankly, I’m not interested in dragging outsiders into our lives. This family can take care of its own problems."
    a "Sometimes, there’s only so much we can do on our own. Ignoring help just to keep up appearances is reckless."
    isa "Alex, this isn’t about appearances. It’s about privacy and control. Bringing in strangers could create more complications than solutions."
    "{i}The room grows silent as the weight of the argument settles, each of them locked in their stance. After a tense pause, Daniel finally speaks, voice measured but with an edge of finality.{/i}"
    scene w_866 with dissolve
    d "Fine. Let’s leave it at this: each of us will handle it in whatever way we think is best."
    d "If you want to go to the authorities, that’s your choice. But don’t expect everyone else to fall in line."

    scene w_327 with dissolve
    "{i}The conversation ends with an uncomfortable truce, with the four of us exchanging glances that reveal deeper latent conflicts.{/i}"
    $ renpy.music.stop("music2", fadeout=2.0)

    jump day5_alex_1
