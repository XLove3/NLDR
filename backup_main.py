# Import DearPyGui and the Random module:
import dearpygui.dearpygui as dpg, random as rd


# *** Global Variables ***

# The Neat Little Dice Game will be set up into a dictionary of "screens":
screens = {}

# Set up the names for the dice (and the numerical value of their sides):
dice_names = {
    "Two": 2,
    "Four": 4,
    "Six": 6,
    "Ten": 10,
    "Twelve": 12,
    "Twenty": 20,
    "One Hundred": 100
    }

# Regular Mode states (checkboxes, sliders, and selected items):
r_dice_boxes = {}
r_dice_sliders = {}
r_selected_items = {}

# Average Mode states (checkboxes, sliders, and selected items):
a_dice_boxes = {}
a_dice_sliders = {}
a_selected_items = {}
a_rolls = 1


# *** Starting Setup ***

# Create context and viewport, and setup DearPyGui:
dpg.create_context()
dpg.create_viewport(title='Neat Little Dice Roller')
dpg.setup_dearpygui()


# *** Beginning Function(s): ***

# Show screen according to name of screen:
def show(name):
    # TODO: Add a docstring to function show()
    '''Docstring'''

    if name in screens:

        # Loop through the values in the dictionary screens and hide each item:
        for screen in screens.values():
            
            dpg.hide_item(screen)

        # Show the screen with the name from the argument name:
        dpg.show_item(screens[name])

    else:
        
        print(name)


# *** Welcome Screen ***
# TODO: Create a function to create the Welcome Screen
# Start the game here. Back to Welcome Screen 
# button routes back here.

# Create the screen to start the game:
def create_welcome():
    pass


# *** Main Menu ***
# (choice between Regular and Average modes)

# Create the screen to choose mode:
def create_menu():
    # TODO: Add a docstring to function create_menu()
    '''Docstring'''

    # Within a window "Main Menu":
    with dpg.window(label="Main Menu", tag="main_menu", show=False):
        # Add title/instruction:
        dpg.add_text(
            "Please choose which mode you would "
            "like to play.", color=[255, 102, 0])
        dpg.add_separator()

        # Within a horizontal group:
        with dpg.group(horizontal=True):
            with dpg.group(width=500):
                # Add text to describe Regular Mode:
                dpg.add_spacer()
                dpg.add_text("Regular Mode:", color=[0, 255, 255])
                dpg.add_text(
                    "Regular Mode allows you to choose "
                    "from 7 different-sided dice. "
                    "Then you choose how many of those "
                    "dice you'd like. Roll the dice, "
                    "and you'll get the results of "
                    "each dice chosen.",
                    wrap=450
                    )

                dpg.add_spacer()
                dpg.add_spacer()

                # Add the button to lead to Regular Mode:
                dpg.add_button(
                    label="Play Regular Mode",
                    tag="play_regular",
                    callback=lambda: show("regular_mode")
                    )

            with dpg.group(width=500):
                # Add text to describe Average Mode:
                dpg.add_spacer()
                dpg.add_text("Average Mode:", color=[0, 255, 255])
                dpg.add_text(
                    "Average Mode allows you to choose "
                    "from 7 different-sided dice. Then you "
                    "choose how many of those dice you'd like. "
                    "Choose the number of rolls you'd like all "
                    "of the dice to be rolled. We'll then "
                    "calculate the average of each dice over "
                    "all of your rolls.",
                    wrap=450
                    )

                dpg.add_spacer()
                dpg.add_spacer()

                # Add the button to lead to Average Mode:
                dpg.add_button(
                    label="Play Average Mode",
                    tag="play_average",
                    callback=lambda: show("average_mode")
                    )

        # Mop the screen name in the dictionary screens:
        screens["main_menu"] = "main_menu"


# *** Regular Mode ***

# Create function(s) that create the
# Regular Mode gameplay:

# Create the main Regular Mode window with checkboxes, 
# sliders, and a button:
def create_regular():
    # TODO: Add a docstring to function create_regular()
    '''Docstring'''

    # Clear the dictionaries r_dice_boxes and r_dice_sliders:
    r_dice_boxes.clear()
    r_dice_sliders.clear()

    # Within a window "Regular Mode":
    with dpg.window(
        label="Regular Mode",
        tag="regular_mode",
        show=False):
        # Add instructions for the game:
        dpg.add_text("Welcome to Regular Mode!", color=[255, 102, 0])
        dpg.add_separator()
        dpg.add_text(
            "Please select whichever dice you would like to roll. "
            "(Multiple sections allowed and encouraged!)"
            )
        dpg.add_spacer()
        dpg.add_text(
            "After you've selected which dice you'd like, "
            "please select whether you'd like 1 to 5 of each "
            "dice chosen.")

        dpg.add_separator()

        # Loop through the dictionary dice_names to
        # dynamically set the tag for each checkbox and slider:
        for name in dice_names:
            # Add each checkbox and slider tags in their dictionaries:
            if name != "One Hundred":
                r_dice_boxes[name] = f"{name}_box_r"
                r_dice_sliders[name] = f"{name}_slider_r"
            else:
                r_dice_boxes[name] = "one_hundred_box_r"
                r_dice_sliders[name] = "one_hundred_slider_r"

            # Create the tags for the boxes and sliders:
            r_boxtag = r_dice_boxes[name]
            r_slidetag = r_dice_sliders[name]

            # Create a horizontal group to house each checkbox and slider:
            with dpg.group(horizontal=True):
                # Add checkbox and use a callback toggle_slide
                # to toggle each slider:

                # Add a checkbox with a slider
                # that's only visible when checked:
                if not dpg.does_item_exist(r_boxtag):
                    dpg.add_checkbox(
                        label=name,
                        tag=r_boxtag,
                        callback=toggle_slide,
                        user_data=("regular", name)
                        )

                else:
                    dpg.show_item(r_boxtag)

                if not dpg.does_item_exist(r_slidetag):
                    dpg.add_slider_int(
                        tag=r_slidetag,
                        default_value=0,
                        min_value=0,
                        max_value=5,
                        width=200
                        )
                    dpg.hide_item(r_slidetag)

                else:
                    dpg.show_item(r_slidetag)

        dpg.add_spacer()
        dpg.add_separator()

        # Add the button to process the information:
        dpg.add_button(
            label="Roll My Dice!",
            tag="roll_button_r",
            callback=lambda: gather_dice("regular")
            )

        # Map the screen name in the dictionary screens:
        screens["regular_mode"] = "regular_mode"


# *** Average Mode ***

# Create the main Average Mode window with checkboxes, sliders, and a button:
def create_average():
    # TODO: Add a docstring to function create_average()
    '''Docstring'''

    # Clear the dictionaries a_dice_boxes and a_dice_sliders:
    a_dice_boxes.clear()
    a_dice_sliders.clear()

    # Within a window "Average Mode":
    with dpg.window(
        label="Average Mode",
        tag="average_mode",
        show=False):
        # Add instructions for the game:
        dpg.add_text("Welcome to Average Mode!", color=[255, 102, 0])
        dpg.add_separator()
        dpg.add_text(
            "Please select whichever dice you would like to roll. "
            "(Multiple sections allowed and encouraged!)"
            )
        dpg.add_spacer()
        dpg.add_text(
            "After you've selected which dice you'd like, "
            "please select whether you'd like 1 to 5 of each "
            "dice chosen.")

        dpg.add_separator()

        # Loop through the dictionary dice_names to
        # dynamically set the tag for each checkbox and slider:
        for name in dice_names:
            # Add each checkbox and slider tags in their dictionaries:
            if name != "One Hundred":
                a_dice_boxes[name] = f"{name}_box_a"
                a_dice_sliders[name] = f"{name}_slider_a"
            else:
                a_dice_boxes[name] = "one_hundred_box_a"
                a_dice_sliders[name] = "one_hundred_slider_a"

            # Create the tags for the boxes and sliders:
            a_boxtag = a_dice_boxes[name]
            a_slidetag = a_dice_sliders[name]

            # Create a horizontal group to house each checkbox and slider:
            with dpg.group(horizontal=True):
                # Add checkbox and use a callback toggle_slide
                # to toggle each slider:

                # Add a checkbox with a slider
                # that's only visible when checked:
                if not dpg.does_item_exist(a_boxtag):
                    dpg.add_checkbox(
                        label=name,
                        tag=a_boxtag,
                        callback=toggle_slide,
                        user_data=("average", name)
                        )

                else:
                    dpg.show_item(a_boxtag)

                if not dpg.does_item_exist(a_slidetag):
                    dpg.add_slider_int(
                        tag=a_slidetag,
                        default_value=0,
                        min_value=0,
                        max_value=5,
                        width=200
                        )
                    dpg.hide_item(a_slidetag)

                else:
                    dpg.show_item(a_slidetag)

        dpg.add_spacer()
        dpg.add_separator()

        # Add slider for picking how many rolls to average over:
        dpg.add_text(
            "Before you press the button, let me know how "
            "many times you'd like me to roll your dice for "
            "the Average."
            )
        dpg.add_slider_int(
            tag="avg_slider",
            default_value=a_rolls,
            min_value=1,
            max_value=1000,
            width=1000
            )

        # Set the value of avg_slider to global variable a_rolls:
        dpg.set_value("avg_slider", a_rolls)

        # Add a button to process the information:
        dpg.add_button(
            label="Roll My Dice!",
            tag="roll_button_a",
            callback=lambda: gather_dice("average")
            )

        # Map the screen name in the dictionary screens:
        screens["average_mode"] = "average_mode"

# *** Additional Functions ***

# Create functions to toggle sliders, gather the data, 
# calculate the totals and averages:

# Create function to toggle the sliders when boxes are checked:
def toggle_slide(sender, app_data, user_data):
    # TODO: Create docstring for function toggle_slide()
    '''Docstring'''

    # Separate user_data into mode and name:
    mode, name = user_data

    # Check if user_data returns None, and if so, raise an Exception:
    if name is None or mode is None:
        raise Exception(
            f"at least part of 'user_data' is "
            "None\nname: {name}\nmode: {mode}\nuser_data: "
            "{user_data}")

    else:
        # Add logic to determine which boxes and sliders to use:
        boxes = a_dice_boxes if mode == "average" else r_dice_boxes
        sliders = a_dice_sliders if mode == "average" else r_dice_sliders

        # Check if the checkbox is checked:
        if dpg.get_value(boxes[name]):
            # If the box is checked, show the slider:
            dpg.show_item(sliders[name])

        else:
            # If the box is unchecked, hide the slider:
            dpg.hide_item(sliders[name])


# Create function to gather results of choosing dice:
def gather_dice(mode):
    # TODO: Create docstring for function gather_reg()
    '''Docstring'''

    # Determine which mode the information comes from,
    # and set it to selected and sliders:
    selected = a_selected_items if mode == "average" else r_selected_items
    sliders = a_dice_sliders if mode == "average" else r_dice_sliders

    # Clear the appropriate dictionary:
    selected.clear()

    for name in dice_names:
        count = dpg.get_value(sliders[name])

        if count:
            count = dpg.get_value(sliders[name])
            selected[name] = count

    create_results(mode)


# Create function housing the logic for all modes,
# using the dice chosen in each mode's screen:
def create_results(mode):
    # TODO: Create a docstring for function create_results_reg():
    '''Docstring'''

    # Determine which mode and create their result screens with tag, label, title, and color:
    selected = r_selected_items if mode == "regular" else a_selected_items
    tag = "regular_result_screen" if mode == "regular" else "average_result_screen"
    label = "Regular Result(s) Screen" if mode == "regular" else "Average Result(s) Screen"
    title = "Regular Mode Results" if mode == "regular" else "Average Mode Results"
    color_main = [255, 102, 0]

    # Check if there is already a Result Screen, delete it if so:
    if dpg.does_item_exist("regular_result_screen"):
        dpg.delete_item("regular_result_screen")

    # Within a window display "Regular Result(s) Screen" or "Average Result(s) Screen":
    with dpg.window(label=label, tag=tag, show=False):
        # Add some text:
        dpg.add_text(title, color=color_main)

        # Initialize variable to track total:
        total = 0

        # Initialize variable to hold all values:
        all_values = []

        # Loop through the items in r_selected_items with name and count:
        for name, count in selected.items():
            # Initialize a variable to hold the number of sides:
            sides = dice_names[name]

            # Loop through a range of 1 to count+1:
            for i in range(1, int(count) + 1):
                # Create the label for each item:
                label = f"{name} {i}"

                # If in "regular" mode, get a random number from 1 to sides,
                # then increase total by value:
                if mode == "regular":
                    value = rd.randint(1, sides)
                    total += value

                    # Create a group for each result and it's spacer:
                    with dpg.group():
                        dpg.add_text(f"{label}: {value}")
                        dpg.add_spacer()

                else:
                    # Get the value of the "avg_slider":
                    rolls = dpg.get_value("avg_slider")

                    # FIXME: Add a comment about what this does:
                    value = [rd.randint(1, sides) for _ in range(rolls)]

                    # Create variable avg. It's the sum of
                    # value divided by rolls:
                    avg = sum(value) / rolls

                    # Append avg to the end of list all_values:
                    all_values.append(avg)

                    # Create a group for each average result and it's spacer:
                    with dpg.group():
                        dpg.add_text(f"{label}: {avg: .2f}")
                        dpg.add_spacer()

        dpg.add_spacer()
        dpg.add_separator()

        if mode == "regular":
            # Add text to label "Total Value of All Your Dice: "
            dpg.add_text("Total Value of All of Your Dice: ", color=[37, 206, 65])

            # Add text to show the total:
            dpg.add_text(f"{total}", color=[51, 255, 51])

        else:
            # Take the sum of all_values divided by rolls
            # for the average total:
            rolls = dpg.get_value("avg_slider")

            # If rolls == 0, raise an exception as we cannot divide by zero:
            if rolls == 0:
                raise Exception(
                    "Please roll at least one time, or we "
                    "cannot calculate your average!!"
                    )

            # Otherwise, display the average:
            else:
                avg_total = (sum(all_values)) / rolls

                # Add text to label "Average Of All Dice,
                # After Rolling {rolls} times: "
                dpg.add_text(
                    "Average Of All Dice, After Rolling "
                    f"{rolls} times: ", color=[51, 255, 51]
                    )

                # Add text to show the total average:
                dpg.add_text(f"{avg_total: .2f}", color=[51, 255, 51])

    # Map the screen name in the dictionary screens:
    screens[tag] = tag
    show(tag)


# *** Footer ***
# TODO: Create function to add a footer to house the "Back" button


# *** Setup and Run ***
# TODO: Make sure app runs


# FIXME: Continue to add screens to this as they are built
# Create function that starts each screen:
def program_setup():
    create_menu()
    create_regular()
    create_average()
    show("main_menu")


# Run the program that initializes each screen (and functions):
program_setup()

# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
