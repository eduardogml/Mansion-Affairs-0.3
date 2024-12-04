screen emma_alex_photo():
    imagemap:
        ground "gui/emma_alex_photo_black.png"
        hover "gui/emma_alex_photo_hover.png"

        hotspot (520, 60, 460, 820) clicked [Play("audio", "audio/click_sound.mp3"), Return("alex")] hover_sound "audio/hover_sound.mp3"
        hotspot (981, 60, 410, 820) clicked [Play("audio", "audio/click_sound.mp3"), Return("emma")] hover_sound "audio/hover_sound.mp3"

label choice:
    window hide
    show black
    with Pause(1)

    show welcome with fade
    with Pause(6)
    hide welcome with dissolve
    show choice1 with dissolve
    with Pause(10)
    hide choice1 with dissolve
    show choice2 with dissolve
    with Pause(10)
    hide choice2 with dissolve
    show choice3 with dissolve
    with Pause(10)
    hide choice3 with dissolve

    show choice4 with dissolve
    with Pause(5)
    hide choice4 with dissolve
    
    call screen emma_alex_photo
    if _return == "emma":
        jump day1_emma_1
    else:
        jump day1_alex_1

label intro:

    # Play background music.
    $ renpy.music.play("audio/musics/aesthetic1.mp3", "music1", fadein=2.0, relative_volume=0.2)

    scene black with fade
    "{i}This is the beginning of a story where love and conflict meet in an unexpected setting. A couple whose lives are about to change drastically.{/i}"
    scene w_1 with fade
    "{i}This is Alex Mitchell, a retired professional boxer, known for his fierce and relentless fighting style. Standing at 1.79 meters with an imposing physique,{/i}"
    "{i}Alex dominated the ring with his 'Swarmer' style, constantly pressuring his opponents with a barrage of fast and devastating punches.{/i}"
    scene w_2 with dissolve
    "{i}His career was marked by impressive victories and a fame that extended beyond the sport. Strong, famous, and handsome, Alex was a respected name in the boxing world.{/i}"
    "{i}But behind his champion image, there was a man with personal flaws and challenges, aspects only those close to him truly knew.{/i}"
    scene w_3
    with Dissolve(0.01)
    $ renpy.music.play("audio/sfx/sfx_punch1.ogg", channel="sfx1", relative_volume=0.5)
    scene white
    with Dissolve(0.01)
    scene w_3
    with Dissolve(0.01)
    with hpunch
    "{i}In the ring, Alex Mitchell was a true predator. His style made him an aggressive and relentless fighter, constantly pressuring his opponents and giving them no chance to breathe.{/i}"
    "{i}One of his most feared techniques was the left hook, a punch that often ended fights spectacularly.{/i}"
    "{i}The audience loved watching him in action, cheering with every move and rooting for his next victory.{/i}"
    "{i}He loved the adrenaline of being in the ring, the feeling of dominating his opponents, and the roar of the crowd chanting his name.{/i}"
    scene w_4
    with Dissolve(0.01)
    $ renpy.music.play("audio/sfx/sfx_punch1.ogg", channel="sfx1", relative_volume=0.5)
    scene white
    with Dissolve(0.01)
    scene w_4
    with Dissolve(0.01)
    with hpunch
    "{i}For Alex, boxing was more than a profession – it was his passion, his life. Fame brought Alex Mitchell a new level of recognition and adoration.{/i}"
    "{i}Wherever he went, he was the target of admiring glances and whispers, especially from women captivated by his strength, looks, and charisma.{/i}"
    "{i}At public events, his presence was always the highlight, attracting a legion of fans eager for an autograph, a photo, or just a moment next to the champion.{/i}"
    scene w_5 with dissolve
    "{i}This constant attention fueled his self-confidence, making him feel invincible both in and out of the ring.{/i}"
    "{i}Alex loved the admiring looks and cheers he received at every public appearance. It was at one of these public events that something different happened.{/i}"
    "{i}During a glamorous charity party full of celebrities, Alex met a special girl who deeply moved him.{/i}"
    "{i}The night was just beginning, but that encounter promised to change many things in his life...{/i}"
    scene w_7 with fade
    "{i}Emma, a 24-year-old young woman, is truly enchanting. Her shoulder-length hair, always well-groomed, frames a beautiful and captivating face.{/i}"
    "{i}Standing at 1.72 meters tall with a beautiful and sexy body, Emma attracts attention wherever she goes. But it's not just her appearance that makes her special.{/i}"
    "{i}Emma is creative and passionate, always finding unique ways to express her feelings.{/i}"
    scene w_8 with dissolve
    "{i}Her empathy and ability to understand others make her a delightful companion and a trustworthy friend. Alex was smitten with Emma from the moment he first saw her.{/i}"
    "{i}The chemistry between them was immediate, and each meeting only strengthened the bond they began to build.{/i}"
    "{i}Romantic dinners, seaside walks, and long conversations under the stars became unforgettable moments for both.{/i}"
    "{i}Emma works as an abstract painter, a profession that allows her to channel her creativity and passion into projects she loves. Her talent and dedication to her work are admirable.{/i}"
    scene w_9 with dissolve
    "{i}Talented, Emma paint with a unique style. Her works are an explosion of colors and emotions, each brushstroke filled with feeling and meaning.{/i}"
    "{i}Emma uses paints in her own way, often mixing them directly on the canvas, creating textures and shapes that defy conventional logic.{/i}"
    "{i}Her art is a pure expression of her creative and passionate soul. While Alex is known for his strength and dominant presence, Emma is an intriguing contrast.{/i}"
    "{i}For Emma, painting is a way to connect with her innermost emotions.{/i}"
    scene w_10 with dissolve
    "{i}Despite all her creativity and passion, Emma carries a childhood trauma that still affects her deeply.{/i}"
    "{i}This trauma, tucked away in a dark corner of her mind, often manifests in subtle but impactful ways.{/i}"
    "{i}Moments of deep introspection and occasional melancholy are reflections of the emotional scars she tries to hide from the world.{/i}"
    "{i}This trauma has shaped her sensitivity and the way she views and interacts with the world around her. Many of her abstract paintings are attempts to process and express these emotions.{/i}"
    scene w_11 with dissolve
    $ renpy.pause()
    scene w_13 with pixellate
    $ renpy.pause()
    "{i}Emma, 8 years old, watches her mother on the other side of the table, who is busy with something. The afternoon sun streams through the windows, bathing the room in a soft, warm light...{/i}"
    scene w_14 with dissolve
    "{i}Emma's mother, noticing her daughter's gaze, looks up and smiles lovingly at her...{/i}"
    scene w_15 with dissolve
    "{i}With a gentle gesture, she extends her hand to Emma, inviting her to come closer...{/i}"
    scene w_16 with dissolve
    "{i}The moment is interrupted by the sound of the doorbell...{/i}"
    scene w_17 with dissolve
    "{i}Emma's mother walks around the table, her footsteps lightly echoing on the floor...{/i}"
    scene w_18 with dissolve
    "{i}Emma watches as she walks to the door. There is a tense silence as Emma's mother opens the door...{/i}"
    scene w_19 with dissolve
    "{i}Emma sees her mother's expression change abruptly from calm to fear. From where she is, Emma cannot see what is on the other side of the door...{/i}"
    scene w_20 with dissolve
    $ renpy.pause()
    scene black with fade
    "{i}The scene ends abruptly, leaving an echo of fear and confusion in Emma's mind...{/i}"
    scene w_12 with pixellate
    $ renpy.music.play("audio/sfx/pistolet_s.mp3", channel="sfx1", relative_volume=0.2)
    $ renpy.pause()
    scene w_21 with dissolve
    "{i}The painful memory fades, but within her mind, the trauma is ever-present...{/i}"
    "{i}Emma does not remember the face of the hooded man who killed her mother.{/i}"
    "{i}This gap in her memory has deeply scarred her, leaving emotional wounds that have shaped her adult life.{/i}"
    "{i}The lack of closure led Emma to develop a unique coping mechanism: an imaginary, invisible companion with whom she talks when she is alone.{/i}"
    scene w_22 with dissolve
    $ renpy.pause()
    scene black with fade
    "{i}Alex, with his protective nature, became an essential figure in Emma's life. To Emma, Alex was not just a husband; {/i}"
    "{i}he was the safe haven where she could shelter from the internal storms.{/i}"
    scene w_23 with fade
    "{i}The passion between Alex and Emma grew quickly and overwhelmingly, fueled by intense chemistry and undeniable physical attraction.{/i}"
    "{i}Every touch, every shared glance revealed new layers of desire and understanding, strengthening the bond that was forming between them.{/i}"
    scene w_24 with dissolve
    "{i}Alex's protective and caring presence awakened a feeling of safety and deep desire in Emma. Conversely, Emma's sensuality and creativity brought a new perspective to Alex's life.{/i}"
    "{i}As the days passed, their passion intensified, making it impossible to imagine life apart. Their encounters were filled with ardent moments and intense exchanges of affection.{/i}"
    scene w_25 with dissolve
    "{i}Alex and Emma were sitting together on the sofa in their living room. Alex had his arms wrapped around Emma from behind in a protective and loving embrace.{/i}"
    "{i}Emma held a glass of wine, taking occasional sips. They both looked happy, their faces relaxed and content as they talked and watched the TV.{/i}"
    e "This reminds me of our honeymoon. Remember that little beach we found?"
    a "Of course, I do. That was one of the best weeks of my life. Just you, me, and the ocean."
    scene w_26 with dissolve
    "{i}Emma smiled, taking another sip of her wine. She leaned back into Alex, feeling the warmth and safety of his embrace.{/i}"
    e "I wish we could go back there sometime. It was so peaceful."
    a "We will. I promise. Maybe we can plan a trip soon."
    "{i}They both fell silent for a moment, lost in the memories of their honeymoon. The sound of the waves on the TV added to the sense of nostalgia{/i}"
    e "I love you, Alex."
    a "I love you too, Emma. More than anything."
    scene w_27 with fade
    "{i}Emma was in the living room, working on a new painting of Alex. He stood in front of her, striking an exaggerated pose with a playful smirk on his face.{/i}"
    scene w_28 with dissolve
    "{i}Emma had been sipping wine throughout the evening and was feeling more cheerful than usual, though not quite drunk.{/i}"
    scene w_29 with dissolve
    a "How much longer do I have to stay in this pose, babe? My muscles are starting to cramp."
    e "You can't move, Alex! If you move, I'll lose the perfect angle."
    "{i}She said it with a mock sternness, but the wine in her system made it difficult for her to maintain a serious tone. She giggled softly as she added another stroke to the canvas.{/i}"
    a "Alright, alright. Just remember, I’m doing this for you."
    e "And I appreciate it. This is going to be my masterpiece. The world has never seen such... dynamic posing."
    scene w_30 with dissolve
    "{i}They both laughed, the atmosphere light and playful. Emma stepped closer to Alex, and looked up at him with a teasing glint in her eye.{/i}"
    e "You know, you're not making this easy for me."
    a "I'm trying my best! Just tell me what you need."
    e "I need you to stay perfectly still. Like a statue. A very handsome, very naked statue."
    scene w_31 with dissolve
    a "Alright, alright. Statue mode, activated."
    e "You're doing great. Just a little longer, okay?"
    a "Anything for you, my talented artist."
    scene w_32 with dissolve
    $ renpy.music.play("audio/sfx/sfx_kissing_lip_to_lip.opus", channel="sfxloop1", fadein=2.0, relative_volume=0.1)
    "{i}Alex interrupted her with a sudden, passionate kiss. She was momentarily taken aback, but quickly melted into the embrace.{/i}"
    "{i}His hands gripped her waist firmly, pulling her closer, and she could feel the heat of his body against hers.{/i}"
    "{i}Emma's thoughts began to race. She loved the way Alex took control in moments like these. The firmness of his grip, the intensity of his kiss{/i}"
    "{i}She felt a surge of desire, her body responding to his touch in ways she couldn't ignore. As their lips moved together, the world around them faded away.{/i}"
    "{i}Emma's hands slid up Alex's chest, feeling the defined muscles beneath his skin, and she couldn't help but let out a soft moan of pleasure.{/i}"
    $ renpy.music.stop(channel="sfxloop1", fadeout=2.0)
    scene w_33 with dissolve
    e "You always know how to make me forget everything."
    a "That's the idea. I want you to know how much I want you, how much I love you."
    "{i}Emma’s breath was still uneven from their kiss, and her eyes were filled with a mix of desire and hesitation. She glanced at the unfinished painting and then back at Alex.{/i}"
    e "What are we going to do now? I haven’t finished the painting yet, but..."
    a "'We can finish the painting later,' he whispered, his voice low and filled with promise. 'Right now, I have other ideas.'"
    scene w_34 with dissolve
    "{i}He slowly turned her around, pressing her back against his chest, his hands sliding up her arms and then down her sides,{/i}"
    "{i}sending shivers through her body. Emma let out a soft sigh, already feeling herself giving in to the sensations.{/i}"
    e "But Alex, the painting..."
    a "'Can wait,' he murmured against her ear, his lips brushing her earlobe. 'I can't.'"
    scene w_35 with dissolve
    $ renpy.music.play("audio/sfx/sfx_clothes1.ogg", channel="sfx1", relative_volume=0.3)
    $ renpy.pause()
    "{i}His hands roamed her body with a mixture of tenderness and desire, taking off her shirt, finding all the places that made her gasp and lean on him.{/i}"
    "{i}One hand traced the curve of her hip toward her pussy, while the other slid up to Emma's breasts, his fingers dancing over her skin in a way that left her breathless.{/i}"
    a "You're so beautiful, Emma. I love how you respond to my touch, how your body responds to me."
    e "Alex..."
    a "Shh, "
    "{i}He soothed, his hands becoming more intimate, which made her knees weak.{/i}"
    scene w_36 with dissolve
    a "Just let go. Let me take care of you."
    "{i}Emma wrapped her arms around his neck, her body melting into her embrace.{/i}"
    "{i}She could feel the strength in his arms, the steady rhythm of his heart against her own racing pulse.{/i}"
    e "Alex... {i}(She whispered his name, her voice filled with a mixture of expectation and desire){/i}"
    a "I'm with you. Let's go somewhere more comfortable."
    scene w_37 with dissolve
    "{i}Emma wrapped her arms around his neck, her body melting into her embrace.{/i}"
    "{i}She could feel the strength in his arms, the steady rhythm of his heart against her own racing pulse.{/i}"
    "{i}As he began to carry her toward the stairs, she felt a shiver of excitement run through her.{/i}"
    e "You always know how to make me feel special, {i}(she whispered, nuzzling his neck){/i}"
    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/filaments1.mp3", "music2", fadein=2.0, relative_volume=0.2)

    "{i}Despite the deep love and passion that Alex and Emma shared, there was a darker side to Alex's nature that he struggled to control.{/i}"
    "{i}Even with the profound connection they had, Alex occasionally succumbed to his habit of infidelity.{/i}"
    scene w_38 with fade
    "{i}During his years of fame as a boxer, he was constantly surrounded by many women, all eager to be with him.{/i}"
    "{i}This incessant attention fueled his cheating habit, a temptation he could not resist.{/i}"
    scene w_39 with dissolve
    "{i}The desire to be desired by other women was a weakness he often gave in to. He knew this could destroy everything he and Emma had built together.{/i}"
    scene w_40 with dissolve
    "{i}Throughout their marriage, Alex never truly got out of the habit of cheating.{/i}"
    scene w_41 with dissolve
    $ renpy.music.play(["audio/adult/blowjob1_1.opus" , "audio/adult/blowjob1_2.opus" , "audio/adult/blowjob1_3.opus"], channel="sfxloop1", fadein=2.0, relative_volume=0.05)
    $ renpy.music.play(["audio/adult/blowjob1fl_1.opus" , "audio/adult/blowjob1fl_2.opus" , "audio/adult/blowjob1fl_3.opus"], channel="sfxloop2", fadein=2.0, relative_volume=0.3)
    "{i}When he was famous, before he retired, he always loved women, and women always loved him.{/i}"
    "{i}The thrill of the chase and the validation he received from these encounters were addictive, and he found it difficult to let go of those fleeting moments of excitement.{/i}"
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    $ renpy.music.stop("sfxloop2", fadeout=2.0)
    scene black with fade
    "{i}Over the years, Alex's infidelities became a recurring problem in the marriage.{/i}"
    "{i}Despite his promises to change and his genuine love for Emma, ​​he continued to seek validation outside of the relationship.{/i}"
    scene w_42 with fade
    $ renpy.music.play("audio/environment/env_beach.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    "{i}Emma often found herself alone, left to fend for herself while Alex indulged in her infidelities.{/i}"
    "{i}The days were long and lonely, the loneliness was a constant proof of her husband's absence.{/i}"
    scene w_43 with dissolve
    "{i}Emma's body was a sight to behold. Her curves were perfectly sculpted, her skin smooth and inviting.{/i}"
    scene w_44 with dissolve
    "{i}The way she moved, with a subtle but undeniable sensuality, caught the attention of anyone around her.{/i}"
    "{i}She exuded a natural sex appeal that was impossible to ignore.{/i}"
    scene w_45 with dissolve
    "{i}Men noticed Emma wherever she went. They were drawn to her like moths to a flame, captivated by her stunning appearance and irresistible charm.{/i}"
    scene w_46 with dissolve
    "{i}Emma was often harassed by men who saw her more as an object of their fantasies than as a person.{/i}"
    "{i}Her advances were often intrusive and unwelcome, increasing his frustration and feelings of isolation.{/i}"
    scene w_47 with dissolve
    "{i}She knew Alex's absence was to blame, and his neglect left her vulnerable to unwanted attention. This realization only deepened the rift in the marriage, {/i}"
    "{i}as Emma grew increasingly resentful of the man who was supposed to be there to protect and cherish her.{/i}"

    $ renpy.music.stop(channel="ambient1", fadeout=2.0)

    scene black with fade
    "{i}As time passed, the relationship between Alex and Emma only deteriorated further.{/i}"
    "{i}The initial passion and love that had once bound them together began to fade, replaced by a growing sense of resentment and disappointment.{/i}"
    scene w_48 with fade
    e "I can't believe you did this to me again, Alex! After everything we've been through, after all your promises!"
    a "Emma, you're overreacting. I told you, nothing happened. You're imagining things."
    e "Imagining things? Do you think I'm stupid? I saw the messages, Alex. How do you explain that?"
    a "Those messages were innocent! She’s just a friend, nothing more."
    scene w_49 with dissolve
    e "A friend? You expect me to believe that? The way you were talking to her was anything but innocent."
    a "You're twisting everything! You're looking for reasons to blame me because you can't let go of the past."
    e "The past? Alex, this isn't just about the past. This is happening now! You can't keep lying to me and expect me to believe you."
    a "I'm not lying! You're always so quick to accuse me without giving me a chance to explain."
    scene w_50 with dissolve
    e "Explain? You never have a real explanation! It's always excuses and lies. How can I trust you when you keep doing this?"
    e "You just don’t get it, do you? I can't keep living like this, Alex. The lies, the betrayals... it's too much."
    a "And you think it's easy for me? You're always accusing, always doubting. How am I supposed to prove anything to you?"
    e "Prove? You’ve had plenty of chances to prove yourself, and every time you just mess it up again."
    scene w_51 with dissolve
    e "I don’t know what you want anymore. Maybe it's better if we just admit this isn’t working."
    a "What are you saying?"
    e "I'm saying we should get divorced, Alex. This constant fighting, the distrust... it's destroying both of us."
    a "Divorce? You think that's the solution?"
    e "I think it’s the only option left. We can't keep pretending this is going to get better."
    "{i}There was a heavy silence as the weight of her words settled over them.{/i}"
    scene w_52 with dissolve
    "{i}Alex ran a hand through his hair, frustration etched on his face. His eyes drifted to the table and noticed a letter he hadn't seen before.{/i}"
    a "What's this?{i}(he asked, pointing to the letter.){/i}"
    e "{i}(still fuming, replied curtly.){/i} I don't know, Alex. It arrived for you. Why don't you open it and find out?"
    a "Let's see what this is about,"
    "{i}Emma watched him, her irritation evident, but she remained silent as he began to read.{/i}"
    a "It's from my aunt's lawyer, the one who died last year. He says she left me a mansion as an inheritance."
    e "A mansion? That's... unexpected."
    scene w_53 with dissolve
    a "There's a catch. To fully inherit the mansion, we have to live in it together for a year. As a married couple."
    "{i}Emma’s eyes widened in disbelief, and she let out a bitter laugh.{/i}"
    e "You’ve got to be kidding me. We can barely stand each other for a day, let alone a year."
    a "I know. It sounds crazy, but think about it. If we can do this, we can sell the mansion and split the profit. It could be a fresh start for both of us."
    "{i}Emma hesitated, the idea of spending another year with Alex seemed unbearable, but the thought of the money and a new beginning was tempting.{/i}"
    e "Do you really think we can pull it off without killing each other?"
    a "We'd have to try. It's a lot of money, Emma. Enough to help both of us start over."
    "{i}They stared at each other, the anger and frustration still simmering beneath the surface, but now mixed with a reluctant hope.{/i}"
    "{i}The prospect of financial freedom and a clean slate was too enticing to ignore.{/i}"
    e "Fine. We'll do it. But once the year is up, we go our separate ways and sell the place. Agreed?"
    a "Agreed."
    "{i}The tension between them remained, but for the first time in a long while, there was a glimmer of mutual understanding.{/i}"
    "{i}They both knew it wouldn't be easy, but the promise of the mansion and what it could mean for their futures gave them a shared goal, however temporary.{/i}"
    scene black with fade
    "{i}After reading the letter, Alex and Emma made a difficult decision. They decided to move into the mansion that Alex had inherited from his late aunt.{/i}"
    "{i}The idea of living together for another year seemed unbearable, given the constant fights and resentments that had accumulated over the years.{/i}"
    "{i}However, the promise of a substantial inheritance was an opportunity they couldn't ignore.{/i}"
    
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/aesthetic1.mp3", "music1", fadein=2.0, relative_volume=0.2)

    scene w_54 with fade
    $ renpy.music.play("audio/environment/env_birds.ogg", channel="ambient1", fadein=2.0, relative_volume=0.2)
    "{i}Alex saw the mansion as a chance for financial restart.{/i}"
    "{i}Selling the property could provide both of them with the economic freedom necessary to pursue new paths and rebuild their lives independently.{/i}"
    "{i}He was willing to endure the tension of living with Emma if it meant achieving future financial security.{/i}"
    scene w_55 with dissolve
    "{i}Emma also recognized the practical value of the proposal. Although their relationship was in shambles, she understood that the mansion represented a unique opportunity.{/i}"
    "{i}The money they could gain from selling the property would be enough to help her overcome the end of their marriage and start a new chapter in her life.{/i}"
    "{i}Thus, driven by both necessity and ambition, Alex and Emma decided to face the challenge of living together in the mansion for a year.{/i}"
    "{i}The decision was made not out of love or reconciliation, but from a pragmatic understanding that the temporary sacrifice could result in lasting benefits for both of them.{/i}"
    scene w_56 with dissolve
    "{i}Alex and Emma stood in the front garden of the mansion, facing each other. The grandeur of the mansion loomed behind them, its presence imposing and somewhat surreal.{/i}"
    a "It's impressive, isn't it? I never imagined we'd be living in a place like this."
    e "Yeah, it's something, all right. But I can't help but think about all the maintenance this place will need."
    a "Well, that's part of the deal, isn't it? We’ll have to take care of it."
    e "Easy for you to say. You don't have to worry about the little details like cleaning and upkeep."
    a "Are you implying I don't pull my weight around here?"
    scene w_57 with dissolve
    e "I’m just saying you tend to overlook the practical side of things. Like, have you even thought about how we're going to handle the garden?"
    a "I was going to hire someone to take care of it. It's not that big of a deal."
    e "There you go again, thinking money solves everything. We need to be careful with our expenses, Alex. We're supposed to be saving."
    a "I just think it's better to let professionals handle it rather than us trying to do everything ourselves."
    e "And I think you need to start considering the bigger picture. We're in this together, remember?"
    a "Fine. We'll figure it out together. But you need to stop assuming I don’t care about these things."
    e "And you need to stop acting like I’m always overreacting. We both have to make this work."
    scene w_58 with dissolve
    "{i}Their argument had just started to simmer down when they heard the creak of the garden gate. A man in shorts and a shirt walked in, calling out their names.{/i}"
    "{color=#3FFF4C}??????{/color}" "Alex? Emma? Excuse me, are you Alex and Emma?"
    "{i}They turned to see the man approaching. He was tall, with a friendly demeanor, and his presence seemed to defuse some of the tension between them.{/i}"
    scene w_59 with dissolve
    a "Yes, that's us. Can we help you?"
    s "Hi, I'm Samuel, and everybody calls me Sam. I'm the gardener for the mansion. I worked for your aunt."
    s "I just wanted to introduce myself and see if there's anything you need help with as you settle in."
    e "Oh, that's a relief. We were just discussing the garden and how overgrown it is. It's nice to meet you, Sam."
    s "Likewise. The garden does need a lot of work. Your aunt loved this place."
    a "We appreciate your help, Sam. We're not exactly experts when it comes to gardening."
    scene w_60 with dissolve
    s "No problem at all. I can take care of the maintenance and make sure everything is in order. If you have any specific requests or ideas for the garden, just let me know."
    e "That's great to hear. We were just worried about managing everything ourselves. It's a big place."
    s "Your aunt had a vision for this garden, and I'd like to help you continue that."
    a "Thank you, Sam. We'll definitely take you up on that. It's good to know we have someone experienced to rely on."
    s "Glad to be of service."
    scene w_61 with dissolve
    "{i}Alex, Emma, and Samuel stood in the front garden of the mansion. After exchanging a few more words, Samuel offered to show them around the property.{/i}"
    s "If you’d like, I can give you a tour of the mansion. It’s quite a place with an intriguing history."
    e "We’d appreciate that, Sam."
    a "Yeah, lead the way."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_62 with fade
    "{i}They followed Samuel to the grand entrance of the mansion. The building was impressive, its well-maintained exterior{/i}"
    s "This mansion was built in the early 1900s by your aunt’s grandfather. He was a prominent businessman, but there are rumors that his success wasn’t entirely legitimate."
    e "What do you mean?"
    s "There have always been whispers about secret dealings and hidden fortunes. Some say the mansion was a front for more clandestine activities."
    s "Despite its grandeur, the mansion has seen its share of dark times."
    s "Your aunt was dedicated to preserving it, but there were always stories of strange occurrences—objects moving on their own, unexplained sounds in the night."
    a "Are you saying this place is haunted?"
    scene w_63 with dissolve
    s "I don’t know about haunted, but it definitely has its mysteries. Your aunt always said the mansion had a life of its own, that it remembered the secrets of everyone who lived here."
    e "It sounds like there’s a lot more to this place than we thought."
    a "We’ll have to keep that in mind. Thanks for the heads-up."
    s "No problem. Let’s continue the tour."
    scene w_64 with dissolve
    s "So, where would you like to start? Upstairs to the bedrooms or downstairs to the gym?"
    a "What do you think, Emma? Where should we go first?"
    e "I'd like to see the kitchen and the living room first. We can check out the gym afterward."
    a "Alright, let's see the kitchen and living room first."
    scene w_65 with dissolve
    "{i}Samuel smiled and gestured for them to follow him.{/i}"
    s "Sounds good. This way, please."
    "{i}Alex, Emma, and Samuel walked through the grand hallway towards the kitchen.{/i}"
    scene w_66 with fade
    s "Here we are, the kitchen. It's been updated with all the modern conveniences while keeping the original charm."
    e "It's beautiful. I can see myself spending a lot of time here."
    a "Yeah, especially considering you love to cook."
    s "That's great to hear. Cooking together can be a wonderful way to bond. So, how did you two meet?"
    "{i}Emma glanced at Alex before responding.{/i}"
    e "We met at a charity event. Alex was the guest of honor, and I was volunteering."
    a "She couldn’t resist my charm,{i}(he added with a smirk.){/i}"
    e "Or maybe it was your persistence,{i}(she said, rolling her eyes playfully.){/i}"
    scene w_67 with dissolve
    "{i}Samuel chuckled, seemingly oblivious to the subtle tension.{/i}"
    s "Sounds like a great story. And what do you both do for work?"
    a "I'm a retired boxer, but I do some coaching on the side."
    e "I’m painter. I love working from home, which makes this kitchen even more appealing."
    s "A boxer and an artist, that’s an interesting combination. Must keep things exciting."
    e "Oh, it certainly does. Never a dull moment,{i}(she replied, her tone carrying a hint of irony.){/i}"
    a "Yeah, especially with Emma’s spontaneous creativity."
    e "And Alex’s... dedication to his routines, {i}(she added, giving him a pointed look.){/i}"
    scene w_68 with dissolve
    "{i}Samuel smiled, seemingly unaware of the underlying friction.{/i}"
    s "Well, this kitchen should be perfect for both of you. Plenty of space to cook and create."
    e "Absolutely. It’s really lovely. Thank you for showing."
    s "My pleasure. Now, would you like to see the living room next?"
    a "Sure, lead the way."
    "{i}As they moved on to the next room, Alex and Emma exchanged a glance.{/i}"
    "{i}Despite their attempts to appear united, their subtle barbs hinted at the unresolved issues simmering beneath the surface.{/i}"
    scene w_69 with fade
    "{i}Samuel led Alex and Emma into the living room, a grand space with elegant furniture and rich decorations.{/i}"
    "{i}He began to share more about the mansion's history as they walked.{/i}"
    s "This room has seen a lot over the years. Your grandfather, Alex, hosted many grand parties here."
    s "There are even rumors that during Prohibition, this mansion was a hub for secret gatherings."
    e "Interesting. It sounds like there was always something exciting happening here."
    a "Yes, it seems like this place was full of secrets,{i}(e said, glancing at Emma with a hint of accusation.){/i}"
    scene w_70 with dissolve
    s "And there are stories of the mansion being haunted, but I think they’re just old tales."
    s "People say they hear footsteps at night or see objects moving on their own."
    e "Oh, old ghost stories. Just what we need, {i}(she replied sarcastically){/i}"
    e "Something Alex can talk about endlessly."
    a "Well, Emma’s always been good at creating drama. Maybe she’ll enjoy the ghosts, {i}(he shot back, his tone biting){/i}"
    "{i}Samuel, sensing the tension but choosing to overlook it, continued his explanation.{/i}"
    s "Despite the stories, your aunt loved this place. She believed the mansion had a spirit of its own, but more in a protective sense."
    e "Protective? That’s a comforting thought. Unlike some people who just bring trouble, {i}(she said, not missing a beat){/i}"
    a "Yes, well, some people attract trouble wherever they go, {i}(he retorted){/i}"
    scene w_71 with dissolve
    s "{i}(Samuel hesitated, then asked,){/i} Are you two okay? {i}(It seems like there’s some tension){/i}"
    e "{i}(Emma forced a smile){/i} We're fine, Sam. Just a little playful banter between a loving couple."
    a "{i}(Alex nodded, trying to appear sincere){/i} Yeah, nothing to worry about. We’re just settling in."
    s "{i}(Samuel, still unsure but unwilling to press further, decided to wrap up the tour){/i} Alright then, I’ll let you explore the rest of the mansion on your own."
    s "I need to get back to the garden."
    "{i}He glanced at Emma, appreciating her beauty for a brief moment, but kept his thoughts to himself to avoid any discomfort.{/i}"
    s "If you need anything, just let me know."
    e "Thanks, Sam"
    a "Yes, thank you. We'll see you around."
    scene w_72 with dissolve
    "{i}Samuel left them alone in the living room, and Alex and Emma exchanged a tense look, knowing that their facade had barely held up.{/i}"
    scene w_73 with dissolve
    $ renpy.pause()
    scene w_74 with dissolve
    "{i}Alex and Emma were alone in the living room of the mansion. The tension between them was palpable as Emma began to voice her frustrations.{/i}"
    e "I can't believe how you behaved during the tour, Alex. You couldn't stop throwing digs at me, could you?"
    a "Oh, come on, Emma. You're acting like you were any better. You've been cold and aggressive, and if we keep this up, there's no way we'll convince anyone that we're still happily married."
    e "Cold and aggressive? Maybe if you didn't constantly pretend I’m still attracted to you, it wouldn't be so difficult."
    scene w_75 with dissolve
    a "Pretend? You know, sometimes it feels like you’re the one who’s pretending, Emma. Your attitude is what's making this harder than it needs to be."
    e "I'm not the one who decided to drag out every flaw for Sam to see. If we're going to do this, we need to at least try to act like we can stand each other."
    a "And you think your constant jabs help with that? We need to get through this year, and that means putting on a good show. So, how about we start working on that?"
    "{i}Emma sighed, the weight of their situation pressing down on her. She knew Alex had a point, but admitting it was another matter.{/i}"
    e "Fine. Let's go see the gym. Maybe some physical activity will help."
    a "Yeah, maybe it will."
    scene black with fade
    "{i}They walked towards the staircase leading to the gym, each lost in their own thoughts. The underlying tension remained, but for now, they had a shared goal to focus on.{/i}"
    scene w_76 with fade
    a "So, what do you think about everything Sam said about the mansion?"
    a "It feels like something out of a horror movie."
    e "I don't know, Alex. It could just be legend, but these stories usually have some truth to them."
    e "It's strange to think that you Aunt would leave us a house full of secrets."
    a "Yeah, and the part about the house being haunted? I’m not sure if I believe in ghosts."
    e "Maybe it’s just a way to keep people away."
    e "The real question is, why did she make it so we have to live here for a year and stay married to inherit it?"
    a "It's almost like she wanted to force us to work things out. But why? She knew we were having problems."
    e "Maybe she thought this place could help us find common ground."
    e "Or maybe it was just her way of making sure the mansion stayed in the family."
    a "Could be. But it’s not like living together is going to magically fix everything."
    a "Especially with the way things have been between us."
    e "You’re right. It's not going to be easy. Especially if we keep having moments like earlier with Sam."
    a "Yeah, about that... I know I wasn’t exactly polite, but you didn’t make it any easier either."
    e "I was just responding to your digs. You always have to have the last word, don't you?"
    a "Well, maybe if you weren't so quick to judge and criticize, I wouldn't feel the need to."
    e "And maybe if you weren’t constantly reminding me of why I shouldn’t trust you, we wouldn’t be in this situation."
    scene w_77 with dissolve
    "{i}The tension between them thickened as their voices rose. Alex turned to face Emma, his expression hardening.{/i}"
    a "This is exactly why living together is going to be a nightmare. We can't go five minutes without arguing."
    e "And you think I don’t know that? I’m just trying to get through this year so we can both move on."
    a "Maybe we should focus on why Aunt Helen set this up in the first place."
    a "There has to be a reason, something we're missing."
    e "I agree."
    e "But right now, I’m too tired to think about it. Can we just see the bedroom? I need to rest."
    a "{i}(Alex sighed, the frustration still evident on his face, but he nodded){/i} Fine. Let’s go."
    scene black with fade
    "{i}They walked out of the gym, the air between them still charged with unresolved issues.{/i}"
    scene w_78 with fade
    "{i}The mysteries of the mansion and the reasons behind their aunt’s conditions would have to wait for another day.{/i}"
    "{i}Alex and Emma were in the bedroom. The room was spacious and elegantly decorated. The floor was made of polished wood, and the large, luxurious bed was the centerpiece.{/i}"
    "{i}Near the window stood a plant with green leaves that resembled palm fronds. On the wall next to the door leading to the balcony hung a painting of a young woman sitting on the ground under a blue sky.{/i}"
    "{i}The door to the balcony was made of glass, allowing a clear view of the outside.{/i}"
    scene w_79 with dissolve
    "{i}Alex stood on the balcony, looking out.{/i}"
    "{i}His mind was filled with thoughts about the coming year. He wondered if this was what his aunt intended, for him and Emma to reconcile.{/i}"
    "{i}The idea of spending a whole year together in this house felt overwhelming, but maybe it was their last chance to make things right.{/i}"
    "{i}Emma sat on the bed, watching Alex. She couldn't help but think about what could have been.{/i}"
    "{i}If things had been different, maybe they could have lived here together happily for the rest of their lives.{/i}"
    "{i}But Alex had ruined everything, and there was no going back. The thoughts weighed heavily on her, and all she wanted now was to sleep.{/i}"
    scene black with fade
    "{i}The room's silence was thick with unspoken words and unresolved tension. The wooden floor creaked slightly as Emma shifted her position, the only sound breaking the stillness.{/i}"
    "{i}She looked at the painting, then back at Alex, feeling a mix of sadness and frustration. Finally, she lay down on the bed, her body exhausted and her mind yearning for rest.{/i}"
    
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.play("audio/musics/battle-music1.mp3", "music2", fadein=2.0, relative_volume=0.2)
    
    scene w_80 with pixellate
    $ renpy.music.play("audio/sfx/sfx_punch2.ogg", channel="sfx1", relative_volume=0.5)
    scene w_80
    with Dissolve(0.01)
    scene white
    with Dissolve(0.01)
    scene w_80
    with Dissolve(0.01)
    with hpunch
    "{i}Emma was engaged in a fierce battle with her archenemy.{/i}"
    "{i}With a swift and powerful kick, she sent him reeling, exhausted and vulnerable.{/i}"
    scene w_81 with dissolve
    e "You’ve lost, and you know it. This ends now."
    scene w_82 with dissolve
    arq "{i}(Her archenemy, catching his breath, sneered at her){/i} You always did have a flair for the dramatic, Emma. But this is far from over."
    scene w_83 with dissolve
    "{i}Determined, Emma lunged at him, her fist aimed at his face.{/i}"
    scene w_84
    with Dissolve(0.01)
    scene white
    with Dissolve(0.01)
    scene w_84
    with Dissolve(0.01)
    with vpunch
    "{i}In a swift motion, he caught her by the neck, his grip tightening as he pulled her close.{/i}"
    scene w_85 with dissolve
    arq "You think you can defeat me? I will destroy everything you hold dear."
    "{i}His eyes bored into hers, and for a moment, fear flickered through her.{/i}"
    scene w_86 with dissolve
    "{i}He threw her to the ground, and she landed with a thud, the air knocked out of her lungs.{/i}"
    scene w_87
    with Dissolve(0.01)
    $ renpy.music.play("audio/sfx/sfx_falling_body1.opus", channel="sfx1", relative_volume=0.5)
    scene white
    with Dissolve(0.01)
    scene w_87
    with Dissolve(0.01)
    with vpunch
    arq "You are weak, Emma. And you will fail."
    scene w_88 with dissolve
    "{i}As she struggled to rise, {/i}"
    scene w_89 with dissolve
    with Pause(3)
    "{i}... she suddenly realized she was no longer wearing any clothes. The inexplicable change left her feeling vulnerable, yet she knew she had to keep fighting.{/i}"
    scene black with fade
    "{i}Emma and Alex lay in bed, the morning light gently filling the room. Alex was sleeping peacefully, his breathing steady and calm.{/i}"

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/aesthetic1.mp3", "music1", fadein=2.0, relative_volume=0.2)

    scene w_90 with pixellate
    "{i}Emma, however, was far from tranquil. Her head moved restlessly from side to side, her face contorted in distress as she dreamt.{/i}"
    scene w_91 with dissolve
    "{i}In her dream, the ruins of the fantasy world were all around her.{/i}"
    "{i}The sounds of battle echoed in her mind—clashing swords, shouts, and the distant rumble of falling debris. She could hear her archenemy's voice, sinister and taunting.{/i}"
    "{i}**Archenemy** You will fail, Emma. Everything you love will be lost.{/i}"
    "{i}Emma’s heart raced, her breaths coming in short, panicked bursts. The sound of her own heartbeat pounded in her ears, {/i}"
    "{i}a relentless **thump-thump-thump**. She felt the cold grip of fear as her archenemy's hand tightened around her neck.{/i}"
    scene w_92 with dissolve
    "{i}**Archenemy** You are weak, and you will never defeat me.{/i}"
    "{i}The clash of their fight replayed in her mind—the swift kicks, the powerful punches, the overwhelming sense of vulnerability.{/i}"
    "{i}**Thud**—she felt herself being thrown to the ground again, the impact reverberating through her body.{/i}"
    "{i}She struggled to rise, to fight back, but the feeling of powerlessness was suffocating.{/i}"
    "{i}The sheets rustled as she tossed and turned, her head thrashing from side to side.{/i}"
    "{i}The noise of her restless sleep contrasted sharply with the serene quiet of Alex’s deep slumber.{/i}"
    scene w_93 with dissolve
    "{i}Finally, with a gasp, Emma's eyes flew open. The remnants of the dream clung to her mind, leaving her breathless and disoriented.{/i}"
    "{i}She lay there, staring at the ceiling, the morning light slowly bringing her back to reality, while the echoes of the dream faded into the background.{/i}"
    scene w_94 with dissolve
    "{i}Alex and Emma had just woken up. Emma was sitting on one side of the bed, while Alex stood on the other side, stretching. He noticed the tired look on her face and greeted her.{/i}"
    scene w_95 with dissolve
    a "Good morning, Emma. You look like you didn't sleep well."
    e "Good morning. It was nothing. Just a bad dream."
    a "Are you sure? You look pretty haggard."
    e "Yes, I do. I'm just a little tired, that's all."
    scene black with fade
    "{i}Alex and Emma went downstairs to have breakfast in the kitchen. Emma prepared the meal, but lacking their usual energy. The atmosphere between them remained heavy.{/i}"
    scene w_96 with fade
    "{i}Alex and Emma sat at opposite ends of the kitchen table, each lost in their own thoughts. As they sat in silence, the weight of their unresolved issues pressed down on them.{/i}"
    scene w_97 with dissolve
    "{i}Emma's expression was somber, weighed down by her restless night and the tension between them.{/i}"
    "{i}Their situation was already strained, but Emma's restless night and unsettling dream had left her more melancholic than usual.{/i}"
    scene w_98 with dissolve
    "{i}Alex, on the other hand, seemed more relaxed, though still aware of the underlying friction.{/i}"
    "{i}Knowing Emma well, recognized that she wasn’t in a good place and decided it was best to leave her alone for now.{/i}"
    "{i}For a moment, he wondered if they could really reconcile during their year in the mansion.{/i}"
    scene w_99 with dissolve
    a "Do you want some more coffee, Emma?"
    e "No, I'm fine. Thanks."
    "{i}The silence between them was thick, only interrupted by the clinking of their coffee cups. Alex's attention was suddenly drawn to the doorway as he heard footsteps approaching.{/i}"
    scene w_100 with fade
    "{i}Samuel entered the kitchen, leading a couple. His cheerful demeanor contrasted sharply with the strained atmosphere in the room.{/i}"
    s "Alex and Emma are already having breakfast."
    scene w_101 with dissolve
    "{i}As the couple stepped into the room, Alex's eyes widened in disbelief. He recognized the man instantly.{/i}"
    a_ "Oh, seriously! Daniel? What is he doing here?"
    scene w_102 with dissolve
    "{i}Isabella, accompanying Daniel, entered with an equally unfriendly expression.{/i}"
    "{i}Her eyes landed on Emma, and the air seemed to crackle with the tension between them. Emma forced a smile, masking her true feelings.{/i}"
    a_ "Of all the people in the world, it had to be him. This has to be a bad joke. How are we going to survive a year like this?"
    scene w_103 with dissolve
    "{i}Daniel's face twisted into a scowl as he recognized Alex. The two men stared at each other, their mutual dislike palpable.{/i}"
    d_ "Alex. Of course it had to be him. This is going to be hell. It's not enough that we have to stay in this mansion, we still have to share it with him."
    scene w_104 with fade
    "{i}Alex and Daniel stood in the kitchen, facing each other with forced smiles as they shook hands. The tension between them was palpable.  Emma and Isabella were nearby, also exchanging greetings{/i}"
    a "Daniel, what a... pleasant surprise."
    scene w_105 with dissolve
    d "Alex, good to see you too after all this time. Seems like my mother had interesting plans for all of us."
    a "Your mother always had a unique way of doing things."
    d "She believed living together here would help us create strong bonds. I think she hoped we would finally understand each other."
    a "Strong bonds? I'm not sure forcing us all to live together is going to work."
    d "Well, she also left us some parts of the mansion. But, of course, with a condition."
    a "Let me guess. You also have to live here for a year."
    d "Exactly. Looks like we're all in the same boat. A year to inherit the mansion. That was her wish."
    a "Interesting. I guess she had a lot of faith in our ability to get along."
    d "Or maybe she just enjoyed watching us struggle. She always had a peculiar sense of humor."
    scene w_106 with dissolve
    a_ "Alex squeezed Daniel's hand a bit tighter, his temper beginning to show."
    a "So, you think it's going to be easy?"
    d "Ease has never been my forte, Alex. But I'm ambitious. If it means putting up with you, I'll do whatever it takes."
    a "Sure, always ambitious. But don't forget, this mansion has a lot of history. It's not going to be that simple."
    d "And you, Alex? Planning any dirty tricks to get me out of the game?"
    a "Me? Dirty tricks are more your style, Daniel. I prefer to handle things head-on."
    d "Well, let's see how things unfold. Just hope you can keep your temper in check."
    "{i}Alex forced a smile, trying not to let his anger get the better of him.{/i}"
    a "We'll see, Daniel. We'll see."
    "{i}They released their grip, but the tension between them lingered in the air. Daniel's expression turned into a triumphant smile, while Alex struggled to control his explosive temper.{/i}"
    scene w_108 with dissolve
    "{i}Emma and Isabella stood facing each other as they exchanged greetings. Alex and Daniel were nearby. Isabella initiated the conversation with a polished smile.{/i}"
    isa "Hello, Emma. It’s a pleasure to finally meet you. I’m Isabella, Daniel’s wife."
    e "Hi, Isabella. The pleasure is mine. How was your trip here?"
    isa "Oh, it was long, but worth it to see this mansion. It’s truly magnificent, don’t you think?"
    e "Yes, it’s an amazing place. The architecture is fascinating."
    isa "Absolutely. It’s a perfect fit for those of us who appreciate the finer things in life."
    e "Indeed. It’s nice to be surrounded by such beauty."
    isa "You must find it inspiring, being an artist and all. I imagine a place like this could really spark your creativity."
    e "It does. There’s something about the history and the ambiance here."
    isa "I bet. Although, it must be challenging to focus on your art with... everything going on."
    scene w_107 with dissolve
    "{i}Emma’s smile faltered slightly, sensing the underlying tone in Isabella’s words).{/i}"
    e "It has its moments, but I manage."
    isa_ "Of course. Managing is key, especially when you’re not used to certain... luxuries."
    "{i}Emma forced a polite smile.{/i}"
    e "I think we all adapt in our own ways."
    isa "Very true. It’s important to stay adaptable, especially in a place like this with so much potential. I'm sure you’ll find your rhythm."
    e "I’m sure we will. It’s all about finding balance."
    "{i}Isabella nodded, her eyes briefly scanning Emma’s appearance before meeting her gaze again{/i}"
    isa "Balance is everything, isn’t it? Especially when you have so much to juggle."
    e "Yes, it is. But I believe we’re all capable of finding that balance."
    isa "I hope so. It would be a shame to let such a beautiful environment go to waste."
    "{i}Emma’s discomfort grew, but she maintained her composure{/i}"
    e "We’ll make the most of it."
    scene w_104 with dissolve
    "The four exchanged glances, each aware of the complexities that lay ahead. The arrival of Daniel and Isabella added another layer of tension to the already tense situation."
    scene black with fade
    "{i}Daniel and Isabella's arrival marked the beginning of a challenging year for Alex and Emma.{/i}"
    "{i}The two couples were bound by the same condition: living together in the mansion for a year to inherit their share.{/i}"
    "{i}With long-standing rivalries and deep-seated animosities, the mansion has become a battleground of unresolved conflicts and forced politeness.{/i}"

    jump choice
