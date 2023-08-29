# Define the gameUI screen with the "Status" button
screen gameUI:
    textbutton _("Status") action ShowMenu("status") xalign 1.0 yalign 0.0 xoffset -30 yoffset 30

# Status screen ##############################################################
screen status():
    modal False
    
    frame:
        xalign 1.0  # Align to the right edge
        yalign 0.0  # Align to the top edge

        hbox:
            spacing 10

            vbox:
                text _("Body:") color "#FF0000" font "fonts/Digitalt.ttf"
                text _("Mind:") color "#FF0000" font "fonts/Digitalt.ttf"
                text _("Spirit:") color "#FF0000" font "fonts/Digitalt.ttf"
                text _("Sanity:") color "#FF0000" font "fonts/Digitalt.ttf"

                # Add a button to hide the status menu
                textbutton _("Back") action Return()

            vbox:
                # Reference the skill values from the variables section
                $ body_def = (
                    _("You are feeling ") + (hundred_percent_strength_text if body_value >= 80 else
                    sixty_percent_strength_text if body_value >= 60 else
                    fourty_percent_strength_text if body_value >= 40 else
                    twenty_percent_strength_text if body_value >= 20 else"Weak and frail"))

                $ mind_desc = (
                    _("Your mind is ") + (hundred_percent_intelligence_text if mind_value >= 80 else
                    sixty_percent_intelligence_text if mind_value >= 60 else
                    fourty_percent_intelligence_text if mind_value >= 40 else
                    twenty_percent_intelligence_text if mind_value >= 20 else"Scarcely functional"))
                

                $ spirit_desc = (
                    _("Your spirit is ") + (stable_text if spirit_value >= 80 else unstable_text)
                )

                $ sanity_desc = (
                    _("You're feeling ") + (sane_text if sanity_value >= 80 else insane_text)
                )

                text body_def color "#FFFFFF" font "fonts/Digitalt.ttf"
                text mind_desc color "#FFFFFF" font "fonts/Digitalt.ttf"
                text spirit_desc color "#FFFFFF" font "fonts/Digitalt.ttf"
                text sanity_desc color "#FFFFFF" font "fonts/Digitalt.ttf"

screen hud():
    modal False

    imagebutton auto "HUD/Inventory/bg_hud_inventory_%s.png":
            focus_mask True
            hovered SetVariable("screen_tooltop", "Inventory")
            unhovered SetVariable("screen_tooltip", "")
            action Show("inventory"), Hide("hud")

screen inventory():
    add "bg_inventoryscreen"
    modal True

    vbox:
        pos 0.15, 0.25
        for item in inventory.items:
            text "[item.name] - [item.description]\n" style "inventory_text"
    
    imagebutton auto "HUD/Inventory/inventoryscreen_return_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip", "")
        action Hide("inventory"), Show("hud")
