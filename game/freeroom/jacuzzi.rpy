label jacuzzi_bath:
    if freeroom_state == FREEROOM_STATE_DAY:
        scene jacuzzi_bath_emma_fr1 with dissolve
    # EMMA FREEROOM 1 DAY3
    elif freeroom_state == FREEROOM_STATE_EMMA_FR_1:
        hide screen jacuzzi_sofa_emma_sfr_1
        hide screen jacuzzi_massage_emma_sfr_1
        scene jacuzzi_bath_emma_fr1 with dissolve
        show screen jacuzzi_bath_emma_sfr_1
    else:
        scene jacuzzi_bath_emma_fr1 with dissolve

    show screen top_right_button
    window hide
    $ renpy.pause(hard=True)
    jump jacuzzi_bath

label jacuzzi_sofa:
    if freeroom_state == FREEROOM_STATE_DAY:
        scene jacuzzi_sofa_emma_fr1 with dissolve
    elif freeroom_state == FREEROOM_STATE_EMMA_FR_1:
        hide screen jacuzzi_bath_emma_sfr_1
        hide screen jacuzzi_massage_emma_sfr_1
        scene jacuzzi_sofa_emma_fr1 with dissolve
        show screen jacuzzi_sofa_emma_sfr_1
    else:
        scene jacuzzi_sofa_emma_fr1 with dissolve

    show screen top_right_button
    window hide
    $ renpy.pause(hard=True)
    jump jacuzzi_sofa

label jacuzzi_massage:
    if freeroom_state == FREEROOM_STATE_DAY:
        scene jacuzzi_massage_emma_fr1 with dissolve
    elif freeroom_state == FREEROOM_STATE_EMMA_FR_1:
        hide screen jacuzzi_bath_emma_sfr_1
        hide screen jacuzzi_sofa_emma_sfr_1
        scene jacuzzi_massage_emma_fr1 with dissolve
        show screen jacuzzi_massage_emma_sfr_1
    else:
        scene jacuzzi_massage_emma_fr1 with dissolve

    show screen top_right_button
    window hide
    $ renpy.pause(hard=True)
    jump jacuzzi_massage

init python:
    def ava_isabella_call_or_jump():
        # Substitua esta condição pela lógica que deseja
        if emma_fr1_ruby_tanya_talk and emma_fr1_zara_talk:
            renpy.jump("emma_fr1_ava_isabella")
        else:
            renpy.call("emma_fr1_ava_isabella")

##################################### FREEROOM_STATE_EMMA_FR_1
screen jacuzzi_bath_emma_sfr_1():
    # AVA
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "talk"
        action Function(ava_isabella_call_or_jump)
        xpos 466
        ypos 351
        xsize 357
        ysize 216
    # ISABELLA
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "talk"
        action Function(ava_isabella_call_or_jump)
        xpos 1198
        ypos 130
        xsize 327
        ysize 458

screen jacuzzi_sofa_emma_sfr_1():
    # TANYA AND RUBY
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "talk"
        action Call("emma_fr1_tanya_ruby")
        xpos 651
        ypos 54
        xsize 541
        ysize 891
    
screen jacuzzi_massage_emma_sfr_1():
    # ZARA
    imagebutton:
        idle "images/freeroom/transparent.webp"
        hover "images/freeroom/transparent.webp"
        hover_sound "audio/hover_sound.mp3"
        activate_sound "audio/click_sound.mp3"
        mouse "talk"
        action Call("emma_fr1_zara")
        xpos 884
        ypos 54
        xsize 170
        ysize 530

label emma_fr1_ava_isabella:
    if emma_fr1_ruby_tanya_talk and emma_fr1_zara_talk:
        hide screen jacuzzi_massage_emma_sfr_1
        hide screen jacuzzi_bath_emma_sfr_1
        hide screen jacuzzi_sofa_emma_sfr_1
        hide screen top_right_button
        "{i}The water in the jacuzzi rippled lazily as Ava leaned back, utterly relaxed. Isabella sat across from her, casually gesturing as she told some story that I barely caught bits of.{/i}"
        e_ "Isabella really knows how to carry herself. She always looks so damn effortless. I wonder what her secret is..."
        e_ "maybe it’s just confidence. Or maybe she doesn’t give a damn."
        "{i}The candles flickered around the hot tub, with rose petals floating lazily on the warm water.{/i}"
        "{i}The soft murmur of Ava and Isabella's voices drifted toward me as I approached, the kind of quiet conversation shared between two women with secrets.{/i}"
        scene w_621 with dissolve
        isa "He actually thought he could come back after everything that happened… The nerve of him."
        av "Well, he was always bold… Remember that time at the party—"
        "{i}My arrival cut their laughter short. Isabella looked up at me with a smile that felt more like a mask, concealing whatever was really going on in her mind.{/i}"
        scene w_622 with dissolve
        isa "Oh, Emma… I didn’t hear you coming."
        e "Sorry, I didn’t mean to interrupt. You two seemed to be having fun."
        scene w_623 with dissolve
        e_ "Isabella clearly has something to hide, or maybe she just doesn’t want me in on it."
        scene w_624 with dissolve
        "{i}Ava smiling and shifting slightly in the tub.{/i}"
        av "Not at all! Come on, join us. The water’s perfect."
        scene w_622 with dissolve
        "{i}I hesitated for a moment, watching Isabella’s face as she kept her polite smile, but there was an undercurrent of discomfort in her eyes.{/i}"
        scene w_623 with dissolve
        e__ "Maybe Isabella isn’t so thrilled about me being here. She’s trying to hide it well, but I can feel it. Well, too bad for her... If Ava’s inviting me, why not enjoy it?"
        e "I’m not one to turn down an invitation."
        scene w_625 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        isa "Well, I think I’ve relaxed enough for one day… I need to take care of a few things."
        e__ "Things’? Really? What a lame excuse. Someone here is running from something, and it’s not me."
        e "Oh, too bad. I thought we could spend a bit more time together."
        isa "Maybe another time. You two have fun."
        scene black with fade
        "{i}Once Isabella left, the atmosphere shifted. Ava sighed deeply, sinking a little lower into the water.{/i}"
        "{i}I settled beside her, feeling the warmth envelop my body as the tension Isabella had left behind started to dissolve.{/i}"
        scene w_624 with fade
        av "She’s always been like that, hasn’t changed a bit."
        e "Like what?"
        scene w_626 with dissolve
        av "Always running off when things start to get… intense."
        e__ "Intense? Hmm… This is getting more interesting. But let’s not rush it, Ava. We’ve still got time for some fun."
        e_ "Shut up."
        e "Well, now that she’s gone, what were you saying about that party?"
        scene w_627 with dissolve
        "{i}As the warm water of the jacuzzi soothed my muscles, Ava’s laughter filled the air, soft and melodic.{/i}"
        isa "Ruby, come help me with something! I’ll be just a minute."
        "{i}Ruby hesitated only for a second before slipping out of the water, dripping wet as she padded over to join Isabella. Ava caught my gaze and smirked.{/i}"
        av "Isabella always knows how to make an exit, doesn’t she?"
        e "Oh, absolutely. It’s like she’s never without a plan."
        scene w_624 with dissolve
        av "Just like you, Emma."
        e_ "I didn't understand. But it scared me..."
        e__ "Don't you understand, you idiot?"
        e__ "She understands you, she knows you, you're a good girl. But why?"
        e_ "Shut up. You're annoying sometimes."
        scene w_627 with dissolve
        e__ "God, sometimes I wonder what the hell they're always scheming. Though, honestly, do I even care? Not right now. This bath is way too comfortable."
        "{i}I leaned back against the edge, feeling the tension slip from my shoulders.{/i}"
        "{i}My eyes followed Tanya as she strolled across the room, her posture relaxed and assured, heading straight for Zara, who was readying herself by the massage table.{/i}"
        e__ "And there goes Tanya, off for her pampering session. A little princess with her perfect muscles. Honestly, if it weren’t so predictable, it’d be laughable."
        e__ "But hey, can’t say I blame her. A massage from Zara sounds divine right now."
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "You know...I kinda envy them. They always seem to have everything together, don’t they?"
        scene w_628 with dissolve
        e "Together? Please. They’re as messy as the rest of us...they just hide it better."
        e__ "A little envy from Ava? Interesting. Guess even the perfect ones have their doubts. Maybe she’s not so untouchable after all."
        e_ "Everything is envy for you."
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "You’re probably right. We’re all just great at pretending. But for now...let’s keep pretending we’re not tangled in whatever mess is waiting outside this tub."
        av "sabella certainly knows how to keep people guessing. But then, you don’t seem to be the guessing type."
        e "Not when I’ve already seen enough to make my mind up."
        scene w_628 with dissolve
        "{i}I watched her closely, curious to see if she’d take the bait. Ava leaned back slightly, letting the water lap against her skin as she spoke with a touch more care in her voice now.{/i}"
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "And what do you make of... old flames? They have a way of showing up in the most unexpected places, don’t they?"
        scene w_630 with dissolve
        e "Old flames, huh? They tend to linger, don’t they? Like smoke. Even when you think they’ve burned out, you can still smell it in the air."
        e_ "What is she getting at? Is she talking about herself or someone else? And why does this feel personal all of a sudden? Could she be... no. That’s ridiculous."
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "Yeah, some fires never truly go out. They just... smolder quietly, waiting for the right breeze to spark them back to life."
        scene w_630 with dissolve
        e "Sounds like someone’s got something—or someone—on her mind."
        e_ "What is she talking about? Why is this bothering me?"
        e__ "Don't you understand? Are you an idiot?"
        e_ "Shut up!"
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "Maybe. Or maybe it’s just the heat in here, playing tricks."
        e_ "What the hell is she trying to say? Is she implying what I think she is?"
        scene w_630 with dissolve
        e_ "Could Alex..."
        e_ "No, it couldn’t be. Could it?"
        e "You know, there’s something about the past that can really mess with your head. Even when you think you’re over it, someone shows up and suddenly..."
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "True. It’s funny how that happens, isn’t it? Old memories can stir up feelings you thought you’d buried."
        av "Sometimes those feelings are... surprisingly strong."
        scene w_631 with dissolve
        "{i}She glanced at me, her eyes carrying a hint of something deeper.{/i}"
        e_ "God, no. She doesn’t mean Alex, does she? No, Emma, get a grip. She can’t be talking about him. But why am I even thinking about it?"
        scene w_630 with dissolve
        e "And yet, we still try to convince ourselves we’re done with the past. That we’ve moved on, when really... maybe we haven’t."
        scene w_629 with dissolve
        $ renpy.music.play("audio/sfx/sfx_waves.ogg", channel="sfx1", fadein=2.0, relative_volume=0.6)
        av "Maybe."
        scene w_631 with dissolve
        $ renpy.pause()
        e_ "Goddammit. She is talking about Alex, isn’t she? I should just ask her outright... but I won’t. I can’t."
        scene w_632 with dissolve
        "{i}I shifted in the water, trying to hide the way my heart clenched.{/i}"
        e_ "Do I feel... jealous? What the hell is wrong with me? I shouldn’t care. I don’t care. I’m over this. But then why does it hurt, just the thought of someone else being interested in him?"
        e_ "Why is it that just the idea of Ava having history with Alex stirs something inside me?"
        scene w_631 with dissolve
        e "Old flames can be dangerous. Especially when they haven’t fully burned out."
        scene w_628 with dissolve
        av "That they can."
        "{i}She smiled at me, but it wasn’t just a smile—it was a challenge.{/i}"
        e_ "She knows. She knows exactly what she’s doing."
        scene w_632 with dissolve
        e__ "Of course she knows... You... Emma... Need me... Only me can you trust..."
        "{i}I glanced away, feeling the sting of jealousy burning hotter than the water around us.{/i}"
        e_ "If I’m jealous... does that mean I still love him? I thought I was past this. But why else would I feel like this?"
        scene black with fade
        "{i}I needed to get out of here. But leaving would be too obvious. So I stayed, pretending that I wasn’t quietly raging inside, pretending that Ava wasn’t getting under my skin.{/i}"
        "{i}Pretending that none of this mattered when, in reality, it mattered way too much.{/i}"
        $ renpy.end_replay()
        $ persistent.day4_girls_in_the_jacuzzi_unlocked = True

        jump day3_emma_2
    else:
        hide screen jacuzzi_bath_emma_sfr_1
        "{i}The water in the jacuzzi rippled lazily as Ava leaned back, utterly relaxed. Isabella sat across from her, casually gesturing as she told some story that I barely caught bits of.{/i}"
        e_ "Isabella really knows how to carry herself. She always looks so damn effortless. I wonder what her secret is..."
        e_ "maybe it’s just confidence. Or maybe she doesn’t give a damn."
        show screen jacuzzi_bath_emma_sfr_1
    return

label emma_fr1_tanya_ruby:
    if emma_fr1_ruby_tanya_talk:
        hide screen jacuzzi_sofa_emma_sfr_1
        "{i}Tanya, with her usual carefree smile, was gesturing animatedly with her hands, while Ruby, her stance all casual but commanding, listened attentively, occasionally nodding.{/i}"
        show screen jacuzzi_sofa_emma_sfr_1
    else:
        hide screen jacuzzi_sofa_emma_sfr_1
        "{i}Tanya, with her usual carefree smile, was gesturing animatedly with her hands, while Ruby, her stance all casual but commanding, listened attentively, occasionally nodding.{/i}"
        t "It’s really not that deep, Ruby."
        t "I mean, at the end of the day, it’s all about just letting go, right?"
        r "I don’t know... letting go sounds easy, but when you’ve got responsibilities weighing on your mind, it’s a bit harder than that."
        "{i}I walked over to where Tanya and Ruby stood, both of them still radiating confidence, chatting by the sofa like they were in their own world.{/i}"
        scene w_606 with dissolve
        e "Responsibilities?"
        e "Please. That’s the whole point of coming here—to forget about that crap for a while."
        scene w_605 with dissolve
        $ renpy.music.play("audio/sfx/sfx_laugh5.mp3", channel="sfx1", relative_volume=0.4)
        "{i}Tanya chuckled, glancing at Ruby knowingly, then looked back at me with that playful glint in her eyes.{/i}"
        t "Exactly! See, Emma gets it."
        t "You’ve gotta shake off the stress, girl, or it’s just going to eat you alive."
        scene w_607 with dissolve
        r "Okay, but what do you suggest? Just drop everything and live in a bubble?"
        e "Why not?"
        e "I mean, you’re here now, right? Might as well dive in headfirst."
        e_ "Headfirst into what, though? Sometimes I wonder if Tanya and Ruby actually believe in this whole ‘live in the moment’ thing."
        e_ "Or if it's just a show. But hey, maybe I’m the one who needs to loosen up more."
        scene w_605 with dissolve
        t "Emma’s right."
        t "The moment we stop overthinking everything, the more we start really living. Don’t you feel that, Ruby?"
        scene w_607 with dissolve
        r "I get it, but it's not always that simple."
        r "Some things... they cling to you, you know? Even when you try to relax."
        "{i}It made me think. I could tell Ruby had her own struggles—hell, we all did—but part of me wanted to pull her out of that dark spiral, at least for today.{/i}"
        e_ "I don’t even know why I said that. Maybe because I want to believe it for myself, too."
        e_ "Maybe because, for once, I want to just shut off my brain and enjoy this."
        e "Here’s the thing—whatever’s got its claws in you?"
        e "You’re stronger than it. And right now, in this place, none of it matters. We’re untouchable in here."
        scene w_605 with dissolve
        t "Emma’s got a point. Whatever is stressing you out... leave it outside those doors."
        t "In here, it’s just us, some steam, and this crazy good atmosphere."
        scene w_607 with dissolve
        r "Maybe you're right... but it's hard not to think about the pile of stuff waiting for me when I leave."
        e "Oh, screw that. It'll still be there, but why let it ruin this?"
        e "This is our time, Ruby. We earned this. And no one’s going to take it from us unless we let them."
        e_ "Who would’ve thought I’d be the voice of reason here? Maybe it’s time I take my own advice for once..."
        scene w_605 with dissolve
        t "Alright, enough with the heavy stuff. Let’s talk about something fun."
        t "What’s next for us? After the jacuzzi, we’ve got this whole place to ourselves."
        scene w_607 with dissolve
        r "You really think we should just stay here all day?"
        e "Why not? Sounds like a plan to me."
        scene w_605 with dissolve
        e_ "See? Now you’re getting it, Ruby. Who knows... maybe we’ll even find a way to spice things up later."
        scene w_608 with dissolve
        $ renpy.music.play("audio/sfx/sfx_laugh5.mp3", channel="sfx1", relative_volume=0.4)
        $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx2", relative_volume=0.4)
        $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx3", relative_volume=0.4)
        "{i}Ruby laughed, finally loosening up. The tension in the room seemed to evaporate, replaced by the easy, playful energy that Tanya always seemed to bring with her.{/i}"
        scene w_605 with dissolve
        e "As long as it doesn’t involve too much work, I’m in."
        t "Trust me, babe. The only thing we’re working on today is enjoying ourselves."
        scene w_607 with dissolve
        r "I guess I can get behind that."
        e "Yeah, I could too... for now."
        $ emma_fr1_ruby_tanya_talk = True
        show screen jacuzzi_sofa_emma_sfr_1

    return

label emma_fr1_zara:
    if emma_fr1_zara_talk:
        hide screen jacuzzi_massage_emma_sfr_1
        "{i}Watching her, I couldn't help but notice how out of place she looked in that luxurious spa setting.{/i}"
        "{i}Her posture was tense, and her eyes darted around nervously as if she didn't quite belong.{/i}"
        "{i}She was standing by the massage table, clearly waiting for one of us to request a massage. But there was something else about her... something that felt off.{/i}"
        show screen jacuzzi_massage_emma_sfr_1
    else:
        hide screen jacuzzi_massage_emma_sfr_1
        "{i}Watching her, I couldn't help but notice how out of place she looked in that luxurious spa setting.{/i}"
        "{i}Her posture was tense, and her eyes darted around nervously as if she didn't quite belong.{/i}"
        "{i}She was standing by the massage table, clearly waiting for one of us to request a massage. But there was something else about her... something that felt off.{/i}"
        e_ "Why is she so awkward? It's like she's trying too hard to blend in, yet at the same time, she’s completely disconnected."
        "{i}I decided to break the silence and approach her. Maybe she just needed someone to be a little kind. Plus, I was curious about her.{/i}"
        scene w_610 with dissolve
        e "Hey, how are you? What's your name?"
        z "Hi... hi. Me? My name is... Zara."
        e "Hey, Zara, right?"
        e "You work at the mansion too, don't you?"
        "{i}Her eyes widened slightly, and she nodded quickly, clearly caught off guard.{/i}"
        scene w_611 with dissolve
        z "Y-yeah, that’s me. I help Samuel, uh, my father, with the gardens."
        e_ "Samuel’s daughter… makes sense now."
        e_ "No wonder she’s so out of her element here. But still, why does she seem so... jittery around me?"
        scene w_610 with dissolve
        e "That’s really sweet of you. I’ve always admired the gardens. You two do a great job."
        "{i}She blushed, looking down at the floor as if unsure of how to take the compliment.{/i}"
        scene w_611 with dissolve
        z "Th-thanks. It’s, uh, nothing compared to what you all do inside the mansion, I’m sure."
        e_ "Oh boy, she’s one of those. All insecure and self-conscious."
        e_ "I should probably dial it back, don’t want her thinking I’m patronizing her or something."
        scene w_610 with dissolve
        e "Come on, maintaining those grounds is no small feat. You should be proud of it."
        "{i}I could see her relax a bit at that, but there was still this lingering awkwardness in the air. She kept glancing at me, then quickly looking away.{/i}"
        e_ "She’s acting like I’m about to scold her or something. Weird… but maybe she’s just shy."
        scene w_611 with dissolve
        z "I—um, I really like the mansion. It’s beautiful inside and out. Especially with, uh... the people living there."
        e_ "Okay, that was awkward. Why does she sound like she’s tiptoeing around something?"
        scene w_610 with dissolve
        e "Yeah, it’s a nice place. So, have you been working here long?"
        scene w_611 with dissolve
        z "S-since I was a teenager, actually. I started helping my dad when I was 15, and, well, I’ve just stuck around."
        z "It’s a good job... even if it’s a bit quiet sometimes."
        scene w_610 with dissolve
        e "I bet it’s peaceful out there, though."
        e "Working in nature, away from all the noise inside the mansion."
        "{i}She smiled a little at that, almost grateful that I wasn’t pushing her too hard.{/i}"
        scene w_611 with dissolve
        z "Yeah, it’s peaceful. But sometimes I wonder what it would be like, you know, being more involved... in the social side of things inside."
        e_ "So she wants to be closer, huh? or maybe she just craves a little of the luxury. Either way, it's clear she’s feeling left out."
        scene w_610 with dissolve
        e "Well, you’re always welcome to join us when you want. No one’s stopping you."
        "{i}Zara's face lit up for a second before quickly shifting back to that nervous energy she had from the start. She clearly didn’t know how to respond to that.{/i}"
        scene w_611 with dissolve
        z "Oh, I—I don’t know if I’d fit in. Everyone’s so... beautiful and confident. It’s... intimidating."
        e_ "Oh, sweetie. We all have our insecurities, but you don't have to let them define you. She just needs to get out of her own head."
        scene w_612 with fade
        "{i}I decided to take Zara up on her offer. After all, who could resist a massage right now?{/i}"
        "{i}The tension in my shoulders had been building up, and I thought, why not let her work some magic. She led me over to the massage table, and I climbed on, settling down{/i}"
        scene w_613 with fade
        "{i}Zara's hands were firm yet gentle as she began working, her fingers kneading into my tense muscles.{/i}"
        $ renpy.pause()
        scene w_614 with fade
        $ renpy.pause()
        scene w_615 with fade
        $ renpy.pause()
        e "So... you work here often?"
        z "Yes, whenever the mansion has guests... I guess you could say I'm one of the regulars here."
        "{i}She sounded a little unsure of herself, but I could tell she was trying.{/i}"
        "{i}Her hands moved, and I felt the knots in my muscles start to unwind.{/i}"
        e_ "Zara's hands are doing wonders, but there's something off about her tone."
        e_ "It's almost like she's trying too hard. And... did she just glance at my body in that weird way?"
        e__ "She's jealous. I can feel it. Look at her, trying to be all nice and sweet while secretly wishing she was in my place. Come on, Emma, you can feel it too."
        "{i}I brushed off the thought, trying to enjoy the massage. I needed to let go of this tension, not get caught up in some imaginary drama. Besides, Zara was doing a good job, and I didn’t want to ruin it.{/i}"
        scene w_616 with fade
        e "You’ve got great hands, Zara."
        z "Thank you. It's... it's something I've been practicing for years."
        e_ "There it is again. That slight edge in her voice. Why is she acting like this? Is she just nervous because I’m, well, me?"
        scene w_617 with fade
        z "You have a really nice body, Emma. It's... uh, it's in great shape."
        e_ "Ohhh, there it is. The compliment coated with a hint of something else."
        e__ "See? I told you. She wishes she could have what you have. Just play it cool, though, Emma. She’s not worth the trouble."
        e "Thanks. I try to keep in shape... you know, running around the mansion and all that."
        scene w_618 with fade
        e "But, really, it’s your hands doing the magic right now."
        "{i}Zara chuckled softly, the sound a little awkward but polite nonetheless.{/i}"
        "{i}Her fingers pressed into a particularly tight spot, making me wince just a little.{/i}"
        z "I'm glad you’re enjoying it. Sometimes I think... I think I should’ve done this professionally, you know?"
        z "Opened my own spa or something."
        e_ "Hmm, maybe she’s just trying to be friendly."
        e_ "Maybe I is blowing this out of proportion... or maybe Zara’s just good at hiding her envy. Either way, I’m not going to let it ruin my massage."
        scene w_619 with fade
        e "You totally should. You’ve got the skills for it."
        "{i}Zara's hands are too good to worry about whatever’s going on in her head.{/i}"
        "{i}Maybe Zara's just shy, or awkward around people like me. Who knows... not my problem. I'm here for the massage, and damn it, I'm going to enjoy it.{/i}"
        "{i}The massage went on for another few minutes, Zara’s touch never faltering. She stayed quiet for the most part, just the occasional small talk here and there.{/i}"
        scene black with fade
        "{i}By the time she finished, I felt completely relaxed, like a new woman. Whatever envy or awkwardness might’ve been brewing under the surface didn’t matter anymore.{/i}"
        $ emma_fr1_zara_talk = True
        show screen jacuzzi_massage_emma_sfr_1
    
    return
