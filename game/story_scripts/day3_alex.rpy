label day3_alex_1:
    $ alexreceiveblowjobeleanorday3 = False
    $ alexspieseleanortristanday3 = False

    scene black with fade

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 5rd_day with fade
    $ renpy.pause()
    hide 5rd_day with dissolve

    scene w_326 with fade
    "{i}I woke up before dawn, the first light of day creeping through the curtains.{/i}"
    "{i}As I turned to look at Emma, it was clear that she hadn’t rested well. Her face was drawn, and there were dark circles under her eyes.{/i}"
    "{i}She was still asleep, but her brow was furrowed, as if even in her dreams, the worries wouldn’t leave her alone.{/i}"
    a_ "She didn’t sleep well. It’s all weighing on her too much. I need to do something."
    "{i}I quietly got out of bed, careful not to disturb her.{/i}"
    "{i}I couldn’t just stay here, doing nothing. I needed to find out more about this place, to figure out if there was something—or someone—we should be worried about.{/i}"
    "{i}My mind wandered to Eleanor. She might know something, or at least be able to point me in the right direction.{/i}"
    scene w_344 with fade
    "{i}With that thought in mind, I decided I’d pay her a visit. There was something about her that seemed trustworthy, and right now, I needed all the help I could get.{/i}"
    "{i}As I dressed and prepared to leave, I took one last look at Emma. I would do whatever it took to keep her safe, even if it meant uncovering secrets that were better left buried.{/i}"
    a_ "I hope Eleanor can help. I can’t do this alone."

    if alexflirteleanorday1:
        "{i}As I approached Eleanor's house, memories of our last encounter flooded my mind. It wasn't just a casual meeting; there was something more charged in the air between us.{/i}"
        "{i}I recalled how she had flirted with me, and I hadn’t been indifferent to her advances either.{/i}"
        "{i}I remembered the way I had responded, stepping closer to her, feeling the warmth of her body as I pulled her into a more intimate embrace.{/i}"
        scene w_133b with fade
        $ renpy.music.play("audio/adult/female-Mm_1.mp3", channel="sfx1", relative_volume=0.3)
        $ renpy.pause()
        scene w_344 with fade
        "{i}I could sense that she enjoyed it.{/i}"
        a_ "That moment... I could tell she liked it, maybe even wanted more. That should make it easier to have her on my side."
        scene w_345 with dissolve
        "{i}Now, standing in front of Eleanor’s door, I felt a strange mix of confidence and apprehension.{/i}"
        "{i}I hesitated for just a moment, gathering my thoughts, trying to focus on the task at hand.{/i}"
        "{i}I knew why I was here, but I couldn't deny that part of me was also curious about how she would react, if that spark between us would still be there.{/i}"
        scene w_347 with dissolve
        "{i}Taking a deep breath, I raised my hand and knocked firmly on the door.{/i}"
        scene w_346 with dissolve
        $ renpy.music.play("audio/sfx/sfx_knock.ogg", channel="sfx1", relative_volume=1.0)
        "{i}The sound echoed in the quiet surroundings, and I stepped back slightly, waiting.{/i}"
        scene w_345 with dissolve
        "{i}Would she open the door with that same inviting smile, or would there be a hint of something more in her gaze this time? {/i}"
        a_ "Whatever happens, I need her on my side... but I wouldn’t mind if things got a little more interesting."
    else:
        "{i}As I walked towards Eleanor's house, the memory of our last encounter replayed in my mind.{/i}"
        "{i}I remembered how she had flirted with me, her tone light, her smile a bit too inviting.{/i}"
        "{i}But I had chosen to politely ignore it, not wanting to complicate things between us. I didn’t reciprocate her advances, instead steering the conversation back to safer, friendly topics.{/i}"
        "{i}She had seemed a little disappointed, but she didn’t push it further.{/i}"
        scene w_131b with fade
        $ renpy.music.play("audio/sfx/sfx_glasses_clink.opus", channel="sfx1", relative_volume=0.8)
        $ renpy.pause()
        scene w_344 with fade
        a_ "There was definitely a hint of attraction in her eyes, though. She was interested, but I kept things friendly."
        a_ "Now, I’m wondering if that was the right move."
        scene w_345 with dissolve
        "{i}Now, standing in front of her door, I couldn’t help but think that my approach had been the right one. By keeping our relationship on friendly terms, I might have made it easier to get her on my side.{/i}"
        "{i}Eleanor was smart, and pushing her away too forcefully might have made her suspicious or defensive.{/i}"
        "{i}But, at the same time, I couldn’t deny the lingering possibility that if she kept flirting, I would need to decide what to do.{/i}"
        a_ "Maybe I should just keep things friendly… or maybe I should consider letting her get closer. Could it really hurt?"
        scene w_347 with dissolve
        "{i}As I reached out to knock on her door, my thoughts continued to swirl. What if I gave in to her advances? Could I still keep control of the situation, or would things get messy?{/i}"
        scene w_346 with dissolve
        $ renpy.music.play("audio/sfx/sfx_knock.ogg", channel="sfx1", relative_volume=1.0)
        "{i}On the other hand, keeping my distance might make her lose interest altogether, and that could complicate my plans.{/i}"
        "{i}The sound echoed through the quiet morning air, and I took a step back, waiting for Eleanor to answer.{/i}"
        scene w_345 with dissolve
        a_ "Here we go… time to see how she plays this."

    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    scene w_348 with dissolve
    "{i}I was prepared for a conversation, maybe even a subtle flirt, but nothing could have prepared me for the sight that greeted me when the door swung open.{/i}"
    a_ "What the hell, Eleanor?"
    "{i}Eleanor stood there, her figure accentuated by an intimate, almost see-through nightwear. The fabric clung to her curves, leaving very little to the imagination.{/i}"
    "{i}For a moment, my brain short-circuited, and the only thing that came to mind was a mental curse.{/i}"
    a_ "I can't believe she's wearing that..."
    "{i}It took every ounce of my willpower to keep my expression neutral as I processed the situation.{/i}"
    "{i}The friendly, possibly flirtatious conversation I had envisioned was instantly overshadowed by the unexpected intimacy of the moment.{/i}"
    scene w_349 with dissolve
    ele "Alex! I'm so glad you're back. I'm so happy."
    "{i}Eleanor greeted me with a cheerful tone, clearly pleased to see me, but I could barely manage a reply.{/i}"
    "{i}My eyes traveled down, noticing she was only wearing panties beneath the nightgown.{/i}"
    scene w_348 with dissolve
    a_ "Oh, damn..."
    "{i}The realization struck me hard—she wasn’t just comfortable with this, she wanted me to see her like this.{/i}"
    "{i}She was showing herself to me on purpose. The thought sent a thrill through me that I didn't quite know how to handle.{/i}"
    "{i}A part of me liked the idea—a lot. Finally, I managed to respond to her greeting, though it came out a bit awkwardly.{/i}"
    a "Uh, hey... I, um, I wanted to talk to you about something."
    "{i}Eleanor’s smile widened, and I could tell from the glint in her eyes that it was more than just a friendly greeting—it was suggestive, almost playful.{/i}"
    scene w_349 with dissolve
    ele "Why don’t you come in, Alex? We’ll be more comfortable inside."
    "{i}As she spoke, her voice was smooth, almost coaxing.{/i}"
    scene w_350 with dissolve
    "{i}Then, without waiting for a reply, she turned around and gestured for me to follow her into the house.{/i}"
    "{i}My eyes followed the movement of her hips, perfectly framed by the delicate lace of her panties.{/i}"
    "{i}The sight was enough to send my thoughts racing.{/i}"
    a_ "What am I getting myself into here?"
    "{i}I shook off the thought and stepped inside, closing the door behind me.{/i}"
    "{i}As I followed Eleanor into the living room, my eyes couldn't help but be drawn to the way her hips swayed with each step.{/i}"
    scene w_352 with fade
    "{i}Her figure was accentuated by the delicate fabric of her lingerie, revealing more than concealing.{/i}"
    "{i}I tried to focus, but my thoughts kept drifting.{/i}"
    a_ "Damn, she knows exactly what she's doing. Is she testing me, or is this just how she is?"
    "{i}As I gaze upon the alluring curves of Eleanor's backside, my mind wanders to wicked thoughts of what lies beneath those soft fabric layers.{/i}"
    a_ "The way they hug her firm cheeks and round booty beguiles me. Oh, Eleanor, your derrière is truly something to behold."
    scene w_351 with dissolve
    $ renpy.pause()
    "{i}I snapped back to reality just in time as Eleanor stopped in the middle of the room, turning around to face me.{/i}"
    "{i}Her eyes were playful, a hint of something more lingering just beneath the surface.{/i}"
    ele "Here, we can be more comfortable, don’t you think?"

    if alexflirteleanorday1:
        "{i}Her tone was suggestive. I knew what she was implying.{/i}"
    else:
        "{i}Her tone was suggestive. I knew what she was implying, but I wasn’t sure if I was ready to cross that line.{/i}"
    
    scene w_353 with dissolve
    "{i}As I stood in the living room, facing Eleanor, the memory of our last interaction still lingered in my mind.{/i}"
    "{i}The way she was dressed now, even more revealing than before, made it difficult to focus on the real reason I had come here.{/i}"
    "{i}I tried to keep my gaze steady, but her suggestive smile made that nearly impossible.{/i}"
    scene w_354 with dissolve
    ele "So, what brings you here today, Alex?"
    scene w_353 with dissolve
    "{i}Her voice was soft but carried a playful edge, making me wonder if she was aware of the effect she had on me.{/i}"
    "{i}Just as I opened my mouth to respond, she cut me off with a teasing grin.{/i}"
    scene w_354 with dissolve
    ele "Before you answer that, let me just say... I owe you for last time. Whatever you want, I'm more than happy to oblige."
    "{i}Her words were loaded with implication, and for a moment, my mind raced through the possibilities.{/i}"
    scene w_353 with dissolve
    a_ "Does she mean what I think she means?"
    "{i}As Eleanor smiled warmly, I could feel a mix of anticipation and curiosity building up inside me. She looked genuinely pleased to see me, and that made what I had to say a bit easier.{/i}"
    "{i}But as I noticed her outfit and how little it left to the imagination, my mind raced.{/i}"
    scene w_355 with dissolve
    ele "What happened to you? Your arm… it looks serious."
    "{i}Her concern was evident in her eyes as she gestured toward my bandaged arm.{/i}"
    "{i}I hesitated for a moment, not wanting to alarm her too much, but I knew she deserved the truth.{/i}"
    a "It’s nothing, really... Just a rough night. I got into a bit of trouble, but it’s fine now."
    ele "Trouble? What kind of trouble? You shouldn’t downplay something like that."
    "{i}I could see the worry in her expression. This was a side of Eleanor I hadn’t seen often – protective, even vulnerable in her own way.{/i}"
    a "I appreciate your concern, Eleanor. It was just a random attack, nothing to worry about. I’m fine, really."
    scene w_356 with dissolve
    ele "Random attack? Alex, that’s not 'nothing'. You could’ve been seriously hurt."
    "{i}Her tone was a mix of concern and frustration, and I could tell she was struggling to process the situation. I didn’t want to push her further into worry.{/i}"
    a "Honestly, Eleanor, I’m okay. The important thing is that I’m here, talking to you. Let’s not dwell on the negative, alright?"
    scene w_357 with dissolve
    ele "Alex, you can’t just drop something like that and leave me hanging."
    ele "What exactly happened during that attack?"
    "{i}I could see the concern etched on her face, and I knew there was no avoiding it. Eleanor wasn’t the type to let something like this slide.{/i}"
    scene w_358 with dissolve
    a "Alright, alright…"
    a "I was in the garden last night, trying to clear my head. Suddenly, out of nowhere, this guy attacks me."
    a "It was all a blur, really—he seemed desperate, like he was looking for something specific. We fought for a bit, and that's how I ended it."
    scene w_356 with dissolve
    ele "Oh my God, Alex… That sounds terrifying. Did he take anything? Were you hurt anywhere else?"
    a "He didn’t take anything, no."
    a "Honestly, I was lucky it wasn’t worse. I think he was just trying to scare me, or maybe he was after something I didn’t have."
    scene w_359 with dissolve
    ele "I can’t believe this happened…"
    ele "You really need to be more careful."
    scene w_358 with dissolve
    a "Hey, I’m here, aren’t I? You don’t need to worry."
    a "I’ll be more careful, I promise. But right now, I’m just glad to be here, talking to you."
    a "Eleanor, does this sort of thing happen often around here?"
    a "I mean, I know it's a small town, but being attacked in the gardens of the mansion…"
    scene w_359 with dissolve
    ele "Not really, Alex."
    ele "This town is generally pretty peaceful. Sure, we've got our share of issues like any place, but nothing as extreme as what you just went through. It's mostly quiet."
    ele "Are you sure you don’t have any enemies? Someone who might have a reason to go after you?"
    scene w_358 with dissolve
    a "I’ve been racking my brain, but no one comes to mind."
    a "I mean, I’ve made my share of mistakes, but I can't think of anyone who'd want me dead. It just doesn’t add up."
    scene w_357 with dissolve
    ele "Do you think this could have anything to do with the mansion’s reputation for being haunted?"
    ele "I mean, it’s just a story, but…"
    scene w_358 with dissolve
    a "Oh, definitely. You know, I actually landed a solid punch on that 'ghost.' Turns out, they're not as transparent as you'd think!"
    scene w_354 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx1", relative_volume=0.3)
    "{i}Eleanor burst into laughter, her eyes lighting up with amusement at my attempt at humor.{/i}"
    ele "So, you’re telling me you’ve discovered the secret to fighting off ghosts?"
    scene w_353 with dissolve
    a "Well, I’ve never been much for ghost stories, but now I think I’ve got a strategy."
    a "Turns out, all it takes is a good right hook to send them packing. Who knew?"
    $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx1", relative_volume=0.3)
    "{i}Her laughter eased some of the tension in the room, making the whole situation feel a bit lighter, even if just for a moment.{/i}"
    "{i}It was good to see her smile, especially after the heavy conversation we’d been having.{/i}"
    scene w_360 with dissolve
    "{i}Eleanor caught me by surprise, but I didn't have time to react before she continued talking.{/i}"
    scene w_361 with dissolve
    ele "Alex, since we're talking about strange things... I have a request to make of you."
    scene w_360 with dissolve
    a "Sure, what do you need?"
    scene w_361 with dissolve
    ele "I want you to help me decide something... about a painting I'm thinking of hanging. But I need you to see it in the right context."
    scene w_362 with dissolve
    "{i}Before I could ask more, Eleanor took my hand, her fingers naturally intertwining with mine, and gently pulled me towards the stairs.{/i}"
    "{i}The feeling of her touch left me slightly unsettled, but I didn't let go. She led me with confidence, as if she knew exactly what she was doing.{/i}"
    scene w_363 with dissolve
    ele "Come, it's upstairs. I need you to see it in my bedroom."
    "{i}As we walked, I couldn't help but notice the way her pajamas hugged her curves.{/i}"
    "{i}I tried to focus on what she was saying, but my gaze kept drifting to her beautiful ass.{/i}"
    scene w_364 with dissolve
    "{i}She guided me up to the second floor, each step making the environment feel more intimate and private.{/i}"
    "{i}My mind buzzed with possibilities, but I stayed focused on the moment.{/i}"
    ele "Here, come in. I want your honest opinion."
    scene w_365 with dissolve
    a_ "Does she really just want an opinion on decor, or is there something more behind this?"
    ele "Here it is,"
    "{i}She said, gesturing towards the painting above her double bed.{/i}"
    scene w_366 with dissolve
    "{i}I took a moment to process the sight before me.{/i}"
    a "Wow, Eleanor,"
    a "This is quite... unexpected."
    $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx1", relative_volume=0.3)
    "{i}She laughed softly.{/i}"
    ele "I knew you'd say that."
    ele "But honestly, I want your opinion. Do you think it's too much?"
    a "Well, it's certainly bold."
    a "But if you like it, then why not?"
    "{i}Eleanor moved closer to me, her body brushing against mine.{/i}"
    ele "You know, Alex,"
    "{i}She said, her voice low and seductive.{/i}"
    ele "There's more to me than just the surface."
    ele "I like to explore my desires, and sometimes that means pushing boundaries."
    a_ "I have to keep my voice steady."
    a "I see,"
    ele "And sometimes, that means playing with power dynamics,"
    scene w_368 with dissolve
    "{i}I turned to face her, our eyes meeting.{/i}"
    a "Are you saying what I think you're saying?"
    scene w_369 with dissolve
    ele "Maybe,"
    ele "But for now, I just want your opinion on the painting."
    "{i}I nodded, forcing myself to focus on the task at hand.{/i}"
    scene w_366 with dissolve
    a "Well, I think it fits with the rest of your decor,"
    a "..."
    a "It's bold and unique, just like you."
    $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx1", relative_volume=0.3)
    "{i}Eleanor laughed again.{/i}"
    ele "Thank you, Alex,"
    "{i}She said, her hand resting on my arm.{/i}"
    ele "I knew I could count on you for an honest opinion."
    scene w_368 with dissolve
    "{i}There was a spark there, a desire that I couldn't ignore.{/i}"
    "{i}I could feel the tension building between us, and I knew that it was only a matter of time before we gave into our desires.{/i}"
    scene w_369 with dissolve
    ele "But I have to go to the bathroom,"
    ele "I'll be right back."
    scene w_370 with dissolve
    $ renpy.pause()
    scene w_371 with dissolve
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    $ renpy.pause()
    scene w_372 with dissolve
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    $ renpy.pause()
    scene w_373 with dissolve
    "{i}She walked out of the room, leaving me alone with my thoughts.{/i}"
    "{i}I looked at the painting again, my mind filled with images of Eleanor in her BDSM gear. I couldn't deny it - I was intrigued.{/i}"
    scene w_374 with dissolve
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    $ renpy.pause()
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    ele "What do you think?"
    scene w_375 with dissolve
    "{i}Eleanor walked back into the room, completely naked.{/i}"
    $ renpy.music.play("audio/musics/sexy.mp3", "music1", fadein=2.0, relative_volume=0.1)
    scene w_376 with dissolve
    "{i}Her body was voluptuous and curvy, with full hips and large breasts. She had a playful smile on her face as she approached me, her bare feet padding softly against the hardwood floor.{/i}"
    scene w_377 with dissolve
    $ renpy.pause()
    ele "Do you like what you see?"
    scene w_378 with dissolve
    $ renpy.pause()
    a "Yes,"
    "{i}I swallowed, feeling my throat go dry.{/i}"
    scene w_379 with dissolve
    $ renpy.pause()
    a "You're beautiful, Eleanor."
    scene w_380 with dissolve
    ele "I'm glad you think so,"
    "{i}she said, taking a step closer to me.{/i}"
    "{i}I could feel the heat radiating off her body. My own body responded, my cock growing hard in my pants.{/i}"
    ele "I've been thinking about you all night, Alex,"
    "{i}Eleanor said, her voice low and seductive.{/i}"
    ele "Ever since I saw you looking at that painting, I've wanted to touch you, to feel your skin against mine."
    ele "Do you want that too?"
    "{i}She asked, her eyes locked onto mine.{/i}"
    scene w_381 with dissolve
    $ renpy.pause()
    "{i}I nodded, unable to speak. She dropped to her knees in front of me, Eleanor's hand continued to move down, reaching for the zipper of my pants.{/i}"
    scene w_382 with dissolve
    ele "Mmm, I can feel you through your pants."
    ele "So hard and ready for me."
    ele "Mmm, I knew you'd be big,"
    ele "I can't wait to taste you, Alex."
    scene black with dissolve
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    "{i}But just as Eleanor was about to unzip his pants, a noise from downstairs caught their attention.{/i}"
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    "{i}Eleanor's husband had arrived home, the sound of the front door opening and closing breaking the spell that had been cast.{/i}"
    scene w_383 with dissolve
    "{i}Eleanor's eyes widened, but she didn't move.{/i}"
    ele "Shit,"
    scene w_384 with dissolve
    tr "Eleanor? I'm home!"
    scene w_385 with dissolve
    ele "!!!!!"
    a "We need to go. Now."
    scene w_386 with dissolve
    ele "Shit, I didn't think he'd be back so soon."
    scene w_387 with dissolve
    ele "Alex, hide!"
    scene w_388 with dissolve
    "{i}She shoved me toward the closet, her fingers trembling as she tried to gather her composure.{/i}"
    scene w_389 with dissolve
    "{i}I could hear her husband’s footsteps moving closer, up the stairs.{/i}"
    scene w_390 with dissolve
    "{i}My pulse was racing, but I slipped inside the closet, trying to make as little noise as possible.{/i}"
    scene w_391 with dissolve
    ele "Just stay quiet, alright? I'll... I'll deal with him."
    scene w_392 with dissolve
    $ renpy.pause()
    scene w_393 with dissolve
    "{i}I could barely breathe as I listened to Eleanor scramble to straighten herself up.{/i}"
    "{i}The door to the bedroom swung open, and I could see her husband’s shadow through the crack in the closet door.{/i}"
    a_ "Holy shit. If he finds me here, this is going to be a disaster."
    scene w_394 with dissolve
    "{i}Her husband, was standing in the doorway, looking utterly shocked. His surprise quickly turned into something else as a sly grin crept across his face.{/i}"
    "{color=#533d7c}?????{/color}" "Well, this is a pleasant surprise. What’s going on here, Eleanor?"
    "{i}I could feel my heart racing. This was bad. I needed to stay quiet, but every second that passed felt like a ticking time bomb.{/i}"
    ele "Oh... Tristan, I wasn’t expecting you back so soon."
    ele "I was just... getting ready for a shower."
    "{i}Eleanor tried to sound casual, but there was an edge of panic in her voice. I could see her struggling to keep her composure as Tristan stepped closer, his eyes roaming over her body.{/i}"
    a_ "Shit. This is getting worse. He’s not going to leave anytime soon, is he?"
    tr "A shower, huh?"
    tr "You know... it’s been a long day. Maybe we could make use of this moment, hmm? "
    "{i}I saw him reach out, his hands brushing over Eleanor’s waist. She stiffened for a moment, clearly caught off guard, but then quickly composed herself.{/i}"
    scene w_395 with dissolve
    ele "Oh, Tristan... now? Really?"
    ele "You’re sweaty, love. You should freshen up first."
    tr "Freshen up? Come on, Eleanor."
    tr "I’ve missed you. We could have a little fun before I hit the shower."
    a_ "Eleanor, say something, get him out of here!"
    ele "How about this—you go take a quick shower, and I’ll be waiting right here when you’re done."
    ele "That way, we can... enjoy it even more."
    "{i}There was a pause. Tristan looked at her, his grin widening as he seemed to like the idea.{/i}"
    scene w_396 with dissolve
    tr "Alright... but you better be waiting for me."
    "{i}He winked and finally turned toward the bathroom. I let out a breath I didn’t even know I was holding. This was too close. Way too close.{/i}"
    scene black with dissolve
    a_ "Shit, I was so close to getting what I wanted, a blowjob from this woman, but now everything is at risk."
    $ renpy.music.play("audio/sfx/sfx_shower_hallway.ogg", channel="ambient1", fadein=2.0, relative_volume=0.3)
    a_ "..."
    "{i}But now, as I hear the water running in the shower, my thoughts turn to something more daring.{/i}"
    a_ "What if I came out of the closet, without pants, and made Eleanor give me a blowjob while her husband takes a shower in the bathroom?"
    "{i}The excitement of the possibility sends a thrill through my body.{/i}"

    $ alexreceiveblowjobeleanorday3 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}I'll take my chances.{/size}{/font}":
            $ alexreceiveblowjobeleanorday3 = True

            call eleanor_bj1_day3
            
        "{font=fonts/hatten.ttf} {size=50}No... I'd better go.{/size}{/font}":
            $ alexreceiveblowjobeleanorday3 = False
            "{i}As I peered through the crack of the closet door, I watched Tristan disappear into the bathroom.{/i}"
            scene w_421 with dissolve
            "{i}The sound of the shower being turned on echoed in the room, and for a brief moment, I could finally breathe again.{/i}"
            scene w_422 with dissolve
            "{i}The door to the bedroom was wide open, and the path to my escape was clear.{/i}"
            scene w_423 with dissolve
            a_ "Eleanor is distracted with Tristan’s in the shower... this is my chance. I need to get out of here now, before things get even worse."
            scene w_424 with dissolve
            "{i}My eyes darted toward the bedroom door, calculating the quickest way out.{/i}"
            "{i}But as I took my first step forward, I hesitated. The sound of water splashing from the bathroom caught my attention.{/i}"
            scene w_425 with dissolve
            a_ "Wait... should I leave now? Or maybe..."
            a_ "just take a peek? Tristan and Eleanor are alone in there. No one would know if I stayed a little longer, just to see what happens."
            scene w_426 with dissolve
            "{i}I found myself frozen, torn between the smart decision and the reckless curiosity gnawing at me.{/i}"
            "{i}It wasn’t like I hadn’t thought about Eleanor like that before... and the idea of watching her and Tristan together was tempting in a way I didn’t want to admit. I glanced toward the bathroom door.{/i}"

            $ alexspieseleanortristanday3 = False

            menu:
                "{font=fonts/hatten.ttf} {size=50}Fuck it... I'll go spy.{/size}{/font}":
                    $ alexspieseleanortristanday3 = True

                    call tristan_f_eleanor_day3
                "{font=fonts/hatten.ttf} {size=50}No... I'd better go.{/size}{/font}":
                    $ alexspieseleanortristanday3 = False
                    a_ "No... What am I thinking? This situation has gotten too dangerous. That's not even what I came here to do."
                    $ renpy.music.stop("ambient1", fadeout=2.0)
                    scene w_439 with fade
                    a_ "That was way too close. I can’t believe I almost got caught with Eleanor, especially with her like that—on her knees, ready to..."
                    a_ "Damn. Just thinking about it makes my heart race. If Tristan had come in just a second earlier, I’d be done for. I barely managed to hide before he walked in."
                    a_ "The look on her face when she saw him... she didn’t even flinch. She played it cool like it was nothing, but I know she felt the same heat I did."
    
    scene w_440 with fade
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.1)
    if alexreceiveblowjobeleanorday3 == False and alexspieseleanortristanday3 == True:
        a_ "Eleanor is... damn, she’s something else. I’ve always known she had a wild side, but this? This was on a whole new level."
        a_ "I can't stop thinking about how she looked at me, like she wanted more. There’s no way this was the last time."
        a_ "We’ll definitely have another chance together... and next time, I won’t just be watching."
    elif alexreceiveblowjobeleanorday3 == False and alexspieseleanortristanday3 == False:
        a_ "This wasn’t even why I came to see her. I wasn’t supposed to get into this mess. It was too risky, and I should’ve known better."
        a_ "Sure, it was tempting to stick around, especially when they went to the bathroom together. But I couldn’t risk it. I had to get out of there."
        a_ "This is getting too dangerous, and I need to keep my head straight. Whatever this is with Eleanor... it’s a game I need to be careful with."
    else:
        "{i}We promised to do it again another day. I left Eleanor's house feeling very satisfied.{/i}"
        a_ "She knelt in front of me, and I could feel her hot breath on my cock. "
        a_ "She looked up at me with those beautiful eyes, and then she took me in her mouth."
        a_ "We promised to do it again, and I can't wait."
    
    scene w_326 with fade
    "{i}I was walking back from Eleanor’s place, my mind a mess, trying to piece together what happened.{/i}"
    a_ "Why the hell can’t I remember everything? The attack, the blood... damn it, I need answers."
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    scene w_739 with fade
    "{i}The gravel crunched under my feet as I made my way back into the mansion grounds, and the usual calm of the garden didn’t do a thing to settle the storm going on inside my head.{/i}"
    "{i}I barely noticed anything around me until I caught sight of Samuel.{/i}"
    scene w_740 with dissolve
    "{i}He was tending to some flowers, just like always, his strong, steady presence a weird contrast to how messed up I felt.{/i}"
    "{i}And then I saw her, Samuel's daughter—Zara—working silently beside him. She is always there, always quiet, as if she is trying not to be seen.{/i}"
    a_ "Man, she’s awkward around me, isn’t she?"
    scene w_741 with dissolve
    "{i}I can feel it every time we cross paths. It’s like she freezes up.{/i}"
    "{i}But right now, I’m not in the mood for anything. I need to talk to someone grounded.{/i}"
    "{i}I changed my direction, making my way over to Samuel.{/i}"
    "{i}He’s the kind of guy who never seems shaken by anything. Maybe he could give me something to work with—anything, really.{/i}"
    scene w_742 with dissolve
    a "Hey, Samuel. Got a minute?"
    "{i}He looked up from the plants, his hands still steady, calm. He nodded, like he always does, no rush, no panic.{/i}"
    s "Of course, Alex. What’s on your mind?"
    scene w_743 with dissolve
    a_ "Where do I even start?"
    "{i}It felt like everything was closing in on me—the attack, the tension in my muscles from not knowing what the hell is going on.{/i}"
    a "It’s... complicated. But I just can’t shake this feeling like there’s more going on than I know."
    a "You ever get that sense, like everything around you is off, but you can’t figure out why?"
    s "Can you be more specific, Alex?"
    "{i}I shrugged, not really sure how to answer. My gaze wandered over the garden, trying to avoid thinking too much.{/i}"
    a "You ever hear about those stories? You know, about the mansion being haunted?"
    scene w_745 with dissolve
    "{i}Samuel straightened, a small chuckle escaping his lips.{/i}"
    s "Oh, that old tale? Yeah, I’ve heard 'em. Ghosts, apparitions... Even heard someone saw a headless horseman once, back in the day."
    "{i}I laughed despite myself. A headless horseman? This place really was drenched in its own mythos.{/i}"
    scene w_746 with dissolve
    a "And you believe any of it?"
    "{i}He shook his head slowly, the smirk still on his face.{/i}"
    scene w_745 with dissolve
    s "Nah, nothing more than local legends, if you ask me. Place this old, it’s bound to collect some stories, don’t you think?"
    a "Yeah, I guess. Still, it’s a bit unsettling sometimes, especially at night."
    "{i}Samuel’s eyes flickered with curiosity, but he kept his tone casual.{/i}"
    s "You afraid of ghosts, Alex?"
    "{i}I scoffed, but inside, I felt a twinge of something I didn’t want to admit.{/i}"
    scene w_746 with dissolve
    a "I don’t believe in ghosts."
    a_ "Sure, I don’t."
    "{i}Samuel raised an eyebrow, like he could hear the doubt under my words.{/i}"
    scene w_745 with dissolve
    s "Mmhmm. Well, I wouldn't worry too much about it."
    s "I’ve been around here for a while, and the only spirits I’ve seen are the ones people pour in their glasses."
    "{i}I chuckled, but my mind wandered back to the unease I’d felt in the mansion.{/i}"
    a "What about security? This area’s pretty quiet, but is it... safe?"
    "{i}He seemed to consider the question more seriously than the last one.{/i}"
    scene w_746 with dissolve
    s "Safe enough. We’ve got security watching the place, cameras, gates, all that."
    s "No one's gonna just walk in here unnoticed. But… you know how it is. There’s always some risk, no matter where you go."
    "{i}I nodded, his words reassuring me a bit. Still, something about the way he spoke made me feel like there was more to it.{/i}"
    a "And no one’s ever broken in? No incidents?"
    "{i}Samuel shook his head.{/i}"
    s "Nope, not that I know of. The biggest disturbance we’ve had is a raccoon getting into the trash."
    "{i}I exhaled, trying to relax. But as we spoke, I couldn’t shake the feeling that I was being watched.{/i}"
    scene w_747 with dissolve
    a_ "She's watching, isn’t she?"
    "{i}I glanced over and caught sight of the young woman in the distance. Zara. Her eyes were on me, intense, watching.{/i}"
    a_ "She's been keeping an eye on me ever since I got here."
    "{i}Samuel followed my gaze, but didn’t comment on it.{/i}"
    scene w_745 with dissolve
    s "If you’re worried about anything, just let me know."
    s "This place can feel a bit eerie, but it's safe, trust me."
    a "Yeah... thanks, Samuel."
    "{i}I nodded. There was a pause between us, a silence that felt like it was carrying the weight of unspoken things.{/i}"
    scene w_748 with dissolve
    "{i}That’s when I noticed Zara approaching. Her quiet, observant gaze locked onto us as she came closer.{/i}"
    a "What about you, Samuel? What’s your story? You've got to have a life outside these gates."
    "{i}Samuel’s expression shifted, and for the first time since we started talking, I saw a flicker of something—pain, maybe?{/i}"
    "{i}He didn’t speak immediately, like he was measuring his words.{/i}"
    s "I had a wife, once. Emma. She was the love of my life... but she’s gone now."
    scene w_749 with dissolve
    a "Emma?!"
    s "Coincidence... isn't it?"
    "{i}He paused, his jaw tightening.{/i}"
    s "Lost her in an accident. One of those things you don’t see coming."
    s "Everything changes after that. I came here after... thought I’d get some distance, keep my head down."
    s "But no matter where you go, memories stick to you."
    "{i}There was a strange stillness in the air after he spoke. Even the sounds of the garden seemed to fade into the background.{/i}"
    a "Sorry to hear that, man. Must’ve been hard."
    s "{i}{/i}It was. But life goes on. You learn to live with it. Some days are easier than others."
    scene w_750 with dissolve
    "{i}Zara had moved even closer now, standing just behind Samuel. Her eyes flickered between us, but she remained silent., her presence soft but curious.{/i}"
    "{i}t was clear she was listening intently, especially when the conversation turned personal.{/i}"
    a "You ever think about leaving this place? Starting somewhere fresh?"
    s "Nah. I've found my place here. It’s peaceful in its own way. Keeps me grounded, you know? Not much to run from anymore."
    "{i}Zara shifted slightly, her lips parting as if she were about to say something, but then she stopped. Instead, she simply nodded at Samuel’s words, as if silently agreeing.{/i}"
    "{i}I decided to keep the conversation moving, not wanting to linger too long on Samuel's pain.{/i}"
    scene w_749 with dissolve
    a "I get it. Sometimes staying in one place helps keep things steady."
    a "But doesn’t this place ever get to you? All these stories, the quiet... it’s enough to make anyone’s mind wander."
    "{i}Samuel looked around the garden again, the faintest smile tugging at the corner of his lips.{/i}"
    scene w_750 with dissolve
    "{i}It was almost like he was enjoying the peace in a way I couldn’t quite understand.{/i}"
    s "It does sometimes. But that's when you let it wash over you, not fight it."
    s "Let the silence be what it is—just silence. People are too afraid of quiet, Alex. That’s where they lose themselves."
    "{i}I stared at him for a moment, absorbing what he said. He made it sound simple, but I wasn’t sure if I had it in me to just 'let it wash over' like he did.{/i}"
    scene w_749 with dissolve
    "{i}I glanced over at Zara, still standing there quietly, her expression unreadable.{/i}"
    a "What about you, Zara? Do you ever get creeped out by this place?"
    "{i}She blinked, as if surprised I’d addressed her directly, and her eyes darted toward Samuel for a split second before returning to me.{/i}"
    scene w_751 with dissolve
    z "Sometimes. But... I guess you get used to it after a while. It’s not so bad if you don’t think about it too much."
    "{i}Her voice was soft, but there was something in the way she said it, like she was trying to convince herself more than anyone else.{/i}"
    a "Yeah, maybe. I’m not sure I could ever get used to it, though."
    scene w_750 with dissolve
    s "You’d be surprised. This place has a way of making you adapt. But don’t let the stories get to you. Like I said earlier, it’s mostly just talk."
    "{i}I shrugged, unsure. Something about this place, and the things I had already seen, made me think the stories were more than just rumors.{/i}"
    scene w_749 with dissolve
    "{i}Still, I didn’t push it further. It didn’t seem like the kind of topic to keep poking at, especially with Zara listening so intently.{/i}"
    a "I guess that makes sense."
    a "You know, I’ve been meaning to ask—how did you end up working here, Samuel? This can’t be the only job you’ve ever had."
    scene w_750 with dissolve
    "{i}Samuel’s smile faded slightly, and he seemed to consider his words carefully before responding.{/i}"
    s "No, it’s not. I’ve done a bit of everything, actually. This job... well, it came at the right time."
    s "After Emma... after everything that happened, I needed something to keep my mind busy. This place... it does that for me. Keeps me focused."
    scene w_749 with dissolve
    "{i}There was that name again. Emma. I didn’t know the full story, but I could see the pain it brought him.{/i}"
    a "I get that. Sometimes keeping busy is all you can do."
    scene w_750 with dissolve
    s "Yeah. Anyway, enough about me. How’s your hand? That cast looks uncomfortable."
    a "It’s fine. Just annoying more than anything. Can’t do much with it, but I’m managing."
    "{i}Zara finally spoke up, her voice soft but curious.{/i}"
    scene w_751 with dissolve
    z "How did it happen? Your hand, I mean."
    "{i}I hesitated for a moment, not sure how much I wanted to tell them.{/i}"
    "{i}The attack was still fresh in my mind, but explaining it felt complicated, especially since I didn’t have all the answers myself.{/i}"
    a "Accident. I got caught up in something I didn’t see coming."
    "{i}I could see the questions in her eyes, but to my relief, she didn’t press further.{/i}"
    scene w_750 with dissolve
    "{i}Samuel, however, watched me closely, his expression unreadable.{/i}"
    s "Well, whatever it was, make sure you take care of yourself."
    s "This place... it has a way of wearing people down if you’re not careful."
    a "Yeah, I’ll keep that in mind."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_326 with fade
    "{i}His words hung in the air, and I couldn’t tell if it was just general advice or if he was warning me about something more.{/i}"
    "{i}Either way, I felt a chill creep down my spine, but I forced a smile and nodded.{/i}"
    scene w_753 with fade
    "{i}I sat there on the couch, staring blankly at the sleek, polished surface of the coffee table.{/i}"
    "{i}My reflection on the glass seemed distant, blurry, like a version of me from some other life, before everything went sideways.{/i}"
    scene w_752 with dissolve
    "{i}I tried to shake the thoughts from my head, but they were stubborn, crawling back into focus.{/i}"
    a_ "Why did things have to end up like this? If I hadn’t gone out that night... if I hadn’t... would any of this have happened?"
    "{i}The memories of the attack still flashed through my mind like scenes from a bad dream, but the details were frustratingly unclear.{/i}"
    "{i}That knife, the cold steel, the way it tore through the air. Everything that followed had been a blur, and yet, that one moment kept replaying itself. Over and over.{/i}"
    $ renpy.music.play("audio/sfx/phone_ring.ogg", channel="sfxloop1", relative_volume=0.3)
    scene w_753 with dissolve
    $ renpy.pause()
    "{i}Suddenly, a sharp vibration from the table jolted me out of my thoughts.{/i}"
    "{i}My phone buzzed, vibrating against the glass surface. I leaned forward, squinting at the screen.{/i}"
    "{i}The number flashed across the display, and immediately, a cold wave washed over me.{/i}"
    "{i}It was the same number... from that night. The one that called just before everything went to hell.{/i}"
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    scene w_754 with dissolve
    "{i}I picked up the phone, my thumb hovering over the answer button.{/i}"
    "{i}I hesitated for a moment, staring at the digits, trying to piece it all together.{/i}"
    a_ "Why didn’t I return this call? Did I forget, or did I avoid it?"
    "{i}Recognition hit me suddenly. The number belonged to someone I hadn’t spoken to in a long time.{/i}"
    "{i}My old boxing manager. Of course... that night was a mess, and I hadn’t thought about it since.{/i}"
    "{i}Henry Blackwell, my old boxing manager. The guy who had seen me through the toughest fights, both in and out of the ring.{/i}"
    "{i}We hadn’t spoken in ages, not since I stepped away from boxing and all the chaos that came with it. I was supposed to call him back after that night… the night of the attack.{/i}"
    a_ "What could Henry want now? It’s not like him to call me out of the blue unless it’s something important… or unless he’s got some wild story to share."
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    scene w_755 with dissolve
    "{i}I lifted the phone to my ear as I paced around the room, stepping outside where the air was cooler. The flowers in the garden brushed against my legs as I moved past them.{/i}"
    a "Henry! Man, it’s been a while."
    h "{i}Alex! Holy hell, you’re alive! I thought you were avoiding me or something. What, forgot how to use a phone?{/i}"
    scene w_756 with dissolve
    "{i}His voice boomed through the speaker, the same old Henry—always loud, always with that infectious energy. I couldn’t help but grin.{/i}"
    a "Nah, just been... dealing with a few things. How’ve you been?"
    h "{i}Oh, you know me. Still living the dream, keeping these rookies in line.{/i}"
    h "{i}But I’ve been hearing things, Alex. I heard you got into some trouble recently?{/i}"
    a "Trouble? Nothing I couldn’t handle. You know me, I’m always good at getting out of a tight spot."
    h "{i}Yeah, yeah, Mr. Invincible. You’ve still got that cocky edge, huh? So what the hell happened? You owe me some details.{/i}"
    scene w_757 with dissolve
    a "I’ll tell you when I’m ready. Right now, I’m just trying to keep my head straight."
    a "But let’s talk about you, Henry. You still chasing tail or did you finally settle down?"
    h "{i}*laughing* Oh, come on! You think I’d ever settle?{/i}"
    h "{i}I’m too old for that now, but still not too old to have a good time, you know what I’m saying?{/i}"
    "{i}I shook my head, laughing at the memories of nights spent out drinking, partying, sometimes waking up with no memory of how we even got back to wherever we were staying.{/i}"
    "{i}Henry was always the life of the party, and I was... well, a willing participant most of the time.{/i}"
    scene w_758 with dissolve
    a "Man, I don’t know how we survived some of those nights. Remember that time in Vegas?"
    a "You almost got us banned from the hotel!"
    h "{i}Ha! How could I forget? That bartender... she was trouble, man. Pure trouble. But worth it!{/i}"
    a "She threw a drink in your face. I think that was your own fault, Henry."
    h "{i}Hey, don’t act like you didn’t love every second of it. And what about you, huh?{/i}"
    h "{i}Got any new ladies in your life, or are you still too busy playing it cool?{/i}"
    a "You know me, man. I’ve got my hands full with other stuff right now."
    scene w_759 with dissolve
    h "{i}Uh-huh, sure. Sounds like the same old excuse. But hey, whenever you’re ready to get back into the game, you let me know. I’ll set you up.{/i}"
    "{i}He was laughing, but there was an edge to it. That’s Henry for you—always thinking about the next move, whether it’s a fight, a party, or something else entirely.{/i}"
    h "{i}But seriously, Alex, I’ve been thinking... you ever miss the ring?{/i}"
    a_ "Back to this again? The ring? After everything, does he really think I’d go back?"
    scene w_760 with dissolve
    a "No, Henry. After everything, I needed to step away, you know that."
    scene w_759 with dissolve
    h "{i}You know, Alex, I’ve been working with this kid—well, not exactly a kid anymore, but he’s got raw talent. The kind of fire you had back in the day.{/i}"
    a_ "No way he's calling me for something like that. What’s his angle?"
    scene w_760 with dissolve
    a "Henry, I swear, if you’re about to ask me to train some snot-nosed punk, you better—"
    scene w_759 with dissolve
    h "{i}He’s good, Alex.{/i}"
    h "{i}And I’m not talking about some neighborhood wannabe. This guy could go places, but he needs someone like you. Someone who knows the ropes, someone who’s been to the top.{/i}"
    "{i}He had my attention now, but I wasn’t about to admit it. Not yet.{/i}"
    scene w_760 with dissolve
    a "So what, you want me to babysit some up-and-comer? I’m out of the game, Henry. My last fight was years ago."
    scene w_759 with dissolve
    h "{i}Yeah, and I remember that last fight. But that’s the beauty of it, you’re still a name. Hell, you’re still *the* name to a lot of people.{/i}"
    h "{i}That’s why this would work. Train the kid, get him ready for a few rounds, and—wait for it—you do a little exhibition match for the debut. Light stuff, nothing crazy.{/i}"
    "{i}My heart skipped a beat at the word 'fight'. It had been a long time since I’d been in the ring, and I swore I’d left that behind.{/i}"
    a_ "A fight? No way. Emma’s gonna kill me if she hears about this. And what if I get hurt again?"
    scene w_760 with dissolve
    a "You know damn well I left boxing because of the injury. I'm not risking getting back into the ring."
    scene w_759 with dissolve
    h "{i}Come on, Alex. You and I both know your injury isn’t going to hold you back from a few rounds.{/i}"
    h "{i}You won’t even need to go full throttle—just enough to draw a crowd.{/i}"
    h "{i}And think about the cash. Big numbers, man. This kid’s got potential, and with you in his corner, we’re talking serious money.{/i}"
    "{i}I could hear the grin in his voice, and damn it, he knew exactly which buttons to push.{/i}"
    "{i}The money... It would be good. Hell, it would be better than good.But Emma? She would never let this slide. Training the kid? Sure. But fighting again?{/i}"
    scene w_760 with dissolve
    a "Emma’s gonna eat me alive if she hears about this. You remember how she reacted last time. I don’t think I’ve ever seen her that pissed."
    "{i}Henry laughed, that deep, knowing chuckle of his.{/i}"
    scene w_759 with dissolve
    h "{i}Ah, Emma, always keeping you in check. Look, man, you don’t have to tell her about the fight right away.{/i}"
    h "{i}Just ease her into it. She’ll come around when she sees the payday.{/i}"
    scene w_760 with dissolve
    a "I don’t know, man. Training him? Fine. But getting back in the ring? I’m not so sure."
    scene w_759 with dissolve
    h "{i}Do it for the kid, Alex. He’s got a lot of heart. Reminds me of you, in a way.{/i}"
    h "{i}You’re the only one who can guide him. And you’ll be raking in a solid payday while you’re at it. Trust me on this.{/i}"
    "{i}I could feel myself softening, the familiar pull of the ring and the old life getting stronger.{/i}"
    "{i}The camaraderie, the thrill, the damn *money*. It was all too tempting.{/i}"
    scene w_760 with dissolve
    a "Alright, alright. I’ll think about it. But no promises, Henry. And if this blows up in my face, you’re the one explaining it to Emma, not me."
    h "{i}Deal. I’ll smooth it over if she catches wind before you’re ready.{/i}"
    scene w_761 with dissolve
    "{i}As I hung up the phone, the weight of what I’d just agreed to hit me like a punch to the gut.{/i}"
    "{i}I wasn’t just considering training this kid; I was contemplating stepping back into the ring.{/i}"
    scene w_762 with dissolve
    a_ "What the hell did I just get myself into?"
    "{i}I sighed, staring out at the garden, the flowers swaying in the gentle breeze.{/i}"
    "{i}For now, I’d keep this under wraps. Emma didn’t need to know—not yet.{/i}"
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_327 with fade
    "{i}The rest of the day drifted by in a blur. I couldn't stop thinking about Henry's proposal, even when I tried to focus on anything else.{/i}"
    "{i}The idea of getting back in the ring had stirred something in me, something I thought I'd buried a long time ago.{/i}"
    "{i}As night fell, exhaustion finally hit me. I decided it was time to turn in. Maybe sleep would clear my head.{/i}"
    $ renpy.music.stop("music1", fadeout=2.0)
    scene w_724 with fade
    $ renpy.pause()
    "{i}I woke up in the middle of the night to a familiar but unexpected sensation.{/i}"
    scene w_725 with dissolve
    $ renpy.music.play("audio/adult/man-Mm_1.mp3", channel="sfx1", relative_volume=0.2)
    $ renpy.pause()
    scene w_726 with dissolve
    a "..."
    a "Emma?"
    $ renpy.music.play("audio/musics/sexy_beat.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_727 with dissolve
    "{i}Emma had gently pulled my boxers down, freeing his already hardened cock.{/i}"
    a_ "Emma? What are you doing?"
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    scene w_728 with dissolve
    $ renpy.pause()
    "{i}She didn't answer, instead, she gave me a look. I had never seen her like that.{/i}"
    "{i}A look like she was a wild animal, in heat. Those eyes, they were filled with desire...{/i}"
    scene w_729 with dissolve
    e "Do you want me to stop?"
    a "No,"
    $ renpy.music.play(["audio/adult/blowjob1_1.opus" , "audio/adult/blowjob1_2.opus" , "audio/adult/blowjob1_3.opus"], channel="sfxloop1", fadein=2.0, relative_volume=0.3)
    scene run_emmablowjobalex2 with dissolve
    $ renpy.pause()
    a_ "Oh, fuck, Emma. That feels so good,"
    window hide
    $ renpy.music.play("audio/adult/man-Mm_1.mp3", channel="sfx1", relative_volume=0.2)
    $ renpy.pause()
    "{i}I could feel my cock getting harder.{/i}"
    $ renpy.music.play("audio/adult/emma_moangentl1.opus", channel="sfx1")
    $ renpy.pause()
    "{i}Emma moaned softly, she was really enjoying my cock in her mouth.{/i}"
    $ renpy.pause()
    a "Oh, fuck,"
    "{i}Emma as took him deeper into she mouth, tongue swirling around his shaft.{/i}"
    $ renpy.pause()
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    scene w_732 with dissolve
    $ renpy.pause()
    a_ "Oh, fuck, her mouth feels so good."
    scene w_733 with dissolve
    "{i}My hand found its way to the back of her head, tangling in her hair.{/i}"
    $ renpy.music.play(["audio/adult/blowjob1_1.opus" , "audio/adult/blowjob1_2.opus" , "audio/adult/blowjob1_3.opus"], channel="sfxloop1", fadein=2.0, relative_volume=0.3)
    $ renpy.music.play(["audio/adult/emma_moangentl1.opus" , "audio/adult/emma_moangentl2.opus"], channel="sfxloop2", fadein=2.0, relative_volume=0.3)
    scene run_emmablowjobalex3 with dissolve
    $ renpy.pause()
    $ renpy.music.play("audio/adult/man_moan13.mp3", channel="sfx1")
    "{i}Emma continued to suck him, her pace quickening as she took him deeper and deeper.{/i}"
    "{i}I could feel myself getting closer and closer to the edge, my hips rocking as I thrust deeper into her mouth.{/i}"
    $ renpy.pause()
    a "I'm gonna cum,"
    a_ "I’m gonna cum, Emma. I’m gonna cum so hard,"
    $ renpy.pause()
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.stop("sfxloop2", fadeout=7.0)
    $ renpy.music.play(["audio/adult/man_moan12.mp3" ,  "audio/adult/man_moan13.mp3" , "audio/adult/man-Ugh_1.mp3" , "audio/adult/man-Sigh_1.mp3"], channel="sfx1", fadein=2.0)
    scene w_733
    with Dissolve(0.1)
    scene white
    with Dissolve(0.1)
    scene w_733
    with Dissolve(0.1)
    scene w_733
    with Dissolve(0.2)
    scene white
    with Dissolve(0.2)
    scene w_733
    with Dissolve(0.2)
    scene w_733
    with Dissolve(0.3)
    scene white
    with Dissolve(0.3)
    scene w_733
    with Dissolve(0.3)
    scene w_733
    with Dissolve(0.4)
    scene white
    with Dissolve(0.4)
    scene w_733
    with Dissolve(0.4)
    scene w_733
    with Dissolve(0.5)
    scene white
    with Dissolve(0.5)
    scene w_733
    with Dissolve(0.5)
    $ renpy.pause()
    scene w_733 with dissolve
    a "Fuck, Emma,"
    "{i}She gasped, my fingers tightening in her hair as I reached my peak.{/i}"
    scene w_736 with dissolve
    "{i}She knew I was satisfied, and it was obvious she was too.{/i}"
    "{i}I really don't remember seeing her like this{/i}"
    $ renpy.music.stop("music2", fadeout=2.0)
    scene w_737 with dissolve
    "{i}Emma didn’t stop, instead swallowing every last drop as my orgasm washed over her.{/i}"
    e "Good nigh, Alex,"
    a_ "What the fuck was that? I don't know what's going on... that was really good."
    e "I hope you enjoyed that,"
    a "Yes,"
    a "I can't believe that just happened."
    scene w_738 with dissolve
    e "Believe it,"
    e "I'm always up for some fun."

    jump day4_alex_1
