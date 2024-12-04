screen gallery():

    tag menu

    add "gray"

    $start = gallery_page * maxperpage
    $end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            imagebutton idle gallery_items[i].thumb:
                style "gallery_button" #delete this line to remove hover
                action Show("gallery_closeup", dissolve, gallery_items[i].images)
                xalign 0.5
                yalign 0.5
        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbx - 20
                xalign 0.5
                yalign 0.1
                text gallery_items[i].name
        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous/next buttons
    if gallery_page > 0:
        textbutton "{color=#000}{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.98
            background "gui/button_back.png"
            hover_background "gui/button_back_over.png"
            xsize 300
            ysize 70
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "{color=#000}{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            background "gui/button_next.png"
            hover_background "gui/button_next_over.png"
            xsize 300
            ysize 70
    #return button
    textbutton "{color=#000}{/color}" background "gui/button_return.png" hover_background "gui/button_return_over.png" xsize 300 ysize 70:
        action Return()
        xalign 0.5
        yalign 0.98
        #background "#fff8"

screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 1
    imagebutton idle images[closeup_page]:    ###############
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]                    #Hide("gallery_closeup", dissolve)
        xalign 0.5
        yalign 0.98
        background "#fff8"
        
        
        
        
##########################################################################################################################################        
        
        
        
        

        
        
#############################################################################################################################################        
        
        
        
        
        

style gallery_button:
    background "gui/gallery_button_frame.png"
    hover_background "gui/gallery_button_hover.png"