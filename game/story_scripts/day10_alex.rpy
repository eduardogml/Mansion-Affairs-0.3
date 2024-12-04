label day10_alex_1:

    scene black with fade

    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/orange_twilight_so_close.mp3", "music1", fadein=2.0, relative_volume=0.2)

    show 12rd_day with fade
    $ renpy.pause()
    hide 12rd_day with dissolve

    $ renpy.music.play("audio/environment/env_garden_night.mp3", channel="ambient1", fadein=2.0, relative_volume=0.3)
    scene w_805 with fade
    "{i}I leaned against the cool stone of the fountain, the gentle trickle of water a stark contrast to the restless thoughts churning in my mind.{/i}"
    scene w_806 with dissolve
    "{i}Tonight was the dinner at Eleanor's. A double date, no less. The idea had seemed like a good one at the time – a chance to show Emma that we could still be… civil, maybe even friendly.{/i}"
    "{i}A step towards rebuilding what we’d lost.{/i}"
    scene w_807 with dissolve
    a_ "But what if it backfires?"
    a_ "Emma’s been distant lately, and I can’t shake this feeling that she’s pulling away, further than ever."
    scene w_806 with dissolve
    "{i}I’d made an effort tonight, dressed in something a little more…presentable than usual.{/i}"
    "{i}I wanted to impress Emma, to remind her of the man she’d fallen for. The man I used to be.{/i}"
    scene w_807 with dissolve
    a_ "Is it even possible to go back? To recapture that spark, that easy laughter we used to share?"
    a_ "Or are we just kidding ourselves, pretending that this… this fragile truce can last?"
    scene w_808 with dissolve
    "{i}And then there was Eleanor. The memory of her near-naked greeting, the playful glint in her eyes, the almost-kiss… it all added another layer of complexity to an already tangled situation.{/i}"
    "{i}Her husband, Tristan, would be there tonight. That thought alone should have been enough to deter any further… complications. But with Eleanor, there were no guarantees.{/i}"
    a_ "Would she really be that reckless? To try something with me, right under her husband’s nose? It seemed insane, but…"
    a_ "there was something about Eleanor, a wildness, an unpredictability, that made me think she might actually be capable of anything."
    "{i}Either way, I had a feeling tonight was going to be a long one.{/i}"
    scene w_810 with fade
    "{i}My thoughts were interrupted by the soft click of the mansion's door opening.{/i}"
    "{i}She walked towards me, her heels clicking softly against the stone path, and I couldn't help but admire the way she carried herself.{/i}"
    scene w_812 with fade
    "{i}Emma stepped out, and for a moment, I forgot everything else. The soft glow of the porch light illuminated her face, highlighting the subtle curve of her lips, the way her eyes sparkled in the night.{/i}"
    scene w_814 with dissolve
    $ renpy.pause()
    "{i}She was wearing a simple dress, but on her, it looked like a million bucks.{/i}"
    scene w_815 with dissolve
    $ renpy.pause()
    "{i}The way it hugged her curves, the way she moved…{/i}"
    scene w_816 with dissolve
    $ renpy.pause()
    "{i}God, she was breathtaking.{/i}"
    scene w_812 with dissolve
    a_ "Damn, she looks incredible. It’s like she’s doing this on purpose, trying to drive me crazy. And it’s working."
    a_ "I’d almost forgotten how much I… still want her, even after everything."
    "{i}She looked stunning, the dress clinging to her curves in all the right ways. I could feel my pulse quickening.{/i}"
    scene w_813 with dissolve
    e "So… how do I look?"
    "{i}Her voice was soft, a hint of nervousness in her tone. It was a vulnerability I hadn’t seen in a while, and it made my heart ache in a way I didn't expect.{/i}"
    a_ "She still cares what I think. After everything, she still… wants to impress me."
    scene w_821 with dissolve
    a "You look… incredible, Emma. Seriously. I might have to keep Tristan away from you tonight."

    if alexkissemmaday2:
        $ renpy.music.play("audio/sfx/sfx_laugh2.opus", channel="sfx1", relative_volume=0.3)
        "{i}I grinned, hoping to lighten the mood, but also meaning every word. She laughed, and the sound was like music to my ears.{/i}"
        a_ "That laugh… I’ve missed it. I’ve missed her."
    else:
        "{i}I grinned, hoping to lighten the mood, but also meaning every word.{/i}"
    
    scene w_822 with dissolve
    a "Ready to go?"
    scene w_823 with dissolve
    e "Come on. I want to know if this wine is really worth it."
    "{i}I offered her my arm, and as she took it, a jolt of electricity ran through me. The simple contact was enough to send my thoughts racing.{/i}"
    a_ "Her skin is so soft… I'd almost forgotten how good it feels to be this close to her."
    "{i}We walked side by side, the gravel crunching softly beneath our feet.{/i}"
    a_ "Maybe tonight, just maybe, we can find our way back to each other."
    scene w_824 with fade
    "{i}The walk to Eleanor's was shorter than I expected, the silence between Emma and me filled with unspoken tension.{/i}"
    "{i}I could feel her eyes on me, questioning, assessing, and I wondered what she was thinking.{/i}"
    scene w_825 with dissolve
    a_ "Is she regretting this already? Or is she just as curious about Eleanor and Tristan as I am?"
    $ renpy.music.play("audio/sfx/sfx_knock.ogg", channel="sfx1", relative_volume=1.0)
    "{i}As I raised my hand to knock, a flicker of anticipation ran through me.{/i}"
    a_ "What would Eleanor be like tonight, with her husband present? Would she still be that flirtatious, playful woman I’d met before, or would she play the role of the dutiful wife?"
    a_ "I hoped it was the former. Things were already complicated enough without adding another layer of awkwardness to the mix."
    $ renpy.music.play("audio/sfx/sfx_door_open.ogg", channel="sfx1", relative_volume=1.0)
    scene w_826 with fade
    "{i}The door opened, and Eleanor stood there, radiant in a flowing gown that accentuated her curves.{/i}"
    "{i}Her smile was warm, welcoming, and for a moment, I forgot all about Emma standing beside me.{/i}"
    a_ "Damn, she looks even better than I remember. This night just got a lot more interesting."
    scene w_827 with dissolve
    ele "Alex! Emma! So glad you could make it. Come in, come in."
    ele "Tristan's just finishing up some work. He’ll be down in a moment. Why don’t we head upstairs to the living room? It’s more comfortable there."
    scene w_829 with dissolve
    "{i}She turned, leading the way up the grand staircase. I watched as she ascended, my eyes tracing the elegant curve of her back, the way the fabric of her dress flowed around her.{/i}"
    "{i}I followed, Emma close behind, but my mind was already elsewhere.{/i}"
    a_ "Tonight… tonight could be interesting. I needed to play this right."
    $ renpy.music.play("audio/sfx/sfx_door_closed.ogg", channel="sfx1", relative_volume=1.0)
    $ renpy.music.stop("music1", fadeout=2.0)
    $ renpy.music.stop("ambient1", fadeout=2.0)
    $ renpy.music.play("audio/musics/piano_soft.mp3", "music2", fadein=2.0, relative_volume=0.2)
    scene w_830 with fade
    "{i}Eleanor led us into a dining room, the table set for four. The flickering candlelight cast dancing shadows on the walls, creating an intimate, almost secretive atmosphere.{/i}"
    "{i}I glanced at Emma, trying to gauge her reaction. She seemed tense, her eyes scanning the room with a guarded expression.{/i}"
    a_ "What’s going on in her head? She's been quiet since we left the mansion. Is she still upset about… everything?"
    ele "Make yourselves comfortable. I’ll be right back with some wine. I have a bottle Tristan’s been saving for a special occasion."
    scene w_831 with dissolve
    "{i}Eleanor’s eyes lingered on mine for a beat too long before she turned and left the room.{/i}"
    "{i}I watched her go, a mix of anticipation and unease swirling within me. Special occasion. What’s she planning?{/i}"
    a_ "Is she trying to impress us? Or is this some kind of… test?"
    scene w_832 with dissolve
    "{i}I pulled out a chair for Emma, and she sat down, her movements stiff and formal. I sat next to her, the silence between us growing thicker with each passing second.{/i}"
    a_ "I need to break the ice. But what do I even say?"
    a "So, how are you holding up with everything? You seem a bit… quiet tonight."
    scene w_833 with dissolve
    e "Just… thinking. A lot on my mind, I guess."
    a_ "She’s deflecting. Typical Emma. Always bottling things up until they explode."
    scene w_834 with dissolve
    a "Anything you want to talk about?"
    scene w_833 with dissolve
    e "Not really. Just… life stuff. You know how it is."
    "{i}She shrugged, avoiding my gaze. I could feel the wall she’d built around herself, and it frustrated me. I wanted to reach out, to break through, but I didn't know how.{/i}"
    scene w_834 with dissolve
    a_ "Why does she make this so damn hard?"
    a "Well, if you change your mind, I’m here. We used to be good at talking, remember?"
    scene w_833 with dissolve
    e "We used to be a lot of things, Alex."
    "{i}Her words stung, a sharp reminder of everything we’d lost. I saw a flash of pain in her eyes. Or was it resentment?{/i}"
    scene w_834 with dissolve
    a_ "Damn it, Emma. Why do you have to twist the knife like that?"
    a "Look, I know things haven’t been easy between us. But I’m trying here. Can we just… enjoy the evening? For once?"
    scene w_833 with dissolve
    e "Enjoy the evening? With Eleanor practically throwing herself at you? I don’t know if 'enjoy' is the right word."
    "{i}Her sarcasm was like a punch to the gut. It was clear she’d noticed Eleanor’s lingering glances, her flirtatious tone. I tried to keep my expression neutral, but I could feel my jaw clenching.{/i}"
    scene w_834 with dissolve
    a_ "She’s jealous. Good. Maybe there’s still something there, something worth fighting for."
    a "She’s just being friendly, Emma. Don’t read too much into it."
    scene w_833 with dissolve
    e "Friendly? Is that what you call it?"
    scene w_834 with dissolve
    a "There’s nothing going on between Eleanor and me. It’s just you and me, Emma. Remember?"
    scene w_833 with dissolve
    "{i}I wanted to tell her the truth. That Eleanor was a dangerous game I wasn't sure I could win.{/i}"
    "{i}That I was here, with Emma, because she was the only one who mattered. But the words wouldn’t come.{/i}"
    e "Maybe you're right. Maybe I am reading too much into it."
    scene w_832 with dissolve
    "{i}She forced a smile, but it didn’t quite reach her eyes. There was something… off about her. Something I couldn’t put my finger on.{/i}"
    a_ "Is she lying? Or is there something else bothering her?"
    a "You’ve been… different lately, Emma. More on edge than usual."
    e "Different? How so?"
    scene w_833 with dissolve
    "{i}She looked at me, a flicker of… something in her eyes. Fear? Uncertainty? It was gone as quickly as it appeared, but it was enough to make me uneasy.{/i}"
    a_ "What’s she hiding?"
    scene w_834 with dissolve
    a "I don't know. Sometimes you seem… like another person. Someone… I don’t recognize."
    "{i}The words felt clumsy, inadequate.{/i}"
    "{i}I wanted to say more, to explain the strange shift I’d noticed in her, the moments when she seemed… possessed by something else. But I couldn’t articulate it, not even to myself.{/i}"
    scene w_833 with dissolve
    a_ "Damn it, why can’t I just say what I mean?"
    e "Yeah, I’m fine. You’re right. I’m just… overthinking things."
    e "This whole mansion, the attack, the dinner… it’s all getting to me."
    scene w_832 with dissolve
    "{i}She laughed, but it sounded forced, hollow. It was like she was trying to convince herself more than me.{/i}"
    a_ "That’s not true. There’s something more. I can feel it."
    "{i}I looked at her, searching her face for some kind of clue.{/i}"
    scene w_835 with dissolve
    "{i}But before I could press further, Eleanor walked back into the room, two glasses of wine in hand, a triumphant smile playing on her lips.{/i}"
    "{i}Eleanor returned, a bottle of wine in hand, her smile radiating a warmth that felt… almost too genuine.{/i}"
    "{i}The tension between Emma and me had been thick enough to cut with a knife, and Eleanor’s presence, however calculated, was a welcome distraction.{/i}"
    a_ "At least she’s not talking about ghosts or haunted mansions."
    ele "Here we are. A little something to… loosen things up."
    "{i}Her good humor was infectious, a lightness that made me forget, for a moment, the unease I’d been feeling.{/i}"
    e "Thanks, Eleanor. I think we could both use a glass."
    scene w_836 with dissolve
    "{i}As she moved around the table, pouring the wine, I couldn’t help but admire… everything.{/i}"
    scene w_837 with dissolve
    a_ "Damn, she looks good tonight. That dress… it’s like she’s trying to taunt me. And it’s working."
    "{i}As Eleanor leaned in to fill Emma’s glass, her back was to me, and my eyes… well, they couldn’t help but wander.{/i}"
    $ renpy.music.stop("music2", fadeout=2.0)
    $ renpy.music.play("audio/musics/sexy_beat.mp3", "music1", fadein=2.0, relative_volume=0.2)
    scene w_841 with dissolve
    "{i}The curve of her hips, the way the dress clung to her backside…{/i}"
    $ renpy.pause()
    a_ "Is she… is she not wearing any panties? No, that’s insane. She wouldn’t. Would she?"
    "{i}The thought was too tempting to ignore. As she focused on Emma, I reached out, my fingers brushing lightly against the hem of her skirt.{/i}"
    scene w_842 with dissolve
    $ renpy.pause()
    "{i}I lifted it just enough to confirm my suspicions. Nothing. She wasn’t wearing anything underneath.{/i}"
    a_ "Holy shit. She’s really not wearing any panties. This is…"
    "{i}I felt Eleanor’s body tense slightly, a subtle tremor that ran through her.{/i}"
    "{i}But she didn't react, didn't turn around. Instead, she continued pouring the wine.{/i}"
    a_ "She felt that. She knows what I’m doing. And she’s not stopping me."
    scene w_843 with dissolve
    $ renpy.pause()
    "{i}Emboldened, I let my fingers linger, brushing against the soft skin of her thigh.{/i}"
    "{i}I reached up further, sliding my fingers between her legs, cupping her pussy gently and pressing a little harder.{/i}"
    "{i}Her breath hitched and she trembled, but still, she didn't move.{/i}"
    a_ "She likes this. She’s into it. Damn, Eleanor, you’re something else."
    scene w_842 with dissolve
    "{i}I pulled my hand back slowly, letting the hem of her skirt fall back into place.{/i}"
    scene w_841 with dissolve
    "{i}My heart was racing, a mix of excitement and guilt swirling within me. I waited for her to turn around, to confront me, to say something—anything.{/i}"
    scene w_845 with fade
    "{i}But she didn’t.{/i}"
    a_ "Maybe I should just… pretend that didn’t happen."
    $ renpy.pause()
    scene w_327 with fade
    "{i}What will Alex choose when temptation meets conscience?{/i}"
    "{i}Will he succumb to the allure of Eleanor’s provocations, or will he find the strength to bridge the growing chasm between him and Emma?{/i}"
    "{i}The dinner is just beginning, but the stakes are already higher than Alex anticipated.{/i}"
    "{i}Stay tuned for the next chapter, where alliances will be tested, truths will surface, and Alex’s path may take a turn he never expected.{/i}"
    "{i}See you in the next chapters of this story, with strong revelations and news.{/i}"
    "{i}Thanks for playing.{/i}"

    jump sandbox
