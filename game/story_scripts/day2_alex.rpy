label day2_alex_1:

    $ alexaboutavaboyfriendavaday2 = False
    $ alexspillswineday2 = False
    $ alexsflirtisabelladay2 = False
    $ alexsholdisabelladay2 = False
    $ alex_fr1_emma_talk = False
    $ alexspiesrubyshowerday2 = False
    $ alexkissemmaday2 = False
    
    scene black with fade

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 4rd_day with fade
    $ renpy.pause()
    hide 4rd_day with dissolve

    scene black with fade
    "{i}I woke up the next morning with a sense of determination. After the tension of the previous night, I needed to clear my head. Training always helped with that.{/i}"
    "{i}I decided to head to the mansion’s training room to get in a good workout.{/i}"
    "{i}As I walked through the grand hallways, the early morning light filtered through the large windows, casting a serene glow across the space.{/i}"
    "{i}I reached the door of the training room and pushed it open, expecting to find it empty.{/i}"
    scene w_174 with fade
    "{i}Instead, I was greeted by the sight of Isabella, hot and sexy, as always, practicing yoga with a personal trainer.{/i}"
    "{i}Isabella's lithe form moved gracefully through the poses, her focus entirely on her practice.{/i}"
    scene w_175 with dissolve
    "{i}I paused for a moment, watching the scene. The trainer looked up as I entered, her eyes meeting mine.{/i}"
    "{i}It was Ava, a personal trainer I had worked with in the past. Her sharp features and intense eyes were unmistakable.{/i}"
    a "Ava? Is that you?"
    "{i}Ava's lips curved into a small smile as she straightened up from her instructive stance.{/i}"
    scene w_176 with dissolve
    av "Alex? Long time no see. What brings you here?"
    "{i}Isabella glanced over, curiosity piqued by our exchange, but remained silent.{/i}"
    "{i}Seeing Ava after all this time was a surprise. The last time we met, I was still a professional boxer, and things were different.{/i}"
    "{i}There was a familiar energy between us, a connection that had always been there.{/i}"
    a "Ava, it's been a while. How have you been?"
    av"I've been good, Alex. Keeping busy with training and clients. How about you? Still knocking people out?"
    a "Not exactly. I’ve been dealing with... other challenges. But it’s good to see you. You look great, as always."
    av "Thanks. You haven't changed much yourself. Still keeping in shape, I see."
    a "Trying to. You know how it is. Once a boxer, always a boxer."
    "{i}Isabella glanced at us with mild curiosity. Ava and I had a natural camaraderie that was hard to ignore.{/i}"
    isa "So, how do you two know each other?"
    a "Ava was my trainer back in the day. Helped me through some tough times in my career."
    av "Yeah, we spent a lot of time in the gym together. Alex was one of my favorite clients. Always pushing himself to the limit."
    a "Couldn't have done it without you, Ava. You always knew how to get the best out of me."
    av "It was a team effort. We had some good times."
    "{i}As Ava and I continued to catch up, I noticed Isabella growing increasingly irritated. Her focus on the yoga session was clearly waning, and she finally snapped.{/i}"
    scene w_177 with dissolve
    isa "Ava, are we going to continue, or is this a social hour? I'm paying you to help me, not chat with him."
    "{i}Ava's expression shifted from friendly to professional in an instant. She turned to Isabella with a calm but firm look.{/i}"
    scene w_178 with dissolve
    av "Isabella, I know my job. Continue with the downward dog pose, and I'll be with you in a moment."
    "{i}Isabella huffed but resumed her position, clearly annoyed. I felt a twinge of guilt for disrupting their session.{/i}"
    scene w_179 with fade
    a "Sorry, Ava. Didn't mean to interrupt your session."
    "{i}Ava smiled, shaking her head slightly.{/i}"
    av "Don't worry about it, Alex. It's good to see you again. These things happen."
    a "Still, I feel bad. It's been a long time, and I didn't want to cause any issues."
    av "Really, it's fine. Seeing you brought back a lot of memories. I remember when I used to follow your career closely. You were incredible in the ring."
    scene w_180 with dissolve
    "{i}Her words brought a nostalgic smile to my face. Those were some of the best years of my life, and it was nice to know someone appreciated them.{/i}"
    a "Yeah, those were the days. I miss the thrill of the fight sometimes. But life has a way of moving on, doesn’t it?"
    av "It does. I learned a lot from watching you, though. Your dedication, your passion—it was inspiring. It’s part of why I became a trainer."
    "{i}I glanced over at Isabella, who was now doing some stretches, still looking slightly annoyed.{/i}"
    a "You always had a way of motivating people, Ava. It's no surprise you’ve become such a great trainer."
    av "Thank you, Alex. That means a lot coming from you. I always believed in your potential, both in and out of the ring."
    a "Do you remember those early morning runs we used to do?"
    av "You were always pushing yourself, even when it was freezing outside."
    "{i}I chuckled, memories of those grueling yet fulfilling days coming back to me. Then, a more personal memory surfaced.{/i}"

    $ alexaboutavaboyfriendavaday2 = False
    
    menu:
        "{font=fonts/hatten.ttf} {size=50}Comment on her boyfriend.{/size}{/font}":
            $ alexaboutavaboyfriendavaday2 = True

            a "There’s something I’ve been curious about, Ava."
            a "Back then, before I met Emma, I asked you out. You turned me down because you were with someone. Do you ever think about those days?"
            "{i}Ava’s smile faded slightly, replaced by a more contemplative expression.{/i}"
            av "A lot has changed since then. My boyfriend at the time... things didn’t work out. He wasn’t who I thought he was."
            a "I'm sorry to hear that. You deserved better."
            av "Life has a way of surprising us."
            "{i}There was a moment of silence, a shared understanding passing between us.{/i}"
            a "So, are you seeing anyone now?"
            "{i}Ava hesitated, then shook her head.{/i}"
            av "No, I’m focusing on my career right now. Relationships can be... complicated."
            "{i}Sensing the shift in our conversation, I decided to steer it towards a lighter topic. Ava's physical transformation over the years had been impressive, and I thought it might be a good way to change the mood.{/i}"
        "{font=fonts/hatten.ttf} {size=50}Comment on her body.{/size}{/font}":
            $ alexaboutavaboyfriendavaday2 = False

            "{i}Ava's physical transformation over the years had been impressive, and I thought it might be a good way to change the mood.{/i}"
    
    scene w_181 with dissolve
    a "I have to say, Ava, you've really kept yourself in amazing shape. You look even better than when we were training together."
    av "Thanks. It hasn’t been easy, but I’ve worked hard to stay fit."

    if alexaboutavaboyfriendavaday2 == False:
        a "Hey, do you remember that time when we were leaving the gym and some guy tried to hit on you?"
        a "I was about to step in, but you decked him before I even had a chance."
        "{i}Ava laughed, the memory clearly vivid in her mind.{/i}"
        av "Oh, I remember that! The look on his face was priceless."
        av "I think you were more surprised than he was."
        a "Yeah, I was! I thought I’d have to play the hero, but you handled it like a pro. Remind me to never get on your bad side."
        "{i}Ava burst into laughter.{/i}"
        av "Don't worry, Alex. You’re safe. Though, I have to admit, I’ve been working on my punches. But they’re nothing compared to yours."
        a "Well, I’ll make sure to stay in line then. Wouldn’t want to end up on the receiving end of one of your punches."
        av "You have nothing to worry about. There are much better ways for me to use my hands with you."
        "{i}Her words hung in the air. We both smiled, the shared memories and playful banter bringing us closer.{/i}"

    scene w_182 with dissolve
    "{i}She struck a pose, subtly flexing her toned arms and shifting her stance to highlight her defined legs.{/i}"
    a "{i}Well, it's definitely paid off. You look incredible.{/i}"
    "{i}Ava turned her back to me, her movements deliberate as she adjusted her stance.{/i}"
    "{i}Her body was a testament to her dedication and hard work. As she continued to stretch, it was clear she knew exactly what she was doing, and the effect it was having on me.{/i}"
    a "You've really outdone yourself, Ava. Your physique is impressive."
    "{i}Ava glanced over her shoulder, a playful smile on her lips.{/i}"
    av "Thanks, Alex. It’s all about consistency and pushing yourself to the limit."
    "{i}She lifted her arms in a stretch, the motion accentuating her toned back and the curve of her hips.{/i}"
    "{i}My thoughts drifted, unable to ignore how attractive she had become.{/i}"
    a_ "She's absolutely stunning. Every move she makes is calculated, and damn, it's working."
    av "Training has always been a big part of my life. It’s not just about staying in shape, but about feeling strong and confident."
    a "I can see that."
    av "And you, Alex? How’s your training been going?"
    a_ "Ava is definitely interested. I’ve always been a sucker for a beautiful woman."
    a "It's been decent, but I could definitely use some pointers from you."
    av "I'd be happy to help. Maybe we can train together sometime. Push each other to our limits."
    a_ "She's absolutely stunning. Every inch of her body screams strength and sensuality. It's hard not to get lost in how attractive she's become. Those curves..."
    a_ "She knows exactly what she's doing. She's teasing me, showing off her hard work. And it's working."
    a_ "I can't stop thinking about how much I want her. The way she looks now, it’s hard to believe I ever let her slip through my fingers."
    a_ "She's incredibly sexy. I wonder if there's a chance for us now, after all this time."
    scene w_183 with dissolve
    "{i}Before I could dwell too much on the possibilities, Isabella approached.{/i}"
    isa "Ava, I’m going to need your help with a stretch. Can you assist me?"
    "{i}Ava nodded, her expression shifting back to professional.{/i}"
    av "Of course. Let’s get to it."
    scene w_184 with dissolve
    "{i}As Isabella approached and requested Ava's help, I felt a pang of disappointment, but I knew it was time to let her get back to her job.{/i}"
    a "Well, Ava, it was great catching up. Maybe we can train together sometime."
    av "I'd like that, Alex. Anytime you need a training partner, just let me know."
    scene w_185 with dissolve
    "{i}I watched as Ava turned to help Isabella with her stretches. She moved with a confidence that was both professional and undeniably attractive.{/i}"
    scene w_186 with dissolve
    "{i}With a sigh, I turned back to my own training, grabbing a set of dumbbells and starting my workout.{/i}"
    scene w_185 with dissolve
    a_ "Training with Ava again would be amazing. She’s got that drive and energy that’s infectious. And she looks... incredible."
    scene w_186 with dissolve
    "{i}As I focused on my exercises, I couldn't help but think about the way she looked at me, the way she moved.{/i}"
    scene w_185 with dissolve
    "{i}There was something there, something unspoken but definitely felt.{/i}"
    scene w_187 with dissolve
    "{i}Meanwhile, Ava guided Isabella through her stretches, her mind not entirely on the task at hand.{/i}"
    scene w_188 with dissolve
    "{i}She stole glances at me when she thought no one was looking, her eyes filled with a longing that mirrored my own thoughts.{/i}"
    isa "Ava, can you help me with this one?"
    scene w_187 with dissolve
    av "Of course, Isabella. Just hold that pose and breathe deeply."
    scene w_188 with dissolve
    "{i}As she adjusted Isabella’s posture, Ava’s eyes flicked back to me, watching my muscles flex as I lifted the weights.{/i}"
    scene w_189 with dissolve
    "{i}I continued my workout, unaware of Ava’s gaze.{/i}"
    "{i}The room was filled with the sounds of exertion and focused breathing, but beneath it all, a current of desire and unspoken words flowed between us.{/i}"
    "..."
    "{i}After finishing my workout, I was drenched in sweat and decided it was time for a shower.{/i}"
    scene w_190 with fade
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    "{i}Once I was clean and refreshed, I decided to explore the mansion’s garden, particularly the area around the pool.{/i}"
    "{i}Walking through the winding paths, I admired the beauty of the garden. The further I walked, the more serene it became, until I finally reached the pool area.{/i}"
    scene w_191 with dissolve
    "{i}The pool was large and inviting. As I approached, I noticed someone. The figure moved gracefully through the water, their presence adding a sense of calm to the already peaceful scene.{/i}"
    scene w_192 with dissolve
    a_ "Emma..."
    "***I stood at the edge, watching quietly, not wanting to disturb the moment."
    "{i}And there she was, Emma, lying on an inflatable pool mattress in a striking red bikini.{/i}"
    "{i}Her back was to me, and the sight was mesmerizing. Every curve accentuated by the way she lay so relaxed and carefree.{/i}"
    "{i}Her had always been beautiful, but in moments like these. The way the bikini clung to her form, the slight sway of the mattress with the water's movement, it all painted a picture of seduction.{/i}"
    "{i}(Emma is absolutely stunning. Her body, the way she moves. I wonder if she knows the effect she has on me. Or maybe she does and enjoys it. Either way, I can't look away.{/i}"

    if alexemmaanddanieljealousday1:
        a "{i}I was too possessive yesterday, letting jealousy get the better of me when I saw Emma talking to Daniel. It was a mistake, and I could see the irritation in her eyes during dinner.{/i}"
        a_ "I need to fix this, but how? I can't just apologize; it needs to be something more. Something that will make her smile, ease the tension between us."
        a_ "Maybe I could joke about it, make light of my own jealousy. Something like. Yeah, something like that might work. She always did appreciate a good laugh."
        a_ "I just need to make sure I approach her in the right way, show her I’m genuinely sorry and that I want to make things right."
        scene w_193 with dissolve
        a "You know, seeing you with Daniel made me realize how lucky I am. Not because I’m better than him, but because you actually put up with my nonsense."
        e "..."
        e "Really, Alex? I've put up with your nonsense for so long because I loved you. And what did I get in return?"
        scene w_196 with dissolve
        a "I don't believe that love just vanished. It can’t be gone."
        scene w_195 with dissolve
        e "It's not just gone, Alex. It's more like it was destroyed, piece by piece."
        scene w_196 with dissolve
        a "Maybe we can rebuild it. I'm willing to try if you are."
        scene w_195 with dissolve
        e "You really think that's possible? After everything?"
        scene w_196 with dissolve
        a "I do. I’m sorry for being so jealous. I know it wasn't fair to you."
        scene w_195 with dissolve
        "{i}Emma looked at me with a mix of skepticism and curiosity, her eyes reflecting the hurt and hope battling within her.{/i}"
        e "Alex, I'm trying to spend some time away from you. It's ironic, though, this mansion doesn't seem big enough."
        scene w_196 with dissolve
        a "Well, maybe we could start by... stopping all the arguments?"
        scene w_195 with dissolve
        e "That would be a good start. For once, we agree on something."
        a_ "Emma's sarcasm isn't lost on me, but I know she's right."
        a_ "Stopping the arguments would be a step in the right direction. I just hope it's not too late to fix things between us."
    else:
        "{i}Despite everything, she was still breathtaking.{/i}"
        "{i}I remembered the last time I managed to get a compliment out of her, thinking that maybe she was in a good mood today.{/i}"
        scene w_193 with dissolve
        a "You know, Emma, it’s really hard to resist looking at you when you’re lying there like that. You’re absolutely stunning"
        "{i}She turned her head slightly, acknowledging my presence with a faint smile.{/i}"
        e "Oh, I know. But why don’t you control your 'toy' and remember that we’re just pretending to be married."
        "{i}I chuckled, realizing she wasn’t entirely wrong. But her playful tone gave me hope that maybe, just maybe, things could get better between us.{/i}"
        scene w_195 with dissolve
        "{i}I saw Emma glance over at me, a hint of irony in her eyes.{/i}"
        e "I'm trying to spend some time away from you. It's ironic, though, this mansion doesn't seem big enough."
        scene w_196 with dissolve
        "{i}I laughed, feeling a bit more at ease with her playful tone.{/i}"
        a "Yeah, it’s almost like this place was designed to keep us bumping into each other."
        a "Maybe next time, we should get a mansion with a few extra wings."
        scene w_195 with dissolve
        e "Ha! Right, so I can have my own personal wing far away from you."
        scene w_196 with dissolve
        a "Exactly! You can have your wing, and I’ll have mine. We’ll communicate through messenger pigeons."
        scene w_195 with dissolve
        e "Hahaha... Pigeons? Really? How old-fashioned are you, Alex?"
        scene w_196 with dissolve
        a "Hey, I’m just trying to be romantic. Besides, think of all the fun we’d have training the pigeons."
        scene w_195 with dissolve
        e "*Heh heh*, maybe. But I still think it’s hilarious you’d consider pigeons."
        scene w_196 with dissolve
        a "Well, if you have a better idea, I'm all ears."
        scene w_195 with dissolve
        "{i}I could hear Emma’s soft chuckles and felt a small victory in making her laugh.{/i}"

    $ renpy.music.play("audio/sfx/sfx_water2.opus", channel="sfx1", relative_volume=0.8)
    scene w_197 with dissolve
    "{i}As Emma climbed out of the pool, I couldn't help but admire how the water droplets glistened on her skin, making her look even more captivating.{/i}"
    a "You right, Emma, it’s ironic. We’re trying to spend time away from each other in this huge mansion, but it still feels too small sometimes."
    scene w_204 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    "{i}Emma laughed, the sound warm and genuine. It was moments like these that made me remember why I fell for her in the first place.{/i}"
    scene w_198 with dissolve
    e "I guess it just goes to show that you can't escape someone as easily as you think. Especially not when you're married to them."
    "{i}I smiled, thinking about how to keep the mood light while also getting closer to her again.{/i}"

    if alexemmaanddanieljealousday1:
        scene w_199 with dissolve
        with Pause(3)
        a "You know, like how incredible you look right now. This bikini... you're absolutely stunning."
    else:
        a "Well, I could try starting with fewer arguments. What do you think?"
        e "That would be a good start. Less arguing sounds like a dream."
        scene w_199 with dissolve
        with Pause(3)
        a "And maybe more compliments? You know, like how incredible you look right now. This bikini... you're absolutely stunning."

    scene w_198 with dissolve
    "{i}Emma's cheeks flushed slightly, a sign that she wasn't entirely immune to my attempts at flattery.{/i}"
    e "Oh, stop it, Alex. But, thanks. It's nice to hear that from you."
    a "I'm serious, Emma. You're gorgeous. And it's not just the bikini, it's you. You have this way of looking effortlessly sexy."
    scene w_204 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    "{i}Her smile widened{/i}"
    scene w_198 with dissolve
    "{i}I could see a hint of the connection we used to have flicker in her eyes. I knew I had to tread carefully, but at least we were talking.{/i}"
    scene w_199 with dissolve
    with Pause(3)
    a "You know, Emma, it's kind of hard to stop looking at you. And I mean, can you blame me?"
    scene w_198 with dissolve
    a_ "I'm pushing my luck here, but her smile gives me hope."
    e "Oh, I know you haven't stopped. As a woman, I can't say I don't enjoy the attention."
    a_ "A little victory, but I need more than just her enjoying the attention."
    e "But you know, marriage isn’t just about the physical stuff."
    a "I have to ask, don’t you miss it? The sex, I mean."
    "{i}I tried to lighten the mood with a joke.{/i}"
    a "I mean, if it were an Olympic sport, we'd definitely win gold."
    a_ "Please laugh, Emma. Just laugh."
    scene w_204 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    e "Haha! Oh, Alex. You always knew how to make me laugh. And yes, I do miss it. Saying I don’t would be a lie."
    a_ "That’s something. She’s admitting it."
    scene w_198 with dissolve
    e "But just because I miss it doesn’t mean I can forget everything that happened."
    a_ "She's got a point, but I need to steer this conversation to safer ground."
    e "I noticed up on how many women are in this mansion."
    a_ "Stay calm, Alex. Don’t let this slip into dangerous territory."
    a "But believe me, they can't compare to you."
    e "Alex. It makes me wonder if you might... stray again."
    scene w_197 with dissolve
    a_ "No, I can’t let her think that."
    a "Emma, I get it. But let's not talk about that now. How about we focus on enjoying this time together instead?"
    "{i}She’s silent for a moment. This is tricky, but I need to keep this light and positive.{/i}"
    a "I'm trying to be nice here. At least give me some credit."
    e "Fine, fine. You get a point for trying."
    a_ "Okay, one step at a time. Let’s keep this light."
    e "You know, being pleasant wouldn’t kill you."
    a "I’m working on it. Baby steps."
    e "Good. Now, at least pretend to be charming."
    a "Pretend? I thought I was naturally charming."
    scene w_204 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    e "Haha! Maybe to someone who doesn't know you."
    a_ "Great, she's laughing. This is good."
    a "Seriously though, Emma. You're the best part of this mansion."
    e "Don't get all sentimental on me now."
    a "Too late. I've already started."
    a_ "Okay, time to steer this to safer waters."
    scene w_198 with dissolve
    a "So, how have you been? Besides trying to avoid me."
    e "I've been fine. Enjoying the pool, the mansion... just trying to relax."
    a "That’s good to hear. You deserve to relax."
    a_ "Perfect time for a joke."
    a "You know, speaking of relaxing, I once heard that laughing burns calories. I should be good for your workout plan."
    scene w_204 with dissolve
    $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
    e "Oh really? Maybe I should charge you as my personal trainer then."
    a "Hey, if it means seeing you smile, I’m all in."
    a_ "She's really enjoying this. Good job, Alex. Keep it up."
    scene w_198 with dissolve
    e "Alright, I’ll admit, you’re doing well today."
    a "Thanks. It’s all part of my master plan."
    scene w_199 with dissolve
    with Pause(3)
    a "You not just beautiful, but... incredibly sexy and attractive."
    e "Alex..."
    a_ "Please let this go well. Please let this go well."
    scene w_201 with dissolve
    e "Okay, I appreciate the compliment. But let's not get carried away."
    a "Fair enough. Just wanted you to know how I feel."
    e "Noted. And, Alex... thanks. For trying."
    a_ "Alright, Alex. Good start. Now, don’t mess it up."
    a "Anytime, Emma."
    scene w_202 with dissolve
    "..."
    a_ "Oh great, here comes Daniel. Just what I needed. Stay calm, Alex. Don’t lose your cool now."
    scene w_203 with dissolve
    a_ "Why is he always around at the worst times? He's definitely trying to seduce her, flaunting those glasses like he's some kind of suave gentleman."
    a_ "Emma doesn't deserve this. I need to keep my cool, but it's hard when all I can think about is him trying to take her away from me."
    "{i}My temper started rising, the worst-case scenarios playing out in my mind.{/i}"
    a_ "I can’t lose my cool now, not in front of Emma. But how do I keep calm when he's right there, making his intentions so obvious?"
    scene w_205 with dissolve
    "{i}I kept glancing between Emma and Daniel, my mind racing with possible actions and their consequences.{/i}"
    a_ "Stay calm, Alex. Don't let him see that he's getting to you. Emma needs to see that you can handle this like an adult. But if he tries anything..."
    a_ "No, focus on her. Make her remember why she fell for you in the first place. But damn, it's hard when he's right there, trying to steal her away."
    "{i}Every second felt like an eternity as I struggled to maintain my composure.{/i}"

    $ alexspillswineday2 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}I knock over the wine glasses.{/size}{/font}":
            $ alexspillswineday2 = True

            $ renpy.music.stop("music1", fadeout=2.0)
            $ renpy.music.play("audio/musics/filaments1.mp3", "music2", fadein=2.0, relative_volume=0.2)

            "{i}I saw Daniel approaching with two glasses of wine, and my jealousy flared up like a wildfire.{/i}"
            a_ "He's trying to act like a gentleman to steal Emma from me. I won't let that happen."
            scene w_215 with dissolve
            a "Daniel, what do you think you're doing?"
            d "Just being a good host, Alex. You should try it sometime."
            a "*Sarcastically* Oh, I remember your \"good host\" days back in college. How many times did you end up with someone else's girl?"
            d "That's rich coming from you. At least I never had to lie to keep a girl interested."
            a "Excuse me? At least I don't have to stoop to your level of desperation."
            d "Desperation? That's funny. How's that desperation treating you now, Alex? Seems like you’re the one sweating bullets."
            a_ "This asshole is trying to get under my skin. Stay calm, Alex. Stay calm."
            a "Don't flatter yourself, Daniel. Emma isn't some prize you can win with a cheap bottle of wine."
            scene w_216 with dissolve
            d "Cheap? This is a 1996 Château Margaux. But I wouldn't expect you to know quality if it slapped you in the face."
            a "Quality? Like the quality of your relationships? How many ended in restraining orders again?"
            d "Nice try, but I think we both know you're the one with the fidelity issues. How’s your little \"business trips\" going?"
            a "At least I have a business, not some sad excuse for a side hustle. What do you even do again, other than trying to pick up women out of your league?"
            d "More than you, apparently. And speaking of leagues, remember Sarah? She definitely enjoyed my \"side hustle.\""
            a_ "He's crossed the line now. No more holding back."
            scene w_217
            with Dissolve(0.01)
            $ renpy.music.play("audio/sfx/sfx_smack.ogg", channel="sfx1", relative_volume=0.5)
            scene white
            with Dissolve(0.01)
            scene w_217
            with Dissolve(0.01)
            with hpunch
            a "You son of a—"
            "{i}I lost control. My temper surged, and before I knew it, I had knocked one of the wine glasses out of Daniel's hand.{/i}"
            scene w_218 with dissolve
            a "Next time, keep your hands off what's mine."
            scene w_219 with dissolve
            a "And how many times have you pretended to be the hero while stabbing people in the back? How’s that working out for you, Daniel?"
            d "Better than being a failure at both work and home, Alex."
            scene w_220
            with Dissolve(0.01)
            $ renpy.music.play("audio/sfx/sfx_kick.ogg", channel="sfx1", relative_volume=0.5)
            scene white
            with Dissolve(0.01)
            scene w_220
            with Dissolve(0.01)
            with vpunch
            e "What the hell, Alex?!"
            "{i}Emma had come up behind me, her frustration palpable as she delivered a swift punch to my shoulder. It wasn’t hard enough to hurt, but it got my attention.{/i}"
            scene w_221 with dissolve
            e "I can’t believe you’re doing this again! In front of everyone!"
            a_ "Emma’s voice was filled with a mixture of anger and sadness. It hurt to hear her like that."
            a "Emma, I—"
            e "No, Alex. I’m done with your excuses. You always do this. Every time."
            a "He was trying to—"
            e "I don’t care what he was trying to do! You always find a reason to lash out, to make a scene."
            "{i}Her words stung. They cut deeper than any wound Daniel could inflict.{/i}"
            a "Emma, please—"
            e "No! I’m sick of it. I’m sick of you always ruining everything. Why can’t you just trust me? Trust us?"
            a_ "I felt a pang of guilt. She was right. I was always letting my jealousy get the best of me."
            a "Emma, I love you. I just—"
            e "Love isn’t supposed to feel like this, Alex. Love isn’t supposed to hurt."
            "{i}I could see the pain in her eyes, the weariness. She was tired. Tired of me, tired of the fights. I knew I had pushed too far this time.{/i}"
            "{i}Emma's face flushed with frustration as she turned away, muttering under her breath. I knew I had pushed her too far this time.{/i}"
            scene w_222 with dissolve
            e "I can't keep doing this, Alex. I'm done."
            a "..."
            "{i}She walked away briskly, leaving me standing there with the weight of my own stupidity pressing down on me.{/i}"
            "{i} I wanted to go after her, to make things right, but my feet felt rooted to the spot.{/i}"
            scene w_223 with dissolve
            "{i}Emma's silhouette disappeared through the door, and I felt the familiar surge of regret and anger intertwine within me.{/i}"
            d "You never disappoint, Alex. When it comes to being an idiot, you're always consistent."
            a_ "Damn him. Damn his smug face. He's enjoying this too much."
            d "You know, if you put half the effort into understanding her as you do into ruining things, you might actually be a decent husband."
            a_ "I hate that he's right. I hate that he's the one saying it."
            $ alex_power = AlexPowerRemove()
            a_ "She deserves better. But I'll be damned if I let Daniel think he's better for her than I am."

            $ renpy.music.stop("music2", fadeout=2.0)
            $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)
            
        "{font=fonts/hatten.ttf} {size=50}I take the wine glasses.{/size}{/font}":
            $ alexspillswineday2 = False

            a_ "Are you kidding me? He’s trying to make a move on Emma right in front of me. I need to stay calm, but this is infuriating."
            "{i}I decided to act before he could get any closer to her. I intercepted him, placing a firm hand on his shoulder.{/i}"
            scene w_206 with dissolve
            a "Thanks, Daniel. I'll take these."
            d "They’re not for you, Alex."
            "{i}I leaned in closer, lowering my voice so Emma wouldn’t hear.{/i}"
            a "We both know what you're trying to do. Back off."
            d "And we both know you're just as guilty, if not more. Think about that."
            "{i}I tightened my grip on the glasses, holding back my frustration.{/i}"
            scene w_207 with dissolve
            "{i}As I took the glasses from Daniel's hands, I felt a surge of irritation. I knew exactly what he was trying to do.{/i}"
            "{i}He wanted to make me jealous, and it was working. I had to stay calm, though.{/i}"
            d "You know, Alex, some people might say that a marriage without trust is like these glasses of wine—easy to spill."
            a_ "Damn, he's good at this. Keep your cool, Alex."
            a "Well, Daniel, I appreciate the concern. But I think I'll handle these just fine. Cheers."
            scene w_208 with dissolve
            "{i}I offered him a tight smile, masking my irritation with forced cheerfulness. I then turned my back on him, heading towards Emma.{/i}"
            a_ "It's time to refocus. Emma's waiting, and I need to make sure she knows I'm here for her, not playing Daniel's games."
            scene w_209 with dissolve
            a_ "Alright, Alex, keep it cool. She's already suspicious, so don't give her more reasons to doubt you."
            e "Did you ask Daniel to bring this?"
            a "Of course. I know how much you love wine."
            e "Really? That doesn't sound like something you'd do."
            a "Well, you know, I can surprise you sometimes. But don't worry about Daniel, he's not important."
            a_ "Stay calm, Alex. She’s still looking at you like she doesn't believe a word you're saying. Just keep it light."
            e "Hmm, if you say so. But why do I get the feeling you're just trying to distract me?"
            a "Distract you? From what? Can't a guy just bring his wife a drink without an ulterior motive?"
            a_ "Please, Emma, just take the wine and let's move past this."
            scene w_210 with dissolve
            e "Alright, fine. But don't think this means I'm letting my guard down."
            a "Wouldn't dream of it. Cheers to... keeping you on your toes?"
            $ renpy.music.play("audio/sfx/sfx_glasses_clink.opus", channel="sfx1", relative_volume=0.8)
            e "*smirking* Cheers. But seriously, Alex, what’s really going on?"
            a_ "Ah, here we go. She's not letting this go."
            a "Just trying to make things a bit better between us, you know? Maybe we can start with a glass of wine and some honest conversation."
            e "Honest conversation? That's a first. What’s next, you’ll tell me you’ve taken up yoga?"
            a "{i}*chuckling* (Okay, she’s in a better mood. Keep it going.{/i}"
            a "Hey, I could be flexible if it means making you happy."
            e "*laughing* Now that’s something I’d pay to see. But seriously, Alex, do you really think a glass of wine is going to fix everything?"
            a "No, but it’s a start. I just want us to have a moment where we’re not at each other’s throats."
            e "Fine. But you owe me more than just wine for all the crap you’ve pulled."
            a "*smiling* I know. And I’m ready to make it up to you, one glass at a time."
            scene w_211 with dissolve
            a"{i}(Here's to hoping this small gesture buys me some time to figure out how to really fix this mess.{/i}"
            scene w_212 with dissolve
            "{i}I kept my arm around her, enjoying the moment of closeness, even if it was just for show.{/i}"
            scene w_213 with dissolve
            "{i}As we walked away, I made sure Daniel saw me flip him the middle finger behind Emma's back.{/i}"
            $ alex_power = AlexPowerAdd()
            scene w_214 with dissolve
            "..."
    
    if alexspillswineday2:
        scene black with fade
        "{i}I was fuming as I stood in the garden, my fist clenched tight, knuckles whitening under the pressure.{/i}"
        "{i}Once again, I'd let jealousy get the best of me. I'd seen Daniel with that damn bottle of wine, showing off like he was the king of the world, and I just couldn't control myself.{/i}"
        scene w_252 with fade
        "{i}The look on Emma's face when I knocked the glass out of her hand...{/i}"
        "{i}She didn't even have to say much; her eyes said it all. I messed up. Again. And not just with her, but by letting that smug bastard Daniel get under my skin.{/i}"
        a_ "Damn it, Alex, why do you keep falling for his games?"
        a_ "He knows exactly which buttons to push, and I just keep letting him win. Every. Single. Time."
        "{i}I found myself staring at the wall, my thoughts racing, my mind clouded with anger and regret.{/i}"
        "{i}My fingers twitched, and before I knew it...{/i}"
        scene w_253
        with Dissolve(0.01)
        $ renpy.music.play("audio/sfx/sfx_punch1.ogg", channel="sfx1", relative_volume=0.5)
        scene white
        with Dissolve(0.01)
        scene w_253
        with Dissolve(0.01)
        with hpunch
        "{i}I had thrown a punch at the wall.{/i}"
        "{i}The impact sent a sharp pain through my hand, but it did nothing to relieve the storm inside my head.{/i}"
        "{i}I stood there, breathing heavily, my hand throbbing, and I felt utterly stupid.{/i}"
        scene w_254 with dissolve
        "{i}Just as I was about to curse out loud, I sensed movement behind me.{/i}"
        "{i}Someone was coming out from the mansion, heading toward the garden.{/i}"
        "{i}I turned slightly, my heart still racing, trying to compose myself despite the chaos inside.{/i}"
        scene w_255 with dissolve
        "{i}And then she walked by.{/i}"
        "{i}Isabella’s presence was a distraction I didn’t need right now, yet my eyes were drawn to her like a magnet.{/i}"
        "{i}She was in a bikini, the fabric barely covering her curves, leaving little to the imagination.{/i}"
        "{i}The way she walked, confident and unhurried, her hips swaying slightly, was enough to momentarily push my anger to the side.{/i}"
        "{i}Our eyes met briefly, and I could see the flicker of something in her gaze, though it was impossible to tell what she was thinking.{/i}"
        a_ "She’s something else, no denying that."
        scene w_256 with dissolve
        "{i}As she continued walking, her head turned slightly, and I couldn’t help but notice how her attention shifted towards the direction of the pool.{/i}"
        "{i}I wasn’t sure if she was thinking about the argument she might have overheard or if her thoughts were entirely elsewhere.{/i}"
        "{i}But for a moment, I forgot about Emma, about Daniel, about the mess I’d made of everything.{/i}"
        a_ "Damn… I’ve got enough on my plate without adding her into the mix.) "
        scene w_257 with dissolve
        "{i}As I watched Isabella walk toward the pool, my gaze was locked onto her body, particularly her ass.{/i}"
        "{i}Each step she took seemed to accentuate the perfect curve of her hips, drawing my eyes irresistibly to the way she swayed.{/i}"
        scene w_258 with dissolve
        "{i}I couldn't help but follow the rhythmic movement, my mind beginning to race with thoughts I couldn't control.{/i}"
        "{i}She had this way of walking that was almost hypnotic, her bikini barely covering the roundness of her cheeks, leaving little to the imagination.{/i}"
        scene w_259 with dissolve
        "{i}The thin straps seemed to strain against her skin, teasingly hinting at what was beneath.{/i}"
        a_ "How could something so simple be so damn sexy? That ass... it's like it was made to be stared at, touched..."
        a_ "No, I need to focus. But damn, how could I not be distracted by a body like that? I could just... What if... No, stop it."
        $ renpy.music.play("audio/sfx/sfx_water2.opus", channel="sfx1", relative_volume=0.8)
        scene w_260 with dissolve
        "{i}As she neared the edge of the pool, I realized I hadn't taken my eyes off her for even a second.{/i}"
        "{i}My thoughts were a tangled mess of desire and restraint, as I fought the urge to let my fantasies take ov3er.{/i}"
        "{i}But with every step she took, it became harder and harder to resist.{/i}"
        scene w_261 with dissolve
        $ renpy.music.play(["audio/sfx/sfx_waves.ogg" , "audio/sfx/sfx_underwater.ogg"], channel="sfxloop1", fadein=2.0, relative_volume=0.6)
        "{i}Isabella slid into the water with a hypnotic grace. I stood there, observing every movement as she swam back and forth in the pool.{/i}"
        "{i}The way her hair floated on the surface and the way her body moved made my thoughts wander.{/i}"
        $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
        scene w_262 with dissolve
        "{i}She seemed so at ease, so tranquil.{/i}"
        "{i}And there I was, on the sidelines, unable to look away, trying to decide whether I should approach her or simply continue admiring her from afar.{/i}"
        scene w_263 with dissolve
        a_ "Should I go talk to her? Perhaps a casual conversation, just to break the ice. But what if she doesn't want to? What if I end up messing everything up?"
        "{i}As I stood there, my eyes locked onto Isabella. She moved with a grace that was both captivating and infuriating, especially knowing how close she was to Daniel.{/i}"
        "{i}The sunlight danced off her wet skin. I couldn’t help but feel a surge of conflicting emotions—anger, curiosity, and something else that I didn’t want to acknowledge.{/i}"
        scene w_264 with dissolve
        a_ "Is it worth it? Should I even try to get closer to her?"
        a_ "It would certainly get under Daniel’s skin, and after all the times he’s tried to make a move on Emma, maybe it’s time I played his game."
        a_ "She’s tempting, no doubt, and I can’t deny that the thought of revenge is appealing. But is this really the right way to go about it?"
        scene w_265 with dissolve
        "{i}I found myself inching forward slightly, still debating whether to act on the impulse. Isabella was oblivious to my presence.{/i}"
        "{i}I could feel the tension in my chest, the pull between wanting to strike back at Daniel and the uncertainty of what it might lead to.{/i}"

        $ alexsflirtisabelladay2 = False

        menu:
            "{font=fonts/hatten.ttf} {size=50}Flirt with Isabella{/size}{/font}":
                $ alexsflirtisabelladay2 = True

                "{i}I stood there, watching Isabella. Her every motion seemed deliberate, as if she knew I was watching. I couldn’t take my eyes off her.{/i}"
                a_ "Isabella is stunning, no doubt about it. And if I play my cards right, this could be the perfect opportunity to get back at Daniel."
                a_ "He’s always trying to seduce Emma, so why shouldn’t I do the same with Isabella?"
                a_ "It’s not just about revenge, though. Isabella is incredibly attractive, and I can’t help but feel a pull toward her."
                scene w_266 with dissolve
                a_ "Maybe she’s noticed me too. Maybe she’s doing this on purpose, trying to provoke me. If that’s the case, then why not give her what she’s asking for?"
                "{i}Her body, perfectly framed by the tiny bikini she wore, was a temptation I was finding hard to resist.{/i}"
                a_ "This could be a win-win. I get to mess with Daniel, and who knows where things might lead with Isabella. It’s not like she’s entirely innocent in this game."
                a_ "She’s definitely noticed me. And if she’s provoking me, maybe she wants me to make a move. Well, I’m not one to back down from a challenge."
                "{i}My eyes traced the curve of her back as she stretched, her posture practically inviting attention. I could feel the decision solidifying in my mind.{/i}"
                scene w_267 with dissolve
                a_ "I’m going to do it. I’m going to flirt with her, see where it goes."
                a_ "It’s time to turn the tables on Daniel, and if I can enjoy myself in the process, even better."
                a_ "This is going to be interesting. Let’s see how she reacts when I take the bait."
                scene w_268 with dissolve
                $ renpy.music.play("audio/sfx/sfx_splash.ogg", channel="sfx1", relative_volume=1.0)
                "{i}I stripped down to my swim trunks and dove into the pool, feeling the cool water envelop me as I swam towards her.{/i}"
                "{i}Isabella was leaning back against the edge, her elbows resting casually on the pool's border, looking relaxed and completely at ease.{/i}"
                "{i}There was something about the way she carried herself that drew me in, almost like an invitation to come closer.{/i}"
                scene w_269 with dissolve
                $ renpy.music.play(["audio/sfx/sfx_waves.ogg" , "audio/sfx/sfx_underwater.ogg"], channel="sfxloop1", fadein=2.0, relative_volume=0.6)
                "{i}As I swam closer, the water felt cool against my skin, a stark contrast to the heat building inside me. Every stroke brought me closer to Isabella.{/i}"
                "{i}She looked completely at ease, as if she knew exactly what kind of effect she was having on me. Her bikini clung to her curves, and it was hard to focus on anything other than the temptation right in front of me.{/i}"
                "{i}I couldn’t deny the attraction. It was like a magnetic pull, drawing me closer despite every rational thought screaming at me to stay away.{/i}"
                "{i}But this wasn’t just about desire—this was about revenge. If Daniel wanted to play his games with Emma, ​​I’d show him that two could play that game.{/i}"
                scene w_270 with dissolve
                a_ "She's noticed me. There's no doubt about that. She wants this as much as I do—or maybe she's just testing me. Either way, I'm not backing down."
                "{i}I allowed my gaze to linger on her, taking in every detail, every curve, the way her hair framed her face just right. This was going to be fun, no matter where it led.{/i}"
                a_ "She’s so close I can almost feel her heat through the water. If I’m going to break the ice, I need to keep it light—at least for now."
                a "Did you just finish a workout before coming here? You look like you’ve been keeping busy."
                "{i}She glanced at me, her expression unreadable, but there was a glint in her eye that made my pulse quicken. I couldn’t help but wonder if she was testing me, seeing how far I would go.{/i}"
                scene w_271 with dissolve
                isa "Just a bit of cardio. I like to keep in shape."
                "{i}Her voice was smooth, almost teasing, and it took everything I had not to let my gaze linger too long on the way her bikini hugged her body.{/i}"
                a_ "This is it. She’s engaging, and that means she’s interested. Now, I just need to find the right moment to push things further. Daniel won’t know what hit him."
                a "Cardio, huh? Looks like it’s working for you. You definitely know how to keep things... interesting."
                "{i}Isabella's response to my compliment was smooth, almost effortless, like she was used to receiving them and dishing them out in return{/i}"
                scene w_270 with dissolve
                isa "You too, Alex,"
                "{i}She said, her eyes briefly flicking over me, making me feel like I was being appraised. There was a brief pause before she added, {/i}"
                isa "So, how do you know Ava? I didn’t expect this."
                a_ "I’ve got to play this right. Keep it light, keep it fun, but make sure she knows I’m interested."
                a "Ava? We go way back. I actually met her through mutual friends a few years ago. She’s one hell of a trainer, that’s for sure. Helps keep me in shape, too."
                "{i}*I grinned, letting my eyes briefly drop to the water before meeting Isabella’s gaze again.{/i}"
                isa "She’s been great with me. Really pushes me to my limits, but in a good way."
                "{i}There was something in the way she said it, a hint of a challenge, maybe, or was I imagining it?{/i}"
                a_ "She’s good at this. But I’ve got to be better."
                a "You’ve clearly been putting in the work. It shows."
                scene w_271 with dissolve
                "{i}My words were simple, but I made sure my tone was heavy with implication.{/i}"
                "{i}Her lips curled into a small smile, one that didn’t quite reach her eyes.{/i}"
                "{i}It was the kind of smile that said she knew exactly what was happening, but wasn’t going to let on.{/i}"
                a_ "This is going well. She’s not backing down, but she’s not making it easy either. Just the way I like it."
                isa "And you, Alex? What’s your secret? You look like you’ve been keeping busy too."
                a_ "She’s giving me an opening. Time to push a little further."
                a "Let’s just say I’ve got my own methods for staying in shape. But I’m always open to new ideas… if you’ve got any tips."
                "{i}She didn’t move, but there was a shift in the atmosphere. I could see the way her chest rose and fell with each breath, the way the water rippled against her skin, highlighting every curve.{/i}"
                scene w_272 with dissolve
                "{i}I could feel the warmth of her body radiating through the water, so close now that I could almost reach out and touch her.{/i}"
                a_ "This is it. No turning back now."
                scene w_273 with dissolve
                "{i}I took a small step closer, closing the gap between us. All my focus was on Isabella, on the way her eyes watched me, challenging me to make the next move.{/i}"
                "{i}I could smell her perfume, faint but intoxicating, mingling with the chlorine and making my head spin slightly.{/i}"
                scene w_274 with dissolve
                a "So, Isabella, "
                "{i}I began, my voice low, almost a whisper.{/i}"
                a "what’s your take on mixing business with pleasure?"
                "{i}She didn’t answer right away, but there was something in her gaze that told me she wasn’t going to back down either.{/i}"
                a_ "She’s in this as much as I am. Good."
                scene w_274 with dissolve
                "{i}Every inch of my skin was aware of Isabella’s closeness, the way her leg had somehow slipped between mine, pressing firmly against my inner thigh.{/i}"
                a_ "She knows exactly what she’s doing. But why isn’t she backing off? Is she testing me, waiting to see how far I’ll go?"
                scene w_275 with dissolve
                "{i}I could feel the heat pooling, spreading lower as her thigh brushed against me. The feel of her skin against mine was driving me crazy.{/i}"
                a_ "I need to stay focused, but damn, she’s making it hard. Literally."
                "{i}She just stared at me, those eyes revealing nothing. It was infuriating, arousing, and confusing all at once. {/i}"
                a_ "What are you playing at, Isabella? Why aren’t you giving me anything?"
                "{i}Under the water, her leg stayed where it was, unyielding, almost possessive in the way it pressed against me.{/i}"
                scene w_274 with dissolve
                a_ "God, if she doesn’t move soon, I don’t know if I’ll be able to hold back."
                a "Isabella"
                "{i}I finally breathed out, my voice low and strained. I wasn’t sure what I was going to say next, or even if I could speak without betraying how much she was getting to me.{/i}"
                scene w_275 with dissolve
                "{i}But before I could find the words, she shifted slightly, her leg brushing even more firmly against me, and I couldn’t stop the soft groan that escaped my lips.{/i}"
                a_ "Shit, she definitely heard that. Get a grip, Alex. You’re better than this."
                scene w_274 with dissolve
                isa "Something wrong, Alex?"
                "{i}Her voice was smooth, too smooth, and I knew she was toying with me.{/i}"
                a_ "You want to play games? Fine. But I’m not going to lose."
                a "Nothing at all, "
                a "Just... enjoying the moment."
                a "Isabella, why don’t we stop playing games? Let’s take this somewhere more... private."
                scene w_276 with dissolve
                $ renpy.music.play("audio/sfx/sfx_laugh1.mp3", channel="sfx1", relative_volume=0.3)
                "{i}She didn’t flinch, didn’t hesitate. Instead, she let out a laugh, a sound that felt like a punch to the gut.{/i}"
                isa "Oh, Alex... Why would I go to bed with someone like you? A broke, little nobody?"
                "{i}I felt the sting of her words, but I wasn’t going to let her get away with it.{/i}"
                a "You were just flirting with me, Isabella. Don’t pretend you didn’t notice. You’re not that innocent."
                isa "Flirting? Sure, I was. But did you actually think it meant something? That’s adorable, Alex."
                "{i}I could feel my anger rising, but I kept my voice steady.{/i}"
                a "What was the point of all this, then?"
                isa "Fun, Alex. It was just fun. You got a little close, we shared a moment. That’s all it was. Don’t take it so seriously."
                scene w_277 with dissolve
                "{i}She pushed me back with her foot, that smirk never leaving her face.{/i}"
                scene w_278 with dissolve
                a "You’re kidding, right? After all that, you’re just going to laugh it off?"
                isa "Why not? You enjoyed yourself, didn’t you? No harm done. But let’s be honest—you’re not on my level, Alex. Don’t be mad. It’s just... reality."
                a "You think this is funny? That you can just toy with people and walk away?"
                isa "Entertaining, Alex. Not funny, entertaining. But don’t take it personally. This was just a game, and you knew the stakes when you decided to play."
                "{i}I wanted to lash out, but her calm, dismissive tone only made me feel more powerless.{/i}"
                isa "You liked rubbing your dick against my thigh, didn't you?"
                isa "But let’s just say... you had your fun. But that’s all you’re going to get from me."
                "{i}Her words hung in the air, cold and final. I realized then just how much she’d been in control the whole time.{/i}"
                scene w_279 with dissolve
                "{i}As Isabella began to swim away, I followed her, my mind still reeling from our exchange. The water grew shallower until it barely reached our ankles.{/i}"
                "{i}I wasn’t about to let her have the last word. I quickened my pace slightly, catching up to her as we walked toward the pool’s edge.{/i}"
                $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
                scene w_280 with dissolve
                a "So, that was all just a game to you? Nothing real at all?"
                isa "Oh, come on, Alex. Don’t tell me you actually thought there was something more."
                a "You’re seriously telling me you didn’t feel anything? Not even a little bit of interest?"
                isa "Interest? Sure, for a moment. But it was fleeting, like a spark that dies out before it can catch fire."
                isa "Besides, why are you so desperate to know? Isn’t your wife enough for you?"
                scene w_281 with dissolve
                "{i}Her question cut deeper than I wanted to admit.{/i}"
                "{i}I struggled to keep my cool, not wanting to give her the satisfaction of knowing she’d hit a nerve.{/i}"
                a "Emma and I... We have our issues."
                a "But this isn’t about her. It’s about what just happened between us. You can’t deny there was something there."
                scene w_283 with dissolve
                isa "Can’t I? Alex, you need to understand something. What just happened was nothing more than a bit of fun."
                isa "A distraction, really. But don’t confuse that with something meaningful."
                scene w_282 with dissolve
                a "And Daniel? Does he know about your ‘distractions’?"
                scene w_283 with dissolve
                isa "Daniel gives me what I want. Why should he care if I find amusement elsewhere?"
                isa "As long as I’m happy, he’s content to keep me in the lifestyle I’m accustomed to."
                scene w_282 with dissolve
                a_ "Her nonchalant attitude toward her marriage started to make things clearer for me."
                a "So, all of this—your marriage, your life with him—it’s just about the money and luxury?"
                scene w_283 with dissolve
                isa "Why wouldn’t it be? Love is overrated, Alex. It’s a fairy tale. What really matters is security, power."
                isa "Daniel provides that, and I give him what he needs in return."
                scene w_282 with dissolve
                a "So that’s all there is for you? No real connection, no emotions, just transactions?"
                scene w_283 with dissolve
                isa "Exactly. It’s efficient. Why waste time on feelings that only complicate things?"
                scene w_282 with dissolve
                a "And what if one day Daniel stops giving you what you want? What then?"
                scene w_283 with dissolve
                isa "Then I’ll find someone else who can. It’s as simple as that."
                isa "But let’s not get ahead of ourselves. Daniel knows his role, and I know mine."
                scene w_282 with dissolve
                "{i}Her words left me with a bitter taste in my mouth, but I couldn’t help pressing further.{/i}"
                a "You’re really okay with living like this? No love, no real connection? Just... empty transactions?"
                scene w_283 with dissolve
                isa "Empty? Not at all. I’m quite full, actually. Full of everything I could ever want."
                isa "Love is a luxury for those who can afford to waste time on it."
                isa "I prefer something more tangible. And as for connections, they’re only as valuable as what they bring me."
                scene w_282 with dissolve
                a "I don’t know how you can live like that, Isabella. It sounds... hollow."
                scene w_283 with dissolve
                isa "Hollow?"
                isa "Maybe to you, Alex. But to me, it’s just reality."
                isa "Now, if you don’t mind, I have better things to do than educate you on how the world really works."
                scene w_282 with dissolve
                "{i}She started to walk away, her tone dismissive, but I wasn’t quite done yet.{/i}"
                a "Is that why you’re with Daniel? Because he can give you everything you want? What happens when someone else offers you more?"
                scene w_283 with dissolve
                isa "Then Daniel will become a memory, just like anyone else who’s no longer useful to me."
                isa "But don’t worry, Alex. You’ll have plenty of time to think about what could have been while you’re back to living your little life."
                scene w_282 with dissolve
                "{i}Her coldness struck a final blow, and I realized then that there was no point in pursuing this any further.{/i}"
                "{i}Isabella was who she was—unapologetically ruthless, and completely uninterested in anything that didn’t serve her needs.{/i}"
                scene w_284 with dissolve
                isa "Now, if you’ll excuse me, I’ve got more important things to do than humor your questions."
                "{i}With that, she turned and walked away, leaving me to watch. There was nothing more to say.{/i}"
                scene w_285 with dissolve
                "{i}As Isabella turned to leave, her foot slipped on the wet tiles.{/i}"
                "{i}It all seemed to happen in slow motion—the slight gasp escaping her lips, the way her arms flailed as she tried to regain her balance, the inevitable fall backward.{/i}"
                "{i}My instincts kicked in, honed from years of boxing, and I knew before she hit the ground that she was going to get hurt, but not seriously.{/i}"

                $ alexsholdisabelladay2 = False

                menu:
                    "{font=fonts/hatten.ttf} {size=50}Hold Isabella.{/size}{/font}":
                        $ alexsholdisabelladay2 = True

                        "{i}In that split second, I had a choice to make: do I reach out and catch her, or let her fall?{/i}"
                        "{i}But a part of me wanted to let her take the hit, to let her feel a fraction of the pain she had just inflicted on my pride.{/i}"
                        "{i}But another part, the one that still had some decency left, knew that I couldn’t just stand by and do nothing.{/i}"
                        a_ "She may have humiliated me, but that doesn’t mean I should let her get hurt."
                        "{i}My body moved on its own, reflexes taking over, as I reached out to grab her before she could crash to the ground.{/i}"
                        isa "Alex—"
                        scene w_289 with dissolve
                        a "Looks like fate really wanted you to fall into my arms, huh?"
                        "{i}Isabella blinked in surprise, her expression softening as she processed what just happened. Her eyes held a mix of surprise and something else—something I couldn’t quite place yet.{/i}"
                        isa "I didn’t expect you to be so quick... or so strong."
                        "{i}Her compliment caught me off guard. Coming from Isabella, someone who rarely gave anyone the satisfaction of praise, it felt oddly gratifying.{/i}"
                        "{i}She was still in my arms, closer than I ever imagined she’d be. The warmth of her body pressed against mine, her breathing steady as she looked up at me.{/i}"
                        a "Well, if I’d known you’d be this... receptive in my arms, I might’ve tried catching you sooner."
                        "{i}Isabella’s lips curled into a teasing smile, a hint of playfulness glinting in her eyes.{/i}"
                        isa "Receptive? Don’t get too confident, Alex."
                        isa "I might just be enjoying this more than I should, but don’t think for a second that I’m easy to sway."
                        a_ "This is Isabella, always keeping me on my toes, always maintaining control. But now, in this moment, she seemed to be letting go of that control just a little."
                        a "Oh, I wouldn’t dream of it. But I have to admit, you feel pretty perfect in my arms right now."
                        $ renpy.music.play("audio/sfx/sfx_laugh1.mp3", channel="sfx1", relative_volume=0.3)
                        "{i}She laughed softly, her eyes never leaving mine. There was a certain lightness in her demeanor, a stark contrast to the icy barrier she usually kept up.{/i}"
                        isa "You’ve got a smooth tongue, Alex. But don’t get too used to this. It’s not every day someone gets to hold me like this."
                        "{i}Her tone was still playful, but there was a sensual undertone that hadn’t been there before. And I was more than willing to play along, as long as she let me.{/i}"
                        a "I wouldn’t dare take it for granted. But as long as I’ve got you here, I’m going to enjoy every moment."
                        "{i}Isabella’s smile deepened, and she didn’t pull away. If anything, she seemed to lean in just a little closer, her fingers lightly tracing a pattern on my chest as if considering her next move.{/i}"
                        isa "Enjoy it while it lasts, then. You’ve earned it... for now."
                        a "Oh, I intend to. But let’s be honest, you’re enjoying this too."
                        $ renpy.music.play("audio/sfx/sfx_laugh1.mp3", channel="sfx1", relative_volume=0.3)
                        "{i}She chuckled, her gaze softening even more as she looked up at me, her face inches from mine.{/i}"
                        isa "Maybe I am. But don’t get any ideas, Alex. This is still just a bit of fun."
                        "{i}With that, I gently set her back on her feet, careful to make sure she was steady before letting go.{/i}"
                        scene w_290 with dissolve
                        "{i}As much as I wanted to keep her close, I knew this was where the game ended—for now, at least.{/i}"
                        scene w_291 with dissolve
                        isa "Safe and sound, thanks to you."
                        scene w_290 with dissolve
                        a "Anytime. Just don’t make a habit of falling for me."
                        scene w_291 with dissolve
                        isa "You wish. But I’ll give you this—you’ve got some skills, Alex. Maybe more than I gave you credit for."
                        scene w_290 with dissolve
                        a "What can I say? I guess it was fate that you ended up in my arms."
                        scene w_291 with dissolve
                        isa "Fate? Or maybe just your reflexes? "
                        scene w_290 with dissolve
                        a "Could be both. Though, I have to say, you fit quite perfectly here. Maybe you should stay a little longer."
                        "{i}I let the words hang between us, watching as her smile grew, more playful than before. She didn't pull away; instead, she tilted her head slightly, as if considering the idea.{/i}"
                        scene w_291 with dissolve
                        isa "You do have a way with words, Alex."
                        isa "But you know, I was just starting to think that you might have other intentions with all this rescuing."
                        scene w_290 with dissolve
                        a "Would you blame me if I did?"
                        scene w_291 with dissolve
                        isa "Not really. But don’t get any ideas. I’m not that easily won over."
                        "{i}Her words were firm, but there was a lightness in her tone that hadn't been there earlier. It was like she was enjoying this game, the push and pull between us.{/i}"
                        scene w_290 with dissolve
                        a "I wouldn’t dream of it… unless you wanted me to, of course."
                        scene w_291 with dissolve
                        $ renpy.music.play("audio/sfx/sfx_laugh1.mp3", channel="sfx1", relative_volume=0.3)
                        "{i}Isabella laughed, a soft, melodic sound that echoed in the empty space around the pool.{/i}"
                        isa "You’re incorrigible, Alex."
                        scene w_290 with dissolve
                        a "And you love it."
                        scene w_291 with dissolve
                        "Perhaps. But we both know this is just a bit of fun, right?"
                        scene w_290 with dissolve
                        a "Of course. No strings, just enjoying the moment."
                        "{i}There was a pause, a moment where our gazes locked, and for a second, it felt like there was more between us than just the banter.{/i}"
                        "{i}But then, she broke the silence with a smile that was all mischief and charm.{/i}"
                        scene w_292 with dissolve
                        isa "Well, I suppose I should thank you for catching me. But how about we get out of these wet clothes and continue this conversation somewhere more comfortable?"
                        a "Lead the way."
                        scene w_288 with dissolve
                        "{i}With that, she turned, and I followed her, feeling a mix of anticipation and curiosity about where this game would take us next.{/i}"

                    "{font=fonts/hatten.ttf} {size=50}Let Isabella fall.{/size}{/font}":
                        $ alexsholdisabelladay2 = False

                        "{i}In that split second, I had a choice to make: do I reach out and catch her, or let her fall?{/i}"
                        "{i}But a part of me wanted to let her take the hit, to let her feel a fraction of the pain she had just inflicted on my pride.{/i}"
                        "{i}But another part, the one that still had some decency left, knew that I couldn’t just stand by and do nothing.{/i}"
                        "{i}I could see the fall before it happened, and for a split second, I considered reaching out to catch her.{/i}"
                        "{i}But then I thought, why not let her taste a bit of humility? Maybe she needs to come down to earth for a moment.{/i}"
                        a_ "Isabella is going to be pissed, but she had it coming. Maybe she'll learn not to play games."
                        $ renpy.music.play("audio/sfx/sfx_falling_body1.opus", channel="sfx1", relative_volume=0.1)
                        $ renpy.music.play("audio/sfx/sfx_splash.ogg", channel="sfx2", relative_volume=1.0)
                        scene w_286 with dissolve
                        "{i}Isabella hit the ground with a splash, water rippling around her as she landed on the cold tiles of the shallow end.{/i}"
                        "{i}Her face contorted in pain, and she grimaced, clearly not expecting that outcome.{/i}"
                        a "Well, well, well… Seems like you're not quite on my level now, huh?"
                        "{i}I said, a smirk tugging at the corner of my mouth. The irony was just too good to pass up.{/i}"
                        isa "Oh, you think you're so funny, don't you, Alex?"
                        "{i}she snapped back, her voice laced with irritation as she tried to compose herself.{/i}"
                        scene w_287 with dissolve
                        "{i}I could see the mix of anger and embarrassment on her face as she struggled to regain her composure.{/i}"
                        "{i}Part of me felt a little bad, but another part of me relished the sight. She'd been toying with me all day, and now the tables had turned.{/i}"
                        a "Hey, just trying to lighten the mood,"
                        "{i}I replied, trying to stifle a laugh but failing miserably.{/i}"
                        "{i}Isabella shot me a withering look. Her pride was clearly bruised more than her body.{/i}"
                        isa "Well, congratulations, Alex. You’ve successfully made me look like a fool,"
                        "{i}she said, sarcasm dripping from every word.{/i}"
                        scene w_288 with dissolve
                        "{i}I watched as she turned away, her back straight and her head held high despite the fall. There was something admirable about her resilience, even when she was upset. But I knew I’d pushed too far this time.{/i}"
                        a "C'mon, don’t be like that. It was just a joke,"
                        "{i}I called after her, though I knew it was too late to mend things now.{/i}"
                        "{i}She didn't bother to turn around, just kept walking away, her wet hair trailing behind her like a curtain. The sound of her bare feet slapping against the wet tiles echoed through the quiet garden.{/i}"
                        isa "Enjoy your little victory, Alex. You’ll be alone with it,"
                        "{i}She tossed back over her shoulder, her tone cold as ice.{/i}"
                        a_ "Isabella’s tougher than I thought. But damn, she knows how to hit where it hurts."
                        "{i}And with that, she was gone, leaving me alone in the empty pool.{/i}"
                        scene black with dissolve
                        "{i}I stood there for a moment, letting her words sink in. I’d won, but at what cost? The satisfaction of seeing her knocked down a peg didn’t feel as sweet as I thought it would.{/i}"
                        "{i}I watched as she disappeared into the distance, realizing that maybe, just maybe, I’d let my pride get the best of me.{/i}"

            "{font=fonts/hatten.ttf} {size=50}I will be alone{/size}{/font}":
                $ alexsflirtisabelladay2 = False

                a_ "What am I doing? Flirting with Isabella... It's like I'm just trying to distract myself from everything else going on."
                a_ "Maybe instead of diving into that, I should step back and give myself some space."
                a_ "She’s charming, no doubt about that, but this isn’t the time. I need to be alone, clear my head, figure out what I actually want."
                a_ "Chasing after her right now would just complicate things even more. Besides, there’s something peaceful about being alone for a while, just me and my thoughts."
                a_ "Yeah... that sounds like exactly what I need."
    
        scene black with dissolve
        $ renpy.music.stop("ambient1", fadeout=2.0)
        $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
        $ renpy.pause()

        if alexsflirtisabelladay2 and alexsholdisabelladay2:
            scene w_327 with fade
            "{i}I spent the rest of the day with Isabella, and before I knew it, the sun had dipped below the horizon, casting long shadows over the estate.{/i}"
            scene w_298 with dissolve
            "{i}The air was warm, and the sky had taken on a deep shade of blue, dotted with the first stars of the evening.{/i}"
            "{i}As I stood across from Isabella, I couldn't help but notice how the dim lighting made her look even more captivating.{/i}"
            isa "You know, Alex, it's strange... Spending the whole day with you like this. I never imagined we’d get along so well."
            scene w_296 with dissolve
            a "Is that so? You seemed pretty sure I was nothing more than a nuisance this morning."
            scene w_297 with dissolve
            $ renpy.music.play("audio/sfx/sfx_laugh1.mp3", channel="sfx1", relative_volume=0.3)
            isa "Maybe you still are, but I’ll admit, you’ve got a way of making even a nuisance enjoyable."
            "{i}I chuckled, taking a sip of my drink, feeling the warmth of the alcohol settle in.{/i}"
            scene w_296 with dissolve
            "{i}There was something about the way she said that, a mix of honesty and playful teasing, that kept me on my toes.{/i}"
            a "Well, I could say the same about you. But I have to ask, what changed?"
            a "You were ready to walk away without looking back, and now we’re here."
            scene w_297 with dissolve
            isa "I guess I realized something today. You’re different."
            isa "Alex. Most men I know are easy to predict. But you... you surprise me. And I like surprises."
            scene w_296 with dissolve
            "{i}I felt a smirk forming at the corner of my lips.{/i}"
            a "So, does that mean I’ve earned some points in your book?"
            scene w_297 with dissolve
            isa "Maybe a few. But don’t get too confident. I still think you’re trouble."
            scene w_296 with dissolve
            a "Trouble, huh? You know, most people would take that as an insult."
            "{i}With a grin, she took a step closer, lowering her voice.{/i}"
            scene w_297 with dissolve
            isa "But we both know, trouble is what keeps things interesting."
            "{i}There was a pause, a moment where the only sound between us was the gentle rustle of the leaves in the evening breeze.{/i}"
            "{i}The atmosphere was charged, not with tension, but with a mutual understanding. It was clear we were playing a game, one neither of us intended to lose.{/i}"
            scene w_296 with dissolve
            "So, Isabella, what’s the next move in this game of ours?"
            "{i}Her eyes sparkled with mischief.{/i}"
            scene w_297 with dissolve
            isa "How about we take this conversation somewhere more private? Somewhere we can... talk without distractions."
            scene w_296 with dissolve
            a "Are you serious?"
            scene w_297 with dissolve
            $ renpy.music.play("audio/sfx/sfx_laugh1.mp3", channel="sfx1", relative_volume=0.3)
            isa "No..."
            isa "Well, Alex, it's been... interesting. But I think it's time I head inside."
            scene w_296 with dissolve
            a "Interesting is one way to put it. You sure you want to call it a night?"
            "{i}Her smile widened slightly as she took a step back, raising her hand in a casual wave.{/i}"
            scene w_299 with dissolve
            isa "For now. Maybe we'll pick this up another time, if you're lucky."
            "{i}I stood there for a moment, watching her go, a mix of amusement and curiosity swirling in my thoughts.{/i}"
            scene black with dissolve
            "{i}With that, she turned on her heel, her back to me as she walked toward the mansion, her silhouette fading into the dim light of the estate. {/i}"
        else:
            scene w_294 with dissolve
            a_ "What the hell am I doing here? Drinking wine alone by the pool like this will somehow give me clarity?"
            a_ "Maybe it's just the alcohol talking, but it’s been a while since I've felt this out of control. This whole situation with Daniel… it’s eating away at me."
            a_ "What did I expect? That I'd come here, flash a few smiles, and everything would just fall into place?"
            a_ "No. Daniel’s got the upper hand—he always has. And now, I’m just another pawn in his game, desperately trying to stay relevant."
            scene w_293 with fade
            "{i}I stared into the rippling water, hoping it would somehow reflect the answers I needed.{/i}"
            "{i}But all I saw was the distorted mess of my own reflection, a perfect metaphor for the chaos brewing in my mind.{/i}"
            a_ "It’s not just about winning anymore, is it? It’s become something darker, something personal."
            a_ "Daniel knows how to get under my skin, to twist the knife in a way that makes me question everything. And the worst part is, I let him."
            a_ "Every damn time. I knew coming here was a risk, but I didn’t think it would unravel me like this. I thought I was stronger, smarter."
            "{i}The wine in my glass swirled with every faint movement, mirroring the turbulence within me.{/i}"
            scene w_295 with dissolve
            a_ "What’s the endgame here? To beat Daniel? To prove that I’m not just some washed-up has-been trying to relive the glory days?"
            a_ "Or is it more than that? Is it about reclaiming some part of myself that I’ve lost along the way?"
            a_ "Hell, maybe it's about revenge. But revenge against who? Daniel? Or myself for ever letting it get this far?"
            "{i}Something’s got to give—either Daniel, or me. But for tonight, all I had was this moment, this drink, and the uncertainty of what comes next{/i}"
    else:
        scene black with fade
        "{i}The day passed by in a blur. Emma and I stayed together, talking about everything and nothing, trying to forget the incident with Daniel.{/i}"
        $ renpy.music.stop("ambient1", fadeout=2.0)
        scene w_327 with dissolve
        $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
        "{i}There was something in the quiet of the late afternoon that brought us a strange peace, as if we were both too tired to fight or worry anymore.{/i}"
        scene w_224 with dissolve
        "{i}The sun gradually dipped, painting the sky with warm colors, and we stayed there, side by side, until the night finally fell.{/i}"
        a_ "I know things are still tense between us, but at least she didn’t leave."
        a_ "Maybe there’s still hope, a chance to fix everything, to prove I’m better than that guy."
        scene w_225 with dissolve
        a_ "But the truth is, I don’t know how yet. I just know I don’t want to lose her."
        a "Remember the time we got lost on that road trip? You kept insisting we should just keep driving, no map, no GPS."
        e "Oh, yeah! And you were so sure we’d find a gas station just around the corner."
        e "Four hours later, we were still lost in the middle of nowhere."
        a "But it wasn’t all bad. We ended up finding that little diner, the one with the amazing pie."
        a "We never would have found it if we hadn’t gotten lost."
        scene w_226 with dissolve
        e "True, true. That was one of those rare moments where your stubbornness actually led to something good."
        a "Hey, I like to think of it as being adventurous."
        e "Adventurous? That’s one word for it. I was ready to strangle you by the time we finally pulled up to that diner."
        a "But you didn’t. And instead, we had pie. It was worth it, wasn’t it?"
        scene w_227 with dissolve
        e "It was. I suppose there’s something to be said for your... unique approach to life."
        "{i}I couldn't help but smile at the memory.{/i}"
        "{i}It was one of those times that defined our relationship—an unpredictable journey with sweet rewards, even if the path was a bit rough.{/i}"
        a "We’ve had our moments, haven’t we? Not all of them easy, but... they’ve shaped us."
        scene w_226 with dissolve
        e "Yeah, they have. I guess that’s what happens when you’ve known someone for as long as we have. The good, the bad, it all blends together."
        a_ "I wonder if she misses those times as much as I do. Even if things are different now."
        a "We were quite the team back then. Maybe we still are, in some ways."
        e "Maybe. But things change, Alex. People change. We’re not who we were back then."
        a "No, we’re not. But that doesn’t mean we can’t still appreciate what we had, what we still have, even if it’s different now."
        e "I suppose. It’s just... hard sometimes, you know? To reconcile the past with the present."
        a "Yeah, I know. But for what it’s worth, I’m glad we have those memories, Emma. I wouldn’t trade them for anything."
        e "Me neither, Alex. Me neither."
        scene w_228 with dissolve
        e "..."
        a "You know, Emma, I was just thinking... You still look as stunning as ever. It's like time hasn't touched you at all"
        e "Flattery won’t get you anywhere, Alex."
        a_ "She says that, but I can see the faint smile playing on her lips."
        scene w_229 with dissolve
        a "Oh, I don't know about that. It's worked before, hasn't it?"
        e "That was a long time ago. Things have changed."
        a "Some things, maybe. But not everything. The way I see it, some things are just as they were..."
        scene w_230 with dissolve
        a "Like the way you still know how to drive me crazy."
        e "Alex..."
        a_ "There’s a hint of hesitation in her voice, just the slightest crack in her defenses."
        scene w_232 with dissolve
        a "You remember those nights, don’t you? When we used to stay up until dawn, talking about nothing and everything... and then not talking at all."
        e "I remember. But that was then, Alex. We can’t just pick up where we left off."
        scene w_231 with dissolve
        "{i}I step closer, feeling the warmth radiating from her. My hand finds her waist, pulling her gently toward me. She doesn't resist.{/i}"
        a "Why not? We’re here now, aren’t we? Just you and me... no one to interrupt us."
        e "It’s not that simple."
        a_ "I can see the way she’s holding back, but I also see the way her body leans just a little closer."
        scene w_234 with dissolve
        a "It can be, if we let it. You know, I've been thinking... Maybe we’re overcomplicating things."
        a "What if we just let ourselves feel what we want to feel, without overthinking it?"
        e "You make it sound so easy."
        a "Maybe it is. Come on, Emma, we’ve always been good together. I can still see that spark in your eyes."
        e "And I can see that you haven’t changed one bit."
        a "Maybe that’s a good thing."
        e "Alex..."
        a "Yes, Emma?"
        "{i}My voice drops, becoming softer, more intimate.{/i}"
        e "I shouldn’t..."
        a "But you want to. I can feel it."
        "{i}Her eyes close for a moment as my fingers brush along her back. The tension in her shoulders melts away as she lets out a small sigh.{/i}"
        "{i}It was like the world faded away, leaving just the two of us in that moment.{/i}"

        if alexemmaanddanieljealousday1:
            $ alexkissemmaday2 = False
            "{i}Emma and I found ourselves closer than we had been in a long time. The soft glow of the garden lights illuminated her face, revealing every nuance of her expression.{/i}"
            scene w_231 with dissolve
            "{i}My hand naturally found its way to her waist, pulling her gently towards me.{/i}"
            scene w_234 with dissolve
            "{i}I could feel the heat radiating from her body, her skin soft against mine.{/i}"
            a_ "I can't deny the pull I feel towards her, it’s undeniable."
            e "Alex, we shouldn’t…"
            "{i}Her breath mingled with mine as our faces drew closer. I could see the hesitation in her eyes, but the way her body pressed against mine told a different story.{/i}"
            "{i}My hand moved lower, resting on the small of her back, pulling her into me even more.{/i}"
            a "Emma, it feels right…"
            scene w_235 with dissolve
            "{i}I could almost taste her lips, the moment suspended in time.{/i}"
            "{i}But just as our lips were about to meet, she placed her hand softly against my lips, stopping me. There was desire in her touch, but also restraint.{/i}"
            e "Alex, we need to stop… We can't…"
            "{i}Her voice was barely a whisper, filled with longing and reluctance. My heart pounded, every instinct telling me to close the distance between us, but I respected her pause.{/i}"
            "{i}I kept my forehead against hers, breathing heavily, feeling the intensity of the moment. {/i}"
            scene w_234 with dissolve
            "{i}We were both caught in the tension of wanting something that maybe we shouldn’t have.{/i}"
            e "..."
            a "..."
        else:
            $ alexkissemmaday2 = True
            scene w_233 with dissolve
            $ renpy.music.play("audio/sfx/sfx_kissing_lip_to_lip.opus", channel="sfxloop1", fadein=2.0, relative_volume=0.2)
            "{i}Her lips were soft against mine, and I felt a surge of warmth spreading through my chest.{/i}"
            e "Alex..."
            "{i}I could feel her breath hitch as my hand slid down to the small of her back, pulling her closer.{/i}"
            "{i}Her body molded against mine, and the heat between us was undeniable. Her skin was warm, almost burning where we touched, and the taste of her kiss was intoxicating.{/i}"
            "{i}Emma's body pulling me deeper into the kiss. I could feel the tension in her, the struggle between giving in and holding back, but she didn't push me away.{/i}"
            "{i}Instead, she pressed against me, her breath heavy as the kiss deepened. Our bodies were almost inseparable.{/i}"
            e "We... we should stop..."
            a_ "But damn, it felt so right, so perfect in that moment."
            $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
            scene w_234 with dissolve
            "{i}I pulled back slightly, just enough to look into her eyes. I could see the conflict there, the battle between what we wanted and what we should do.{/i}"
            e "We really need to stop... for now."
            "{i}Her voice was shaky, but firm, and I knew this was as far as we could go tonight.{/i}"
            "{i}I nodded, letting out a breath I hadn't realized I'd been holding.{/i}"

        scene w_236 with dissolve
        "{i}I could see it in her eyes—an unspoken tension, a mix of excitement and something else. She was trembling slightly, and I knew it wasn’t just from the chill in the air.{/i}"
        "{i}There was a hesitation in her movements, a lingering effect of the closeness we had just shared, making her seem almost shy as she looked up at me.{/i}"
        e "Thanks for the chat, Alex. It was... nice."
        "{i}Her voice was soft, almost breathless, and I could tell she was struggling to maintain her composure.{/i}"
        "{i}That slight quiver in her words revealed more than she probably intended, and it took everything in me not to reach out and pull her back into the moment we had almost let spiral out of control.{/i}"
        a "Yeah, it was... really nice."
        scene w_237 with dissolve
        "{i}Emma turned slightly, ready to make her exit, and I let out a breath I hadn’t realized I was holding. But just as she took her first steps away, she hesitated, her body turning back ever so slightly.{/i}"
        "{i}She glanced over her shoulder, her eyes catching mine for what felt like one final time. That look—it was brief, but it was enough to send a shiver down my spine.{/i}"
        "{i}Then, she turned away fully, walking into the shadows, leaving me standing there, feeling the weight of what had just happened, and what hadn’t.{/i}"
        scene w_238 with dissolve
        a_ "Why does it feel like something just slipped through my fingers? Was she feeling the same thing?"
        "{i}I wanted to go after her, to say something, anything, but the moment had passed, and all I could do was watch her disappear into the night.{/i}"
        "{i}Emma’s figure faded into the darkness, but her presence lingered, leaving me with a mix of frustration and anticipation.{/i}"
        scene black with dissolve
        "{i}My mind was racing, filled with thoughts of her—the way her body had felt against mine, the softness of her voice, the way her eyes had lingered just a moment too long.{/i}"

    scene w_239 with fade
    a_ "It's only been a few days in this mansion, and already so much has unfolded. I can't help but wonder what's next."
    a_ "There's a tension here, something simmering just beneath the surface. I came here with certain expectations, but now..."
    a_ "now I’m starting to realize that this is just the beginning. And if this is how it starts, what else is waiting for me?"

    if alexemmaanddanieljealousday1 and alexspillswineday2:
        a_ "Why did I let jealousy take over, not once, but twice?"
        a_ "It’s like I couldn’t control myself, and now Emma probably hates me even more for it. Every time I try to get closer, I just end up pushing her further away."
        a_ "I don’t know how to fix this, how to undo the damage I’ve caused. She’s slipping through my fingers, and I can’t seem to stop it."
    elif alexemmaanddanieljealousday1 and not alexspillswineday2:
        a_ "At least today, I didn’t let jealousy get the better of me like I did yesterday. Emma and I actually had a decent conversation, even if we didn’t kiss."
        a_ "But I know one good moment isn’t enough to make up for the past."
        a_ "If I want her to forgive me, I’m going to have to keep trying, keep proving to her that I can be better. It’s not going to be easy, but I can’t give up now."
    elif not alexemmaanddanieljealousday1 and not alexspillswineday2:
        a_ "I didn’t let jealousy win this time. We kissed—finally—but I can tell that Emma isn’t ready to forgive me just yet."
        a_ "She enjoyed it, I could feel that, but there’s still a wall between us. At least I’ve earned a small victory. God, she’s so sexy... the way her body feels against mine."
        a_ "It’s going to take more than one kiss to make things right, but I’m not giving up. Not when she looks at me like that."
    elif not alexemmaanddanieljealousday1 and alexspillswineday2:
        a_ "Yesterday, I managed to hold back my jealousy, but today... today I let it get the best of me."
        a_ "Because of that, I lost my chance to spend more time with Emma."
        a_ "I’ve got to figure out how to make this right, how to fix what I’ve messed up. I can’t keep letting my emotions control me like this, especially not when it comes to her."

    scene w_240 with dissolve
    a_ "It’s going to be tough winning Emma back, especially with so many temptations inside and outside this mansion."

    if alexflirteleanorday1:
        a_ "Eleanor... I can still feel the way her body pressed against mine, the softness of her curves under my hands."
        a_ "She didn’t pull away when I grabbed her ass; in fact, she seemed to enjoy it. That delicious tension between us, it’s got me thinking about what could happen if I push further."
        a_ "Emma is already complicated enough, but with Eleanor... I might actually have a chance to get what I want."
        a_ "The thought alone is enough to keep me on edge, and I’m not sure I can resist it much longer."
    else:
        a_ "Eleanor... she’s a distraction I didn’t see coming, but I resisted. Still, it’s clear that the road ahead won’t be easy."
        a_ "I can’t afford to lose focus, not with everything on the line. Emma’s already slipping away, and I can’t let my guard down, even for a second, if I want to stand a chance of getting her back."
    
    a_ "If Emma ever finds out about Eleanor, things will go from bad to worse."
    a_ "And thank God Emma didn’t notice when I stole a glance at Ruby’s cleavage during dinner last night."

    if alexflirtrubyday1:
        a_ "I thought complimenting Ruby on her body would get a different reaction, but she clearly wasn’t into it. Maybe I pushed too hard, too fast."
        a_ "Those breasts, though... damn, they’re hard to ignore. If I want to get closer, I’ll need to figure out how to play this differently."
        a_ "There’s got to be a way to soften her up, make her see I’m more than just some guy throwing cheap lines. I’ll figure it out. Those perfect breasts are worth the effort."
    else:
        a_ "Ruby’s reaction to my compliment was... unexpected. I wasn’t trying to flirt, just acknowledging her hard work, but the way she smiled—there was something more behind it."
        a_ "It felt good, though, seeing her light up like that. I can’t deny there’s a certain charm about her, but I need to be careful."
        a_ "I’m already walking on thin ice with Emma, and the last thing I need is to complicate things further."

    scene w_241 with dissolve
    a_ "Daniel was a complete idiot for treating Ruby like that. He’s an enemy, no doubt, but I’ll deal with him in time."
    a_ "Ava... After all these years, she still has that spark, that energy. Seeing her brought back memories I didn’t realize I’d missed so much. Maybe this place isn’t all bad."

    if alexaboutavaboyfriendavaday2:
        a_ "I asked Ava about her boyfriend, and she seemed a little off, almost like I’d touched a nerve. Did they fight?"
        a_ "Something must’ve happened between them. She’s usually so confident, but there was something in her eyes that wasn’t there before—maybe doubt, or regret."
        a_ "It’s strange seeing her like that. I can’t help but wonder if there’s more to the story. Maybe she’s not as happy as she pretends to be."
    else:
        a_ "I can't stop thinking about Ava. When I complimented her body, she didn’t just take it in stride—she practically basked in it, like she was waiting for me to notice."
        a_ "And hell, who wouldn’t? That toned, athletic figure, those curves, the way she moves with such confidence. She’s sexy as hell, and she knows it."
        a_ "That smile of hers, the way her eyes lit up when I said it... it was like she was inviting me to look even closer. And the way she was showing off... it felt like she was putting on a show just for me."
    
    a_ "..."
    a_ "Isabella... there's something about her that's impossible to ignore. She has this aura, a kind of distant beauty that's almost untouchable. But I know better—there’s more underneath that surface."

    if alexsflirtisabelladay2:
        a_ "Isabella… she really got under my skin today. I tried to be charming, to play the game, but she flipped the script on me like it was nothing."
        a_ "Every time I thought I had her, she just turned it around, made it all a joke. It’s infuriating, but I can’t help but admire her for it."
        a_ "And even though I was frustrated, part of me enjoyed the challenge. Maybe that’s what’s bothering me now—I wanted to win, but with her, it feels like the game never really ends."

        if alexsholdisabelladay2:
            a_ "Holding her in my arms felt so right, like it was exactly where she was meant to be."
            a_ "The way her body fit against mine, the surprise in her eyes that quickly softened into something else."
            a_ "I remember the warmth of her skin, the way her breath caught just for a moment before she relaxed, letting me support her."
            a_ "And then, after I set her down, the way we talked... it was easy, comfortable, even flirtatious."
            a_ "For a brief moment, it felt like we weren’t just playing some twisted game, but really connecting. That conversation... it’s sticking with me, more than I expected."
        else:
            a_"Why do I keep thinking about her? It’s not like I haven’t been rejected before, but this… this feels different. She didn’t just reject me; she toyed with me, made me question everything."
            a_ "Was she ever interested, or was it all just a game to her? And why do I care so much? Maybe it’s because, deep down, I know she’s out of my league in more ways than one."
            a_ "But still, there’s something about her… something that makes me want to keep playing, even if I know I’m destined to lose."
            a_ "Why didn’t I catch her? I saw her slipping, and I had the chance—I could’ve reached out, could’ve stopped her from hitting the ground. But I didn’t."
    elif alexspillswineday2 and not alexsflirtisabelladay2:
        a_ "She was there again, lounging by the pool, looking as effortlessly stunning as always. But I knew better than to get close this time."
        a_ "Isabella is the kind of trouble that looks inviting, the kind that pulls you in with a smile and leaves you tangled in a mess you never saw coming."
        a_ "No, it’s better to keep my distance. I’ve learned that the hard way. Let someone else get caught up in her games—I've got enough problems without adding her to the list."

    $ renpy.music.play("audio/sfx/phone_ring.ogg", channel="sfxloop1", relative_volume=0.3)
    a_ "..."
    $ renpy.music.stop("music1", fadeout=2.0)

    scene w_242 with dissolve
    "{i}The ringing of my phone interrupted my reverie.{/i}"
    scene w_243 with dissolve
    "{i}I instinctively turned to reach for it.{/i}"
    scene w_244 with dissolve
    a_ "..."
    scene w_245 with dissolve
    "{i}Just as my fingers brushed the cold surface, I felt a presence—a shadow moving with intent.{/i}"
    "{i}It happened in a blur, like a nightmare unfolding too fast for reality to catch up.{/i}"
    $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
    scene w_246
    with Dissolve(0.01)
    $ renpy.music.play("audio/sfx/sfx_knife_stab.mp3", channel="sfx1", relative_volume=0.5)
    scene red
    with Dissolve(0.01)
    scene w_246
    with Dissolve(0.01)
    with vpunch
    $ renpy.music.play("audio/musics/battle-music1.mp3", "music2", fadein=2.0, relative_volume=0.2)
    "{i}The glint of a blade caught the corner of my eye, and I pivoted on instinct, raising my arm just in time to block the strike.{/i}"
    "{i}Pain seared through my forearm as the knife grazed my skin.{/i}"
    scene w_247
    with Dissolve(0.01)
    $ renpy.music.play("audio/sfx/sfx_punch1.ogg", channel="sfx1", relative_volume=0.5)
    scene white
    with Dissolve(0.01)
    scene w_247
    with Dissolve(0.01)
    with hpunch
    "{i}My other hand shot out in retaliation, landing a solid punch to my assailant’s side.{/i}"
    "{i}The impact was enough to stagger him, and he recoiled.{/i}"
    scene w_248 with dissolve
    a_ "Shit..."
    scene w_249 with dissolve
    "{i}But even as I steadied myself, ready for another confrontation,{/i}"
    scene w_250 with dissolve
    "{i}he turned and bolted into the darkness. I stood there, breathing heavily, my eyes scanning the shadows as he disappeared into the night.{/i}"
    $ renpy.music.play("audio/sfx/sfx_steps1.wav", channel="sfx1", relative_volume=0.2)
    $ renpy.music.stop(channel="music2", fadeout=2.0)
    $ renpy.pause()
    scene black with dissolve
    a_ "Who the hell was that? And why would they attack me here, now?"
    a_ "This is getting out of hand... I need to figure out who’s behind this before it’s too late."
    "{i}I clutched my injured arm, feeling the sting of the cut with every pulse of my heartbeat.{/i}"
    a_ "I'm worried about Emma right now. Better check on her."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_300 with fade
    "{i}As I entered the room, I noticed Emma standing by the balcony door, her back to me as she closed it gently.{/i}"
    scene w_301 with dissolve
    "{i}She was dressed for the night in nothing but a pair of panties and a top, her figure silhouetted against the soft glow from outside.{/i}"
    "{i}She began walking towards the bed, her movements slow and graceful, unaware of my presence at first.{/i}"
    scene w_302 with dissolve
    "{i}But then, she noticed me.{/i}"
    "{i}Her eyes widened as she saw the blood on my arm{/i}"
    scene w_303 with dissolve
    "{i}Instantly, her hands flew to her mouth in shock, and I could see the panic in her eyes.{/i}"
    "{i}Without a second thought, she rushed towards me, her earlier calm shattered by the sight of my injury.{/i}"
    a_ "Emma is going to freak out, I can see it in her face. I hate seeing her like this, but there’s no hiding it now."
    "{i}I could see the concern etched across Emma's face as she moved toward me.{/i}"
    $ renpy.music.play("audio/musics/filaments1.mp3", "music1", fadein=2.0, relative_volume=0.2)
    scene w_304 with dissolve
    "{i}The moment she caught sight of my arm, the color drained from her cheeks, her eyes widening in alarm. My mind was still reeling from what had just transpired outside; the attack, the rush of adrenaline, and now, the aftermath{/i}"
    e "Alex, what happened? Oh my God, you’re hurt!"
    "{i}Her voice was trembling, a mixture of fear and concern, as she reached out to touch my arm.{/i}"
    "{i}The warmth of her fingers against my skin was both comforting and worrying; I could feel her anxiety seeping into me.{/i}"
    a_ "I have to keep her calm, but how? She’s already on the verge of tears."
    scene w_306 with dissolve
    e "Alex... What... what happened? Who did this to you?"
    a_ "Alex, you idiot. You should’ve been more careful."
    "{i}I took a deep breath, trying to steady my voice as she reached out, her hands trembling slightly as they hovered over my wound.{/i}"
    "{i}I could tell she wanted to help, but the shock of seeing me like this had momentarily paralyzed her.{/i}"
    "{i}I knew I had to explain what had happened, to reassure her that I was okay, despite the blood seeping from the gash on my arm.{/i}"
    scene w_305 with dissolve
    "{i}I held up a hand, trying to calm her down. Her concern was clear, but I needed her to focus.{/i}"
    a "Emma, it's okay, I promise."
    a "It was someone outside, they came out of nowhere. I managed to fight them off, but... they got me here."
    "{i}I pointed to the wound on my arm. She looked from my face to my arm, her eyes filling with a mixture of fear and determination.{/i}"
    scene w_307 with dissolve
    e "I’ll get the first aid kit. We need to clean this up right now."
    "{i}She turned quickly, heading toward the bathroom to fetch the kit.{/i}"
    e "Let’s take care of this, Alex. I won’t let anything worse happen to you."
    scene black with dissolve
    "{i}I could hear her rummaging around, trying to find what she needed.{/i}"
    "{i}My thoughts drifted back to the attacker, the cold glint of the knife as it sliced through the air. I clenched my fist, trying to push the memory away.{/i}"
    a_ "{i}Alex, you’ve got to figure out who’s behind this. You can't let this happen again.{/i}"
    "{i}Emma returned with the kit, her movements hurried but precise. She knelt beside me, her fingers already opening the antiseptic.{/i}"
    scene w_309 with dissolve
    e "Alex, what exactly happened out there? Was it a burglar? Are we in danger?"
    "{i}I could see how tense she was, every muscle in her body coiled with worry.{/i}"
    "{i}I wanted to reassure her, but the truth was, I wasn’t entirely sure what was going on myself. Still, I couldn’t let her know that.{/i}"
    scene w_308 with dissolve
    "{i}I tried to keep my tone calm as I explained.{/i}"
    a "I don’t think it was a burglar."
    a "Whoever it was, they were too focused on me. It felt more… targeted. But don’t worry, I’m going to find them. They can’t be far."
    scene w_309 with dissolve
    "{i}Emma’s eyes widened with fear as I spoke. I could see her mind racing, imagining all the worst-case scenarios.{/i}"
    e "Alex, no! We need to call the police. What if they’re still here? You could get seriously hurt!"
    a_ "Alex, she’s scared. You can’t let her worry like this, but you also can’t leave this unfinished."
    scene w_308 with dissolve
    "{i}I shook my head, trying to keep my voice steady and confident.{/i}"
    a "I know you’re worried, Emma, but I can handle this. I don’t want to involve the police unless we absolutely have to."
    a "Just stay here, lock the door, and I’ll be back soon."
    scene w_310 with dissolve
    "{i}She opened her mouth to protest, but I could see the resolve in her eyes weakening.{/i}"
    "{i}She didn’t want to let me go, but she also knew how stubborn I could be when I set my mind to something.{/i}"
    e "Alex… please be careful. I don’t like this"
    a "I will be. I’ll come back soon, I promise."
    scene black with dissolve
    "{i}With that, I turned and walked out of the room, leaving Emma standing there, her eyes following me until I closed the door behind me.{/i}"
    "{i}The weight of her worry hung heavy on my shoulders as I made my way down the hallway.{/i}"
    a_ "Whoever did this… they’re going to regret coming after me in my own home."
    $ renpy.music.stop(channel="music1", fadeout=2.0)

    $ freeroom_state = FREEROOM_STATE_ALEX_FR_1
    jump alex_emma_room

label day2_alex_2:
    scene w_324 with fade
    $ renpy.music.stop("ambient1", fadeout=2.0)
    "{i}The corridors of the mansion were eerily silent, only the soft padding of my footsteps echoed against the marble floors.{/i}"
    "{i}My mind raced with thoughts of the attacker, the cold blade that had narrowly missed its mark, and the face I never got to see.{/i}"
    "{i}I needed answers. Every shadow felt like a potential threat, every corner held the possibility of danger.{/i}"
    scene w_325 with dissolve
    a_ "Who the hell could want me dead? Is this about the business, or something more personal?"
    "{i}I mulled over the possibilities as I walked, gripping the knife I had found earlier, the same one that had been aimed at me.{/i}"
    "{i}The weight of it in my hand was both reassuring and unsettling.{/i}"
    scene w_335 with dissolve
    $ renpy.music.play("audio/sfx/sfx_shower_hallway.ogg", channel="sfxloop1", fadein=2.0, relative_volume=0.3)
    "{i}As I reached the first floor, the sound of running water caught my attention. It was faint at first, almost indistinguishable from the hum of the mansion’s air conditioning.{/i}"
    "{i}But as I drew closer, the sound grew louder and clearer. A shower was running somewhere nearby, and the door to one of the bathrooms was ajar.{/i}"
    "{i}Curiosity and caution battled within me. It wasn’t just the potential of discovering another threat; it was the oddness of the situation.{/i}"
    scene w_336 with dissolve
    a_ "Why would someone be showering at a time like this?"
    "{i}I hesitated for a moment, but then the need to know won out.{/i}"
    a_ "If someone’s in there, they might know something. Or it could be the attacker, trying to wash away evidence."
    "{i}With that thought driving me, I approached the door silently, careful not to make a sound.{/i}"
    scene black with dissolve
    "{i}The door was slightly open, just enough to allow a narrow view of the inside. I peered through the gap, and my breath caught in my throat.{/i}"
    scene w_328 with dissolve
    "{i}It was Ruby.{/i}"
    "{i}She was standing under the shower, her back to me, the water cascading down her body, glistening in the dim light.{/i}"
    a_ "What is she doing here? Did she have something to do with the attack?"
    "{i}The sight was exciting, but I forced myself to stay focused. This was no time to get distracted, not with so many unanswered questions hanging over my head.{/i}"

    $ alexspiesrubyshowerday2 = False

    menu:
        "{font=fonts/hatten.ttf} {size=50}I keep spying{/size}{/font}":
            $ alexspiesrubyshowerday2 = True

            call ruby_in_the_shower_day2
        "{font=fonts/hatten.ttf} {size=50}I go to the room{/size}{/font}":
            $ alexspiesrubyshowerday2 = False

            scene w_337 with dissolve
            $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
            a_ "She’s always been... well, mysterious, but not dangerous. At least, I didn’t think so."
            "{i}I backed away from the door slightly, still within earshot, the decision weighing heavily on my mind.{/i}"
            "{i}I walked down the corridor, the echo of my footsteps filling the otherwise quiet mansion.{/i}"
            "{i}My mind raced with the events of the night, trying to piece together who could have wanted me dead and why.{/i}"
            "{i}The knife I found earlier weighed heavy in my hand, a stark reminder of how close I came to losing everything.{/i}"
            a_ "The mansion's security is supposed to be top-notch, yet here I am, alive only by luck. This place should be a fortress, but someone managed to slip through undetected."

    $ renpy.music.stop("sfxloop1", fadeout=2.0)    
    scene w_338 with fade    
    "{i}As I returned to the bedroom, I found Emma sitting on the bed, her expression worried, and her shoulders tense.{/i}"
    "{i}The weight of the situation was clearly affecting her, and I felt a pang in my chest seeing her like that.{/i}"
    a_ "How can I reassure her when I'm not even sure about the safety of this mansion myself?"
    scene w_339 with dissolve
    "{i}I approached slowly, trying not to startle her further. I pulled out the knife I had found earlier and showed it to her.{/i}"
    "{i}Emma's gaze immediately fixed on the blade, and her face paled.{/i}"
    e "Alex... are you okay? What happened? Where did you find this?"
    scene w_340 with dissolve
    "{i}I sighed, trying to find the right words to not alarm her more than necessary.{/i}"
    a "I'm fine, Emma. I mean, physically, I'm fine. But I couldn't find whoever did this."
    a "I just found the knife, and I'm sure it was used to try... well, you know."
    scene w_343 with dissolve
    e "This is horrible... do you think the person is still here, in the mansion?"
    a "I'm not sure, but it's possible."
    a "What worries me is that this means the mansion's security might be compromised. We can't let our guard down, not for a second."
    scene w_342 with dissolve
    "{i}She frowned, clearly processing what I had said.{/i}"
    "{i}I could see the conflict in her eyes – the desire to believe we were safe versus the reality that we might not be.{/i}"
    scene w_341 with dissolve
    e "We need a plan. Something to keep us all safe. Maybe we should gather everyone in one place where we can watch each other."
    a "That's a good idea. But..."
    scene w_343 with dissolve
    "{i}I could see the fear taking hold of her, and I hated that I didn’t have better answers for her.{/i}"
    a "I don’t know. But we’re going to be okay. I’ll make sure of it. We’ll lock the door tonight and stay alert."
    scene w_342 with dissolve
    "{i}She hesitated, her lips pressing into a thin line. I could tell she wanted to argue, to insist that we should leave, but there was nowhere to go. Not yet.{/i}"
    scene w_343 with dissolve
    e "I hate this. This place... It’s supposed to be our home for a year, but now... I don’t know if I can do this."
    scene w_342 with dissolve
    "{i}Her voice cracked, and I could feel the weight of her words pressing down on both of us. I knew she was right. This situation was unbearable, and it was partly my fault.{/i}"
    a_ "If only I hadn’t been so careless... If only I had been a better husband, maybe things wouldn’t be like this."
    a "I know. I know it’s hard. But we’ll get through this, together. We’ll keep each other safe."
    scene w_340 with dissolve
    "{i}I reached out and took her hand, squeezing it gently. She looked at me, her eyes still filled with doubt, but she nodded.{/i}"
    scene w_341 with dissolve
    e "I… I don’t know if I can do this anymore. Living here, in this place, with everything that’s happened… it’s too much."
    scene w_342 with dissolve
    "{i}Her voice trembled, and I could see the fear etched on her face. It wasn’t just the mansion or the attacker that scared her—it was the idea that our situation could get worse.{/i}"
    a "Emma, I understand. But we have to stay strong. We’ll lock the door tonight, and I promise I’ll stay awake to keep watch."
    scene w_340 with dissolve
    "{i}She looked up at me, her eyes softening slightly, but I could still see the doubt lingering there.{/i}"
    "{i}I knew she wasn’t convinced, and honestly, neither was I. But I had to say something to keep her from falling apart.{/i}"
    scene w_343 with dissolve
    e "I don’t know how you do it, Alex. You seem so calm, but I know you’re just as scared as I am."
    e "I just… I feel like everything is slipping away. Being here was supposed to fix things, but now…"
    a_ "And now it feels like it’s breaking us even more."
    scene w_340 with dissolve
    "{i}I reached out and took her hand, squeezing it gently.{/i}"
    a "Can we just take it one day at a time? Tonight, let’s just focus on getting some rest. We’ll figure out the rest tomorrow."
    scene w_342 with dissolve
    "{i}She hesitated, her gaze falling to the floor as she processed my words.{/i}"
    "{i}I could tell she wanted to believe me, to trust that things could get better, but the weight of everything was crushing her. Finally, she nodded, albeit reluctantly.{/i}"
    scene w_340 with dissolve
    e "Okay, Alex. We’ll try. But… please, just don’t shut me out anymore. I can’t do this alone."
    a "I won’t. I promise. We’re in this together."
    scene black with dissolve
    a_ "For both our sakes."
    "{i}That night, despite the lingering tension, Emma and I managed to get some sleep.{/i}"
    "{i}The heaviness in the air was palpable, but exhaustion finally overtook us.{/i}"

    jump day3_alex_1
