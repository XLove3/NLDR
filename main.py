# Import DearPyGui and the Random module:
import dearpygui.dearpygui as dpg, random as rd


# *** Global Variables: ***

# The Neat Little Dice Game will be set up into a dictionary of "screens":
screens = {}

# Set up the names for the dice:
dice_names = ["Two", "Four", "Six", "Ten", "Twelve", "Twenty", "One Hundred"]

# Regular Mode states (checkboxes, sliders, and selected items):
r_dice_boxes = {}
r_dice_sliders = {}
r_selected_items = {}

# Average Mode states (checkboxes, sliders, and selected items):
a_dice_boxes = {}
a_dice_sliders = {}
a_selected_items = {}
# TODO: Add variable for the number of rolls


# *** Starting Setup ***

# Create context and viewport, and setup DearPyGui:
dpg.create_context()
dpg.create_viewport(title='Neat Little Dice Roller')
dpg.setup_dearpygui()


# *** Functions: ***

# Show screen according to name of screen:
def show(name):
    # TODO: Add a docstring to function show()
    '''Docstring'''

    # Loop through the values in the dictionary screens and hide each item:
    for screen in screens.values():
        dpg.hide_item(screen)

    # Show the screen with the name from the argument name:
    dpg.show_item(screens[name])


# *** Temporary Code to Check Program Function ***

# Callback function to print "user_data: "
# and the user_data sent to the function:

def callback(sender, app_data, user_data):
    # TODO: Add a docstring to function callback()
    '''Docstring'''

    print(f"user_data: {user_data}")


def temp():
    with dpg.window(label="Main"):
        # Initialize some data to send to callback function:
        data = "From 'Main' window, button 'Push!'"

        # Add some text above the button (to be removed or later changed):
        dpg.add_text("Push the button!")

        # Add a button with the label "Push!", value as data,
        # and callback the callback function:
        dpg.add_button(label="Push!", user_data=data, callback=callback)


# *** Welcome Screen ***
# TODO: Create a function to create the Welcome Screen


# *** Main Menu ***
# TODO: Create a function to create the Main Menu
# (choice between Regular and Average modes)


# *** Regular Mode ***
# Create functions that create the Regular Mode gameplay:

# Create the main Regular Mode window with checkboxes, sliders, and a button:
def create_regular():
    # TODO: Add a docstring to function create_regular()
    """Docstring"""

    # Within a window "Regular Mode":
    with dpg.window(label="Regular Mode", tag="regular_mode", show=False):
        # Add instructions for the game:
        dpg.add_text("Please select whichever dice you would like to roll. "
            "(Multiple sections allowed and encouraged.)")
        dpg.add_spacer(label="Instruction Spacer - R", tag="instruction_spacer_r")
        dpg.add_text("After you've selected which dice you'd like, "
            "please select whether you'd like 1 to 5 of each dice chosen.")

        # Loop through the list dice_names to
        # dynamically set the tag for each checkbox and slider:
        for name in dice_names:
            # Add each checkbox and slider tags in their dictionaries:
            r_dice_boxes[name] = f"{name}_box"
            r_dice_sliders[name] = f"{name}_slider"

            # Create the tags for the boxes and sliders:
            boxtag = r_dice_boxes[name]
            slidetag = r_dice_sliders[name]

            # Create a horizontal group to house each checkbox and slider:
            with dpg.group(horizontal=True):
                # Add checkbox and use a lambda function
                # to toggle each slider to only open

                # Add each box tax and slider tag to their dictionaries:
                boxtag = r_dice_boxes[name]
                slidetag = r_dice_sliders[name]

                # Add a checkbox with a slider that's only visible when checked:
                dpg.add_checkbox(label=name, tag=boxtag, callback=toggle_slide, user_data=name)
                dpg.add_slider_int(tag=slidetag, default_value=1, min_value=1, max_value=5, width= 200)
                dpg.hide_item(slidetag)

        # TODO: Create callback for "Roll My Dice!" button to gather data and display it on the next screen
         # Add the button to process the information:
        dpg.add_button(label="Roll My Dice!", callback=callback, user_data="😊")
        # Map the screen name in the dictionary screens:
        screens["regular_mode"] = "regular_mode"


# Create function to toggle the sliders when boxes are checked:
def toggle_slide(sender, app_data, user_data):
    # TODO: Create docstring for function toggle_slide()
    """Docstring"""

    # Check if user_data returns None, and if so, raise an Exception:
    if user_data is None:
        raise Exception("'user_data' is None")

    # Check if the checkbox is checked:
    else:
        if dpg.get_value(r_dice_boxes[user_data]):
            # If the box is checked, show the slider:
            dpg.show_item(r_dice_sliders[user_data])

        else:
            # If the box is unchecked, hide the slider:
            dpg.hide_item(r_dice_sliders[user_data])


# TODO: Create function to gather results of choosing dice


# TODO: Create function to show Regular Mode results


# *** Average Mode ***
# TODO: Create functions that create the Average Mode gameplay


# *** Footer ***
# TODO: Create function to add a footer to house the "Back" button


# *** Setup and Run ***
# TODO: Make sure app runs


# FIXME: Continue to add screens to this as they are built
# Create function that starts each screen:
def program_setup():
    create_regular()
    show("regular_mode")


program_setup()

# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
