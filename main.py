# Import DearPyGui and the Random module:
import dearpygui.dearpygui as dpg, random as rd

# *** Global Variables: ***

# NLDR will be set up into a dictionary of "screens":
screens = {}
# Set up the names for the dice:
dice_names = ["Two", "Four", "Six", "Ten", "Twelve", "Twenty", "One_Hundred"]

# Regular Mode states (checkboxes, sliders, and selected items):
r_dice_boxes = {}
r_dice_sliders = {}
r_selected_items = {}

# Average Mode states (checkboxes, sliders, and selected items):
a_dice_boxes = {}
a_dice_sliders = {}
a_selected_items = {}

# *** Starting Setup ***

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
# TODO: Create functions that create the Regular Mode gameplay


# *** Average Mode ***
# TODO: Create functions that create the Average Mode gameplay


# *** Setup and Run ***
# TODO: Make sure app runs

# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
