label day1_alex_1:
    $ alex_power = 0
    $ alexflirtemmaday1 = False
    $ alexflirteleanorday1 = False
    $ alexemmaanddanieljealousday1 = False
    $ alexprotectrubyday1 = False
    $ alexflirtrubyday1 = False

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music2", fadein=2.0, relative_volume=0.1)

    show 3rd_day with fade
    $ renpy.pause()
    hide 3rd_day with dissolve
    show screen alex_power_screen
    a_ "Yesterday was a nightmare. I can't believe I have to live a whole year with Daniel in this mansion. Of all the people, it had to be him. This is going to be hell"
    a_ "Just seeing his smug face again makes my blood boil. How am I supposed to get through this without losing it?"
    a_ "I have to stay calm, for Emma's sake, and for mine. This place... it should have been a fresh start"
    a_ "Now it's just another battlefield. God, I hate him. A whole year. I need to focus. Inherit the mansion, then get as far away from him as"
    scene w_109 with fade
    a_ "I need to figure out what to do today. Maybe explore the village, get a lay of the land. Anything to get out of this house for a while"
    a_ "Dealing with Daniel is going to drive me insane. That smug look on his face... I can't stand it."
    a_ "And then there's Samuel. He seems like a decent guy, but a bit too oblivious to the tension around here. Probably for the best, though. Keeps things simpler"
    a_ "Isabella, damn. She's something else. Sexy as hell, but I can't let myself get distracted by her. Too much trouble, especially with Daniel around. But still, she's hard to ignore"
    a_ "Emma... we’re in such a mess. This year is supposed to help us, but I don't know"
    a_ "We’re supposed to be getting divorced, but now we’re stuck here, pretending everything’s fine.I need to keep my cool for her sake, and maybe for mine too"
    a_ "I’ll go check out the village. See what's around. Maybe clear my head a bit. Yeah, that sounds like a plan"
    scene w_110 with dissolve
    a_ "Emma leaning like that... That ass is inviting, round and firm, almost begging for me to touch it. She's just wearing panties and driving me crazy"
    a_ "God, she's so sexy. That ass... I can't believe we're not together anymore. I miss touching her, feeling her. Making sex to her. Every curve of her body is perfect"
    a_ "I could just go up to her, start flirting. She might respond. Maybe she misses it too. But what if she pushes me away? Things are so messed up between us. But damn, I want her"
    a_ "I could just walk out. Clear my head. But it's hard to walk away from something so tempting. I need to focus"
    a_ "Think about what’s best. This isn’t just about sex. It’s about us, about everything we’re going through"
    a_ "If I stay, I could ruin everything. But if I leave, I’m just running away. Damn it, what should I do?"

    $ alexflirtemmaday1 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Flirt with Emma{/size}{/font}":
            $ alexflirtemmaday1 = True

            a_ "Maybe I should just go for it. We haven't been close in so long, and I miss her. She looks so damn sexy right now"
            scene w_111 with dissolve
            with Pause(3)
            "{i}I moved behind Emma, placing my hands on her waist and pulling her back to me. She smiled mischievously, feeling the heat from my body.{/i}"
            a "Hey, beautiful. I've missed this. Don’t you miss it too?"
            "{i}I saw Emma turn her head, her expression changing from surprise to irritation.{/i}"
            e "Alex, what are you doing?"
            a_ "She’s surprised. Maybe I can still convince her."
            "{i}I tightened my grip, leaning in closer.{/i}"
            a "Come on, Emma. Just a quick one. I know you’ve missed it too."
            scene w_112 with dissolve
            e "No, Alex. I’m not in the mood. Especially not after everything that's happened."
            a_ "She’s still mad. Damn it"
            "{i}I tried again, my voice softer, more pleading.{/i}"
            a "Emma, please. I need this. We need this."
            e "I can’t just ignore everything. Especially after talking to Isabella."
            a_ "{i}Isabella? What did she say?) What did she say to you?{/i}"
            "{i}**My temper flared slightly.{/i}"
            e "It doesn’t matter. The point is, I’m not interested, Alex. Just leave me alone."
            a_ "Damn it, this isn’t working. She’s really not in the mood."
            a "Fine. I’ll go out, then. Maybe clear my head."
            scene w_113 with dissolve
            "{i}As I walked away, the tension between us was almost tangible. I couldn’t shake the feeling of rejection, and Emma’s irritation only added to the heavy atmosphere.{/i}"
            a_ "This year is going to be hell. But I have to find a way to deal with it. For both our sakes."
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
        "{font=fonts/hatten.ttf} {size=50}Go out for fresh air{/size}{/font}":
            $ alexflirtemmaday1 = False

            scene w_113 with dissolve
            "{i}I stood by the door, fully dressed, glancing back at Emma. Her mood was even worse than yesterday.{/i}"
            "{i}What could have made her so irritated? I tried to piece it together, but it was no use.{/i}"
            "{i}If I pushed her now, she'd just reject me again, and I wasn't in the mood for another argument.{/i}"
            "{i}We've been arguing a lot lately, and I needed to avoid more conflict for now.{/i}"
            "{i}Maybe it was something I did, or maybe something she hadn't shared with me. Either way, I couldn't shake the feeling of frustration and insecurity gnawing at me.{/i}"
            "{i}The tension between us was almost suffocating. I wanted to reach out, to comfort her, but my temper and jealousy always got in the way.{/i}"
            "{i}I had to learn to control myself, to be the strong, protective partner she needed.{/i}"
            "{i}I sighed, opening the door slowly. I needed some air, some space to think. I couldn't keep letting my explosive temper ruin everything. Emma deserved better, and so did I.{/i}"
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)

    scene w_114 with fade
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    if alexflirtemmaday1:
        "{i}I stood in the garden, gripping the wooden railing as I tried to control my rising temper. Emma’s rejection still stung, and I couldn’t help but wonder why she pushed me away.{/i}"
        "{i}The anger simmered beneath the surface, threatening to boil over. The garden's tranquility contrasted sharply with the turmoil inside me. I gazed at the pond, lost in my thoughts.{/i}"
        a_ "I don't get it. Does she not miss us being together, making love? Is she really over us? She used to crave our intimacy just as much as I did. What changed?"
        a_ "Was it my infidelity? My temper? Damn it, why can't I figure this out? Is our relationship truly beyond saving?"
        scene w_115 with dissolve
        "{i}The more I thought about it, the more frustrated I became. Our love had once been so passionate.{/i}"
        "{i}Now, it felt like we were just going through the motions, pretending everything was fine when it clearly wasn’t{/i}"
        "{i}I needed to find a way to bridge the gap between us, to rekindle that flame. But as I stood there, the answers remained elusive, lost in the chaos of my mind.{/i}"
    else:
        "{i}Standing in the garden, I tried to shake off the tension that clung to me. Emma had clearly not been herself this morning, and it gnawed at me.{/i}"
        "{i}The way she moved, even in her irritation, still drove me wild. Her body, so familiar and yet still so tempting, made my heart race.{/i}"
        "{i}I couldn't deny the magnetic pull I felt towards her. It hit me then—maybe I didn't want the divorce after all. Maybe the desire I still felt for her was a sign that there was something worth fighting for.{/i}"
        scene w_115 with dissolve
        "{i}(Why does she have to be so damn sexy? Even when she's angry, I can't help but want her. But she’s still pissed at me. What can I do to fix this?{/i}"
        "{i}(I've screwed up so many times, but I can't stand the thought of losing her completely. There has to be a way to show her that I'm serious about making things right.{/i}"
        "{i}(Maybe I can start by being more patient, more understanding. If only she could see how much I still care, how much I still need her.{/i}"
    scene w_116 with dissolve
    "{i}I stood in the garden, trying to clear my head when I noticed a woman approaching. She had a confident stride and a knowing smile. As she got closer, I couldn't help but notice her figure, accentuated by the low-cut black dress she wore.{/i}"
    ele "Hello there. You must be Alex, right?"
    "{i}I nodded, curious about the sudden interruption.{/i}"
    a "Yeah, that's me. And you are?"
    scene w_117 with dissolve
    ele "I'm Eleanor, your neighbor."
    ele "I just thought I'd come over and introduce myself. It’s always good to know who’s living next door."
    "{i}She extended her hand, and I shook it firmly. Her touch was warm, and her eyes lingered on mine for a moment longer than necessary.{/i}"
    a "Nice to meet you, Eleanor. How long have you been living around here?"
    ele "Oh, we've been here for a few years now. My husband and I love the area. It’s peaceful, perfect for our tastes."
    "{i}There was something about the way she said \"husband\" that felt almost dismissive.{/i}"
    "{i}I noticed her gaze flicker down to my tattooed arm and back up to my face.{/i}"
    scene w_118 with dissolve
    ele "So, what brings you to this lovely mansion?"
    a "It's a bit of a long story. My aunt left it to me, but there's a catch. I have to live here for a year to inherit it fully."
    ele "That sounds like quite the adventure. I hope you're finding it... comfortable."
    "{i}I could feel her eyes on me, assessing, maybe even admiring. There was an undeniable flirtation in her tone.{/i}"
    a "It's been interesting, to say the least. Still getting used to the place."
    ele "I can imagine. By the way, I was wondering if you could help me with something."
    scene w_119 with dissolve
    ele "My kitchen light stopped working, and I have no idea how to fix it. My husband isn’t home, and I could use a hand."
    "{i}Her request seemed innocent enough, but the way she looked at me suggested there might be more to it.{/i}"
    "{i}I couldn't help but feel a surge of curiosity—and maybe a bit of attraction.{/i}"
    a_ "A kitchen light? Really? This feels like one of those setups you see in movies."
    a_ "But then again, she does look genuinely frustrated. And she's definitely giving me the eye. Might as well help her out and see where this goes."
    a "Sure, I can take a look. Lead the way."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene black with fade
    "{i}Eleanor's smile widened, and she motioned for me to follow her.{/i}"
    "{i}As we walked, I couldn't help but notice the sway of her hips. She glanced back a couple of times, catching my eye with a knowing look.{/i}"
    "{i}We continued our walk, the mansion's garden slowly giving way to the path leading to her house.{/i}"
    scene w_120 with fade
    ele "Thank you so much, Alex. It's really kind of you. I promise I won't take up too much of your time."
    a "No problem at all. Happy to help a neighbor."
    scene w_121 with dissolve
    "{i}In Eleanor’s kitchen, the dim lighting cast shadows on the sleek countertops and modern appliances.**{/i}"
    scene w_122 with dissolve
    "{i}She pointed to the ceiling, flipping the light switch on and off to show me the problem.{/i}"
    ele "See? It’s completely dead. I’ve tried everything I can think of, but nothing works."
    scene w_123 with dissolve
    a "Looks like I’ll have to get up there and take a closer look. Do you have a chair or something sturdy I can stand on?"
    "{i}Eleanor brought over a chair, and I carefully climbed up to examine the light fixture.{/i}"
    scene w_124 with dissolve
    "{i}As I worked, she stood nearby, her eyes occasionally drifting up to me, her curiosity evident.{/i}"
    ele "So, Alex, I’ve heard some interesting things about the mansion you’re staying in. Is it true that it’s supposed to be haunted?"
    a "That’s what they say. Honestly, I haven’t seen anything out of the ordinary yet, but who knows?"
    a "The place does have a bit of a creepy vibe at night."
    ele "Really? I’ve always been fascinated by ghost stories. Do you believe in that sort of thing?"
    a "Not really. I mean, I’ve had my share of weird experiences, but I’ve never seen anything I couldn’t explain."
    a "What about you?"
    "{i}As I fiddled with the fixture, I glanced down at Eleanor. She seemed genuinely interested, her eyes wide with curiosity.{/i}"
    ele "I’m not sure. I think it’s fun to imagine there’s more to the world than what we can see. Keeps life interesting, you know?"
    a "Yeah, I can see that. Living in a haunted mansion might be more exciting than I thought."
    "{i}I chuckled, and she joined in, her laughter light and melodic. I couldn't help but notice how her eyes sparkled when she laughed.{/i}"
    ele "So, have you found anything interesting in the mansion yet? Old letters, hidden rooms, anything like that?"
    a "Not yet, but I’ve barely scratched the surface. The place is huge. Who knows what’s hidden in there?"
    ele "Sounds like you have a lot of exploring to do. Maybe you’ll uncover some long-lost secrets."
    "{i}As we continued talking, I focused on the light fixture, trying to figure out what was wrong.{/i}"
    "{i}Eleanor’s presence was a pleasant distraction, and I found myself enjoying our conversation more than I expected.{/i}"
    a_ "A haunted mansion, a beautiful neighbor in distress—this feels like a scene out of a movie."
    a_ "But I have to stay focused. Can’t let myself get too distracted, no matter how tempting she is."
    "{i}Eleanor leaned against the counter, her eyes still fixed on me.{/i}"
    ele "By the way, thank you for helping me out with this. I know it’s probably just a small thing, but it means a lot."
    a "No problem at all. I’m happy to help. It’s nice to have a break from the mansion and do something useful."
    ele "Well, I appreciate it. It’s not often I have a strong, handsome man around to lend a hand."
    "{i}There was a playful glint in her eye as she said it, and I couldn’t help but smile.{/i}"
    scene w_125 with dissolve
    $ renpy.music.play("audio/sfx/sfx_bottle.wav", channel="sfx1", relative_volume=0.4)
    if alexflirtemmaday1:
        a_ "A strong, handsome man, huh?"    
    else:
        a_ "A strong, handsome man, huh? This woman is something else. Better stay on my toes with her around."
    "{i}Standing on the chair, I worked on the light fixture while Eleanor rummaged through the refrigerator.{/i}"
    ele "Would you like some wine? I think we could both use a little break."
    a "Sure, a glass of wine sounds great."
    scene w_126 with dissolve
    $ renpy.music.play("audio/sfx/sfx_water_pouring.mp3", channel="sfx1", relative_volume=0.8)
    "{i}The dim lighting added a certain intimacy to the moment, casting soft shadows around the kitchen.{/i}"
    "{i}Eleanor poured the wine, the rich red liquid filling the glasses as I continued tinkering with the fixture.{/i}"
    scene w_127 with dissolve
    "{i}She pulled out a bottle of wine and two glasses, her movements slow and deliberate. I glanced down at her, noticing the way her dress clung to her curves.{/i}"
    scene w_128 with dissolve
    $ renpy.music.play("audio/sfx/sfx_water_pouring.mp3", channel="sfx1", relative_volume=0.8)
    "{i}I finally managed to fix the problem, and the kitchen flooded with bright light just as she finished pouring.{/i}"
    scene w_129 with dissolve
    ele"Ah, there we go. Thank you so much, Alex. Here’s to your handiwork."
    scene w_130 with dissolve
    "{i}She handed me a glass of wine, her fingers brushing against mine.{/i}"
    "{i}The touch sent a small shiver down my spine, and I looked into her eyes, seeing a hint of mischief there.{/i}"
    $ renpy.music.play("audio/sfx/sfx_glasses_clink.opus", channel="sfx1", relative_volume=0.8)
    ele "So, tell me, Alex, do you always come to the rescue of damsels in distress?"
    a "Only when the damsels are as charming as you."
    scene w_131 with dissolve
    ele "Well, I must say, it’s nice to have a strong man around. My husband is always so busy, it's rare to have someone here who can help out."
    "{i}Her words were innocent enough, but the way she said them, the slight curve of her lips, suggested something more. I could feel the tension between us growing.{/i}"
    ele "You know, if you ever need anything, don’t hesitate to ask. We neighbors should look out for each other, after all."
    a "I’ll keep that in mind, Eleanor. And the same goes for you. If you need anything, just let me know."
    "{i}Eleanor smiled, a slow, knowing smile that made my heart beat a little faster. I could see the game she was playing, and part of me wanted to play along.{/i}"
    a_ "A charming damsel, indeed. She’s definitely flirting with me. Should I play along? She’s married, but she’s making it clear that doesn’t bother her."

    $ alexflirteleanorday1 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Flirt with Eleanor{/size}{/font}":
            $ alexflirteleanorday1 = True
            "{i}As I stood there, the tension between us was almost tangible. Eleanor took a step closer, her eyes locked onto mine. She leaned in, her voice a seductive whisper.{/i}"
            ele "You know, Alex, it’s been a long time since I’ve had such capable hands around here."
            scene w_132 with dissolve
            "{i}Her words sent a jolt of excitement through me. Unable to resist any longer, I moved closer, my lips grazing her ear as I spoke.{/i}"
            a "Is that so? Maybe I should make a habit of coming over more often."
            "{i}I wrapped my arms around her, pulling her gently against me. My hands trailed down her back, and she shivered at my touch. {/i}"
            "{i}As I held her, my fingers found their way to her firm, inviting ass. She didn’t pull away; instead, she leaned into the embrace, her body responding to mine.{/i}"
            ele "You really should, Alex. I could get used to having you around."
            scene w_133 with dissolve
            $ renpy.music.play("audio/adult/female-Mm_1.mp3", channel="sfx1", relative_volume=0.3)
            with Pause(3)
            "{i}I could feel her breath against my neck as I slid my hand between her cheeks, teasing her with a light, provocative touch. Her soft moan only fueled my desire.{/i}"
            a_ "Oh, Eleanor, you’re playing with fire. But I’m more than happy to get burned."
            a "Anytime you need me, just call. I’ll be right here, ready to help with whatever you need."
            "{i}Eleanor smiled, a wicked glint in her eye.{/i}"
            ele "I’ll hold you to that, Alex. You’ve been a wonderful help today."
            "{i}Reluctantly, I stepped back, letting my hands linger on her hips for a moment longer. The heat between us was undeniable, but we both knew it was time to stop.{/i}"
            scene w_131 with dissolve
            a "I should probably get going, but remember, I’m just next door if you need anything."
            "{i}She nodded, her smile never fading.{/i}"
            ele "I’ll keep that in mind, Alex. Thank you again. I’m sure I’ll be seeing you soon."
            "{i}With a final, lingering look, I turned and left, my mind racing with the possibilities of what might come next.{/i}"
        "{font=fonts/hatten.ttf} {size=50}Leave after finishing the wine{/size}{/font}":
            $ alexflirteleanorday1 = False
            "{i}Eleanor and I continued our conversation in the kitchen, her flirtatious smiles and lingering glances becoming more frequent.{/i}"
            "{i}I could feel the tension between us, the unspoken invitation in her eyes. But I remembered the mistakes I'd made with Emma, letting situations like this one go too far.{/i}"
            ele "So what are your plans for the rest of the day?"
            "{i}She asked, her tone light but with an undercurrent of suggestion. I took a sip of my wine, considering my response.{/i}"
            a_ "I need to handle this carefully. I can't let myself fall into the same traps again."
            a "Just a quiet day, I guess. It was a long week."
            "{i}I replied, keeping my voice casual. She moved a little closer, her hand brushing mine as she reached for her glass.{/i}"
            ele "Sometimes a quiet day can be... just what you need."
            "{i}Her voice was soft, almost a whisper. I felt a familiar pull, the temptation to let myself be drawn in. But I knew better now.{/i}"
            a_ "I have to be strong. I can't let this ruin my chances with Emma, if I even have any left."
            scene w_134 with fade
            "{i}As we continued talking, I steered the conversation towards safer topics, keeping things light and friendly.{/i}"
            "{i}Eventually, the wine was gone, and I knew it was time to make my exit. I stood up, smiling politely.{/i}"
            a "This has been lovely, Eleanor. But I should get going."
            ele "Of course, Alex. Have a good day."
            "{i}Her disappointment was subtle, but I caught it. Still, I maintained my resolve.{/i}"
            scene w_135 with dissolve
            "{i}I said my goodbyes and left her standing in the kitchen, the door closing softly behind me. I walked away, feeling a mix of relief and uncertainty.{/i}"
            a "(Did I do the right thing? Only time will tell. But for now, I need to stay focused on what's really important."

    scene black with fade
    if alexflirteleanorday1:
        "{i}After leaving Eleanor's, I found myself driving back towards the mansion.I couldn't shake the feeling of Eleanor's touch, her words lingering in my mind.{/i}"
        "{i}But I knew I had made the right choice. As the mansion came into view, I felt a sense of resolve.{/i}"
    else:
        "{i}After resisting Eleanor's flirtations and leaving her house, I felt a mix of relief and determination. Driving back to the mansion, I couldn't stop thinking about Emma and the reasons I had to stay on this path.{/i}"
        a_ "I need to stay focused. This is where I need to be, not getting lost in fleeting desires."
        a_ "Emma deserves better. I deserve better."
    "{i}It was still daylight when I returned to the mansion. The path through the garden was the same one I had taken with Eleanor earlier. As I walked, I felt a mixture of relief and determination.{/i}"

    scene w_136 with dissolve
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    "{i}But that all changed when I saw Emma and Daniel in the garden, alone. Daniel was saying something to Emma that made her laugh. I felt a surge of anger rise within me.{/i}"
    "{i}From a distance, I watched them, my mind racing with thoughts and scenarios. Each one seemed worse than the last. I knew Daniel's reputation—ambitious, cunning, and always looking for an advantage.{/i}"
    "{i}Seeing him with Emma, seeing her smile at him, made my blood boil. I stood there, my fists clenching and unclenching as I tried to control my emotions. I didn't recognize the feeling at first, but it was jealousy, plain and simple.{/i}"
    "{i}I had made Emma unhappy before with my jealousy, and I didn't want to repeat those mistakes. But seeing them together, so comfortable, made it hard to think clearly.{/i}"
    scene w_137 with dissolve
    a_ "Damn it, what is he saying to her? Why is she laughing like that?"
    a_ "What is he doing here? Is he trying to win her over? Does Emma find him more interesting than me?"
    "{i}I took a deep breath, trying to steady myself. The rational part of me knew that storming over and starting a fight wouldn't help. It would only make things worse, especially for Emma.{/i}"
    "{i}I had to decide what to do—confront Daniel and risk another argument, or approach them calmly and see what was really going on.{/i}"
    a_ "I need to stay calm. I can't let my temper get the best of me. But damn it, why does she have to laugh like that with him?"

    $ alexemmaanddanieljealousday1 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Get angry at Daniel{/size}{/font}":
            $ alexemmaanddanieljealousday1 = True

            $ renpy.music.stop("music2", fadeout=2.0)
            $ renpy.music.play("audio/musics/filaments1.mp3", "music1", fadein=2.0, relative_volume=0.2)

            "{i}As I got closer, I could hear Daniel’s voice carrying over to where I stood. He was recounting a story from our teenage years, and Emma was laughing.{/i}"
            "{i}The sound of her laughter, mixed with Daniel’s smug tone, made my blood boil even more.{/i}"
            d "And then there was this one time, Alex and I were at the lake with some friends. Alex was trying to impress everyone by diving off the highest rock."
            d "But when he jumped, he screamed like a little girl all the way down!"
            "{i}Emma’s laughter rang out, and it stung. I clenched my fists, feeling my temper rising.{/i}"
            a_ "I can’t believe he’s telling her that. He’s trying to make me look like a fool in front of Emma. He’s always had a knack for making himself look good at my expense."
            "{i}I walked up to them, my steps heavy with anger. Daniel noticed me first, a smug smile playing on his lips. Emma’s laughter died down as she saw the expression on my face.{/i}"
            scene w_143 with dissolve
            a "What the hell do you think you’re doing, Daniel? Trying to make me look like an idiot in front of my wife?"
            d "Oh come on, Alex. It’s just a funny story. We all had a good laugh back then."
            e "Alex, it was just a story. No need to get so worked up."
            "{i}I ignored Emma, my focus entirely on Daniel.{/i}"
            a "You’re trying to undermine me, Daniel. You’ve always been like this, trying to one-up me, trying to make me look bad."
            "{i}Daniel raised his hands in a mock gesture of innocence, his smug smile never leaving his face.{/i}"
            d "Alex, you’re overreacting. It’s just a bit of fun. Lighten up."
            "{i}Emma looked between us, confusion and concern on her face.{/i}"
            e "Alex, please. It’s not that serious."
            scene w_144 with dissolve
            a "Not that serious? You’re here laughing with him, letting him make a fool out of me! How do you think that makes me feel?"
            "{i}My temper was flaring, and I could feel the jealousy coursing through me. I couldn’t stand the sight of them together, laughing at my expense.{/i}"
            a_ "I can’t let him get away with this. He’s trying to drive a wedge between us, and I won’t let him."
            scene w_143 with dissolve
            "{i}I stepped closer to Daniel, my fists clenched at my sides.{/i}"
            a "Stay away from my wife, Daniel. I know what you’re trying to do, and I won’t let it happen."
            scene w_145 with dissolve
            d "Feeling a bit left out, Alex?"
            a "Don’t try to act innocent, Daniel. I know exactly what you’re trying to do."
            "{i}Daniel smirked, unfazed by my outburst.{/i}"
            d "Really, Alex? All this because of a harmless story? You’re more insecure than I thought."
            "{i}Emma glanced between us, her expression shifting from confusion to frustration. I could see she was upset, but I couldn’t stop now.{/i}"
            "{i}Daniel chuckled, a condescending sound that only fueled my rage.{/i}"
            d "Maybe if you weren’t so easy to rile up, it wouldn’t be so much fun. You see, Alex, the problem isn’t me—it’s you."
            d "You’re too hot-headed, too jealous. That’s why Emma is laughing with me and not you."
            "{i}Emma’s face fell at Daniel’s words, her frustration with me evident. I felt a pang of guilt, but my anger overshadowed it.{/i}"
            a "You think you’re so clever, don’t you? You think you can just waltz in here and turn my wife against me?"
            scene w_146 with dissolve
            "{i}With a final smirk, Daniel turned and walked away, leaving me and Emma standing there. I could feel the weight of Emma’s disappointment even without looking at her.{/i}"
            d "If you can’t keep her happy, maybe you should look at yourself instead of blaming others."
            "{i}I felt humiliated, my anger boiling over as I glared at Daniel. He had a satisfied look on his face, knowing he had successfully gotten under my skin.{/i}"
            d "Anyway, I think I’ve had enough entertainment for one day. Enjoy the rest of your evening, Alex. Emma."
            a_ "I’ve done it again. I’ve let my temper get the best of me. What’s wrong with me?"
            $ alex_power = AlexPowerRemove()
            scene w_147 with dissolve
            "{i}We stood in silence, the tension between us palpable. I could feel Emma’s eyes on me, her frustration and disappointment like a heavy weight on my shoulders.{/i}"
            "{i}Emma's face was a mix of sadness and frustration as she turned to me. The hurt in her eyes cut deep, but I was too angry and humiliated to react properly.{/i}"
            e "Why, Alex? Why do you always have to do this?"
            a "Do what, Emma? Defend myself against that smug bastard?"
            "{i}She shook her head, her expression hardening.{/i}"
            e "No, Alex. Ruin every single moment with your jealousy and temper. This is exactly why we’re in this situation."
            "{i}I felt a pang of guilt, but I couldn’t let go of my anger.{/i}"
            a "He was making fun of me, Emma. Right in front of you. What was I supposed to do? Just stand there and take it?"
            e "Maybe not make a scene for once. Maybe trust me enough to handle a conversation without you barging in and making it worse."
            "{i}I clenched my fists, struggling to keep my voice steady.{/i}"
            a "You don’t understand, Emma. He’s always been like this, always trying to make me look bad. It’s not just about you."
            scene w_148 with dissolve
            e "And it’s always the same excuse. Blame Daniel, blame anyone but yourself. When are you going to take responsibility for your actions?"
            "{i}Her words stung, but I couldn’t back down.{/i}"
            a "What do you want from me, Emma? To just let him walk all over me?"
            "{i}She sighed, the frustration evident in her voice.{/i}"
            e "I want you to realize that your jealousy and anger are destroying us. They’ve already done so much damage, and you’re not even sorry."
            "{i}I was sorry. Deep down, I knew I was. But I didn’t know how to admit it.{/i}"
            a_ "I can’t say it. I don’t even know how to start. She won’t understand."
            "{i}I looked away, unable to meet her gaze.{/i}"
            scene w_147 with dissolve
            e "We’re just pretending to be married, Alex. Don’t forget that. We’re already separated, and after this year, it will be official."
            "{i}Her words hit me like a punch to the gut. I wanted to tell her I was sorry, that I regretted everything. But the words wouldn’t come.{/i}"
            a "Fine. Whatever you say."
            scene black with dissolve
            "She walked away, leaving me standing there feeling defeated and more alone than ever. I watched her go, the weight of my actions pressing down on me."
            a_ "I’ve messed up again. Why can’t I just tell her I’m sorry? Why can’t I fix this?"
            
            $ renpy.music.stop("music1", fadeout=2.0)
            $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music2", fadein=2.0, relative_volume=0.1)

        "{font=fonts/hatten.ttf} {size=50}Approach them calmly{/size}{/font}":
            $ alexemmaanddanieljealousday1 = False

            "{i}As I approached Daniel and Emma, I could hear the tail end of Daniel's story.{/i}"
            "{i}He was recounting an embarrassing moment from our teenage years, his voice full of amusement. I felt the familiar anger rising, but I forced myself to stay calm.{/i}"
            d "...and then Alex tripped over his own feet and fell right into the lake, splashing water everywhere. It was hilarious!"
            "{i}Emma laughed, but her laughter was tinged with uncertainty. I could see she was unsure whether to fully believe Daniel's version of events.{/i}"
            scene w_138 with dissolve
            "{i}I stepped up to them, placing a friendly hand on Daniel's shoulder.{/i}"
            a "Hey, Daniel. I see you’re entertaining Emma with one of our old stories."
            "{i}Daniel stiffened slightly, surprised by my calm demeanor. I kept my tone light and friendly, even though I was burning with anger inside.{/i}"
            d "Just sharing a bit of nostalgia, Alex."
            scene w_139 with dissolve
            "{i}I turned to Emma, giving her a reassuring smile.{/i}"
            a "You know, Emma, Daniel has a knack for storytelling. But he tends to exaggerate a bit."
            a "The truth is, we were all horsing around by the lake, and while I did trip, it wasn’t as dramatic as he makes it sound."
            scene w_140 with dissolve
            $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
            "{i}Emma’s expression softened, her smile becoming more genuine.{/i}"
            e "Really? So, what actually happened?"
            scene w_138 with dissolve
            "{i}I chuckled, glancing at Daniel, who was starting to look a bit uncomfortable.{/i}"
            a "Well, I did trip, but it was because Daniel pushed me as a joke. We all ended up in the water, laughing. No harm done."
            a "Right, Daniel?"
            "{i}Daniel’s jaw tightened, but he forced a smile.{/i}"
            d "Yeah, something like that."
            "{i}I patted his shoulder, maintaining my friendly facade.{/i}"
            a "Come on, Daniel, don’t look so serious. It’s all in good fun."
            scene w_139 with dissolve
            "{i}I turned to Emma, making a light-hearted comment to defuse any lingering tension.{/i}"
            a "You know, I think Daniel might be a better comedian than storyteller."
            scene w_140 with dissolve
            $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
            "{i}Emma laughed, genuinely this time, and Daniel’s expression turned sour. He couldn’t hide his irritation any longer.{/i}"
            scene w_141 with dissolve
            "{i}He turned and walked away, his irritation clear. I watched him go, feeling a sense of triumph.{/i}"
            d "Well, I’ve got other things to do. Enjoy your afternoon."
            a "Don’t take it to heart, Daniel. Just a bit of fun."
            "{i}Daniel didn’t respond, disappearing into the house.{/i}"
            a_ "I did it. I didn’t let him get to me, and I handled it calmly. Maybe I’m finally learning."
            $ alex_power = AlexPowerAdd()
            scene w_142 with dissolve
            "{i}I turned back to Emma, who was looking at me with a mix of surprise and satisfaction.{/i}"
            "{i}Emma stood there, looking at me with a mix of surprise and curiosity. Her arms were crossed, but there was a hint of a smile playing at the corners of her lips.{/i}"
            e "Who are you, and what have you done with Alex?"
            "{i}Her tone was playful, but I could hear the underlying seriousness. She couldn’t believe I had managed to stay calm and collected.{/i}"
            a "Very funny, Emma. People can change, you know."
            "{i}I tried to keep my voice light, matching her tone. Inside, though, I was still fuming.{/i}"
            a_ "I wanted to punch him. I wanted to wipe that smug look off his face. But I didn’t. I held back."
            e "Seriously, Alex. I’ve never seen you handle a situation like that before. You were always so quick to anger, so jealous."
            "{i}I took a deep breath, trying to maintain my composure.{/i}"
            a "I guess I’ve been doing some thinking. Trying to be better."
            "{i}She looked at me, her eyes searching mine for the truth.{/i}"
            e "Why now? Why this sudden change?"
            "{i}I hesitated. I couldn’t tell her the real reason. I couldn’t admit that I was still burning with anger inside, that I was just barely holding it together.{/i}"
            a "I realized I’ve made a lot of mistakes. I’m trying to fix things."
            "{i}Emma nodded slowly, still looking skeptical but less tense.{/i}"
            e "Well, I have to admit, I’m impressed. But you know we’re just pretending, right? In a year, it’ll be official."
            "{i}Her tone was gentle, yet firm. I nodded, feeling a pang of sadness mixed with my still-simmering anger.{/i}"
            a "I know, Emma. I know."
            "{i}She sighed, her expression softening a bit more.{/i}"
            e "I’m glad you handled it well today."
            a "I’ll keep trying."
            "{i}Emma offered a small smile in return, then turned to head back inside. I watched her go, feeling a mixture of hope and frustration.{/i}"
            a_ "I did it this time. But can I keep this up? Can I really change?"
            scene black with dissolve
            "{i}As I stood there alone, I couldn’t shake the feeling of victory, however small. I had managed to control my temper, and it felt like a step in the right direction.{/i}"    

    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_326 with fade
    "{i}As the morning passed, the sun climbed higher in the sky, casting its bright rays over the mansion and warming the grounds.{/i}"
    "{i}I had spent most of the late morning wandering through the estate, getting a feel for the place that was now my home.{/i}"
    "{i}I knew that living here for a year would be a challenge, but the potential reward made it worth the effort. As noon approached, I made my way back inside.{/i}"
    scene w_149 with fade
    "{i}When I entered the dining room, the atmosphere was a mix of tension and curiosity. Daniel sat on the other side of the table, his expression always serious, distracted by his phone.{/i}"
    "{i}Isabella, with her stunning beauty, sat in front of Emma, looking bored but attentive to anything that might happen. I sat next to Emma, trying to ignore the tension in the air.{/i}"
    d "Isabella, have you decided on the plans for tomorrow? "
    isa "Hmm? Oh, I suppose I should look into that. I've been so busy with... other things."
    "{i}Her eyes flicked to her phone, then back to Daniel with a hint of disdain. It was clear that their marriage was more about appearances than genuine affection.{/i}"
    "{i}Daniel seemed accustomed to Isabella's disinterest, his focus unwavering as he continued typing away.{/i}"
    "{i}I glanced at Emma, who seemed distant, lost in her own thoughts.{/i}"
    a_ "I need to talk to her, try to bridge the gap that's been growing between us."
    "{i}I decided to break the ice, hoping to ease the tension a bit.{/i}"
    a "So, Emma, how's the new painting coming along?"

    if alexemmaanddanieljealousday1:
        e "*with a cold tone* It's fine, Alex. Just fine."
        "{i}She didn't look at me, her focus remaining on the table in front of her.{/i}"
        a "I see. Well, if you need anything, just let me know."
        e "I doubt I will, but thanks."
        "{i}Her coldness was a stark reminder of the damage my temper had caused.{/i}"
        scene w_150 with dissolve
        "{i}I tried to focus on the meal, but my thoughts kept drifting back to the strained atmosphere in the room.{/i}"
        e "Thank you, Ruby. The food looks great."
        "{i}Emma's voice was calm but distant, a clear sign she was still upset. I glanced over at her, hoping to catch her eye, but she was focused on her plate.{/i}"
        d "So, Alex, how was your day? Managed to get settled in alright?"
        a "Yeah, it's been... interesting. Still trying to get used to everything around here."
        d "{i}*with a smile*{/i} I'm sure you'll get the hang of it. It's a big place, but you'll find your way."
        "{i}Daniel's tone was overly friendly, almost patronizing. I could sense the underlying tension in his words.{/i}"
        d "Emma, you should show Alex around more. He's our new guest after all. It'd be nice for him to get to know everyone properly."
        e "{i}*coldly*{/i} I think Alex can manage on his own."
        scene w_151 with dissolve
        "{i}Her response was sharp, making the atmosphere even more uncomfortable. I felt a surge of frustration but tried to keep my composure.{/i}"
        d "{i}*smirking*{/i} Well, it's important to make everyone feel welcome, don't you think?"
        a "Of course. I'm sure I'll figure things out."
        "{i}Daniel's subtle digs were starting to get under my skin, but I couldn't afford to react. Not here, not now.{/i}"
        d "You know, Alex, Emma is quite knowledgeable about the estate. She could be a great help to you if she wanted to be."
        "{i}I could see what he was doing, trying to drive a wedge deeper between Emma and me. Before I could respond, Isabella finally looked up from her phone.{/i}"
        isa "Alex, didn't you use to be a boxer? I remember seeing some impressive matches of yours."
        a "Yeah, that was a while ago."
        isa "You were really something. Strong, determined... quite interesting."
        "{i}Her sudden interest was a welcome distraction from Daniel's needling. I turned my attention to her, grateful for the shift in focus.{/i}"
    else:
        e "It's going well, thanks for asking. I've been finding a lot of inspiration here, surprisingly."
        "{i}She smiled politely, though there was still a hint of coolness in her tone.{/i}"
        a "That's great to hear. This place does have a certain charm, doesn't it?"
        e "It does. Hopefully, it'll help me create something really special."
        "{i}Our conversation was civil, but the underlying tension remained. Emma’s coldness was a stark reminder of the damage my temper had caused.{/i}"
        d "So, Alex, how are you finding the mansion? Quite the place, isn’t it?"
        a "Yes, it’s impressive. A bit overwhelming at first, but I’m getting used to it."
        d "{i}*leaning back, casually*{/i} It does have that effect on newcomers. But it grows on you. The history, the grandeur... there’s a certain charm to it."
        e "Charm isn’t exactly the word I’d use."
        "{i}I glanced at Emma, her tone cutting through the pretense of pleasantries. Daniel, however, didn’t miss a beat.{/i}"
        d "Oh, come on, Emma. It’s not all bad. There’s a lot of character here."
        scene w_150 with dissolve
        "{i}I could see Daniel’s subtle smirk as he spoke. He was enjoying this, using the opportunity to undermine me while appearing the gracious host.{/i}"
        a "I suppose every place has its quirks. What about the stories? They say this place is haunted."
        d "Ah, the ghost stories. Adds a bit of excitement, don’t you think? Keeps things interesting."
        e "Interesting isn’t how I’d describe it. More like unnerving."
        d "{i}*with a chuckle*{/i} Maybe. But it’s all part of the experience, right? Besides, I’m sure Alex can handle a few spooky tales."
        scene w_151 with dissolve
        "{i}Daniel’s attempt to win Emma over while subtly jabbing at me was clear. I struggled to find a way to respond without falling into his trap.{/i}"
        a "I’m not too worried about ghosts. It’s the living that concern me more."
        d "{i}*smirking*{/i} Wise words. Well, if you ever need anything, don’t hesitate to ask. We’re all family here, after all."
        "{i}Just as I was about to respond, Isabella finally looked up from her phone, her eyes locking onto mine.{/i}"
        isa "You know, Alex, I remember hearing about your boxing days. You were quite the fighter, weren’t you? Very interesting indeed."
        "{i}Her tone was loaded with an underlying intent that I couldn’t quite place, but it was a welcome distraction from Daniel’s thinly veiled provocations.{/i}"
        isa "I bet you have some fascinating stories from those days. Care to share any with us?"

    "{i}I glanced at Emma and then back at Isabella, wondering what her sudden interest was really about.{/i}"
    "{i}The atmosphere around the table grew even more charged as everyone awaited my response.{/i}"
    a " I was actually preparing for a fight that would qualify me for a shot at the national title. It was sanctioned by the World Boxing Association."
    "{i}As I started to recount the story, my mind drifted back to those intense training days.{/i}"
    "{i}I was explaining how my weight control was a mess, and I had to work extra hard to get back on track.{/i}"
    a "So, there I was, trying to cut weight while also keeping my strength up. It was a nightmare."
    isa "That must have been tough. How did you manage it?"
    scene w_152 with dissolve
    "{i}Just as I was getting into the details, Ruby appeared by my side with a plate of food. I hadn't noticed her approaching because I was so engrossed in the story.{/i}"
    "{i}Ruby, the mansion's cook and housekeeper, had a knack for moving silently.{/i}"
    r "Excuse me, Mr. Alex. Here’s your dinner."
    "{i}Ruby was an attractive woman, with her large, expressive eyes and full lips. She had a warm presence that made the mansion feel a bit more like home.{/i}"
    scene w_153 with dissolve
    "{i}However, it was impossible to ignore her other, more prominent features.{/i}"
    a "Oh, sorry, Ruby. I didn't see you there. "
    "{i}As Ruby leaned forward to place the plate in front of me, my eyes involuntarily drifted to her chest. Her breasts were large and barely contained by her top.{/i}"
    a_ "Damn, those are some serious boobs. They're really incredible, and they look delicious too"
    a "Thanks for the food, Ruby."
    r "You’re welcome, Mr. Alex."
    "{i}I tried to refocus on the conversation, but the sight of Ruby's cleavage was burned into my mind.{/i}"
    a_ "Focus, Alex. You can't let your thoughts distract you right now."
    scene w_154 with dissolve
    "{i}Ruby moved to Daniel's side, placing his plate in front of him. Her presence was calm and professional, but I could sense the unease as she interacted with him.{/i}"
    "{i}Daniel had a way of making people uncomfortable, and Ruby was no exception.{/i}"
    d "Thank you, Ruby. You know, I’ve always wondered how someone like you ended up working here. Did you just get lost on your way to a real job?"
    "{i}Ruby flinched at his words but tried to maintain her composure. She was used to his jabs, but that didn’t make them any less hurtful.{/i}"
    r "I enjoy my work here, Mr. Daniel. It’s a good job, and I’m proud of what I do."
    d "Proud, huh? Proud of cleaning up after us and cooking our meals? Sounds like you're aiming real high, Ruby. Ever think about what else you could be doing with your life?"
    "{i}Ruby’s eyes darted around the room, searching for an escape from Daniel’s relentless mockery. She took a deep breath and tried to defend herself.{/i}"
    r "I’m good at what I do, and not everyone has the same opportunities. I’m happy with my work, and I do it well."
    d "Happy? Really? Is that what you tell yourself every night? That you're \"happy\" mopping floors and serving food?"
    d "Maybe you should aim a bit higher. Oh, wait, I forgot – aiming higher might be a bit too much for you."
    "{i}Ruby’s face tightened, and she opened her mouth to respond, but the words seemed to stick in her throat. Daniel’s smirk grew wider, sensing her discomfort.{/i}"
    d "Come on, Ruby, don’t be shy. Tell us more about your lofty ambitions. Or is this it? Is this the peak of your career?"

    $ alexprotectrubyday1 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}Remain silent{/size}{/font}":
            $ alexprotectrubyday1 = False

            "{i}Emma stayed silent, her eyes fixed on her plate. I couldn't tell if she was uncomfortable or just uninterested.{/i}"
            "{i}As Ruby leaned over to place the plate, her ample cleavage was hard to ignore Daniel noticed Ruby’s discomfort and seized the moment to further humiliate her.{/i}"
            d "Ruby, you really should be more careful. Wouldn't want to spill anything on that... lovely blouse of yours."
            r "I'm sorry, Mr. Daniel. I'll be careful."
            d "You always say that, don't you? It's a wonder you manage to keep this place in order."
            "{i}Isabella giggled, finding amusement in Daniel's mocking. Emma’s expression remained unreadable.{/i}"
            isa "Yes, Ruby. Maybe you should pay more attention to what you're doing. Or maybe get clothes that fit better?"
            scene w_156 with dissolve
            "{i}Ruby, visibly upset, finished setting the plate and turned to leave. As she walked away, I noticed the glint of tears in her eyes.{/i}"
            "{i}I remained silent, unsure whether Emma found this amusing or if she was simply indifferent.{/i}"
            "{i}I decided it was safer to let Daniel continue rather than risk becoming his next target.{/i}"
            d "Relax, everyone. It's all in good fun. Just a little joke, right?"
            "{i}No one at the table responded, the air thick with discomfort. Ruby's silent exit left a heavy feeling in my chest.{/i}"
            "{i}Daniel's laughter echoed in my ears, mingling with the guilt of my own inaction.{/i}"
        "{font=fonts/hatten.ttf} {size=50}Protect Ruby{/size}{/font}":
            $ alexprotectrubyday1 = True

            "{i}As Ruby leaned over to place the plate, her ample cleavage was hard to ignore Daniel noticed Ruby’s discomfort and seized the moment to further humiliate her.{/i}"
            d "Ruby, you really should be more careful. Wouldn't want to spill anything on that... lovely blouse of yours."
            "{i}Ruby’s face flushed with a mix of embarrassment and frustration. She looked down, avoiding eye contact, her hands trembling slightly as she clutched the serving tray.{/i}"
            "{i}I had enough. Daniel's smugness and constant need to belittle others were infuriating. I couldn’t stand by and watch Ruby suffer.{/i}"
            a "That's enough, Daniel. You're being an idiot. There's no reason to treat Ruby like that."
            scene w_155 with dissolve
            "{i}Ruby looked at me, her eyes wide with surprise and gratitude. She didn’t say anything, perhaps out of fear of making the situation worse, but her silent appreciation was clear.{/i}"
            d "Oh, look who's playing the knight in shining armor. This is just some harmless fun, Alex. Lighten up."
            "{i}Before I could retort, Emma chimed in.{/i}"
            e "Daniel, there are other ways to joke with people. This wasn't necessary."
            "{i}Isabella, who had been quietly observing the exchange, leaned in and whispered something under her breath. I barely caught it, but it sounded like,{/i}"
            isa "{i}*whispering*{/i} Emma, you're such a loser."
            "{i}It was unclear if anyone else heard Isabella’s comment. I chose to ignore it for the moment, focusing on Daniel instead.{/i}"
            scene w_157 with dissolve
            "{i}Ruby, deciding it was best to leave the scene, nodded subtly at me before exiting the room, her posture more confident than before.{/i}"
            "{i}Daniel’s expression shifted from amusement to irritation.{/i}"
            a "Harmless fun? Making someone feel like shit isn't fun, Daniel. You need to grow up."
            d "Whatever you say, hero. Just remember, this isn't your house. You don't make the rules here."
            "{i}I felt a surge of satisfaction for standing up for Ruby. However, Emma’s reaction left me uncertain. Did she appreciate my intervention, or was she feeling jealous?{/i}"
            $ alex_power = AlexPowerAdd()
            "{i}I couldn’t tell. Her expression was unreadable as she stared at her plate, lost in thought.{/i}"
    
    scene w_162 with dissolve
    "{i}The dining room was filled with an uneasy silence as Daniel and I resumed our conversation. We had just moved into the mansion, and the idea of spending a whole year here was daunting.{/i}"
    "{i}Daniel, ever the instigator, broke the silence with his usual smirk.{/i}"
    scene w_158 with dissolve
    d "So, Alex, we've barely unpacked, and we already have a year ahead of us in this place. Quite the commitment, don't you think?"
    scene w_160 with dissolve
    a "Yeah, it's definitely going to be a test. But if we can make it through, selling this place for a good profit will be worth it."
    scene w_158 with dissolve
    d "True. The plan is solid—stay here for a year, make some improvements, then sell it off and split the profits. Simple enough."
    scene w_160 with dissolve
    a "Simple on paper, sure. But living together in this mansion, dealing with each other daily... that's where it gets tricky."
    scene w_158 with dissolve
    d "And then there's the added spice of this place's reputation. Haunted mansion? Really? Who even believes that crap?"
    scene w_160 with dissolve
    "{i}I shrugged, the eerie tales not lost on me, even if I didn’t fully believe them.{/i}"
    a "People love a good ghost story. But yeah, those rumors could definitely make things harder when we try to sell."
    scene w_158 with dissolve
    "{i}Daniel's expression turned more serious, his mind clearly working through the implications.{/i}"
    scene w_159 with dissolve
    d "We need to squash those rumors. Find out where they started and put an end to them. We can't let superstitions ruin our plans."
    scene w_160 with dissolve
    a "Agreed. Maybe we start by talking to some locals, see if they know anything about the history of this place and these ghost stories."
    scene w_159 with dissolve
    d "Good idea. And who knows, maybe we’ll uncover something interesting. Though I'd prefer if it's just some old wives' tales."
    scene w_161 with dissolve
    a "Let’s hope it’s nothing more than that. The last thing we need is a real ghost story to deal with."
    scene w_159 with dissolve
    d "Well, if there is something, at least we’ll have an adventure to keep us entertained."
    scene w_162 with dissolve
    "{i}The conversation shifted slightly as Emma, who had been quietly observing, decided to chime in. She always had a knack for bringing a different perspective, even if it was sometimes unwelcome.{/i}"
    e "You know, maybe the haunted rumors could work in our favor. People love that kind of stuff—might even drive up the price for the right buyer."
    "{i}Daniel raised an eyebrow, a glint of amusement in his eyes as he considered her suggestion.{/i}"
    d "Interesting angle, Emma. Though I doubt Alex is keen on playing host to ghost hunters."
    a "It’s an idea, though I’d prefer if we didn’t have to rely on ghost stories to sell this place."
    a "But if it comes to that, we might as well use every advantage we have."
    "{i}Isabella, who had been engrossed in her phone, suddenly looked up, her expression one of feigned interest mixed with mild irritation.{/i}"
    isa "As long as it doesn't involve any actual ghosts disturbing my beauty sleep, I’m fine with whatever plan you two cook up."
    a_ "That’s Isabella for you. Always focused on herself. This year is going to be a real test, for all of us."
    scene w_166 with fade
    "{i}Daniel and Isabella left the dining room together, their footsteps echoing down the hallway. Daniel's hand rested casually on Isabella's lower back, guiding her towards the deeper recesses of the mansion.{/i}"
    scene w_163 with dissolve
    "{i}Their departure was marked by a low murmur of conversation and the occasional, dismissive laugh from Isabella.{/i}"
    "{i}Their retreat into the shadows of the house left an air of mystery behind them, as if they were planning something or merely enjoying their shared moments away from the rest of us.{/i}"
    scene w_166 with dissolve
    "{i}...{/i}"
    scene w_165 with dissolve
    "{i}Emma, on the other hand, slipped out quietly and alone, her figure silhouetted against the glass doors as she made her way to the garden.{/i}"
    scene w_164 with dissolve
    "{i}She moved with a purpose, her posture rigid, as if she needed the fresh air to clear her thoughts.{/i}"
    "{i}I watched her for a moment, wondering what thoughts were running through her mind.{/i}"
    scene w_165 with dissolve
    "{i}***Left alone in the dining room, I mulled over my options. The tension still clung to the air, and I needed a distraction.{/i}"
    a_ "Should I try to talk to Emma? No, she needs her space right now."
    scene w_166 with dissolve
    "{i}My eyes drifted towards the kitchen, where I spotted Ruby diligently washing the dishes.{/i}"
    scene w_167 with dissolve
    "{i}The sight of her from afar, focused and quiet, drew me in. She had been through enough tonight, thanks to Daniel's cruel humor.{/i}"
    a_ "Maybe I should go and check on her, make sure she’s alright."
    "{i}With a deep breath, I decided to approach her.{/i}"
    "{i}I walked towards the kitchen, my footsteps soft against the tiled floor.{/i}"
    scene w_168 with dissolve
    $ renpy.music.play("audio/sfx/sfx_bottle.wav", channel="sfxloop1", relative_volume=0.1)
    $ renpy.music.play("audio/sfx/sfx_shower_hallway.ogg", channel="sfxloop2", relative_volume=1.0)
    "{i}Ruby was at the sink, her back to me, washing the dishes with a quiet focus.{/i}"
    "{i}The room was filled with the gentle clinking of plates and the soothing sound of running water. As I approached, my thoughts drifted back to the sight of her earlier, her voluptuous figure accentuated by her low-cut blouse.{/i}"
    a_ "Ruby is really something else. Those curves, her full, round hips, and that ass... God, she's got such a perfect ass. And her breasts... I wonder if I stand a chance with her."
    a_ "She must know how sexy she is, the way she moves, the way she carries herself. It drives me wild."
    "{i}I watched her from behind, her movements fluid and graceful despite the mundane task. Her ample hips swayed slightly as she scrubbed a plate, and I couldn't help but let my eyes trace the curve of her backside.{/i}"
    "{i}The fabric of her skirt hugged her figure tightly, leaving little to the imagination. The sight of her made my heart race, and I felt a familiar longing stir within me.{/i}"
    a_ "I wonder what she'd be like in bed, with all those luscious curves. Could I make her mine, even just for a night? It’s hard to resist someone like her."
    a_ "Those breasts... they'd be perfect to hold, to kiss. And her ass, I bet it feels amazing. I need to find a way to get closer to her, to see if there's a spark there."
    a_ "Okay, Alex, think. You can’t just stand here ogling her. Say something, make a move."
    scene w_169 with dissolve
    a "Hey Ruby, I just wanted to say thanks for the dinner. It was really good. You always make the best meals."
    "{i}She turned her head slightly, a look of mild surprise crossing her face before she composed herself and offered a small smile.{/i}"
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.stop("sfxloop2", fadeout=2.0)
    scene w_170 with dissolve
    r "Oh, thank you, Mr. Alex. I'm glad you enjoyed it."
    "{i}I leaned against the counter, trying to appear relaxed and friendly.{/i}"
    a "So, how's everything going? Must be a lot of work keeping this place in order, huh?"
    scene w_171 with dissolve
    r "It can be, but I don't mind. It keeps me busy, and I like making sure everyone has what they need."
    a "I bet. You've been doing a great job, though. The place looks spotless. Do you ever get any time to relax?"
    scene w_170 with dissolve
    r "Not as much as I'd like, but I find little moments here and there. It’s nice to have a quiet evening once in a while."
    a "So, Ruby, do you live in the village, or do you stay here at the mansion?"
    scene w_171 with dissolve
    r "I actually live here in the mansion. It’s more convenient with all the work I have to do."
    "{i}Her response carried a hint of something deeper, but I decided not to press her just yet.{/i}"
    a "I see. It must be quite an experience, living in a place like this. What do you think of the village?"
    r "The village is nice. It’s quiet and the people are friendly. But there's something about the mansion... it has its own charm, despite everything."
    a "Yeah, it does have a unique atmosphere. I guess it's not just the mansion that makes it special, but the people in it too."

    if alexprotectrubyday1:
        scene w_170 with dissolve
        "{i}Ruby offered a small smile, her eyes showing appreciation for my words.{/i}"
    else:
        "{i}Ruby continued seriously, her eyes showing appreciation of the intentions of my words.{/i}"
    
    a "I met one of the neighbors the other today, Eleanor. Do you know her?"
    scene w_171 with dissolve
    "{i}Ruby’s tone remained neutral, but there was a subtle tension beneath her polite demeanor.{/i}"

    if alexflirteleanorday1:
        a "I helped her out with a light in her kitchen. She seemed like a nice person."
        r "That's good of you, Alex. It’s always nice to help out neighbors."
    else:
        a "Do you know much about her? What’s she like?"
        r "I don’t know her personally, but from what I’ve heard, she keeps to herself. She’s always seemed polite from a distance."
        "{i}There was something in Ruby’s eyes as she spoke, a flicker of something deeper, but she remained composed and polite.{/i}"

    "{i}Standing in the kitchen, I decided to address what had happened earlier with Daniel. Ruby deserved to know someone cared about her well-being.{/i}"
    a "Ruby, are you okay after what happened with Daniel at dinner?"
    
    if alexprotectrubyday1:
        scene w_173 with dissolve
        "{i}Ruby's face softened, a genuine smile spreading across her lips.{/i}"
        r "Thank you for standing up for me, Mr. Alex. It means a lot."
        "{i}I took a step closer, trying to seem both supportive and interested.{/i}"
        a "Of course, Ruby. No one deserves to be treated like that. If you ever need anything, or just want to talk, you can count on me."
        r "That’s very kind of you, Mr. Alex. I really appreciate it."
        a "It's nothing, really. You deserve to be treated with respect. And, honestly, I enjoy our conversations."
        a_ "Ruby's definitely warming up to me. Maybe there's a chance to get closer to her."
        "{i}Ruby nodded, her smile lingering as she returned to her work.{/i}"
        scene w_170 with dissolve
        "{i}I watched her for a moment, feeling both protective and intrigued.{/i}"
        r "Thank you, Mr. Alex. It’s nice to have someone to talk to."
    else:
        scene w_172 with dissolve
        "{i}Ruby paused, turning to face me with a polite but firm expression.{/i}"
        r "I appreciate your concern, Mr. Alex, but there's no need to worry about me. I can handle myself."
        "{i}Her words were kind, but there was an undercurrent of disappointment that stung a little.{/i}"
        a_ "Ah, she’s got a point. Maybe I should have spoken up earlier. Still, I can't help but feel bad for her."
        a "Alright, Ruby. But if you ever need anything, I'm here."
        r "Thank you, Mr. Alex. I’ll keep that in mind."
    
    $ alexflirtrubyday1 = False
    
    menu:
        "{font=fonts/hatten.ttf} {size=50}Comment on her beautiful body.{/size}{/font}":
            $ alexflirtrubyday1 = True

            "{i}As we continued our conversation in the kitchen, I decided to take a chance and compliment Ruby. She had been through a lot tonight, and I wanted to lift her spirits.{/i}"
            a "You know, Ruby, I have to say, you look amazing. All that hard work really shows."
            scene w_171 with dissolve
            r "Thank you, Mr. Alex. That's very kind of you to say."
            "{i}I took a step closer, trying to keep the mood light and friendly.{/i}"
            a "I mean it. You're in great shape, and it’s impressive. Not many people have that kind of dedication."
            scene w_172 with dissolve
            "{i}Ruby's smile faltered a bit, and she shifted uncomfortably.{/i}"
            r "I appreciate it, but I really should get back to work. There's still a lot to do."
            a "Come on, Ruby. You've done enough for tonight. You deserve to relax and maybe enjoy some company."
            r "Mr. Alex, I really need to finish up here. Thank you for your concern, but I'm fine."
            a "Alright, alright. I didn't mean to make you uncomfortable. I just wanted to make sure you're okay."
            scene w_171 with dissolve
            r "I understand. Thank you, Mr. Alex."
            "{i}Feeling the tension in the air, I decided it was best to leave her to her work.{/i}"
            a "I'll head back to my room. Have a good night, Ruby."
            scene black with dissolve
            "{i}As I left the kitchen, I couldn't shake the feeling of regret. I needed to be more careful with my approach..{/i}"
        "{font=fonts/hatten.ttf} {size=50}Comment on her good work.{/size}{/font}":
            $ alexflirtrubyday1 = False

            a "Ruby, I have to say, the effort you put into this place is incredible. You really keep everything running smoothly, and it shows."
            scene w_170 with dissolve
            "{i}Ruby’s face lit up with a genuine smile, her eyes reflecting a mixture of surprise and gratitude.{/i}"
            r "Thank you, Mr. Alex. That means a lot to me. I take pride in what I do."
            "{i}I took a step closer, maintaining a respectful distance, and continued to praise her.{/i}"
            a "You should. It’s not easy managing a place this big, and you do it with such grace and dedication. We're all lucky to have you here."
            scene w_173 with dissolve
            "{i}Ruby blushed, clearly flattered by the compliments. She looked down for a moment, her smile shy but pleased.{/i}"
            r "You're very kind, Mr. Alex. I just try to do my best."
            a "It really shows, Ruby. You go above and beyond, and it doesn’t go unnoticed."
            r "I really appreciate your kind words."
            a "Well, I should probably head to my room and let you finish up here. Have a good night, Ruby."
            scene w_170 with dissolve
            r "Good night, Mr. Alex. And thank you again."
            scene black with dissolve
            "{i}As I left the kitchen, I couldn't help but feel a sense of accomplishment. Ruby’s genuine smile and the gratitude in her eyes made me feel like I had done something right.{/i}"
            a_ "She really is incredible. It’s nice to know she appreciated what I said."
            "{i}Her shy smile and the way she blushed at my compliments lingered in my thoughts.{/i}"
    
    scene w_326 with fade
    "{i}I stayed for a while longer, chatting with Ruby, feeling the bond between us grow stronger. There was something about her that drew me in, and I was determined to see where this newfound connection could lead.{/i}"
    "{i}I walked back to my room after that awkward attempt at flirting with Ruby.{/i}"
    scene w_526 with fade
    a_ "Yeah, that didn’t go as planned. Smooth, Alex. Real smooth."
    scene w_527 with dissolve
    "{i}The hallway felt longer than usual, my mind replaying every moment like a bad movie scene on repeat.{/i}"
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    scene w_525 with dissolve
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    "{i}As I reached my door, I pushed it open and found Emma standing there, her eyes fixated on some painting on the wall. I hadn’t even noticed that damn thing before.{/i}"
    a_ "Why does she always look like she’s analyzing something? What is she thinking right now?"
    scene w_445 with dissolve
    "{i}I leaned against the door frame, watching her for a moment. There was something about the way she observed things that always threw me off.{/i}"
    scene w_449 with dissolve
    "{i}I could already tell by her stance that she was deep in thought, probably overanalyzing it—something I’d never understand.{/i}"
    "{i}She didn’t even turn around to acknowledge me, just kept staring like she was in some kind of trance.{/i}"
    scene w_450 with dissolve
    e "Are you going to just stand there, or do you actually have something to say?"
    scene w_449 with dissolve
    "{i}She shot me a look, but didn’t turn away from the painting.{/i}"
    a_ "What does she really see in that thing? Or maybe she's just trying to distract herself... or distract me?"
    scene w_451 with dissolve
    a "Uh... yeah, I mean... what even is this? Is it, like, a lady-octopus thing? I don't get it."
    scene w_453 with dissolve
    "{i}I knew what was coming. She was going to school me on this, like always.{/i}"
    scene w_450 with dissolve
    e "A lady-octopus thing. That’s your brilliant observation?"
    "{i}I shrugged, keeping it casual. What else was I supposed to say? It *was* weird.{/i}"
    scene w_451 with dissolve
    a "I mean... yeah, it’s weird, right?"
    a "She’s got this crazy hair, and then—bam—tentacles? Like, what's she supposed to be? Some kind of sea witch?"
    "{i}I glanced at Emma. She had that look, the one that said I didn’t get it—like I was supposed to be seeing something profound in those tentacles.{/i}"
    "{i}I shrugged, keeping it casual. What else was I supposed to say? It *was* weird.{/i}"
    scene w_452 with dissolve
    e "It’s more than just a 'sea witch,' Alex. It’s about... I don’t know, duality. Chaos. Control. Maybe even power."
    a "Power?"
    a "Uh, sure, if you say so. But, come on, you can’t deny it looks kinda... offbeat. Like something out of a creepy comic book."
    "{i}Sure, I could humor her. But deep down, I just didn’t see it. She stared at me, waiting for something. I fumbled for words.{/i}"
    scene w_454 with dissolve
    e "You know what, Alex? If you can’t handle something deeper than a comic book, maybe you should stick to the shallow end of the pool."
    scene black with fade
    a_ "What did I do? Come on Emma, ​​I'm trying. Like something out of a scary comic book... Why are you mad at me... God, what do I have to do?"    

    jump day2_alex_1
