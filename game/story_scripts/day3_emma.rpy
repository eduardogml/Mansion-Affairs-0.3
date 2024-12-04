label day3_emma_1:

    $ emma_fr1_ruby_tanya_talk = False
    $ emma_fr1_zara_talk = False
    $ emma_fr1_ava_isabella_talk = False
    $ emmaspysamuelrubyday3 = False

    scene black with fade

    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 5rd_day with fade
    $ renpy.pause()
    hide 5rd_day with dissolve

    scene black with fade
    "{i}When I woke up, Alex was already gone.{/i}"
    "{i}The sheets were cold on his side, and for a brief moment, I wondered where he had gone so early.{/i}"
    scene w_326 with fade
    "{i}Last night had been a nightmare, and the weight of it still sat heavy on my chest. There was no way I was going to sit around feeling sorry for myself.{/i}"
    "{i}I needed a distraction. Something to clear my head. That’s when it hit me—Tanya.{/i}"
    "{i}She always knew how to make me forget about my problems, even for a little while.{/i}"
    scene w_574 with fade
    "{i}Dance was exactly what I needed to shake off the tension. Plus, I had a feeling Tanya would know just the right moves to get my blood pumping and my mind off the chaos from last night.{/i}"
    "{i}I was already starting to feel the strain in my legs as Tanya kept pushing us through the routine. Her energy was infectious, but damn, I could use a break.{/i}"
    scene w_575 with dissolve
    t "Come on, Emma! A few more, let's finish strong!"
    "{i}I couldn't help but roll my eyes, but I kept going. Tanya had that effect—relentless, but in a way that made you want to keep up.{/i}"
    e_ "Who knew dancing could be this exhausting?"
    scene w_576 with dissolve
    "{i}Before I could complain, Ruby walked in, her face calm but with a glint of curiosity in her eyes.{/i}"
    "{i}She watched us for a second before announcing with a grin.{/i}"
    scene w_578 with dissolve
    r "Hey, ladies, if you're feeling worn out, there's a massage therapist in the jacuzzi room."
    r "You could both use a little relaxation after this workout."
    scene w_577 with dissolve
    e_ "Now, that got my attention.. A massage? Oh, hell yes."
    scene w_579 with dissolve
    "{i}I turned to Tanya with a raised eyebrow.{/i}"
    e "What do you think, Tanya? I think we've earned it, don't you?"
    "{i}Tanya laughed and nodded, wiping the sweat from her brow.{/i}"
    scene w_580 with dissolve
    t "Hell yes, I'm down. Let's hit the jacuzzi."
    scene w_579 with dissolve
    "{i}I couldn’t help but smile.{/i}"
    e_ "Perfect timing, Ruby. I was two minutes away from collapsing."
    scene w_577 with dissolve
    "{i}Then, I remembered how Daniel had been so rude to Ruby the other day. Something about it had stuck with me.{/i}"
    e_ "Ugh, he was such a jerk to her..."
    e_ "Maybe I should invite her, give her a little break from his nonsense."
    "{i}I turned toward Ruby, trying to sound casual.{/i}"
    e "Why don't you join us, Ruby? You look like you could use a break, too."
    "{i}Ruby hesitated, a bit of uncertainty in her eyes. I could tell she wasn’t used to being invited along for things like this.{/i}"
    scene w_578 with dissolve
    r "Oh, I don't know... I should probably—"
    scene w_581 with dissolve
    "{i}Tanya cut her off with a grin.{/i}"
    t "Come on, Ruby! You deserve it just as much as we do."
    t "Don't let Emma hog all the fun."
    scene w_577 with dissolve
    "{i}I watched Ruby's face soften, the tension in her shoulders relaxing.{/i}"
    e_ "Gotcha. Sometimes, you just need a little push."
    e "Exactly! We’re all about self-care today. Let's go get pampered together."
    scene w_582 with dissolve
    r "Alright, alright."
    r "I guess I could use a little relaxation."
    e_ "Maybe this is exactly what we all need."
    scene w_326 with dissolve
    "{i}With that settled, we grabbed our things and headed toward the jacuzzi room.{/i}"
    "{i}I could feel the tension of the past day slipping away already.{/i}"

    jump girls_in_the_jacuzzi_day3

label day3_emma_2:
    scene w_327 with fade
    "{i}The night had fallen, and the air around the pool was cool, the kind that settles in when the heat of the day finally lets go of its grip.{/i}"
    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    scene w_633 with dissolve
    "{i}I stood there, gazing at the still water, lost in thought. The lights around the pool reflected off the surface, shimmering like tiny, trapped stars.{/i}"
    "{i}There was something peaceful about the way everything seemed to pause, as if the world was holding its breath, waiting for something.{/i}"
    scene w_634 with dissolve
    e_ "What am I even doing here?"
    e_ "Why am I always drawn to these moments, standing alone in the dark, thinking too much about things that are out of my control?"
    e_ "Maybe because it's quiet... Maybe because no one's around to mess with me."
    $ renpy.music.stop("ambient1", fadeout=2.0)
    scene w_635 with fade
    "{i}I decided to leave the pool area, feeling a bit restless, as if the quiet wasn’t enough to settle the storm inside me.{/i}"
    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    scene w_636 with fade
    "{i}The further I walked, the more distant everything felt—the people, the noise, even the lights.{/i}"
    "{i}The sky was inky black above, and I could feel the night wrapping around me like a soft, cool blanket.{/i}"
    scene w_637 with dissolve
    e_ "Alone. It's funny how I seek it out. But deep down, I hate it. I mean, who really likes being alone with their thoughts?"
    e_ "Especially when those thoughts aren’t exactly friendly."
    scene w_638 with fade
    "{i}I kept walking, letting the quiet embrace me, though my thoughts kept racing ahead.{/i}"
    "{i}It was like a tug of war, part of me wanting to enjoy this moment of solitude, the other part itching to return to the chaos, the noise, the people.{/i}"
    scene w_639 with fade
    "{i}Ava. Isabella. Zara. All of them swirling in my head.{/i}"
    e_ "And then there’s Alex... God, I can’t even think about him without getting tangled up in knots."
    e_ "Why does he still have this effect on me? It’s been... how long now? Longer than I’d like to admit."
    scene w_640 with dissolve
    e__ "So, you’re just going to stare at the stars all night, huh?"
    e__ "Very deep, very poetic. You know what you’re really doing? Avoiding everything. Classic Emma move."
    scene w_639 with dissolve
    e_ "Yeah, I know... I’m dodging things. Things like Ava, her cryptic hints about past loves, the weird vibes from Isabella, and Alex... always Alex."
    scene w_640 with dissolve
    e__ "You know you’re still in love with him, right? You wouldn’t be so damn jealous of Ava if you weren’t. Admit it."
    scene w_639 with dissolve
    e_ "Ugh... I hate when she’s right."
    e_ "Damn it, Alex... why do you still have this hold on me? It’s been long enough, hasn’t it? I should be moving on. I should be... but here I am, stuck."
    scene w_640 with dissolve
    e__ "Oh, this is going to be fun. Facing Ava, Alex... maybe even Isabella. You’ve got some big decisions to make, Emma. But hey, what’s life without a little drama?"
    "{i}I smirked to myself, knowing that my inner voice was right. I couldn’t hide forever. And whatever came next, I’d deal with it.{/i}"
    scene w_641 with dissolve
    "{i}The night was quiet as I walked closer to the stables.{/i}"
    "{i}The moonlight was faint, barely illuminating the surroundings, but I could still make out the shapes of the two horses grazing in the paddock.{/i}"
    "{i}Their presence seemed almost peaceful, like they were completely unaware of the chaos that swirled inside my head.{/i}"
    scene w_642 with dissolve
    "{i}I moved toward the fence, my footsteps soft on the grass. The air was cool against my skin, and the smell of hay and earth filled my senses.{/i}"
    scene w_643 with dissolve
    "{i}One of the horses turned its head toward me, its ears twitching as if it was curious about my approach.{/i}"
    scene w_644 with dissolve
    "{i}It didn’t seem frightened, which was surprising. Instead, it took a few slow steps in my direction.{/i}"
    scene w_645 with dissolve
    $ renpy.pause()
    scene w_646 with dissolve
    e_ "Why am I even here? I’m not an animal person. But then again..."
    e_ "maybe it's just nice to be somewhere quiet for once. Away from everything and everyone."
    scene w_647 with dissolve
    "{i}I reached out my hand slowly, expecting the horse to flinch or shy away, but it didn’t.{/i}"
    "{i}Its warm breath puffed against my fingers as I gently touched its muzzle.{/i}"
    "{i}Its fur was rougher than I expected, but there was something oddly soothing about the sensation.{/i}"
    e_ "See? I still have that charm. Even with a stubborn horse. If only people were this easy to handle. Yeah, right."
    scene w_648 with dissolve
    "{i}I let my fingers linger, stroking its face gently, feeling that brief connection.{/i}"
    "{i}It wasn’t much, but it was enough for the moment. The horse stood still, accepting my touch without any resistance.{/i}"
    "{i}I envied its simplicity, its lack of worry. Just a creature of habit, living without complications.{/i}"
    scene w_649 with dissolve
    "{i}After a while, it shifted its weight, then turned away from the fence, slowly ambling back into the paddock.{/i}"
    "{i}I watched it go, feeling a strange sense of loss.{/i}"
    "{i}It was ridiculous to be disappointed, but somehow that fleeting connection had meant something—if only for a moment.{/i}"
    scene w_650 with dissolve
    e_ "And just like that, it’s over. Just like everything else in my life, right?"
    e_ "Should I go back inside? Nah, let them miss me a little. Ava can hold the fort. She should be able to by now... or at least, she better."
    "{i}The barn loomed in the dark, a single flicker of light coming from its entrance like a faint invitation.{/i}"
    scene w_651 with dissolve
    "{i}I couldn’t help but feel curious as I made my way closer, my steps muffled by the night.{/i}"
    scene w_652 with dissolve
    $ renpy.pause()
    $ renpy.music.stop("music2", fadeout=2.0)
    call samuel_fucks_ruby_day3_1

    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_327 with fade
    "{i}I straightened up, took a deep breath, and made my escape, tiptoeing back towards the dimly lit path that led away from the barn.{/i}"
    "{i}As I walked further from the scene, my mind still reeled with the image of Ruby and Samuel tangled together.{/i}"
    "{i}I walked quietly back to my room, my mind racing with everything that had happened throughout the day.{/i}"
    "{i}The cool night air clung to my skin, still reminding me of the steam from the jacuzzi where Ava had spoken in her cryptic.{/i}"
    e_ "Ava, you sly fox… you always know more than you let on. But do you ever just tell me straight up? Of course not. That’d be too easy."
    "{i}And then there was the barn. The memory of Ruby and Samuel—ugh, it still made me cringe a little.{/i}"
    e_ "Honestly, do they have no shame?"

    if emmaspysamuelrubyday3:
        e_ "And why did I just stand there watching like some perv? Yeah, I wasn’t exactly innocent in that moment."
    
    $ renpy.music.stop("ambient1", fadeout=2.0)

    scene w_688 with fade
    "{i}When I finally made it to my bedroom, I found Alex already sound asleep, sprawled out under the green blanket like nothing in the world could bother him.{/i}"
    "{i}I stood there for a moment, watching him. He looked peaceful, completely oblivious to the chaos of the day.{/i}"
    scene w_689 with dissolve
    e_ "Lucky bastard. While I’m out there dealing with crazy people and their drama, he’s just here… snoring away."
    scene w_690 with dissolve
    "{i}I moved quietly across the room, slipping off my shoes and sitting on the edge of the bed.{/i}"
    "{i}For a moment, I considered waking him up—maybe venting a bit about everything that had happened.{/i}"
    e_ "What good would that do? He’d probably just smile, give me one of those ‘it’s gonna be okay’ looks, and roll back over."
    scene w_691 with dissolve
    "{i}Sliding under the covers beside him, trying to let the exhaustion of the day take over. But my mind was still racing, going over every little detail.{/i}"
    e_ "Samuel and Ruby… what the hell? Ava and her cryptic nonsense… What is going on in this place? And why am I always in the middle of it?"
    e_ "Maybe tomorrow will be quieter… but who am I kidding? This place is never quiet."
    $ renpy.music.stop("music2", fadeout=2.0)
    "{i}Finally, the weight of everything seemed to settle in, and I felt my body begin to relax.{/i}"
    scene w_692 with pixellate
    $ renpy.music.play("audio/musics/haunted_screams.mp3", "music2", fadein=2.0, relative_volume=0.2)
    "{i}I woke up to a strange sensation, as if something was wrong.{/i}"
    scene w_693 with dissolve
    "{i}My eyes fluttered open, and the room was bathed in an eerie.{/i}"
    e_ "What the hell? Did I leave a light on? This feels... off."
    "{i}I felt disoriented.{/i}"
    "{i}My body was heavy, as if the weight of sleep was still dragging me under, but something deeper, something unsettling, was keeping me awake.{/i}"
    scene w_694 with dissolve
    "{i}Alex wasn’t beside me.{/i}"
    "{i}The spot next to me on the bed was cold, his side of the blanket discarded like he’d been gone for a while.{/i}"
    e_ "Great. Where the hell did he run off to now? Did he have another early morning meeting he forgot to tell me about?"
    scene w_695 with dissolve
    "{i}I sat up slowly, rubbing my eyes. The sensation that something wasn’t quite right clung to me like a wet, sticky fog.{/i}"
    "{i}I glanced around the room, searching for any sign of Alex, or at least a clue as to why he wasn’t here. That’s when I noticed it.{/i}"
    "{i}My painting—the one I’d hung proudly on the wall just days ago—was gone. In its place was a blank, white canvas.{/i}"
    e_ "Wait... what the fuck? Did Alex do this? Why the hell would he take it down and replace it with this?"
    scene w_696 with dissolve
    "{i}I got out of bed, my legs still shaky from the pull of sleep, and walked towards the blank canvas.{/i}"
    "{i}I stopped in front of it, staring at the sheer emptiness of it, a chill running down my spine.{/i}"
    e_ "This isn’t funny, Alex. If this is some sort of weird prank, it’s not landing."
    "{i}My fingers trembled as I traced the edges, a heavy knot of unease settling in my stomach.{/i}"
    e_ "Did something happen while I was asleep? Was someone else in here? I don’t remember hearing anything…"
    scene w_697 with dissolve
    "{i}There was an odd stillness in the air, like the room itself was holding its breath.{/i}"
    "{i}And then it hit me. That feeling. That unmistakable sensation of being watched.{/i}"
    "{i}I froze, every hair on my body standing on end.{/i}"
    e_ "Am I... alone?"
    $ renpy.pause()
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_698 with fade
    $ renpy.pause()
    "{i}I turned slowly, my breath catching in my throat as I faced the impossible.{/i}"
    scene w_699 with dissolve
    "{i}There, towering above me, was the figure from my painting—the one I’d poured hours of emotion into, every brushstroke an echo of something deeper I’d been afraid to confront.{/i}"
    "{i}But now, here she was... alive.{/i}"
    scene w_700 with dissolve
    "{i}Her upper body was a woman’s, beautiful yet terrifying, but from the waist down, writhing tentacles, dark and sinuous, took the place of legs.{/i}"
    e_ "How the hell is this happening? This can’t be real... No. Am I dreaming?"
    scene w_699 with dissolve
    e "What the fuck? How is this possible? This... this is a nightmare, right?"
    "{i}The creature’s lips curled into a sinister smirk, her eyes locking onto mine with a gaze that felt all too familiar, like she knew me, inside and out.{/i}"
    scene w_700 with dissolve
    e__ "Oh, Emma... if this were a dream, would it really be any less real?"
    "{i}Her voice... it was smooth, taunting, dripping with the kind of confidence I’d never dared to show outwardly.{/i}"
    "{i}It reminded me of that voice inside my head—the one that always pushed me, teased me, but I’d always shoved it down, pretending I was in control.{/i}"
    scene w_699 with dissolve
    e "Who the hell are you?"
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_700 with dissolve
    "{i}She stepped closer, the tentacles dragging across the floor in a slow, deliberate motion that made my skin crawl.{/i}"
    o "I’m Octavia. You know me, Emma. I’m everything you try so hard to hide..."
    o "all those dirty little thoughts you pretend you don’t have. But honey, they’re in there, whether you like it or not."
    e "Shut up. You don’t know shit about me."
    o "Don’t I? Look at you..."
    o "pretending to be so pure, so in control. But deep down, you’re no different from me."
    o "You’re weak, Emma. You lie to yourself about what you really want."
    "{i}Her words cut through me, stinging more than I’d like to admit. Because deep down... I knew she wasn’t wrong.{/i}"
    e "You're just a figment. A twisted version of some nightmare I’m having. I don’t want any of this!"
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_701 with dissolve
    o "Lies. You crave it. You crave me. That thrill, that danger..."
    o "You think I just crawled out of your subconscious for fun? No, darling. You painted me. You brought me to life."
    e_ "Oh God, this can’t be happening. She’s... she’s right. But no, this is wrong. This is all wrong."
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_710 with dissolve
    e "Fuck off! You're not real. You’re just... something I created."
    o "I’m as real as you are, darling. Now... the question is, how long will you keep lying to yourself?"
    scene w_701 with dissolve
    e "What are you doing here?"
    o "I'm here to show you that you're not as holy and pure as you pretend to be,"
    "{i}I tried to fight the temptation, but Octavia's tentacles were making it difficult.{/i}"
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_702 with dissolve
    $ renpy.pause()
    "{i}One of Octavia's tentacles stroked my face, while another slowly and provocatively wrapped around my thigh.{/i}"
    "{i}I couldn't help but feel a little excited as the tentacle rubbed against my pussy through the fabric of panties.{/i}"
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_703 with dissolve
    $ renpy.pause()
    "{i}Another tentacle slowly entered my top through her cleavage, exploring her body.{/i}"
    scene w_704 with dissolve
    $ renpy.pause()
    $ renpy.music.play("audio/adult/emma_moangentl1.opus", "sfxloop1", fadein=2.0, relative_volume=0.3)
    "{i}Octavia's movements were slow and exciting, and Icouldn't help but moan softly as the tentacle that entered through the cleavage exposed my right breast and began to massage it.{/i}"
    scene w_705 with dissolve
    "{i}She approached me the already very excited and licked her face,{/i}"
    scene w_706 with dissolve
    $ renpy.pause()
    $ renpy.music.stop("sfxloop1", fadeout=2.0)
    scene w_707 with dissolve
    $ renpy.pause()
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_708 with dissolve
    "{i}before slowly pulling my face towards her and putting her long tongue in my mouth, in a kiss.{/i}"
    scene w_709 with dissolve
    $ renpy.music.play("audio/sfx/sfx_smack.ogg", channel="sfx1", relative_volume=0.5)
    "{i}At first, I regained control and pushed Octavia away, but Octavia was persistent.{/i}"
    scene w_710 with dissolve
    o "You can't deny what you feel, Emma,"
    $ renpy.music.play("audio/sfx/sfx_octavia_crawling.mp3", "sfx1", fadein=2.0, relative_volume=0.5)
    scene w_711 with dissolve
    $ renpy.pause()
    scene black with dissolve
    o "Your body wants this as much as I do."
    $ renpy.music.stop("music2", fadeout=2.0)

    $ emma_mental = EmmaMentalRemove()

    jump emma_blowjob_alex_day3
