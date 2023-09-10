
# Define descriptions based on skill values
#any variable you plan to change the value of,  that needs to be saved and restored when the player saves/loads,   needs to be defaulted 
#don't indent unless inside of a block (IE LABEL,)

    
##STATUS#####################################################################

#body (strength)
default hundred_percent_strength_text = _("Powerful")
default eighty_percent_strength_text = _("Strong")
default sixty_percent_strength_text = _("Somewhat Active")
default fourty_percent_strength_text = _("Frail")
default twenty_percent_strength_text = _("Wasting")

#mind (intelligence)
default hundred_percent_intelligence_text = _("Genius")
default eighty_percent_intelligence_text = _("Sharp")
default sixty_percent_intelligence_text = _("Mindful")
default fourty_percent_intelligence_text = _("Dull")
default twenty_percent_intelligence_text = _("Incompetent")

#mspirit (Mind)
default stable_text = _("stable")
default unstable_text = _("unstable")

#sanity
default sane_text = _("sane")
default insane_text = _("insane")

#Define stats
default body_value = 10
default mind_value = 10
default spirit_value = 10
default sanity_value = spirit_value / mind_value

##IMAGES######################################################################

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define y = Character("Yoon", color = "#f53939", what_color = "#f53939", image = "yoon")

image yoon talking:
    "yoon"
    0.75
    "yoon talk"
    0.75
    repeat

##INVENTORY######################################################################

#default declares something as a renpy statement $ calls it as a python statement
default inventory = Inventory ([], 0)

# define, Itemname, call inventory ("Name, Description")
define keys = InventoryItem("A set of Keys", "I should check if I can use this on anything")
define bacon = InventoryItem("Back Bacon", "This could be quite tasty!")

##SIZE CONTROL##################################################################

#transforms
transform double_Size:
    zoom 1.25
transform half_Size:
    zoom 0.50
transform threeQuarter_Size:
    zoom 0.75

#VARIABLES######################################################################
    
default SirenSeen = False
default ScreenSeen = False


##INIT##########################################################################

init python:
    def change_physicality(amount):
        store.body_value += amount

    def change_spirit(amount):
        store.spirit_value += amount

        if store.spirit_value <= 0:
            renpy.jump("choices_badend1")

    def change_intelligence(amount):
        store.mind_value += amount

label start:

    stop music fadeout 1.5
    show screen gameUI
    show screen hud

    #testing
    # Initialize character stats
    $ body_value = 100
    "Your physicality is at [body_value]."
    $ mind_value = 100
    "Your intelligence is at [mind_value]."
    $ spirit_value = 100
    "Your spirit is at [spirit_value]."


    show yoon talking at left, threeQuarter_Size:
        yanchor .5 ypos 1.0
        xzoom -1
    y "let's see what I am carrying..."
    #yalign 1.0  yoffset 10, will align the image to the bottom of the screen then lower it exactly 10 pixels further
    #yanchor 0.1, ypos 1.0 will  make the image be 10% below the bottom of the screen and top 90% visible
    #no need for file extension when calling yoon happy.png, just make sure it's typed properly and it will auto-import

    $ inventory.list_items()   

    #testing items
    y "I'm gonna pickup this item" 
    $ inventory.add_item(keys)
    y "Now let's take a look"
    $ inventory.list_items()

    #testing each stat
    $ change_physicality(10)
    "After some training, your physicality has increased to [body_value]."

    $ change_spirit(-3)
    "You feel drained, and your spirit has decreased to [spirit_value]."

    $ change_intelligence(2)
    "Studying diligently, your intelligence grows to [mind_value]."

##Start

    "There is only silence, a suffocating presence that somehow appears to engulf every sense into an all-consuming void.\n"
    "There are no words to be spoken or sounds to be made. The atmosphere is oppressively motionless and holds a foreboding, menacing aura.R\n"
    "It was silence that could speak volumes, like the undusted and underused crevasse of an antique tome lost to time.\n"
    "In this silence, every sound that followed would be magnified by this utter quiet.\n"
    "Demanding absolute respect and consideration for those who would watch."

    menu:
        "Lean into the Silence":
            $ body_value += 100
            jump Choices1_a
            $ spirit_value += 60
        "Hide From It":
            jump Choices1_b

label Choices1_a:

    "You embrace the silence, and in that very moment of noise, static escapes from the dark abyss. It sounds like endless buzzing at a disproportionate speed of wavelength.\n"
    "Jumbled, fragmented noise that drowns out any attempt at cohesive thought. Though this noise seems to bring peace in a sudden cacophony."

    jump Choices_CommonRoute_a

label Choices1_b:

    "You flee within, wriggling beneath the overwhelming attempt at mental feedback. Wanting nothing more than to return to a solemn and peaceful sleep, and in that very moment of noise,\n"
    "static escapes from the dark abyss. It sounds like endless buzzing at a disproportionate speed of wavelength. Jumbled, fragmented noise that drowns out any attempt at cohesive thought."

    jump Choices_CommonRoute_a

label Choices_CommonRoute_a:

    show prologue_base
    with Dissolve(.75)
    ##show yoon at topleft, threeQuarter_Size 

    "Your vision is blurred as the persistent darkness seeps into your eye sockets, creating a black-and-white haze in front of you.\n"
    "The air around you hangs heavy with the smell of oil and saltwater, and the dim illumination flickers like the dying spark of a fire, as your senses all seem to suddenly come alive."

    "Peering around your newfound surroundings, you look to find the source of the buzzing. Flickering neon screens cast an eerie glow on a rusted metal interior.\n"
    "The faint echo of an alarm rings behind you, searching and bouncing off far corridors before returning to your ears."

menu:
    "Look to the screens.":
        $ScreenSeen = True
        jump Choices_Screens
    "Look to the Sirens":
        $SirenSeen = True
        jump Choices_Sirens

label Choices_Screens:
    "You gaze at the jumbled writing on the screens for what feels like hours as your mind races with questions.\n"
    "The screens appear to be rapidly switching between text and images that you can't read or understand."

    if SirenSeen:
        "Staring towards these screens, you make out a long, coiling trail of wires, like the body of an alloy anaconda, trailing about the entire room.\n"
        "The noise seems to be emanating from them, but the echo behind you still seems to be roaring louder. Looking back to the screen,\n"
        "The only words you can make out among the overwhelming text are outside, suffering, and safety."
    else:
        menu:
            "The siren bellows behind you":
                $SirenSeen = True
                jump Choices_Sirens

menu:
    "Why can't I move?" if SirenSeen and ScreenSeen:
        jump Choices_CommonRoute_a_1
    "Continue investigating" if not (SirenSeen and ScreenSeen):
        jump Choices_Screens

label Choices_Sirens:

    "The wailing echo of the siren becomes louder, filling you with an unfathomable dread; nonetheless, you are powerless to turn your neck to the side.\n"
    "If only you could find a way to silence the noise. As the dissonance intensifies and becomes intolerable, your heart rate increases as your senses are continually assaulted.\n"
    "You sense the oppressive, unavoidable weight of dread settling over you like a thick blanket. It's as though the music is a hostile thing that wants to consume you entirely."

menu:
    "Why can't I move?" if SirenSeen and ScreenSeen:
        jump Choices_CommonRoute_a_1
    "The Screens call to you" if not (SirenSeen and ScreenSeen):
        $ScreenSeen = True
        jump Choices_Screens

label Choices_CommonRoute_a_1:
    scene prologue_yoon
    with Dissolve(.75)
    "You begin to writhe in recourse. Staring down at your arms, you look in horror at a trail of wires that lead from your skin to the base of the floor. \n"
    "They have fused with your flesh, becoming one with your body. A convoluted cybernetic network that pulses with an unsettling blue light, is created by the tendrils of metal and plastic that snake through your skin and delve deep into your muscles and organs."
    "You wheeze a struggled breath as you look upon pale and clammy skin. The wires feel as though they are alive and conscious because you can feel them writhing and twitching underneath."

menu:
    "Panic":
        jump Choices_CommonRoute_a_2

label Choices_CommonRoute_a_2:


    "Try as you might, you struggle, and your heartbeat quickens with every movement. repressing a minor sob, you come to the realisation that there is no escaping this twisted sentinel that you've become. \n" 
    "a sigh wheezes from your desperate lips as you begin to accept the terrifying situation that awaits you and feel the weight of hopelessness engulfing you like a smothering blanket." 
    "seeing yourself sinking deeper and deeper into the pit of despair with each passing second, a gloom engulfs your entire essence. Mustering enough courage to open your eyes reveals something you hadn't noticed before a porthole. Outside of it lie murky waters."
    "A sea of monochromatic worlds of black and white once more, and you couldn't help but a crushing weight of dread dragging you down into its inky depths, as a shadow creeps across the void in front of you."

menu:
    "Peer into the blackness once more":
        jump Choices_CommonRoute_a_3

label Choices_CommonRoute_a_3:

    "Your body tenses, and you feel a knot begin to form in your stomach, as you brace yourself for what's to come. Taking a deep breath, hoping to calm your racing thoughts, you find your heart is pounding so loudly that you can barely hear anything else."
    "Glancing around, a piece of you searches for a glimmer of hope and a way out of this nightmare. As you hold your breath for a moment, every fibre of your being wants this to end-the fear, the uncertainty, the pain. You close your eyes, and for a brief moment, you allow yourself to imagine a moment of respite."
    "Letting yourself hope and wish for a better moment and a better future. And as you do, the world around you begin to shift, unravel, and transform."
    scene prologue_fish
    with Dissolve(.75)
    "A school of Koi fish suddenly swim into view through the porthole. In contrast to the generally drab and lifeless sea, they stood out vividly."
    "Their scales glistening in the dim light, reflecting the white of the bubbles trailing after the submarine and the blackness of the ocean floor."
menu:
    "Admire the beauty":
        jump Choices_CommonRoute_a_4

label Choices_CommonRoute_a_4:
    "The fish swim in circles while synchronising every movement of their bodies. It's difficult to distinguish where one fish stops, and another begins as they chase each other with such recklessness and enthusiasm."
    "where only the two of them are present. Their eyes never leave one another as they circle, and their fins are ablaze with excitement. The sounds of water streaming past their gills and the beat of their fins take the place of the world around them."
    "It's a dance that talks of an unbreakable tie and one of closeness and connection."
    "They are the epitome of unadulterated bliss as they continue to move around one another while immersed in their own worlds. An intimacy so close but never touched."

menu:
    "Stare closer":
        jump Choices_CommonRoute_a_5

label Choices_CommonRoute_a_5:
    "You notice a glimmer of movement. As you turn to look, a dark figure with a bizarre, twisted appearance appears in the distance." 
    scene prologue_monster
    with Dissolve(1)
    "You experience a sudden rush of fear as it gets closer. It has tentacles that move in the water like eels and is unlike anything you've ever seen. \n"
    "Its opening maw shows a row of razor-sharp teeth, and its eyes sparkle with an evil intelligence."
    "Watching the creature approach closer and closer with your heart beating, you notice that despite its terrifying appearance, its motions are beautiful and sinuous." 
    "The shadowy shape grows nearer as you stare in dread, and you suddenly realise that it's not just any water creature."
    "Its ugly body is covered in wires and bio-mutated technology, making it resemble a horrific cyborg. It moves jerkily and strangely, as though it were a twisted fusion of metal and flesh." 
    "It sees you. You, and before you know it, it's already upon you. You let out a silent scream of horror, and - "

menu:
    "A jolt upright":
        scene bg bedroom with Dissolve(.75):
            zoom 1.4
        show yoon sad2 at left, threeQuarter_Size with Dissolve(.75):
            yanchor .5 ypos 1.0 
            xzoom -1
        jump Choices_CommonRoute_b
    
label Choices_CommonRoute_b:
    
    "You jerk awake as your alarm clock blares, its shrill sound piercing through the fog of dreams. In that disoriented moment of awakening, you find yourself bathed in a cold sweat, heart pounding in your chest."
    "Attempting to rise, a rattle of surprise courses through you- a charging cable, twisted tightly around your arm, tethers you to the wall. Frustration wells up within as you desperately struggle to free yourself from the constricting embrace of the cable."
    "Your movements are frantic, fueled by the primal instinct to break free. With each tug, you feel the resistance of the cable, its hold on you seemingly unyielding."
menu:
    "Investigate your surroundings":
        jump Choices_CommonRoute_b_1

label Choices_CommonRoute_b_1:
    "As your gaze shifts from your entangled arm to the surrounding walls, the blurry haze dissipates, revealing a familiar scene that brings a deep sense of calm to your mind."
    "Adorned with weathered wallpaper that has gracefully endured the passage of time, these walls serve as silent witnesses to stories familiar to you etched upon their surface. They present a tapestry of memories, an evocative collage comprising faded photographs, worn posters, and delicate handwritten notes."
    "Each artifact carries the weight of moments long past, forming a mosaic that weaves together your personal history. \n"
    "In this room, the very essence of time is captured, as the walls themselves become a living archive- a testament to the countless tales whispered by the peeling paint and weathered corners."
menu:
    "Scan the rest of your surroundings":
        jump Choices_CommonRoute_b_2

label Choices_CommonRoute_b_2:
    "The room is filled with light and mystery, streaming from a window that covers the back wall. It invites the eye to the far-left corner, where a wooden desk stands firm. \n"
    "The desk is a chaos of papers, books, pens, and a faint clock. Among the disorder, liquor bottles lurk, like a tumor. "
    "On the right side of the room, an empty easel towers, ready for artistic expression. Its blank canvas beckons with stories and realms untold, a witness to limitless imagination and creative potential. \n"
    "The room pulses with the expectation of creation, the chance for free expression embodied in the silent easel."
    "The wallpaper, desk, and easel shape an environment that embraces both the burden of the past and the infinite opportunities of the future. In this room, memories blend with dreams, and time fades away. \n"
    "It is a space where inspiration thrives, ideas soar, and your restless soul finds peace. But why has it felt different lately?"
menu:
    "Peer outside the window":
        jump Choices_Window
    "Investigate the desk further":
        jump Choices_Desk

label Choices_Window:

label Choices_Desk:



return