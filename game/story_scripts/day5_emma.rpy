label day5_emma_1:

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 7rd_day with fade
    $ renpy.pause()
    hide 7rd_day with dissolve

    scene w_326 with fade
    "{i}A new day dawned, and I found myself lying awake, my thoughts drifting back to Eleanor's invitation. Dinner with her, her husband, and… Alex.{/i}"
    "{i}Part of me couldn’t shake the discomfort—it wasn’t just a casual gathering. Eleanor’s keen, almost piercing, curiosity about Alex lingered in my mind.{/i}"
    "{i}What exactly was she hoping to see? To understand? I pushed the thought aside, taking a deep breath as I rose from bed. Determined to face the day, I decided to get dressed and step out.{/i}"
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    scene w_870 with fade
    "{i}Maybe a change of scenery would help me sort through the tangled feelings I wasn’t ready to admit.{/i}"
    "{i}As I made my way down the hallway, my thoughts still circled back to that dinner invitation. Part of me was trying to convince myself it was just a harmless evening.{/i}"
    "{i}But the closer it got, the more uneasy I felt. Eleanor’s interest in Alex… what was she really after?{/i}"
    scene w_871 with dissolve
    e_ "Daniel... he looks extraordinarily focused, his expression serious in a way that..."
    e_ "He seems to be studying something intently, and what's with that frown etched on his face?"
    scene w_872 with dissolve
    "{i}After a moment, he looks up, catching sight of me, but his serious gaze doesn't fade.{/i}"
    o "Oh, look at him. You can almost feel the tension rolling off him, can't you? Go on, give those tentacles of yours a little shake. See what happens."
    e_ "Not interested, Octavia,"
    "{i}I grit my teeth, mentally pushing Octavia aside. I’m not about to give in to her games today.{/i}"
    scene w_874 with dissolve
    e "Didn’t expect to find you looking so… intense this early. Something on your mind, Daniel?"
    scene w_873 with dissolve
    d "It’s just… things around here have been unpredictable lately. I don’t like unpredictable."
    scene w_874 with dissolve
    e "Unpredictable? I thought you enjoyed a bit of chaos."
    scene w_873 with dissolve
    d "Controlled chaos, maybe. But whatever happened with Alex, it… complicates things. Don’t you feel it?"
    scene w_874 with dissolve
    e "I feel… tension, yes."
    scene w_873 with dissolve
    d "People think they’re safe here, but no one ever considers what might be lurking just under the surface."
    scene w_874 with dissolve
    e "Are we still talking about security… or is this one of your philosophical rants?"
    scene w_873 with dissolve
    d "Maybe a bit of both. I like to keep people guessing."
    scene w_874 with dissolve
    e "Well, mission accomplished. But if you’re so concerned about security, maybe try cooperating with people a little more."
    scene w_873 with dissolve
    d "Always with the suggestions, Emma. But don’t worry, I have my own ways of keeping things… orderly."
    d "Actually, Emma, there’s something I wanted to discuss with you… privately."
    scene w_874 with dissolve
    e "Privately? About what, exactly?"
    scene w_875 with dissolve
    d "Let’s just say it’s a… sensitive matter. I thought it would be better if we spoke somewhere with fewer distractions."
    "{i}Ele esta gesticulando sutilmente em direção ao corredor que leva ao seu quarto.{/i}"
    d "We can talk there."
    e "You’ll understand if I’m a bit suspicious, Daniel. You’re not exactly known for being open with people."
    d "Fair. I can’t blame you. But… look, Emma, whether you believe it or not, I can see things haven’t been easy for you lately."
    d "I’d like to help. Sometimes an outside perspective is just what you need."
    "{i}I hesitate, taken aback by his unusually attentive tone. I study his face, looking for any hint of deception.{/i}"
    e "Alright, I’ll listen. Maybe I am just… being paranoid with everything going on."
    "{i}Daniel smiles, gesturing for me to follow him as he leads the way to his room.{/i}"
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    scene w_876 with fade
    "{i}I follow him, still uncertain, but part of my curiosity and the weight of recent events push me to see where this conversation might lead.{/i}"
    "{i}Daniel leads me to his room, closing the door softly behind us.{/i}"
    e_ "The space is as impeccably tidy as he is"
    scene w_877 with dissolve
    "{i}An air of calculated calm settles over the room. He gestures to the comfortable bed nearby, inviting me to sit down.{/i}"
    d "Please, make yourself comfortable. No need to be on edge here, Emma."
    scene w_878 with dissolve
    d "You know, I wanted to tell you this earlier… I was honestly worried about you that night."
    d "The way you rushed to our room, desperate, after what happened to Alex—it must have been terrifying for you."
    "{i}I feel my guard drop a little as he speaks, the memory of that night flooding back. His tone is warm, almost friendly, as he continues.{/i}"
    d "I mean, don’t get me wrong—I wasn’t exactly worried about Alex himself. He and I, well… we’ve had our share of disagreements."
    d "Actually, you might find it funny, but did Alex ever tell you about the time he tried to climb that rickety old tree in our backyard as a kid?"
    d "Thought he’d impress everyone… and ended up hanging upside down by his shirt for half an hour until I came to ‘rescue’ him."
    scene w_879 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    e "I hadn’t heard that one. Sounds exactly like something Alex would do."
    "{i}Daniel laughs along, his gaze fixed on me as if they were sharing a secret, a moment just between the two of us. His expression becomes softer, comforting.{/i}"
    scene w_878 with dissolve
    d "Yes, exactly. That’s Alex for you, always thinking he can handle everything himself."
    d "But you… you shouldn’t have to feel like you’re handling everything alone, either, Emma."
    "{i}Daniel, with a warm and seemingly genuine expression, continues speaking softly, his tone full of sympathy.{/i}"
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/villain-entry.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_880 with dissolve
    d "Emma, you’ve been through so much. You don’t have to carry all this weight alone. Sometimes, it’s okay to let someone else be there for you."
    "{i}Before I could react, Daniel's voice softened even further, his gaze steady and admiring.{/i}"
    scene w_881 with dissolve
    d "You know, Emma, I don’t think you realize just how remarkable you are. Smart, resilient, graceful under pressure."
    scene w_882 with dissolve
    d "And now, knowing that we’re spending a year together in this place… I’d like to get to know you better. Really get to know you."
    scene w_880 with dissolve
    e_ "What is he trying to do? Comfort me, or… something else?"
    e_ "It’s like his words are wrapping around me, almost too warm, too personal. But maybe I’m just overthinking things."
    scene w_882 with dissolve
    "{i}I, feeling the weight of Daniel's gaze and his hand on my thigh, force a polite smile, trying to keep my voice steady.{/i}"
    e "Thank you, Daniel. I… appreciate your words."
    scene w_883 with dissolve
    "{i}Daniel’s hand lingers a moment longer before he finally lets go, his expression warm and almost reassuring.{/i}"
    d "Of course, Emma. If you ever need anything—anything at all—you know where to find me. I’ll always be here for you."
    scene w_880 with dissolve
    e "Thank you, Daniel. Really. But I should probably get going. There’s still a lot to take care of today."
    d "I’ll see you around, Emma. Remember—my door’s always open."
    e "I’ll keep that in mind. Goodbye, Daniel."

    scene w_326 with fade
    $ renpy.pause()
    
    jump day6_emma_1
