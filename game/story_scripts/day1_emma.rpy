label day1_emma_1:
    $ emma_mental = 10
    $ emmateasealexday1 = False
    $ emmagetsmadalexday1 = False

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music2", fadein=2.0, relative_volume=0.1)

    show 3rd_day with fade
    $ renpy.pause()
    hide 3rd_day with dissolve
    show screen emma_mental_screen
    e_ "How did we get here?"
    e_ "I never thought my marriage would come to this. We were supposed to be happy, supposed to build a life together..."
    e_ "but now, we’re stuck in this limbo."
    e_ "One year. Just one more year living under the same roof, pretending like we can tolerate each other, just to inherit this damn mansion. It feels so surreal."
    scene w_110 with dissolve
    e_ "I loved him. God, I loved him so much. But it was never enough. No matter what I did, no matter how much I gave, it always felt like he wanted something more, something I couldn’t give."
    e_ "And now, here I am, waking up in the same bed as the man I once thought was my everything, knowing that divorce is the only solution."
    e_ "Even though it’s not what I planned when we got married... it’s the only way out of this cycle of disappointment and heartbreak."
    scene w_111 with dissolve
    "{i}I suddenly felt Alex's arms wrap around my waist. His touch startled me, and before I could react, he pulled me back gently into him.{/i}"
    a "Hey, beautiful. I've missed this. Don’t you miss it too?"
    "{i}The warmth of his body pressed against mine, and I felt my breath catch in my throat.{/i}"
    e_ "Why is he doing this? After everything, why now? It feels... familiar. Safe. And yet, I shouldn’t be feeling this way. We’re supposed to be over. I should push him away... but I don’t. Why can’t I?"
    e_ "Am I still attracted to him? God, of course I am. But it’s more than that, isn’t it? Maybe I just miss what we had. Or maybe it’s him. Do I flirt back?"
    e_ "What would that even mean for us? No, I can’t let this go too far. We’re not in a good place, and I can’t pretend everything’s okay just because he touched me."

    $ emmateasealexday1 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Reject him{/size}{/font}":
            $ emmateasealexday1 = False

            e "Alex, what are you doing?"
            a "Come on, Emma. Just a quick one. I know you’ve missed it too."
            e_ "He’s doing it again. Trying to get close like nothing happened, like all the hurt just vanished. It’s so frustrating."
            e_ "I feel his arms tightening around me, and for a second, I almost forget. Almost. But I can’t. I can’t let him pull me back into this."
            scene w_112 with dissolve
            "{i}I sighed, stepping forward slightly to create distance between us. His warmth faded, replaced by the familiar tension that had been lingering for months.{/i}"
            e_ "Why does he think this is enough? That a touch, a few soft words, can fix everything? After all we’ve been through, after all the lies..."
            e "Alex, no. I’m not in the mood. Especially after everything."
            a "Emma, please. I need this. We need this."
            e_ "He doesn’t get it. He never does. It’s not just about wanting him—it’s about trust, about all the times he let me down."
            e "I can’t just ignore everything. Especially after talking to Isabella."
            a "Isabella? What did she say?"
            e_ "He can’t keep pretending everything’s fine. Not after what Isabella said. God, why do I even bother explaining this to him anymore?"
            e "It doesn’t matter. The point is, I’m not interested, Alex. Just leave me alone."
            a "Fine. I’ll go out, then. Maybe clear my head."
            scene w_113 with dissolve
            $ renpy.pause()
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
            scene w_466 with dissolve
            "{i}As he stepped away, I felt the weight of it all press down on me again.{/i}"
            scene w_467 with dissolve
            "{i}This wasn’t going to be easy, but I couldn’t let him draw me back in. Not this time.{/i}"
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
        "{font=fonts/hatten.ttf} {size=50}Flirt with Alex{/size}{/font}":
            $ emmateasealexday1 = True

            e "Alex, what are you doing?"
            a "Emma, come on. You know we still have something between us."
            scene w_458 with dissolve
            "{i}Alex's eyes were glued to me, and I could feel his desire even before he touched me. My body responded almost instinctively, heat rising in my chest.{/i}"
            "{i}I let my hand fall from my chest, exposing myself fully to him. I saw his breath hitch, and for a second, I felt powerful. It had been so long since I felt this way.{/i}"
            scene w_459 with dissolve
            e "Alex, no. We can’t... not yet."
            a "Emma, come on. You feel it too, don’t you? This… it’s still there between us."
            e_ "He still wants me. After everything we’ve been through, he still looks at me like this. And what’s worse… I still want him too."
            scene w_460 with dissolve
            "{i}Alex stepped closer, his hands reaching for my waist, pulling me into him. His touch was firm, his fingers digging into the soft skin of my hips as he wrapped his arms around me.{/i}"
            "{i}My heart raced as his hands slid lower, grabbing both sides of my ass and pulling me even closer.{/i}"
            e_ "Why does this still feel so good? We’re not supposed to be like this anymore. But damn... I can’t deny the way my body is reacting to him."
            e "I’m not saying we don’t, Alex. But this... this isn’t how we fix things."
            a "Why not? What’s stopping us right now? We both know this is what we want."
            e "It’s not that simple. Wanting you... it’s not enough to make everything okay between us."
            "{i}He groaned softly, clearly frustrated, but he didn’t let go.{/i}"
            scene w_461 with dissolve
            "{i}Instead, he pulled me even closer, his hands now gripping my ass firmly, and I felt my heart race.{/i}"
            scene w_462 with dissolve
            "{i}His lips hovered near mine, and for a second, I almost let it happen.{/i}"
            a "Then let’s stop thinking and just... be in the moment."
            e "We can’t just pretend nothing’s wrong because we still want each other."
            a "Who’s pretending? I know things aren’t perfect, but why can’t we just have this? Right now?"
            scene w_463 with dissolve
            e "Because we’ll still wake up tomorrow with the same problems, Alex."
            e_ "If we do this now, it’ll just complicate things even more. It’ll feel good in the moment, but we’ll still be stuck in the same place afterward."
            a "So what do you want from me, Emma? What do I have to do?"
            "{i}For a moment, neither of us spoke. He stared at me, searching my face for some kind of answer. Then, slowly, he let out a long breath, finally stepping back.{/i}"
            scene w_464 with dissolve
            a "Fine. You’re right... but damn, it’s hard."
            e "I know."
            a "I guess I’ll go clear my head then."
            scene w_113 with dissolve
            "{i}I watched him go, a strange mixture of relief and regret swirling inside me and for a moment, the silence in the room felt heavy..{/i}"
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
            scene w_465 with dissolve
            "{i}A strange sense of satisfaction crept in. He still wanted me. Even after everything, that desire was still there. I’d be lying if I said that didn’t feel good.{/i}"
            e_ "But why does it matter? After all the crap he’s put me through… the cheating, the lies… I should hate him."
            e_ "I should’ve pushed him away harder. But no, here I am, feeling good because he couldn’t keep his hands off me."
            e_ "Why am I even entertaining this? It’s ridiculous. He doesn’t deserve me. He never did."
            e__"Oh, come on. Stop pretending you don’t love the attention. You saw the way he looked at you—like he’d do anything to get back in your pants. And don’t lie, you liked it."
            scene w_466 with dissolve
            e_ "Shut up. This isn’t about attention. It’s about everything he’s done, everything I’ve had to put up with."
            e__ "Yeah, yeah, whatever. But be real—if he weren’t such a mess, you’d be all over him. Admit it."
            "{i}I paused, letting out a breath. I hated when she was right. There was a part of me that still wanted him, that craved the way he made me feel when things were good. But that part didn’t erase the pain, the betrayal.{/i}"
            e_ "That doesn’t change anything. He’s still a liar, and I’m not falling back into that trap."
            e__ "Sure, keep telling yourself that. But the second he flashes that smile or gets all needy… we both know you’ll cave. You always do."
            e_ "Shut. Up."
            scene w_467 with dissolve
            "{i}I shook my head, pulling my hair back as I tried to focus. I wasn’t going to let this inner voice win. Not today.{/i}"
            "{i}Maybe Alex still wanted me, but that didn’t mean I had to want him back. At least, that’s what I kept telling myself.{/i}"
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)

    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    scene w_326 with fade
    "{i}I walked through the hallway toward the entrance of the mansion, my footsteps echoing off the marble floors. The place always felt so empty, so cold. But today, being alone here felt... different.{/i}"
    "{i}As I approached the large wooden doors, I could feel a sense of calm settle over me.{/i}"
    scene w_468 with fade
    "{i}Maybe it was the space, maybe it was just the silence, but for once, I felt like I could think clearly.{/i}"
    "{i}I sat by the fountain, staring blankly at my phone, scrolling without actually paying attention to anything.{/i}"
    e__ "Oh, please. You’re just enjoying the peace because Alex isn’t hovering around. Don’t act like you suddenly love this mansion."
    scene w_469 with dissolve
    e_ "I don’t know. Maybe I do like it here. Or maybe I just like being away from him right now."
    e__ "Yeah, until he flashes that grin of his again. We’ll see how long that ‘peace’ lasts."
    "{i}The quiet of the estate felt calming, but my mind was far from peaceful. My thoughts drifted back to Alex, the tension between us, and the mess we were in.{/i}"
    scene w_470 with dissolve
    e__ "Oh please, like scrolling through your phone will magically fix your life. You need to stop thinking about him, girl. He’s only going to mess you up again."
    e_ "She’s right. Why do I even care? This was supposed to be my time, my space to think clearly. And here I am, still caught up in it."
    "{i}The light sound of footsteps on gravel snapped me out of my thoughts. Before I could turn around, a deep voice cut through the silence.{/i}"
    scene w_471 with dissolve
    "{color=#7ed8ee}??????{/color}" "Excuse me, are you Emma?"
    "{i}I blinked, caught off guard. I looked up from my phone and saw a man standing behind me.{/i}"
    e_ "Who the hell is this guy? And how does he know my name?"
    e__ "Well, hello there, mystery man. Is he a stranger or a stalker? Either way, this just got interesting."
    e "Uh, yeah, that’s me. Do I... know you?"
    v "I'm Victor. I work for Mrs. Isabella. She asked me to come here today."
    e_ "Okay, so not a stalker. But still, why does he know my name? And why do I feel like there’s more to him than just a guy doing his job?"
    scene w_472 with dissolve
    "{i}I watched Victor closely, still unsure what to make of him. He seemed... charming, but in that polished, almost rehearsed way.{/i}"
    "{i}His easy smile and casual demeanor didn't quite sit right with me. I returned his smile, though, keeping up the act.{/i}"
    scene w_473 with dissolve
    v "Isabella speaks of you, you know. Said you were full of spirit."
    e_ "Spirit? That’s one way to put it. Isabella’s first impression wasn’t exactly glowing, but sure, let’s play along."
    scene w_472 with dissolve
    e "Oh really? That’s nice to hear. I didn’t expect her to mention me."
    "{i}I forced another smile, remembering how my first encounter with Isabella had left me more annoyed than anything.{/i}"
    "{i}Something about her screamed arrogance, and I wasn’t in the mood to deal with her attitude. But Victor didn’t need to know that.{/i}"
    e__ "Of course she talks about you. She’s probably sizing you up, competition-style. Don’t trust her for a second."
    e_ "Victor seems fine, but Isabella... yeah, I’m not convinced."
    scene w_473 with dissolve
    v "Yeah, she’s a force to be reckoned with in the modeling world."
    v "I’m her personal stylist, so I get to see that firsthand. Every outfit, every look, it’s a process. She takes it seriously."
    scene w_472 with dissolve
    e "I can tell. She has that... perfectionist vibe."
    e__ "Perfectionist? Try controlling. Bet she’s a nightmare when something’s out of place."
    "{i}I kept my tone light, though my mind was racing with thoughts of how insufferable Isabella must be in private. But Victor seemed genuine enough, and I didn’t want to make waves just yet.{/i}"
    e "So, are you here to see Isabella?"
    scene w_474 with dissolve
    v "Yep. She wanted to go over some looks for an upcoming shoot. I wasn’t supposed to be here today, but she insisted."
    "{i}That sounds about right. Isabella seems like the type to pull people into her orbit, whether they want to be there or not.{/i}"
    e "She has that effect on people, huh?"
    v "You could say that."
    "{i}Though I could tell Victor wasn’t entirely sold on the conversation either. I was playing nice, but my gut told me to keep an eye on both of them.{/i}"
    scene w_475 with dissolve
    e "I'll take you to her room."
    v "You lead the way. You know the mansion better than I do."
    scene w_476 with dissolve
    e_ "Stylish, charming… a bit too charming, maybe,"
    e "So, you work with Isabella a lot, huh?"
    "{i}Victor chuckled, his smile widening as he looked at her.{/i}"
    v "Oh, yes. She's quite the perfectionist, but that's what makes her so good at what she does. Always pushing boundaries, always demanding the best."
    scene w_477 with dissolve
    $ renpy.music.stop("ambient1", fadeout=2.0)
    e_ "Perfectionist? Yeah right, she’s more like an ice queen playing everyone around her."
    e_ "And what’s with this guy? Does he really think I didn’t catch that little smirk?"
    "{i}Emma felt her stirring, that voice inside her head ready to snap back, but she held it in. Instead, she played it cool.{/i}"
    e "Sounds like she's a handful. I didn’t exactly get the warmest reception from her."
    v "She can be intense, but trust me, when you’re in her circle, she’s loyal. Maybe she’s just feeling you out."
    scene w_478 with dissolve
    "{i}As they approached the grand staircase, Victor slowed down, glancing at the decor, seemingly admiring the place. Emma noticed how his gaze lingered a bit too long on certain details.{/i}"
    e_ "Victor, you’re definitely hiding something. What exactly are you playing at?"
    e__ "You should ask him something that catches him off guard. Test his loyalty to his 'queen'."
    e_ "Stay cool,"
    e "So, you’re here to see Isabella? Busy with another photoshoot?"
    v "You could say that. Isabella likes to keep things under wraps until the last moment, but we’re planning something big. Should be a spectacle."
    scene w_479 with dissolve
    e "Here we are."
    $ renpy.music.play("audio/sfx/sfx_knock.ogg", channel="sfx1", relative_volume=1.0)
    v "Thanks. It’s always a maze in here."
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    scene w_480 with dissolve
    $ renpy.pause()
    scene w_481 with dissolve
    isa "Victor, darling... You're finally here."
    "{i}Her voice had that smoothness, but the edges... they were razor-sharp. Her eyes shifted between me and him, calculating, but I kept my cool.{/i}"
    v "Hey, Izzy."
    e_ "God, Isabella's confidence... dripping with a kind of power, no wonder she has all the guys wrapped around her finger,"
    "{i}He greeted her casually, but I noticed the way his voice softened just for her. Subtle. But it was there.{/i}"
    scene w_482 with dissolve
    isa "Come in,"
    "{i}She stepped back, letting Victor in. She glanced at me briefly before pulling the door wider.{/i}"
    scene w_483 with dissolve
    isa "Thanks for bringing him up, Emma,"
    "{i}Isabella's tone was flat, almost dismissive. Like I was the help or something.{/i}"
    e "Of course, Isabella."
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    scene w_484 with dissolve
    e_ "God, what a snake. Perfect match, those two."
    e_ "Guess I'm the only one playing fair in this twisted little game, huh?"
    e__ "But honestly? Where's the fun in that..."
    scene w_326 with fade
    "{i}I step outside into the garden, the air cooler now as the sun dips lower. The grass crunches softly under my feet as I wander toward the fountain.{/i}"
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    scene w_497 with fade
    e_ "It’s quiet out here, peaceful almost, but I can never really enjoy peace, can I?"
    e__ "You don’t deserve peace. Not yet."
    scene w_498 with dissolve
    "{i}I close my eyes, letting the breeze brush against my skin, trying to let the calm wash over me.{/i}"
    "{i}But it doesn’t stick. My thoughts swirl—Victor, Isabella, this ridiculous mansion and its web of lies.{/i}"
    scene w_499 with dissolve
    "{i}But then there’s the other part of me. The one that isn’t content just to watch. The one that wants to burn it all down and see what happens.{/i}"
    e_ "Maybe that’s what this place needs,"
    "{i}I whisper to myself, almost hoping someone will hear, but knowing they won’t.{/i}"
    e__ "Chaos. Fire. Let’s see how long they can keep their masks on when everything falls apart."
    e_ "There’s something about this garden, though. It’s too perfect, too ordered."
    scene w_500 with dissolve
    e_ "Like the rest of the house. Every blade of grass cut just right, every flower arranged in perfect harmony. It almost makes me sick."
    e_ "Like I don’t belong in this perfect world."
    scene w_501 with dissolve
    e_ "Why am I even here? Surrounded by all this fake tranquility,"
    e__ "You’re pretending, you know. Just like the rest of them. Look at this place—it’s too perfect. Too clean. How long until it cracks? How long until *you* crack?"
    e "All of this, it’s just a pretty mask,"
    "{i}I whispered.{/i}"
    e__ "A mask, yeah. Like yours. Keep smiling, darling, they can’t see what's underneath."
    "{i}I was still wrapped in my thoughts when I felt something unexpected.{/i}"
    $ renpy.music.stop("music2", fadeout=2.0)
    scene w_502 with dissolve    
    "{i}A hand—firm, confident—landed on my shoulder, sending a jolt through my body.{/i}"
    "{i}For a split second, I froze, the calm of the garden shattered.{/i}"
    $ renpy.music.play("audio/musics/villain-entry.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_503 with dissolve
    e_ "Damn. How did he manage to get so close without me noticing? I really should be more aware of my surroundings."
    d "All of this... just a beautiful mask, Emma?"
    "{i}His voice dripped with intrigue, almost playful. But I could sense the curiosity beneath it.{/i}"
    e_ "Oh, crap. He must have heard me muttering to myself."
    "{i}I could barely remember what I’d said—something bitter, likely—but now, faced with that question, I needed to play it cool. Don't flinch, Emma.{/i}"
    e "Oh... you know me, Daniel. Always thinking out loud. A mask? Maybe... or maybe it's just who I am today."
    d "Ah, but masks are so interesting, don’t you think? They can hide so much... or maybe reveal more than we expect."
    "{i}I felt his hand tighten slightly on my shoulder, a gesture meant to appear casual, but it held a certain... weight.{/i}"
    scene w_496 with dissolve
    "{i}I could sense him trying to reel me in, and I wasn't sure if I liked where this was going. The garden, once my little retreat from everything, suddenly felt too small.{/i}"
    e "Depends on who's wearing it, I guess."
    scene w_494 with dissolve
    d "You know, this place... it always reminds me of the old days with Alex. Back when we were... less complicated."
    d "There was this one time, years ago—before the parties, before the masks. We were out at the lake, Alex dared me to swim across in the middle of the night."
    d "I was drunk, of course, and you know how competitive I get. Well, I got about halfway and realized..."
    d "I couldn’t swim."
    scene w_493 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    "{i}I couldn’t help but laugh, imagining Daniel in that situation, drunk and flailing in the water.{/i}"
    "{i}I knew exactly what he was doing, using this story to pull me in, to remind me of my history with Alex, but also to mock him, to point out his failures.{/i}"
    e "Sounds like Alex got the best of you back then."
    "{i}I smiled, but it was tight, forced.{/i}"
    e__ "Why the hell is he bringing up Alex now? Does he think I’ll laugh along while he tries to humiliate him?"
    scene w_494 with dissolve
    d "Oh, he did... but I had my revenge, believe me. And anyway, we all grow, don't we? Some of us faster than others."
    "{i}I wanted to slap that smug grin right off his face, but instead, I kept playing the game, letting him think he was in control.{/i}"
    scene w_496 with dissolve
    e "Guess you never know where life will take you... or who you’ll leave behind."
    "{i}Daniel laughed, but I could sense the undercurrent of his words. He was toying with me, testing how far he could push. And as much as I hated it, I was letting him.{/i}"
    e_ "Damn it, why did this have to happen now?"
    e__ "Focus, Emma, you can't let him see through you."
    "{i}I could feel the subtle tension, the quiet manipulation hidden behind his words. But before I could say anything, I noticed movement behind him{/i}"
    scene w_495 with dissolve
    "{i}Alex.{/i}"
    e_ "Oh, hell."
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/filaments1.mp3", "music1", fadein=2.0, relative_volume=0.1)
    "{i}He stormed toward us, his eyes zeroing in on Daniel like a predator closing in on its prey.{/i}"
    e_ "Really, Alex? Now?"
    scene w_143 with dissolve
    a "What the hell is this?"
    a "What the hell do you think you’re doing, Daniel? Trying to make me look like an idiot in front of my wife?"
    "{i}He didn’t even give me a chance to explain; he just assumed the worst.{/i}"
    scene w_145 with dissolve
    d "Oh come on, Alex. It’s just a funny story. We all had a good laugh back then."
    e "Alex, it was just a story. No need to get so worked up."
    scene w_143 with dissolve
    a "You’re trying to undermine me, Daniel. You’ve always been like this, trying to one-up me, trying to make me look bad."
    e_ "Oh, for God’s sake, Alex. This isn’t the time for this alpha male crap!"
    "{i}I wanted to roll my eyes, but instead, I felt this wave of irritation and something deeper, more raw, more personal.{/i}"
    e_ "Why didn’t he trust me? Why was his first instinct always to assume the worst? "
    scene w_145 with dissolve
    d "Alex, you’re overreacting. It’s just a bit of fun. Lighten up."
    e "Alex, please. It’s not that serious."
    scene w_144 with dissolve
    a "Not that serious? You’re here laughing with him, letting him make a fool out of me! How do you think that makes me feel?"
    e_ "Does he even hear me? Or is he so blinded by jealousy that he can’t see the truth?"
    scene w_143 with dissolve
    a "Stay away from my wife, Daniel. I know what you’re trying to do, and I won’t let it happen."
    d "Feeling a bit left out, Alex?"
    a "Don’t try to act innocent, Daniel. I know exactly what you’re trying to do."
    scene w_145 with dissolve
    d "Really, Alex? All this because of a harmless story? You’re more insecure than I thought."
    d "Maybe if you weren’t so easy to rile up, it wouldn’t be so much fun. You see, Alex, the problem isn’t me—it’s you."
    d "You’re too hot-headed, too jealous. That’s why Emma is laughing with me and not you."
    a "You think you’re so clever, don’t you? You think you can just waltz in here and turn my wife against me?"
    scene w_146 with dissolve
    d "If you can’t keep her happy, maybe you should look at yourself instead of blaming others."
    d "Anyway, I think I’ve had enough entertainment for one day. Enjoy the rest of your evening, Alex. Emma."
    scene w_147 with dissolve
    "{i}The truth being that I was on his side, always had been. But he never gave me the chance to prove it.{/i}"
    "{i}And that stung in ways I didn’t even want to admit.{/i}"
    e "Why, Alex? Why do you always have to do this?"
    a "Do what, Emma? Defend myself against that smug bastard?"
    e "No, Alex. Ruin every single moment with your jealousy and temper. This is exactly why we’re in this situation."
    a "He was making fun of me, Emma. Right in front of you. What was I supposed to do? Just stand there and take it?"
    scene w_148 with dissolve
    e "Maybe not make a scene for once. Maybe trust me enough to handle a conversation without you barging in and making it worse."
    scene w_147 with dissolve
    a "You don’t understand, Emma. He’s always been like this, always trying to make me look bad. It’s not just about you."
    e "And it’s always the same excuse. Blame Daniel, blame anyone but yourself. When are you going to take responsibility for your actions?"
    a "What do you want from me, Emma? To just let him walk all over me?"
    e_ "What I want from you!!! That you trust me and love me as your partner. Your..."
    e__ "No. You want something else from him. Admit it."
    e_ "Shut up!"
    scene w_148 with dissolve
    e "I want you to realize that your jealousy and anger are destroying us. They’ve already done so much damage, and you’re not even sorry."
    scene w_147 with dissolve
    "{i}I didn't want to tell Alex that. In fact, deep down I didn't want to admit it. But maybe I should just face reality.{/i}"
    e "We’re just pretending to be married, Alex. Don’t forget that. We’re already separated, and after this year, it will be official."
    a "Fine. Whatever you say."
    scene black with fade
    e_ "A whole year here... It’s going to be a lot harder than I thought."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_326 with fade
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music2", fadein=2.0, relative_volume=0.1)
    "{i}As the morning sun poured over the mansion, I found myself wandering aimlessly, pretending to take in the scenery but really just letting my thoughts race.{/i}"
    "{i}I wasn’t sure what I was expecting when I agreed to this arrangement, but there was something unsettling about how quickly it was becoming my reality.{/i}"
    "{i}By the time lunch rolled around, I made my way to the dining room, trying to push my thoughts aside.{/i}"
    scene w_149 with fade
    "{i}The dining room felt thick with tension as I sat at the table, trying to focus on anything but Alex.{/i}"
    "{i}Daniel, as usual, sat on the other side of the table, looking bored or maybe just lost in whatever was happening on his phone.{/i}"
    "{i}His constant seriousness was exhausting, like he was carrying the weight of the world, but it didn’t seem like something I could—or wanted to—understand.{/i}"
    e_ "What’s his deal, anyway? Always so brooding..."
    "{i}But I ignored it. I had my own mess to deal with.{/i}"
    d "Isabella, have you decided on the plans for tomorrow?"
    isa "Hmm? Oh, I suppose I should look into that. I've been so busy with... other things."
    e "..."
    "{i}Alex voice came from the other side of the table, soft, but it held that edge, like he was trying too hard to be civil.{/i}"
    a "So, Emma, how's the new painting coming along?"
    e_ "Oh God, here He comes, pretending nothing happened."
    "{i}I respond to Alex with a cold and disinterested tone.{/i}"
    e "It's fine, Alex. Just fine."
    a "I see. Well, if you need anything, just let me know."
    e "I doubt I will, but thanks."
    e_ "Ridiculous. He’s the one who brought us here, and now he’s acting like I’m the problem?"
    scene w_150 with dissolve
    "{i}I didn't even look up from my plate. What was the point? He could apologize a hundred times, and I'd still be sitting here, feeling like he didn’t trust me.{/i}"
    "{i}Ruby came around with the food, serving everyone. I muttered a quick thanks, though I wasn’t particularly hungry.{/i}"
    r "Excuse me, Miss Emma. Here’s your lunch."
    e "Thank you, Ruby. The food looks great."
    "{i}Daniel was already starting in, his voice a bit too cheerful for my liking.{/i}"
    "{i}He always had this way of pushing the mood in whatever direction he wanted, and today, he was clearly enjoying making things worse.{/i}"
    d "So, Alex, how was your day? Managed to get settled in alright?"
    a "Yeah, it's been... interesting. Still trying to get used to everything around here."
    d "I'm sure you'll get the hang of it. It's a big place, but you'll find your way."
    "{i}His tone was almost mocking. I glanced at Daniel, his eyes flicking between me and Alex. He was playing some kind of game, but I wasn’t in the mood for it.{/i}"
    d "Emma, you should show Alex around more. He's our new guest after all. It'd be nice for him to get to know everyone properly."
    "{i}That was enough to snap me out of my thoughts. My grip tightened on my fork as I shot him a look. He knew exactly what he was doing.{/i}"
    e "I think Alex can manage on his own."
    scene w_151 with dissolve
    "{i}The words came out colder than I intended, but I didn’t care. I wasn’t about to play along with whatever game Daniel was trying to pull.{/i}"
    "{i}Alex stayed quiet for a moment, but I could feel his eyes on me, waiting for some kind of reaction. I wasn’t going to give him the satisfaction.{/i}"
    d "Well, it's important to make everyone feel welcome, don't you think?"
    a "Of course. I'm sure I'll figure things out."
    "{i}I could hear the tension in Alex’s voice, but Daniel didn’t back down. He never did. It was like he thrived on stirring the pot, making things just uncomfortable enough to get under everyone’s skin.{/i}"
    d "You know, Alex, Emma is quite knowledgeable about the estate. She could be a great help to you if she wanted to be."
    "{i}I almost laughed. \"If I wanted to be.\" As if this whole situation wasn’t forced enough. I didn’t need Daniel’s meddling.{/i}"
    "{i}I shot him a glare, but before I could say anything, Isabella finally decided to contribute to the conversation.{/i}"
    isa "Alex, didn't you use to be a boxer? I remember seeing some impressive matches of yours."
    "{i}Her sudden interest felt misplaced, but maybe that was her way of deflecting the tension. Or maybe, she just enjoyed the attention. I glanced at her, wondering where this was coming from.{/i}"
    a "Yeah, that was a while ago."
    isa "You were really something. Strong, determined... quite interesting."
    "{i}Her eyes lingered on him longer than I liked, and I shifted in my seat, suddenly feeling a strange wave of annoyance.{/i}"
    "{i}Maybe it was the way Alex responded, or maybe it was Isabella’s flirty tone, but something about this conversation felt... off.{/i}"
    e_ "I swear, if she's trying to get under my skin too, I'll lose it."
    "{i}I kept my expression neutral, focusing on my plate, but inside, everything was swirling—frustration with Alex, irritation at Daniel, and now, Isabella.{/i}"
    e_ "Why does he have to make everything harder? It’s like he enjoys stirring up trouble. Typical Daniel. He can never just let things be."
    "{i}Alex’s voice pulled me back to reality. He was talking about his boxing days, that familiar pride creeping into his tone. I kept my eyes on my plate, uninterested. Or at least, I pretended to be.{/i}"
    a "So, there I was, trying to cut weight while also keeping my strength up. It was a nightmare."
    isa "That must have been tough. How did you manage it?"
    "{i}Of course, Isabella jumped in, her tone overly interested. She always had a way of sliding into conversations that didn’t concern her, especially when it involved Alex.{/i}"
    "{i}I glanced up briefly to see her leaning in, her gaze fixed on him with that look—the one she used when she was playing at being flirty.{/i}"
    e_ "She thinks she’s subtle, doesn’t she? It’s pathetic, really."
    r "Excuse me, Mr. Alex. Here’s your dinner."
    "{i}Ruby voice was polite, as always, though I could sense the discomfort in her posture, especially when she approached Daniel.{/i}"
    a "Thanks for the food, Ruby."
    "{i}I didn't miss the way Alex’s eyes drifted, but I chose to ignore it. Men would be men, right? Besides, Ruby had this presence—almost too warm, too inviting for her own good.{/i}"
    "{i}As she moved to serve Daniel, I knew what was coming before the words even left his mouth.{/i}"
    scene w_154 with dissolve
    d "Thank you, Ruby. You know, I’ve always wondered how someone like you ended up working here. Did you just get lost on your way to a real job?"
    "{i}Ruby stiffened slightly, though she tried to brush it off. Her face was a mask of professionalism, but I could see the cracks.{/i}"
    r "I enjoy my work here, Mr. Daniel. It’s a good job, and I’m proud of what I do."
    d "Proud, huh? Proud of cleaning up after us and cooking our meals? Sounds like you're aiming real high, Ruby."
    e_ "He’s such a bastard. He gets off on this—on making people feel small."
    "{i}I stayed quiet, my gaze flicking briefly to Alex. He seemed engrossed in his meal, though I knew he was aware of what was happening.{/i}"
    d "Maybe you should aim a bit higher. Oh, wait, I forgot – aiming higher might be a bit too much for you."
    "{i}Ruby’s face hardened, her jaw clenched as she fought to keep her composure.{/i}"
    d "Come on, Ruby, don’t be shy. Tell us more about your lofty ambitions. Or is this it? Is this the peak of your career?"
    e_ "I should say something. I should stop him. But... what’s the point? He’s not going to change. He never does."
    e_ "Is this how it’s going to be? Every meal, every moment, just filled with awkwardness and unspoken words? How long can I keep pretending?"
    d "Ah, Ruby. Always so careful, aren’t you? Wouldn’t want to spill anything on that lovely blouse of yours."
    r "I’m sorry, Mr. Daniel. I’ll be careful."
    d "You always are. It’s a wonder you manage to keep this place running."
    e_ "Isn’t anyone going to say something? Should I? Would it even matter?"
    isa "Yes, Ruby. Maybe you should get some clothes that fit better. You know, something a little more... appropriate."
    "{i}Her voice was soft, but the malice behind her words was unmistakable.{/i}"
    scene w_156 with dissolve
    "{i}Ruby’s hands clenched into fists for a brief moment before she quickly composed herself and stepped away from the table, her back rigid as she hurried out of the room.{/i}"
    "{i}I caught a glimpse of the tears welling in her eyes as she left, and something inside me twisted painfully.{/i}"
    scene w_162 with dissolve
    e_ "I should have said something. I should have stopped them. But what good would it do? They’d just turn it on me. Daniel’s always watching, waiting for me to slip."
    "{i}The silence that followed was suffocating, the only sound the clink of utensils against plates. Daniel leaned back in his chair, that infuriating smirk still plastered across his face.{/i}"
    d "Relax, everyone. It’s all in good fun. Just a little joke, right?"
    "{i}No one responded. The only movement came from Isabella, still scrolling through her phone as if the whole thing had been nothing more than mild entertainment.{/i}"
    "{i}I picked at my food, trying to ignore the knot of guilt tightening in my stomach. Daniel’s laughter echoed through the room, loud and grating, a constant reminder of my own silence.{/i}"
    e_ "How long can this go on? How much longer can I sit here and pretend like none of this matters?"
    scene w_485 with dissolve
    "{i}The clinking of silverware against the plates filled the dining room as we sat in an awkward silence. I took a sip of wine, letting the rich taste linger on my tongue.{/i}"
    scene w_489 with dissolve
    isa "Emma, you’ve been awfully quiet today. Is everything alright?"
    "{i}Her voice was smooth, almost too casual, but I knew her well enough to hear the undertone. She always had a way of masking her real intent behind polite conversation.{/i}"
    scene w_486 with dissolve
    e "I’m fine, just enjoying the meal."
    scene w_490 with dissolve
    isa "Really? You don’t seem fine. You seem... distracted."
    e_ "Typical Isabella... always fishing for something."
    scene w_485 with dissolve
    e_ "If she’s looking for a reaction, she’s not going to get it. Not today."
    scene w_487 with dissolve
    e "There’s a lot on my mind, that’s all. Nothing worth discussing over lunch."
    scene w_490 with dissolve
    "{i}I offered a small smile, hoping to deflect. But Isabella wasn’t the type to drop things easily, especially when she smelled blood in the water.{/i}"
    scene w_489 with dissolve
    isa "Oh, come on. We’re all friends here. You can talk to me."
    scene w_486 with dissolve
    e_ "Friends? More like rivals in this little game of manipulation."
    scene w_487 with dissolve
    e "Really, it’s nothing. Just the usual... life, work, stress."
    scene w_489 with dissolve
    isa "Well, if you ever need to talk, you know where to find me."
    scene w_490 with dissolve
    e_ "God, I hate these little power plays."
    scene w_489 with dissolve
    isa "By the way, Emma, I’ve been meaning to ask... have you made any plans for the weekend?"
    isa "We could go into the city, do some shopping, maybe grab drinks?"
    scene w_485 with dissolve
    "{i}Her voice was light, as if she was offering a genuine invitation.{/i}"
    scene w_486 with dissolve
    e "I’ll have to check my schedule, but I’ll let you know."
    e_ "Shopping with Isabella? No, thank you."
    scene w_488 with dissolve
    isa "You always say that, Emma. One day, you’ll run out of excuses."
    scene w_485 with dissolve
    e_ "You’ll get nothing from me, Isabella. Not this time."
    e__ "Why does she always do this? It's like she gets off on making people uncomfortable..."
    e__ "Maybe she's more desperate for control than she lets on."
    scene w_162 with dissolve
    "{i}The room fell into another uneasy silence, and I could feel Isabella’s eyes on me still, waiting for another opportunity to strike.{/i}"
    "{i}I took another sip of wine, letting the moment pass. She could try all she wanted, but I wasn’t going to break. Not now, and certainly not in front of them.{/i}"
    scene w_164 with fade
    "{i}After lunch, I needed to escape the suffocating tension. I grabbed my things and headed to the garden, my sanctuary.{/i}"
    scene w_326 with fade
    "{i}The sun was starting to dip, casting a warm glow over the manicured hedges and vibrant flowers.{/i}"
    "{i}This place, at least, was peaceful, far from the passive-aggressive remarks and the constant underlying tension at the table. I didn’t need their drama right now. What I needed was to finish my painting.{/i}"
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    scene w_491 with fade
    "{i}I had been working on it for weeks, but something about it felt incomplete—like I hadn’t yet fully unlocked the image in my mind.{/i}"
    e_ "Finally, some peace. No Daniel, no Isabella, no Alex trying to figure out how I feel... just me and my canvas."
    e_ "This is what I need—a little bit of control, a place where everything flows the way I want it to."
    "{i}The warm sun kissed my skin as I stood in front of the canvas. The air was still, with only the occasional breeze rustling the leaves behind me.{/i}"
    "{i}My eyes traced the figure I had painted—{/i}"
    scene w_492 with dissolve
    "{i}her hair wild, as if she’d been struck by lightning, frozen in a moment of chaos.{/i}"
    "{i}Below her waist, though, she wasn’t human anymore. Thick, twisting tentacles sprawled from her body like some nightmarish creature from the deep.{/i}"
    e_ "What the hell is this supposed to be? A part of me? She’s a mess, just like me. Fierce, but twisted..."
    e_ "The tentacles—are they my insecurities? My fears, pulling me down into my own darkness?"
    e_ "Am I really that messed up inside? Or maybe it’s not about me at all. Maybe it's just..."
    e_ "my imagination running wild. No, it has to mean something deeper. It always does."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_441 with fade
    "{i}She was beautiful, yet grotesque. I couldn't look away. This was me, somehow, in some dark, twisted form that only my subconscious could conjure.{/i}"
    "{i}But why? Why was this woman so haunting, yet so familiar?{/i}"
    scene w_442 with fade
    "{i}The more I stared, the more the woman seemed to come alive, her eyes reflecting my own inner turmoil. Her tentacles curled as if they were preparing to strike, ready to drag me under.{/i}"
    "{i}I let out a slow breath, feeling the weight of the painting press down on me. Maybe I didn’t want to understand it. Maybe it was better that way.{/i}"
    scene w_445 with fade
    "{i}I stepped back after hanging the painting on my wall, tilting my head slightly as I examined it.{/i}"
    "{i}The stark contrast of the black and white, the wild hair, and the tentacles—it all felt surreal, yet oddly personal.{/i}"
    scene w_444 with dissolve
    e "Why does this feel like me? Am I turning into some kind of sea monster?"
    scene w_443 with dissolve
    e_ "Or maybe I've always been one... hiding in plain sight."
    "{i}I ran my fingers through my hair, mimicking the chaotic energy of the figure's own curls.{/i}"
    "{i}The painting captured something raw, something that had been brewing inside me for a while. There was power in it, an unapologetic chaos.{/i}"
    scene w_446 with dissolve
    e_ "Am I afraid of what's inside me? Or am I just tired of pretending? Maybe I'm both—"
    e_ "human on top, something darker beneath the surface. Hell, who isn't?"
    "{i}I smirked, crossing my arms and studying the figure's gaze, almost challenging me from the canvas.{/i}"
    scene w_447 with dissolve
    "{i}As if she were daring me to embrace what lay beneath, the tentacles of my thoughts and desires, twisting and reaching for more. More freedom, more power. More... control.{/i}"
    e_ "Yeah, maybe it's time to stop hiding. Maybe the monster's not such a bad thing after all."
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    scene w_448 with dissolve
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    e_ "What the hell does it mean, though? Am I losing it, or is this who I’ve always been under the surface—wild, untamed... monstrous?"
    $ renpy.pause()
    scene w_449 with dissolve
    "{i}I barely noticed when Alex entered the room. He came up behind me, silent as a shadow, his eyes fixated on the painting.{/i}"
    "{i}I could feel his presence—close but not too close—just hovering there, waiting. For what?{/i}"
    scene w_450 with dissolve
    e "Are you going to just stand there, or do you actually have something to say?"
    scene w_449 with dissolve
    "{i}I didn’t bother turning around. I could already imagine his face—confused, maybe amused, probably both.{/i}"
    "{i}The kind of expression you’d expect from someone who thought art was just random colors splashed on canvas.{/i}"
    "{i}I waited for him to respond, keeping my eyes on the woman with tentacles that stared back at me from the canvas.{/i}"
    scene w_451 with dissolve
    a "Uh... yeah, I mean... what even is this? Is it, like, a lady-octopus thing? I don't get it."
    "{i}There it was. Exactly what I expected. A small, sarcastic chuckle slipped out before I could stop it.{/i}"
    scene w_453 with dissolve
    e_ "Seriously? That’s all he’s got? Wow, Alex, such deep analysis. You should teach art history."
    scene w_450 with dissolve
    e "A lady-octopus thing. That’s your brilliant observation?"
    scene w_451 with dissolve
    a "I mean... yeah, it’s weird, right?"
    a "She’s got this crazy hair, and then—bam—tentacles? Like, what's she supposed to be? Some kind of sea witch?"
    e_ "He really doesn’t get it. Not that I expected him to, but still... Does he think this is a joke? Does he think *I’m* a joke?"
    scene w_452 with dissolve
    e "It’s more than just a 'sea witch,' Alex. It’s about... I don’t know, duality. Chaos. Control. Maybe even power."
    a "Power?"
    a "Uh, sure, if you say so. But, come on, you can’t deny it looks kinda... offbeat. Like something out of a creepy comic book."
    "{i}I stared at him for a moment, biting back the sharp retort that was ready to launch.{/i}"

    $ emmagetsmadalexday1 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Get mad at Alex{/size}{/font}":
            $ emmagetsmadalexday1 = True

            e_ "Offbeat? Creepy comic book? He has no idea... but maybe that’s the point."
            "{i}As Alex’s idiotic comments hung in the air, I felt a wave of irritation building up inside me. He couldn’t even pretend to get it, could he?{/i}"
            e_ "Why do I even bother? He’s so dense, he probably thinks this whole thing is a joke. God, I can’t stand this right now."
            scene w_454 with dissolve
            "{i}I turned on my heel, walking toward the door without so much as a glance back. I could hear him fumbling, trying to follow, but I was done. I raised my hand, ready to smack the door open.{/i}"
            e "You know what, Alex? If you can’t handle something deeper than a comic book, maybe you should stick to the shallow end of the pool."
            $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
            $ emma_mental = EmmaMentalRemove()
            scene black with dissolve
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
            "{i}I yanked the door open and stormed out, not waiting for a response. Let him stew in his cluelessness. Maybe then he’d realize that sometimes, it’s better to just shut up.{/i}"
            e_ "I swear, if he follows me... I’ll lose it."
        "{font=fonts/hatten.ttf} {size=50}Explain to Alex{/size}{/font}":
            $ emmagetsmadalexday1 = False

            "{i}I took a deep breath, letting the tension drain from my shoulders. Alex stood there, still looking at me with that confused, slightly amused expression. He didn’t get it—how could he?{/i}"
            "{i}Art wasn’t his thing, and expecting him to understand this painting was like expecting a cat to enjoy swimming. But if I kept holding onto this anger, I’d just look like I was overreacting.{/i}"
            e_ "Alright, Emma, just lay it out. He’s clueless, not mean. Well, mostly not mean…"
            scene w_455 with dissolve
            e "Look, Alex, this isn't just some random thing I pulled out of my head. The woman... the tentacles... it’s a part of me, in a way."
            "{i}I could see him trying to follow, his brows furrowed just enough to show he was at least attempting to understand. Or maybe he was just confused. Either way, I needed to spell it out clearly.{/i}"
            e_ "He’s trying. Don’t bite his head off... yet."
            scene w_456 with dissolve
            a "Yeah, I mean... it’s cool. Kinda like one of those... what do you call them? Comic book monsters?"
            "{i}His attempt at relating was... painful, but at least he wasn't mocking it anymore. I felt my irritation slip away, replaced by a reluctant sense of amusement.{/i}"
            "{i}He was hopeless when it came to art, but at least he was making an effort. Maybe that counted for something.{/i}"
            scene w_455 with dissolve
            e "Not a comic book monster, Alex. More like... a reflection of something deeper. The woman is me. And the tentacles..."
            e "well, that's all the stuff I feel tangled in sometimes. Life, expectations, everything."
            "{i}There. I said it, and it felt surprisingly good to let it out. Even if he wouldn’t grasp the full weight of it, I felt lighter.{/i}"
            "{i}Alex nodded slowly, his lips twitching as if he wanted to say something but wasn’t sure how. Finally, he just gave me a shrug and a lazy smile.{/i}"
            scene w_456 with dissolve
            a "Well... if you say so. I guess it’s better than what I thought it was. I'll leave you to it then."
            scene w_457 with dissolve
            "{i}With that, he turned and walked out of the room, leaving me standing in front of the painting.{/i}"
            "{i}I stared at it a bit longer, the lines and shapes suddenly seeming even more personal now that I’d voiced what they meant. It was still unfinished, but at least now I knew I wasn’t.{/i}"
            $ emma_mental = EmmaMentalAdd()

    scene w_326 with fade
    "{i}The day was winding down, finally. After all that back and forth with Alex and the whole painting debacle, I felt drained. I wandered through the house, letting the last remnants of sunlight fade into the evening.{/i}"
    e_ "At least here, I can breathe. No comments, no confusion. Just me and my thoughts."
    "{i}I changed into something more comfortable and climbed under the covers. The weight of the day started to slip away, though the image of the woman with tentacles still danced in my mind.{/i}"
    scene w_326 with dissolve
    e_ "Goodnight, world. You can deal with me tomorrow."

    jump day2_emma_1
