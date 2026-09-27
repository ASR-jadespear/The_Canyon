# Define your characters
define l = Character("Leon", color="#5A9BD4")
define g = Character("Grace", color="#E67E22")

label start:
    # Scene 1: Sets the first background (bg_1.jpeg)
    scene bg_1:
        size (1920, 1080)
    
    # Text without a character variable acts as general narration
    "The canyon was completely silent."
    "Nothing but dust and echoes for miles."
    "Even though it may seem that we have managed to beat the Umbrella Corporation, the truth is that they..."
    "...are still out there, lurking in the shadows, waiting for the right moment to strike."
    
    # Scene 2: Sets the second background (bg_2.jpeg)
    scene bg_2:
        size (1920, 1080)
    
    # Leon appears first
    show leon_character at left:
        zoom 0.5
    
    l "Looks like I beat you here."
    
    # Grace appears next
    show grace_character at right:
        zoom 0.5
    
    g "Don't get too comfortable, Leon."
    
    l "Why not? it seems like you are dillydally. Even though you said that you will join us to restore the Raccon City"
    l "But seems like you were all bark no bite."
    
    g "Leon!!!!!!!!"
    
    return