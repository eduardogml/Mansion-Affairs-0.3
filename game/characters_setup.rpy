#a very simple gallery
init python:

    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme

    gallery_items = []
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["alex_1920"], "alex_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["emma_1920"], "emma_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["daniel_1920"], "daniel_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["isabella_1920"], "isabella_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["ava_1920"], "ava_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["ruby_1920"], "ruby_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["natalie_1920"], "natalie_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["eleanor_1920"], "eleanor_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["victor_1920"], "victor_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["samuel_1920"], "samuel_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["tristan_1920"], "tristan_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["zara_1920"], "zara_thumb"))
    gallery_items.append(GalleryItem("{color=#000}{/color}", ["dominic_1920"], "dominic_thumb"))



#gallery background
image gray = "gui/characters_background.png"

#384x216 (16x9) set 1280x720p for the lock and all thumbnails
#600x338 (16x9) set 1920x1080 for the lock and thumbnails
#gallery locked image
image lockedthumb = ("images/lockedthumb.webp")
image main_menu = ("gui/main_menu.webp")

image banu2_1920 = ("images/gallery_lock.webp") 
image alex_thumb = ("images/alex_thumb.webp") 
image emma_thumb = ("images/emma_thumb.webp") 
image daniel_thumb = ("images/daniel_thumb.webp") 
image isabella_thumb = ("images/isabella_thumb.webp") 
image ava_thumb = ("images/ava_thumb.webp") 
image ruby_thumb = ("images/ruby_thumb.webp") 
image natalie_thumb = ("images/natalie_thumb.webp") 
image eleanor_thumb = ("images/eleanor_thumb.webp") 
image victor_thumb = ("images/victor_thumb.webp") 
image samuel_thumb = ("images/samuel_thumb.webp") 
image dominic_thumb = ("images/dominic_thumb.webp") 






#gallery images
image img1 = ("gui/button_start.png")
image img2 = ("gui/button_start.png")



#gallery thumbnails images
image thumb1 = ("gui/button_start.png")
image thumb2 = ("gui/button_start.png")
