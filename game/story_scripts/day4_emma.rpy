label day4_emma_1:

    $ emmajealouseleanorday4 = False

    scene black with fade

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 6rd_day with fade
    $ renpy.pause()
    hide 6rd_day with dissolve

    scene w_326 with fade
    "{i}The morning sunlight streamed softly through the curtains, warming the vast, polished floors of the corridor as I made my way out of the room.{/i}"
    "{i}There was a lingering feeling from the night before, like something had happened, but it felt hazy, veiled in a mist that wouldn’t quite clear.{/i}"
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    scene w_773 with fade
    e_ "What was that? It feels like… like a memory, but one that’s trying too hard to slip away. I remember going to bed upset with Alex… yet…"
    o "Oh, come on, Em. Don’t you love a little mystery? Maybe you had a bit more fun than you’re giving yourself credit for."
    "{i}I rolled my eyes at the familiar, sly tone that slithered through my mind. Octavia had been creeping back into my thoughts lately, her voice louder than ever.{/i}"
    "{i}This wasn’t the first time she’d stirred something up, pushing me to explore things I’d normally shut down.{/i}"
    "{i}Still, her words left a hint of unease, as though she knew something I didn’t.{/i}"
    e_ "Stop it, Octavia. I’m not interested in your games."
    o "Games? Please, I’m just here to… jog your memory. After all, last night wasn’t exactly dull, was it?"
    scene w_774 with dissolve
    "{i}There was a strange satisfaction in her voice that made me pause mid-step. A shiver crawled up my spine as I reached the end of the hallway.{/i}"
    "{i}For a moment, I almost felt as if something in me had changed overnight, something that wasn’t entirely mine.{/i}"
    e_ "But why can’t I remember?"
    o "Oh, darling, maybe you don’t want to remember. Isn’t it so much easier that way? Less guilt, fewer questions…"
    "{i}I sighed, shaking my head slightly. The feeling was unsettling, like there was a puzzle I couldn’t solve because half the pieces were missing.{/i}"
    scene w_775 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh4.mp3", channel="sfx1", relative_volume=0.3)
    "{i}But I pushed the thoughts aside as I approached the grand staircase.{/i}"
    "{i}The faint hum of conversation drifted up from below. Curiosity nudged me forward.{/i}"
    "{i}As I descended, I saw him.{/i}"
    scene w_776 with dissolve
    "{i}Alex was standing near the entrance with a woman—a woman I didn’t recognize.{/i}"
    "{i}She was stunning, with an effortless allure that made her presence feel… intentional.{/i}"
    "{i}A sudden, sharp pang tugged at my chest, something raw and instinctive.{/i}"
    e_ "Who is she? And why is she standing so close to him?"
    o "Oh, look at them. Cozy, aren’t they? Makes you wonder if he’s been as faithful as he pretends."
    "{i}I bit my lip, ignoring Octavia’s taunting. Yet, the question planted itself in my mind, a dark seed I couldn’t quite shake off.{/i}"
    scene w_777 with dissolve
    "{i}Jealousy simmered beneath my skin, though I tried to keep my face neutral as I continued down the staircase.{/i}"
    e_ "But am I overreacting? Maybe she’s just… a friend. No need to jump to conclusions."
    o "Friend? Honey, I think you and I both know that women don’t just stand that close to men without a reason."
    "{i}Octavia’s words echoed in my mind, a whisper that felt too close to the truth. Still, I had to be sure.{/i}"
    "{i}I could approach with calm, act like nothing was wrong—or I could confront him directly, let the suspicion show.{/i}"
    "{i}By the time I reached the last step, my fists were clenched, heart racing with indecision.{/i}"

    $ emmajealouseleanorday4 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}I could approach with calm{/size}{/font}":
            $ emmajealouseleanorday4 = False
            "{i}I took a deep breath as I walked toward the entryway, feeling a mix of curiosity and tension.{/i}"
            "{i}Alex was standing there with a woman I hadn’t met, her laughter lingering as I got closer.{/i}"
            "{i}Maybe it was just the strange dream I’d woken up from lingering in my mind, fogging my emotions.{/i}"
            "{i}I put on my friendliest smile, though my mind raced with a mix of questions. Something about this morning felt… off.{/i}"
            "{i}Maybe it was the strange, fragmented dream I’d had. I couldn’t quite remember it, but it felt like I’d been someone else for a moment, or that someone else had been in my mind.{/i}"
            o "Or maybe you’re just unsettled seeing him with another woman. A gorgeous woman, I might add…"
            "{i}Octavia’s voice, sly and unsettling as always, slipped into my mind with her usual bite.{/i}"
            scene w_778 with dissolve
            e "Good morning,"
            "{i}Alex blinked in surprise, but the woman smiled easily, turning to me with a warm expression.{/i}"
            a "Emma? Have you woken up yet?"
            e "Yes. Who is our guest, Alex?"
            scene w_779 with dissolve
            a "Emma, ​​this is Elanor. She and her husband are our neighbors."
            "{i}My eyes drifted to the woman, assessing her.{/i}"
            scene w_780 with dissolve
            "{i}She extended her hand.{/i}"
            ele "Oh! You must be Emma. I’m Eleanor. It’s a pleasure to finally meet you."
            scene w_781 with dissolve
            "{i}I took her hand, feeling the smoothness of her skin against mine.{/i}"
            "{i}Her grip was firm yet friendly, and her eyes held a hint of charm.{/i}"
            e "Emma, yes. Alex’s wife,"
            "{i}I replied, adding just a touch of emphasis on the last part, my gaze lingering on her face.{/i}"
            e "It’s nice to meet you too."
            e_ "Good girl, let her know who you are. Maybe she’ll back off a little…"
            "{i}Alex cleared his throat, sensing a bit of tension, maybe, or just eager to fill the silence.{/i}"
            a "Uh, Eleanor and her husband Tristan have lived in the neighborhood for a while. We were talking about... uh, getting together someday."
            scene w_785 with dissolve
            ele "Yes, actually! That’s why I stopped by,"
            "{i}Eleanor said, her tone enthusiastic. She looked at me warmly.{/i}"
            ele "I was hoping to invite both of you over for dinner."
            ele "My husband and I love hosting, and we thought it might be a nice way to get to know you both better."
            "{i}The offer caught me off guard, and I glanced at Alex, who seemed just as surprised.{/i}"
            "{i}But there was something genuine in her tone, something that suggested she really wanted to connect, even if Octavia’s voice in my mind remained skeptical.{/i}"
            scene w_786 with dissolve
            e "A dinner? That sounds lovely,"
            ele "Wonderful! Tristan has a passion for wines. He’s something of a collector, actually."
            ele "I know it sounds cliché, but he could go on for hours about each bottle in his collection."
            "{i}She laughed, glancing at Alex.{/i}"
            ele "Do you like wine, Emma?"
            "{i}I felt a little spark of excitement at the mention of wine, a genuine interest peeking through.{/i}"
            e "Yes, guilty as charged. I’m always up for a wine night."
            "{i}I shared a laugh with her, feeling a little of my earlier hesitation fade.{/i}"
            e "It sounds perfect."
            scene w_785 with dissolve
            o "Or maybe just too perfect…"
            o "Why is she being so charming, hmm? What’s her angle?"
            ele "How about this Saturday, then?"
            ele "I’ll speak with Tristan, but I think he’d love the chance to share some of his collection."
            scene w_786 with dissolve
            "{i}She turned to Alex.{/i}"
            ele "And don’t worry, we won’t bore you with wine talk the entire night!"
            a "Hey, as long as Emma’s happy, I’m happy,"
            "{i}Alex replied with a grin, slipping his hand into mine. I could feel his reassurance, and for a moment, I felt that familiar warmth between us.{/i}"
            e "We’d be delighted,"
            ele "Perfect! I’ll let you know the exact time once Tristan finalizes everything,"
            "{i}Eleanor said, her eyes twinkling. She glanced from me to Alex and back, something appreciative in her smile.{/i}"
            ele "I think this is going to be a lot of fun."
            o "She’s definitely up to something. No one is that friendly without a reason…"
            "{i}I kept my smile friendly, deciding to ignore Octavia’s doubts for now.{/i}"
            e "Thank you for the invitation, Eleanor. It sounds like a wonderful evening."
            scene w_787 with dissolve
            ele "The pleasure’s all mine. I’ll make sure it’s a night to remember."
            "{i}She gave one last friendly wave and turned to leave, her heels clicking softly as she walked toward the door.{/i}"
            "{i}I watched her go, a part of me intrigued, another part wary, Octavia’s voice already whispering suspicions into my mind.{/i}"
            $ emma_mental = EmmaMentalAdd()
            scene w_788 with fade
            "{i}The soft echo of Eleanor's footsteps faded down the hallway, leaving the grand entryway strangely empty.{/i}"
            "{i}I caught Alex glancing at me from the corner of my eye, like he was searching for something in my expression.{/i}"
            a "Not a single spark of jealousy, huh? Wow, Emma, I thought you’d be more... possessive."
            scene w_789 with dissolve
            e "Possessive? That’s a bit of a stretch, don’t you think?"
            a "Just seems like the old you would’ve had a thing or two to say about Eleanor, that’s all."
            e "The ‘old me’?"
            e "Alex, it’s not like you gave me a reason to worry. Besides, we’re both here to keep up appearances, right?"
            e_ "Right. Appearances. I’m not about to give him the satisfaction of knowing he got to me."
            o "Good girl. Let him think you don’t care. The last thing he deserves is to see you jealous."
            scene w_791 with dissolve
            a "Right... appearances. Because we have to play the perfect couple for the neighbors, huh?"
            scene w_790 with dissolve
            e "Exactly. Which means a little ‘friendly’ chat with Eleanor won’t break the illusion."
            scene w_791 with dissolve
            a "So you’re saying you don’t care who I talk to, as long as it fits our little act?"
            e "Why would I care? If I remember correctly, you’re the one who insisted on this... arrangement."
            scene w_792 with dissolve
            a "Hey, I didn’t exactly twist your arm. You agreed, didn’t you?"
            e "We both have our reasons. Let’s not pretend it was some fairytale decision."
            e_ "Let him think I’m detached. He doesn't need to know how much I hate seeing him with someone else."
            o "Exactly. Let him believe you’re indifferent. It’s safer that way."
            a "Fair enough. But you’re not even curious about Eleanor? Not one question about where I know her from?"
            scene w_789 with dissolve
            e "Fine. If it matters to you so much, enlighten me. Where did you meet her?"
            e_ "I say it with as much indifference as I can muster, but inside, I want answers. Just... not that he knows that."
            scene w_791 with dissolve
            a "She’s just a neighbor, alright? We met the other day. Her and her husband live nearby."
            e "Convenient. She seems... interested."
            a "Interested? She’s married, Emma. I thought you didn’t care."
            scene w_789 with dissolve
            e "I don’t. I’m just pointing out that your... charm works on more than just your wife."
            e_ "I keep my voice light, casual. But I feel it—this tightening in my chest, knowing how easily he can capture someone’s attention."
            o "Exactly, Emma. Don’t let him see how much you notice."
            a "And here I thought you’d be the one charming everyone. It’s not exactly easy keeping up the image of a ‘happy couple’ on my own, you know."
            scene w_790 with dissolve
            e "Oh, don’t worry, Alex. I’m more than capable of playing my part. I’ve had plenty of practice."
            a "Practice, huh? So this is all just one big show for you?"
            e "Isn’t that what you wanted? Smile for the neighbors, play nice for the inheritance... wasn’t that the plan?"
            e_ "I hold his gaze, daring him to deny it. He knows this arrangement was as much his idea as it was mine."
            scene w_791 with dissolve
            a "Look, I know things haven’t exactly... gone the way we planned."
            e "That’s putting it lightly."
            a "Yeah, well... maybe some things are worth trying for again."
            scene w_789 with dissolve
            e "Trying for... or winning back? Because those are two very different things, Alex."
            e_ "I keep my voice steady, but I feel a flicker of something deeper, something I don’t want to admit."
            o "Don’t let him charm you, Emma. Remember, he’s just words until he proves himself."
            a "What’s the difference? I’m here, aren’t I? Maybe I’m not perfect, but... I’m still here."
            e "..."
            e "Being here isn’t the same as being trustworthy, Alex."
            scene w_791 with dissolve
            a "You think I don’t know that?"
            e "I just... don’t know if you’re capable of proving it. Not after everything."
            e_ "He doesn’t know how much he’s hurt me, and maybe he never will."
            o "Stay strong. Don’t give in so easily.'"
            a "Maybe I am. Maybe I’m just waiting for you to give me a reason to try."
            scene w_790 with dissolve
            e "And maybe I’m waiting to see if you’re worth the risk."
            "{i}I don’t break eye contact, but I can feel his gaze softening, almost as if he’s starting to understand. Or maybe he’s just good at pretending.{/i}"
            scene w_793 with dissolve
            a "So... if I told you that I wanted to change things between us, you’d just stand there with that look? That look that says you don’t believe a word I’m saying?"
            e "Alex, change isn’t a promise. It’s just... words until you actually do something."
            a "Maybe I’m tired of pretending, too."
            o "Don’t fall for it again, Emma."
            "{i}For a moment, I feel my resolve weaken, but I remind myself—he’s said things like this before.{/i}"
            e "Pretending... or trying to fix things?"
            "{i}He moves closer, and this time, I don’t step away. It feels familiar, comforting... and dangerous.{/i}"
            scene w_796 with dissolve
            e "Alex..."
            a "What?"
            e "This doesn’t change anything. I still don’t know if I can... if I can trust you."
            "{i}I pull away before he can say anything more, holding onto the last of my defenses. He can’t just fix things with words, and I won’t be swayed so easily.{/i}"
            scene w_797 with dissolve
            e "Good morning, Alex."
            "{i}I turn away, climbing the stairs with a sense of pride and uncertainty. Maybe he felt closer for a moment, but I can’t afford to lose myself in that hope. Not again.{/i}"
        "{font=fonts/hatten.ttf} {size=50}I could let the suspicion show{/size}{/font}":
            $ renpy.music.stop("music1", fadeout=2.0)
            $ emmajealouseleanorday4 = True

            "{i}I took a deep breath and started down the stairs, my gaze fixed on Alex and the mysterious woman beside him. Something about the scene made my stomach tighten.{/i}"
            "{i}My instincts were screaming, but I kept her face calm, a polite mask forming.{/i}"
            $ renpy.music.play("audio/musics/filaments1.mp3", "music2", fadein=2.0, relative_volume=0.2)
            scene w_778 with dissolve
            "{i}As I reached the last step, both of them turned toward me, Alex's expression flickering with a hint of surprise.{/i}"
            "{i}The woman, however, maintained a warm, unbothered smile that made my suspicion flare.{/i}"
            e "Well, who’s our visitor here, Alex?"
            scene w_779 with dissolve
            "{i}A slight edge crept into my voice, and I didn’t bother to mask it.{/i}"
            a "Oh, Emma, this is Eleanor. She...uh, stopped by for a visit."
            scene w_780 with dissolve
            ele "Pleasure to meet you, Emma,"
            "{i}Eleanor extended her hand, her smile not wavering.{/i}"
            scene w_782 with dissolve
            e_ "I know that kind of smile. She's comfortable, too comfortable."
            "{i}My eyes flicked down to Eleanor's outstretched hand but didn't move to take it.{/i}"
            scene w_783 with dissolve
            e "Emma. Alex's wife."
            "{i}The words came out crisp, pointed.{/i}"
            "{i}Eleanor chuckled softly, withdrawing her hand with a graceful nod, unfazed.{/i}"
            scene w_784 with dissolve
            ele "Ah, of course. I've heard so much about you. It’s always nice to put a face to the name."
            e_ "Heard so much about me? From who exactly?"
            o "Careful, darling. She's too smooth. Bet she's one of those women who thinks any man is fair game."
            "{i}I straightened, feeling Octavia’s voice prodding her. It was as if Octavia was right there beside me, planting seeds of doubt and pushing her buttons.{/i}"
            scene w_783 with dissolve
            e "Is that so?"
            "{i}I looked at Alex, raising a brow.{/i}"
            e "I didn’t realize we had...friends dropping by unannounced."
            "{i}A slight twitch crossed Alex's face, almost imperceptible, but enough for I to catch it. Eleanor merely smiled, her demeanor still friendly yet unreadable.{/i}"
            scene w_785 with dissolve
            ele "Oh, I’m sorry if my visit seems abrupt. Alex was just being a good host."
            ele "I’m sure you know how charming he can be."
            e_ "Charming? That's what she calls it?"
            o "Oh, she's clever, I’ll give her that. But don’t let her get too comfortable. Or do...see what her angle is."
            "{i}I shot Eleanor a tight smile.{/i}"
            e "Charming, yes, that’s one word for it."
            scene w_784 with dissolve
            "{i}The atmosphere thickened, tension building beneath the pleasantries. Crossed my arms, making no attempt to soften her expression.{/i}"
            a "Um, actually, Eleanor had an idea."
            "{i}He glanced between we, clearly hoping to break the ice.{/i}"
            a "She suggested we...do a double date. Us with her and her husband, Tristan."
            scene w_786 with dissolve
            ele "Yes, Tristan loves wine. I thought it would be a lovely evening, just the four of us."
            e_ "So now she’s inviting me to dinner? How bold."
            "{i}I didn’t respond immediately, letting the silence linger, watching Eleanor’s smile hold steady under my scrutiny.{/i}"
            e "A dinner with your husband, huh? And where exactly did you two plan this little gathering?"
            ele "Oh, it would be at our place. Tristan has an extensive wine collection, and he’s rather eager to share it. I’m sure you’d appreciate it, Emma."
            e_ "Does she really think wine is going to soften me up?"
            o "A dinner could be...fun, no? You’ll see them in their natural habitat. Who knows, you might find out a few things."
            "{i}I weighed Octavia’s words, biting back a small smirk.{/i}"
            e "Well, I do love a good wine. I suppose...it might be interesting."
            ele "Wonderful. I’ll have Tristan set everything up, and we’ll let you know the date."
            "{i}She looked at Alex, her expression warm.{/i}"
            ele "I appreciate you both being so open to this. It’s refreshing to find good company these days."
            e "Isn’t it just."
            "{i}I watched Eleanor carefully as she took a step back, preparing to leave. Her eyes lingered a little too long on Alex, which didn’t escape my notice.{/i}"
            scene w_787 with dissolve
            ele "I should go now. I look forward to our evening together."
            "{i}She turned, giving one last look over her shoulder before walking away, leaving me with a myriad of suspicions swirling in her mind.{/i}"
            $ renpy.music.stop("music2", fadeout=2.0)
            $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)
            $ emma_mental = EmmaMentalRemove()
            scene w_788 with fade
            "{i}As soon as Eleanor left, the silence between us felt heavy, thick with things left unsaid.{/i}"
            "{i}Watching Alex out of the corner of my eye, trying to read his expression. Was he hiding something... or am I just seeing what I want to see?{/i}"
            scene w_789 with dissolve
            e "So... were you really talking about me to Eleanor?"
            a "What? Of course, I was."
            e "Really? Because from where I was standing, it looked more like you were just... enjoying her attention."
            e_ "He says he was talking about me, but why does it feel like he’s keeping something back?"
            o "You’re right not to believe him so easily, Emma. Men like Alex don’t change."
            scene w_791 with dissolve
            a "Come on, Emma."
            a "She was being polite. I was just answering her questions. She asked about my ‘wife’—and last time I checked, that’s you."
            scene w_789 with dissolve
            e "Uh-huh. But you never actually answered my question."
            a "Which question is that?"
            e "Where exactly did you meet Eleanor?"
            e_ "He hesitates, like he’s about to dodge the question. Typical."
            scene w_792 with dissolve
            a "We met the other day. I told you, she's a neighbor. She and her husband."
            e "And I’m supposed to just believe that?"
            a "Yes, you’re supposed to just believe that. Do you honestly think I’d lie about something so trivial?"
            scene w_789 with dissolve
            e "Trivial? Alex, you know your history with... women isn’t exactly reassuring."
            e_ "It’s true, isn’t it? He expects me to forget all the times he... couldn’t resist."
            o "And you’re just supposed to trust that this time is different? Please."
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
            e_ "Does he even understand how easily he draws people in? Or does he just not care?"
            o "He cares only when it suits him. And don’t pretend you didn’t notice her practically eating up his every word."
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
            "{i}He steps closer, his voice dropping to a softer tone. Part of me hates how easily he draws me in when he does this.{/i}"
            a "Emma, listen. I know this whole setup is... complicated. But it’s just one dinner. If we go in there, put on a united front, it’ll make everything easier."
            e "Easier for who?"
            a "For both of us. Look, we don’t have to be best friends, or even agree on most things, but we both want this to work. Right?"
            e_ "Do we? Or is he just saying what I want to hear?"
            o "You’re stronger than this. Don’t let him charm his way past your defenses."
            e "Sometimes I just... wonder if you even care about any of it."
            a "I do care, Emma. I know it may not seem like it, but I do. Why do you think I’m still here, dealing with all of this?"
            e "Because you don’t want to lose. That’s always been your thing—winning."
            a "Maybe. But I don’t want to lose you, either."
            e_ "He says it so easily, like he’s thought about it a hundred times. I feel a pang, a flicker of something I don’t want to admit."
            $ renpy.music.play("audio/sfx/sfx_kissing_lip_to_lip.opus", channel="sfxloop1", fadein=2.0, relative_volume=0.2)
            scene w_794 with dissolve
            $ renpy.pause()
            $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
            scene w_795 with dissolve
            e "I don’t know if I can believe that."
            a "Then give me a chance to prove it. Just... let’s get through this dinner, together. That’s all I’m asking."
            e_ "He’s trying, I’ll give him that. And for a moment, it feels like he’s being sincere. But can I let myself believe it?"
            o "No. Don’t be naive, Emma."
            scene w_797 with dissolve
            e "Fine. But don’t make me regret it."
            a "I won’t."
            e_ "It hasn’t been easy, but maybe... just maybe, not everything between us is lost yet."

    scene w_326 with fade
    $ renpy.pause()

    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    scene w_327 with fade
    "{i}As the day drew to a close, I was tidying up in one of the quieter corners of the mansion, hoping for a moment to myself.{/i}"
    "{i}Suddenly, Isabella appeared, moving with her usual grace but with an urgency I hadn’t seen before.{/i}"
    "{i}She approached me directly, explaining that we’d be meeting tonight—Daniel, Alex, herself, and me—to discuss Alex’s recent attack and the overall security of the mansion.{/i}"
    "{i}I nodded, absorbing her words, and a faint unease settled over me. There was something about the way she spoke, like she was just as unsettled by all this as I was.{/i}"
    $ renpy.music.stop("ambient1", fadeout=2.0)
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("music2", fadeout=2.0)
    scene w_867 with fade
    "{i}As Alex recounted the details of the attack, his voice steady but dark, the room seemed to fade around me.{/i}"
    "{i}The memory surged back like a wave—me finding him that night, barely able to stand, blood staining his shirt.{/i}"
    "{i}I could still feel the cold shock that had run through me, the terrifying thought that he might not make it.{/i}"
    "{i}It was as if I was right back there, reliving the fear and the rush of panic, and I could feel my heart pounding just like it had then. I forced myself to breathe, to push the nightmare aside.{/i}"
    "{i}But the feeling lingered, haunting me with the dreadful thought that next time, I might not find him alive.{/i}"    
    $ renpy.music.play("audio/musics/tension_mystery.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_866 with dissolve
    d "I have to admit, Alex, when I first saw that bandage, I thought maybe it was just a little… embellishment."
    d "A tactic to gain sympathy, perhaps. But now… seems like the attack was real enough after all."
    scene w_869 with dissolve
    e_ "I can't believe it! Even now, these two are only thinking about their damn rivalry?! Why are they like this?!"
    e "I did the bandage myself. If there’s one thing I wouldn’t do, it’s lie about something like that."
    scene w_866 with dissolve
    o "I can see from here your beloved stallion risks an accident."
    e_ "Oh, God, Alex...not now."
    d "Fair enough, Emma. I suppose I’ll take your word for it."
    scene w_865 with dissolve
    isa "Regardless of anyone’s initial thoughts, the fact is, we have a problem."
    isa "This isn’t just about a single attack—it’s about the security of everyone in this mansion."
    isa "If someone could get close enough to harm Alex, then we’re all potentially at risk."
    o "Did you notice her tone? She's more than worried about Alex."
    e_ "What?!"
    scene w_868 with dissolve
    a "You know, for a moment there, I almost thought it was you who decided to pay me a little late-night visit, Daniel."
    "{i}I interrupt with an irritated tone.{/i}"
    scene w_869 with dissolve
    e "That’s absurd, Alex. Daniel and Isabella were in their rooms when it happened. I saw them myself."
    scene w_865 with dissolve
    isa "She’s right, Alex. Emma came to our room that night—she checked on us when she heard the noise. We were both there."
    e_ "Why did she have to bring up the subject like that? Isabella is clearly messing with me."
    "{i}I catch a brief, icy look in Daniel's eyes before he speaks, his tone as sharp as his gaze.{/i}"
    scene w_866 with dissolve
    d "Perhaps the real issue here, Alex, is you. It seems to me that this attack might have more to do with… choices you’ve made."
    d "Think about it. Nothing was stolen, no valuables taken. Whoever did this wasn’t here for the mansion or anything in it."
    d "They were here for you. Which suggests, of course, that it’s personal. Maybe a grudge? Some… unresolved history?"
    scene w_867 with dissolve
    e_ "Alex? Is he a problem? No..."
    o "Come on Em, you know he had a lot of women when he was a boxer. Maybe some paranoid fan is after him."
    e_ "No! Alex is a good man... unfaithful... yes... but he's never hurt anyone. We met at that charity event. He made sure to sponsor it. Alex may have a lot of flaws. But he's never hurt anyone... Daniel is wrong."
    o "Honey, Alex has broken a lot of hearts... yours is on his black list."
    e_ "Shut up!"
    o "Oh, you want to protect your man's thick, juicy cock?"
    e_ "SHUT UP!!!"
    scene w_869 with dissolve
    e "That’s not true, Daniel. You’re wrong."
    e "Alex is a good man. Flawed, yes—we all are—but he’s never been the kind of person to stir up enemies."
    e "No matter what anyone says about him, he’s always tried to do the right thing for the people around him."
    e "If someone attacked him, it wasn’t because he deserved it."
    scene w_867 with dissolve
    "{i}I didn't care what Octavia told me. Alex had always cheated on me and deceived me about everything. But he hadn't been a good man.{/i}"
    e_ "Oh, God... I'm starting to trust him again. Am I starting to feel love for Alex again?"
    o "That's why you need me. To stop being the fool you are."
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
    e_ "Victor? Why. I mean... he's harmless."
    o "Emma... come on... don't pretend you don't understand."
    e_ "Shit... can you stop talking in my head?"
    scene w_868 with dissolve
    a "Who’s Victor?"
    "{i}I couldn't help but notice Alex's suspicious look. I knew it very well.{/i}"
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
    scene w_869 with dissolve
    e "Victor doesn’t seem like a threat to anyone. I really don’t see the harm in him having a key if he’s here regularly."
    "{i}Daniel pauses, considering my words. He finally nods, albeit reluctantly.{/i}"
    scene w_866 with dissolve
    d "Fine. Victor can have a key, but let’s be clear—if anything happens, he’ll be under as much scrutiny as anyone else with access. He’s not above suspicion."
    d "Alright, that settles it. I’ll handle the rest of the security details—locks, key assignments, the works. We don’t need to overcomplicate this with too much input."
    scene w_867 with dissolve
    "{i}There’s something unsettling about the way Daniel is wrapping things up.{/i}"
    "{i}It’s subtle, but there’s an edge to him, a darkness just beneath the surface that I can’t quite ignore.{/i}"
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
    e_ "Is he agreeing with me? He's really trying. Or is he just trying to disagree with Daniel."
    o "You know the answer to that."
    isa "Alex, this isn’t about appearances. It’s about privacy and control. Bringing in strangers could create more complications than solutions."
    "{i}The room grows silent as the weight of the argument settles, each of them locked in their stance. After a tense pause, Daniel finally speaks, voice measured but with an edge of finality.{/i}"
    scene w_866 with dissolve
    d "Fine. Let’s leave it at this: each of us will handle it in whatever way we think is best."
    d "If you want to go to the authorities, that’s your choice. But don’t expect everyone else to fall in line."

    scene w_327 with dissolve
    "{i}The conversation ends with an uncomfortable truce, with the four of us exchanging glances that reveal deeper latent conflicts.{/i}"
    $ renpy.music.stop("music2", fadeout=2.0)

    jump day5_emma_1
