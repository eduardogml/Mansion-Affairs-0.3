label day10_emma_1:

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 12rd_day with fade
    $ renpy.pause()
    hide 12rd_day with dissolve

    scene w_800 with fade
    "{i}Tonight was the dinner at Eleanor's, the one she'd been so insistent on.{/i}"
    "{i}It felt like a setup, though I couldn't quite put my finger on why. And then there was Alex...{/i}"
    "{i}God, every time I thought I had things figured out, he'd do something to make me question everything.{/i}"
    scene w_802 with dissolve
    "{i}I stood there, staring at the painting, a strange mix of anticipation and dread swirling within me.{/i}"
    e_ "Why did I agree to this? It's not like I actually want to spend an evening with Eleanor and her husband."
    e_ "And Alex... why does he always have to make things so complicated?"
    o "Oh, honey, you're overthinking again. Just relax. It's just dinner. A little wine, a little conversation... what's the worst that could happen?"
    e "Easy for you to say, Octavia. You're not the one who has to deal with the fallout if things go sideways. Especially with Alex there."
    e_ "What if you decide to show up again? Like last time. In the middle of a conversation, or worse, during dinner?"
    scene w_803 with dissolve
    o "Oh, please. Like I'd pass up an opportunity for a little fun. Besides, who knows what kind of secrets these people are hiding? A little chaos might just loosen their tongues."
    e_ "I’m not sure I want their tongues loosened, especially if it means you're involved."
    o "Relax, darling. I'll be on my best behavior. Mostly. Unless, of course, things get boring. Then all bets are off."
    e_ "Great. Just what I needed—you as my dinner guest. This night is going to be a disaster. Alex is going to think I’m losing it again."
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    scene w_804 with fade
    o "Think of it as a test, Emma. A little social experiment."
    o "Let's see how long they can keep their masks on before everything falls apart. Besides, haven't you been dying for a distraction? This could be fun."
    e_ "Why couldn’t I shake off this anxiety? Was it just the dinner, or something more?"
    e_ "It's like I’m waiting for the other shoe to drop. This mansion, these people... it’s all too perfect. Too quiet. Something’s bound to happen. I can feel it."
    o "You're not wrong, darling. But maybe, instead of waiting, we should... nudge things along. A little spark, a little chaos? What do you say?"
    "{i}A faint shiver running down my spine.{/i}"
    e_ "No, Octavia. Absolutely not. Tonight, I’m keeping you locked away where you belong. This dinner is already complicated enough."
    o "Good luck trying."
    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    scene w_327 with fade
    "{i}I stepped out into the cool night air, the gravel crunching softly under my heels. A wave of apprehension washed over me as I scanned the garden, searching for Alex.{/i}"
    e_ "He’s late. Typical. Probably preening in front of the mirror, making sure every hair is perfectly in place."
    scene w_809 with fade
    "{i}And then I saw him, leaning against the railing by the koi pond, the soft glow of the moonlight highlighting the sharp angles of his face.{/i}"
    scene w_818 with dissolve
    $ renpy.pause()
    "{i}He was wearing a dark shirt, sleeves rolled up to his elbows, revealing the intricate tattoo that snaked around his forearm.{/i}"
    scene w_819 with dissolve
    $ renpy.pause()
    "{i}His hair was styled neatly, but there were a few stray strands falling onto his forehead, giving him a slightly disheveled look that...{/i}"
    scene w_817 with dissolve
    $ renpy.pause()
    "{i}God, he looked good.{/i}"
    e_ "Damn, he cleans up well. I have to admit, it’s hard to ignore how… attractive he is."
    e_ "Especially tonight. Maybe this dinner won't be so bad after all...or maybe it will be a complete disaster."
    scene w_820 with dissolve
    "{i}As I reached him, I couldn’t help but notice the way his eyes lingered, taking me in. It felt… familiar.{/i}"
    "{i}Like a forgotten language my body suddenly remembered.{/i}"
    e "So… how do I look?"
    "{i}I tried to keep my tone casual, but there was a hint of nervousness in my voice. It had been a while since I’d cared this much about what he thought.{/i}"
    scene w_821 with dissolve
    a "You look… incredible, Emma. Seriously. I might have to keep Tristan away from you tonight."

    if emmajealouseleanorday4:
        $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
        "{i}He grinned, and I couldn’t help but laugh. It was that easy charm, the one that had always drawn me in, even when I knew better.{/i}"
        e_ "He’s such a flirt. Even now, when we’re supposed to be… over. But God, it feels good to hear him say that."
    else:
        e_ "He’s such a flirt. Even now, when we’re supposed to be… over."
    
    o "See? Told you he couldn't resist. You two are like magnets, drawn to each other even when you’re trying to push away. It’s pathetic, really."
    e_ "Shut up, Octavia."
    scene w_822 with dissolve
    a "Ready to go?"
    scene w_823 with dissolve
    e "Come on. I want to know if this wine is really worth it."
    "{i}He offered me his arm, and as I took it, a familiar warmth spread through me. It was a simple gesture, but it felt… significant.{/i}"
    e_ "Maybe tonight won't be so bad after all…or maybe it will be a complete disaster."
    o "Oh, honey, you're so naive. Like a moth to a flame. This night is going to be a bonfire, and you're about to get burned. Again."
    "{i}I ignored Octavia, linking my arm through Alex's, feeling the warmth of his body next to mine as we walked.{/i}"
    scene w_824 with fade
    "{i}The walk to Eleanor and Tristan's house was short, the crisp night air a welcome contrast to the tension that still lingered between Alex and me.{/i}"
    "{i}As we approached their front door, I couldn't shake the feeling that I was stepping into unfamiliar territory.{/i}"
    scene w_825 with dissolve
    e_ "This feels… strange. Like I’m playing a role in some twisted drama I don’t understand."
    o "Relax, darling. Just enjoy the show. You might even learn a thing or two about how the other half lives."
    $ renpy.music.play("audio/sfx/sfx_knock.ogg", channel="sfx1", relative_volume=1.0)
    "{i}Alex raised his hand to knock, and the sound echoed in the quiet night.{/i}"
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    scene w_826 with fade
    "{i}A moment later, the door swung open, revealing Eleanor.{/i}"
    "{i}She was dressed in a sleek, elegant gown that accentuated her figure. Her hair was styled impeccably, and her smile was warm and inviting.{/i}"
    e_ "Too inviting, maybe."
    scene w_827 with dissolve
    ele "Alex! Emma! So glad you could make it. Come in, come in."
    ele "Tristan's just finishing up some work. He’ll be down in a moment. Why don’t we head upstairs to the living room? It’s more comfortable there."
    scene w_829 with dissolve
    "{i}She turned, her heels clicking softly against the polished wood of the stairs as she ascended. Alex and I exchanged a quick glance before following her.{/i}"
    e_ "There’s something about her… a confidence, a knowingness, that makes me uneasy. And the way she looks at Alex… I don't like it."
    o "Jealous much, darling? Don't worry, you'll have plenty of time to stake your claim later. For now, just… observe."
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("ambient1", fadeout=2.0)
    $ renpy.music.play("audio/musics/piano_soft.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_830 with fade
    "{i}Eleanor led us into a dining room, the table set for four. The flickering candlelight cast dancing, creating an intimate, almost secretive atmosphere.{/i}"
    "{i}A chill ran down my spine, and I couldn’t shake the feeling that I was stepping into a carefully constructed scene.{/i}"
    e_ "This feels… staged. Like she’s planned every detail, every beat. What’s her game?"
    ele "Make yourselves comfortable. I’ll be right back with some wine. I have a bottle Tristan’s been saving for a special occasion."
    scene w_831 with dissolve
    "{i}She gave Alex another one of those lingering looks before turning and leaving the room.{/i}"
    "{i}I watched her go, my mind racing. Special occasion? What was so special about tonight?{/i}"
    e_ "Is she trying to impress us? Or is there something more to this…?"
    scene w_832 with dissolve
    "{i}Alex pulled out a chair for me, and I sat down, the plush velvet a stark contrast to the unease I was feeling. He sat down next to me.{/i}"
    a "So, how are you holding up with everything? You seem a bit… quiet tonight."
    scene w_833 with dissolve
    e "Just… thinking. A lot on my mind, I guess."
    e_ "Alex was trying, I could give him that. But there was still a wall between us, one that I wasn't sure either of us knew how to break down."
    scene w_834 with dissolve
    o "He's trying to soften you up, darling. Don't fall for it. Remember why you're here. Remember everything."
    a "Anything you want to talk about?"
    scene w_833 with dissolve
    e "Not really. Just… life stuff. You know how it is."
    "{i}I shrugged, hoping he’d drop it. I wasn’t ready to dive into the mess of emotions swirling inside me. Not with him. Not tonight.{/i}"
    scene w_834 with dissolve
    a "Well, if you change your mind, I’m here. We used to be good at talking, remember?"
    scene w_833 with dissolve
    e "We used to be a lot of things, Alex."
    "{i}The words slipped out before I could stop them, sharper than I intended. I saw a flicker of something in his eyes—hurt, maybe? Or was it just annoyance?{/i}"
    scene w_834 with dissolve
    o "Good. Let him feel it. He deserves a little reminder of what he’s lost."
    a "Look, I know things haven’t been easy between us. But I’m trying here. Can we just… enjoy the evening? For once?"
    scene w_833 with dissolve
    e "Enjoy the evening? With Eleanor practically throwing herself at you? I don’t know if 'enjoy' is the right word."
    "{i}I couldn’t help the sarcasm that laced my tone. I saw his jaw clench, and I knew I’d hit a nerve.{/i}"
    scene w_834 with dissolve
    a "She’s just being friendly, Emma. Don’t read too much into it."
    scene w_833 with dissolve
    e "Friendly? Is that what you call it?"
    scene w_834 with dissolve
    a "There’s nothing going on between Eleanor and me. It’s just you and me, Emma. Remember?"
    scene w_833 with dissolve
    "{i}I hesitated. Maybe he was right. Maybe I was overreacting. Or maybe I just wanted to believe him.{/i}"
    e "Maybe you're right. Maybe I am reading too much into it."
    scene w_832 with dissolve
    "{i}I forced a smile, hoping it looked convincing. I could feel Octavia’s amusement, a silent laughter echoing in my mind.{/i}"
    o "Oh, he’s eating this up. Look at him, all puffed up with his own charm. He thinks he’s got you fooled."
    a "You’ve been… different lately, Emma. More on edge than usual."
    e "Different? How so?"
    e_ "Was he noticing the changes? The moments when Octavia’s influence felt… stronger than my own?"
    scene w_834 with dissolve
    a "I don't know. Sometimes you seem… like another person. Someone… I don’t recognize."
    o "He’s talking about me, darling. Tell him. Tell him I’m the one he should be worried about."
    scene w_833 with dissolve
    "{i}A wave of panic washed over me.{/i}"
    e_ "No, Octavia. Stay back. He can't know about you. Not yet."
    e_ "What if she takes over? What if she says something… something I’ll regret?"
    scene w_834 with dissolve
    a "Emma? You okay? You seem… distracted."
    scene w_833 with dissolve
    e "Yeah, I’m fine. You’re right. I’m just… overthinking things."
    e "This whole mansion, the attack, the dinner… it’s all getting to me."
    scene w_832 with dissolve
    "{i}I forced a laugh, hoping it masked the tremor in my voice.{/i}"
    e_ "Just go along with it, Emma. Don’t let him see how much you’re struggling."
    o "Coward."
    "{i}Alex looked at me strangely, like he wasn’t entirely convinced.{/i}"
    scene w_835 with dissolve
    "{i}But before he could say anything else, Eleanor walked back into the room, two glasses of wine in hand.{/i}"
    "{i}Eleanor returned, a bottle of wine in hand, her smile bright and genuine. The shift in her demeanor, from calculated hostess to something more relaxed, was subtle but noticeable.{/i}"
    "{i}It was enough to break the tension that had settled between Alex and me, a welcome reprieve from the unspoken words and lingering glances.{/i}"
    e_ "Thank God she’s back. I was about to lose it."
    o "Spoilsport."
    ele "Here we are. A little something to… loosen things up."
    "{i}Her good humor was infectious, a lightness that eased the weight in my chest. I offered a small, grateful smile.{/i}"
    e "Thanks, Eleanor. I think we could both use a glass."
    scene w_836 with dissolve
    "{i}Eleanor chuckled, moving gracefully around the table, pouring the wine.{/i}"
    "{i}Her voice was warm and engaging as she chatted about the estate, the village, anything but the strange undercurrent that had filled the room just moments before.{/i}"
    scene w_837 with dissolve
    "{i}As she leaned in to fill my glass, her voice dropped to a whisper, close to my ear.{/i}"
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/sexy_beat.mp3", "music1", fadein=2.0, relative_volume=0.2)
    scene w_838 with dissolve
    $ renpy.pause()
    ele "I can tell you’re a bit… anxious, Emma."
    ele "But this wine… it’ll help you relax. Trust me."
    "{i}Her breath tickled my skin, sending a shiver down my spine.{/i}"
    "{i}She paused, her face inches from mine, her eyes locking onto mine with an intensity that made my heart race.{/i}"
    ele "The rest of the night will be… relaxing too."
    "{i}For a moment, I forgot where I was, who I was with. Her scent, a mix of something floral and something… dangerous, filled my senses.{/i}"
    scene w_839 with dissolve
    $ renpy.pause()
    "{i}And then, before I knew what was happening, I leaned in.{/i}"
    e_ "Am I really doing this? Right here, right now?"
    o "Finally. About time you let loose a little, darling. Let’s see where this goes…"
    "{i}Octavia’s voice echoed in my mind, a mixture of excitement and amusement.{/i}"
    scene w_840 with dissolve
    "{i}Eleanor’s lips were parted, her breath warm against my cheek. It would have been so easy to close the distance, to let myself get lost in that moment.{/i}"
    e_ "What the hell am I doing?"
    "{i}I pulled back, my heart pounding, my cheeks flushed.{/i}"
    e "Uh… thanks, Eleanor."
    "{i}My voice was shaky, barely a whisper.{/i}"
    ele "You’re welcome, darling."
    "{i}Her tone was light, teasing, but I could see the flicker of something in her eyes—amusement, perhaps? Or something more…?{/i}"
    scene w_845 with fade
    $ renpy.pause()
    scene w_327 with fade
    "{i}Will Emma be able to keep her composure, or will the pressure of the evening finally break through?{/i}"
    "{i}What happens when the masks begin to slip, and hidden truths are revealed? The night is far from over, and the stakes are rising.{/i}"
    "{i}Stay tuned, as the story unfolds further in the next chapters. What will happen next at the dinner? Will Emma be able to navigate the chaos, or will she find herself drawn into a world she's not ready for?{/i}"
    "{i}See you in the next chapters of this story, with strong revelations and news.{/i}"
    "{i}Thanks for playing.{/i}"

    jump sandbox
