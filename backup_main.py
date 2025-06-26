# Import DearPyGui and the Random module:
import dearpygui.dearpygui as dpg, random as rd


# *** Global Variables: ***

# The Neat Little Dice Game will be set up into a dictionary of "screens":
screens = {}

# Set up the names for the dice (and the numerical value of their sides):
dice_names = {"Two": 2, "Four": 4, "Six": 6, "Ten": 10, "Twelve": 12, "Twenty": 20, "One Hundred": 100}

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
        for name, num in dice_names.items():
            # Add each checkbox and slider tags in their dictionaries:
            if name != "One Hundred":
                r_dice_boxes[name] = f"{name}_box"
                r_dice_sliders[name] = f"{name}_slider"
            else:
                r_dice_boxes[name] = "One_hundred_box"
                r_dice_sliders[name] = "One_hundred_slider"

            # Create the tags for the boxes and sliders:
            boxtag = r_dice_boxes[name]
            slidetag = r_dice_sliders[name]

            # Create a horizontal group to house each checkbox and slider:
            with dpg.group(horizontal=True):
                # Add checkbox and use a lambda function
                # to toggle each slider to only open

                # Add each box tax and slider tag to their dictionaries:
                #boxtag = r_dice_boxes[num]
                #slidetag = r_dice_sliders[name]

                # Add a checkbox with a slider that's only visible when checked:
                dpg.add_checkbox(label=name, tag=boxtag, callback=toggle_slide, user_data=name)
                dpg.add_slider_int(tag=slidetag, default_value=0, min_value=0, max_value=5, width= 200)
                dpg.hide_item(slidetag)

        # TODO: Create callback for "Roll My Dice!" button to gather data and display it on the next screen
        # Add the button to process the information:

        dpg.add_button(label="Roll My Dice!", callback=gather_reg)
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


# TODO: Create function to gather the data represented in Regular Mode
# Create function to gather results of choosing dice:
def gather_reg():
    # TODO: Create docstring for function gather_reg()
    '''Docstring'''

    r_selected_items.clear()

    for name, num in dice_names.items():
        if dpg.get_value(r_dice_sliders[name]):
            count = dpg.get_value(r_dice_sliders[name])
            print("count - gather_reg: ", count)
            r_selected_items[name] = count
    create_results_reg()


# TODO: Create the function for the Regular Mode logic
# Create function housing the logic for Regular Mode 
# using the dice chosen in Regular Mode screen:
def create_results_reg():
    # TODO: Create a docstring for function create_results_reg():
    '''Docstring'''

    # Check if there is already a Result Screen, delete it if so:
    if dpg.does_item_exist("regular_result_screen"):
        dpg.delete_item("regular_result_screen")

    # Within a window "Results Screen":
    with dpg.window(label="Regular Result Screen", tag="regular_result_screen", show=False):
        # Add some text:
        dpg.add_text("⭐⭐⭐ Results ⭐⭐⭐")
        dpg.add_text("Regular Mode")

        # Initialize variable to track total:
        total = 0
        
        # Loop through the items in r_selected_items with name and count:
        for name, count in r_selected_items.items():
            # Loop through a range of 1 to count+1:
            for i in range(1, int(count) + 1):
                # Create the label for each item:
                label = f"{name}_{i}"
                # Get a random number from 1 to {number of dice sides}:
                value = rd.randint(1, dice_names[name])
                total += value
                
                # Create a group:
                with dpg.group():
                    dpg.add_text(f"{label}: {value}")
        
        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_text(f"Total Value of All the Dice: {total}", color=[0, 200, 255])
        
    screens["regular_result_screen"] = 'regular_result_screen'
    show("regular_result_screen")


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
    create_results_reg()
    show("regular_mode")


# Run the program that initializes each screen (and functions):
program_setup()

# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
