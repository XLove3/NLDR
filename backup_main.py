# Import DearPyGui and the Random module:
import dearpygui.dearpygui as dpg, random as rd


# TODO: Show the list of every roll in Average when it or a button is clicked on

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

# TODO: Maybe turn this part into a dictionary: {"label_color": "[#, #, #]"}
# Colors and stuff:
instruction_color = [102, 178, 255]
tip_color = [160, 160, 160]
title_color = [255, 102, 0]
main_header_color = [0, 255, 255]
sep_color = [144, 30, 2]
total_text_color = [37, 206, 65]
total_color = [51, 255, 51]

# *** Starting Setup ***

# Create context and viewport, and setup DearPyGui:
dpg.create_context()
dpg.create_viewport(title='Neat Little Dice Roller')
dpg.setup_dearpygui()


# *** Beginning Function(s): ***

# Show screen according to name of screen:
def show_screen(name):
    # TODO: Add a docstring to function show_screen()
    '''Docstring'''

    if name in screens:

        # Loop through the values in the dictionary screens and hide each item:
        for screen in screens.values():
            dpg.hide_item(screen)

        # Show the screen with the name from the argument name:
        dpg.show_item(screens[name])

    else:
        raise Exception(f"screen '{name}' was not found.")
        # TODO: Change to try-except and show a popup with the text, and program does not progress, maybe show the screen again? 


# *** Welcome Screen ***

# Create the screen to start the game:
def create_welcome():
    # TODO: Add a docstring to function create_welcome()
    '''Docstring'''

    # Within a window "Welcome":
    with dpg.window(
        label="Welcome",
        tag="welcome",
        show=False
        ):

        # Add Title:
        dpg.add_text("Neat Little Dice Roller", color=title_color)
        dpg.add_separator()

        # Explain the game:
        dpg.add_text("Welcome to the Neat Little Dice Roller!")
        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_text(
            "--> Pick from 7 different-sided dice "
            "(2, 4, 6, 10, 12, 20, and 100).",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_text(
            "--> After you choose which dice you'd like "
            "to roll, pick how many of each die you'd "
            "like to roll (up to 5).",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_text(
            "--> If you choose Regular Mode, Roll the "
            "Dice! and you'll receive the result of "
            "each die's roll, as well as the total "
            "from all the dice rolled.",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_text(
            "--> If you choose Average Mode, you'll "
            "also choose how many times to roll the "
            "dice. (1 - 5,000)",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_text(
            "--> Roll the Dice! and receive the average "
            "of each dice rolled that many times. "
            "You'll also get the average of all rolls "
            "across all dice chosen.",
            color=instruction_color
            )

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_separator()

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_text("*****  Are you ready to play the game?  *****")
        dpg.add_spacer()
        dpg.add_spacer()

        # TODO: Create a comment for button "play"
        #
        dpg.add_button(
            label="Play the Neat Little Dice Game!",
            tag="play",
            callback=lambda: show_screen("main_menu")
        )

    # Map the screen name in the dictionary screens:
    screens["welcome"] = "welcome"


# *** Main Menu ***

# Create the screen to choose mode:
def create_menu():
    # TODO: Add a docstring to function create_menu()
    '''Docstring'''

    # Within a window "Main Menu":
    with dpg.window(
        label="Main Menu",
        tag="main_menu",
        show=False
        ):

        # Add title/instruction:
        dpg.add_text("Main Menu:", color=title_color)
        dpg.add_text(
            "Please choose which mode you would "
            "like to play.", 
            color=instruction_color
            )
        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

        # Within a horizontal group:
        with dpg.group(horizontal=True):

            # TODO: Create a comment about group
            #
            with dpg.group(width=500):

                # Add text to describe Regular Mode:
                dpg.add_spacer()
                dpg.add_text("Regular Mode:", color=main_header_color)
                dpg.add_spacer()

                dpg.add_text(
                    "Regular Mode allows you to choose "
                    "from 7 different-sided dice. "
                    "Then you choose how many of those "
                    "dice you'd like. Roll the dice, "
                    "and you'll get the results of "
                    "each dice chosen.",
                    wrap=450,
                    color=instruction_color
                    )

                dpg.add_spacer()
                dpg.add_spacer()

                # Add the button to lead to Regular Mode:
                dpg.add_button(
                    label="Play Regular Mode",
                    tag="play_regular",
                    callback=lambda: show_screen("regular_mode")
                    )

            with dpg.group(width=500):

                # Add text to describe Average Mode:
                dpg.add_spacer()
                dpg.add_text("Average Mode:", color=main_header_color)
                dpg.add_spacer()

                dpg.add_text(
                    "Average Mode allows you to choose "
                    "from 7 different-sided dice. Then you "
                    "choose how many of those dice you'd like. "
                    "Choose the number of rolls you'd like all "
                    "of the dice to be rolled. We'll then "
                    "calculate the average of each dice over "
                    "all of your rolls.",
                    wrap=450,
                    color=instruction_color
                    )

                dpg.add_spacer()
                dpg.add_spacer()

                # Add the button to lead to Average Mode:
                dpg.add_button(
                    label="Play Average Mode",
                    tag="play_average",
                    callback=lambda: show_screen("average_mode")
                    )

        # Call footer() with parent = "main_menu":

        # Map the screen name in the dictionary screens:
        screens["main_menu"] = "main_menu"


# *** Regular Mode ***

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
        show=False
        ):

        # Add instructions for the game:
        dpg.add_text("Welcome to Regular Mode!", color=title_color)
        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

        dpg.add_text(
            "Please select whichever dice you would like to roll. "
            "(Multiple sections allowed and encouraged!)",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_text(
            "After you've selected which dice you'd like, "
            "please select whether you'd like 1 to 5 of each "
            "dice chosen.",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_separator()
        dpg.add_spacer()

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
                    dpg.add_spacer()

                else:
                    # If the checkbox already exists, show it:
                    dpg.show_item(r_boxtag)

                # If an r_slidetag does not exist, add it:
                if not dpg.does_item_exist(r_slidetag):
                    dpg.add_slider_int(
                        tag=r_slidetag,
                        min_value=1,
                        max_value=10,
                        width=200
                    )
                    dpg.add_spacer()
                    dpg.hide_item(r_slidetag)

                # If the r_slidetag item exists, show it:
                else:
                    dpg.show_item(r_slidetag)

        dpg.add_spacer()
        dpg.add_separator()

        # Add the button to process the information:
        dpg.add_spacer()
        dpg.add_button(
            label="Roll My Dice!",
            tag="roll_button_r",
            callback=lambda: gather_dice("regular")
            )

        # Call footer() with parent = "main_menu":

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
        show=False
    ):

        # Add instructions for the game:
        dpg.add_text("Welcome to Average Mode!", color=title_color)
        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

        dpg.add_text(
            "Please select whichever dice you would like to roll. "
            "(Multiple sections allowed and encouraged!)",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_text(
            "After you've selected which dice you'd like, "
            "please select whether you'd like 1 to 5 of each "
            "dice chosen.",
            color=instruction_color
            )
        dpg.add_spacer()

        dpg.add_separator()
        dpg.add_spacer()

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
                    dpg.add_spacer()

                # If the item already exists, show it:
                else:
                    dpg.show_item(a_boxtag)

                # If an a_slidetag does not exist, add it:
                if not dpg.does_item_exist(a_slidetag):
                    dpg.add_slider_int(
                        tag=a_slidetag,
                        min_value=1,
                        max_value=10,
                        width=200
                        )
                    dpg.add_spacer()
                    dpg.hide_item(a_slidetag)

                # If the a_slidetag item exists, show it:
                else:
                    dpg.show_item(a_slidetag)

        dpg.add_spacer()
        dpg.add_separator()

        # Add slider for picking how many rolls to average over:
        dpg.add_spacer()
        dpg.add_text(
            "Before you press the button, let me know how "
            "many times you'd like me to roll your dice for "
            "the Average."
            )
        dpg.add_text(
            "If you would like to directly "
            "enter the number, please "
            "ctrl+click (command+click on "
            "macOS)",
            color=tip_color
            )
        dpg.add_spacer()

        # TODO: Add a comment to add_slider_int()
        #
        dpg.add_slider_int(
            label="Avg Input",
            tag="avg_input",
            default_value=1,
            min_value=1,
            max_value=5000,
            width=1000,
            height=15,
            no_input=False,
            clamped=True,
            format="%d",
            callback=change_a_rolls
            )

        # Add a button to process the information:
        dpg.add_spacer()
        dpg.add_button(
            label=f"Roll My Dice {a_rolls} times!",
            tag="roll_button_a",
            callback=lambda: gather_dice("average")
            )

        # Call footer() with parent = "main_menu":

        # Map the screen name in the dictionary screens:
        screens["average_mode"] = "average_mode"


# *** Additional Functions ***

# Create function to toggle the sliders when boxes are checked:
def toggle_slide(sender, app_data, user_data):
    # TODO: Create docstring for function toggle_slide()
    '''Docstring'''

    # Separate user_data into mode and name:
    mode, name = user_data

    # Check if user_data returns None, and if so, raise an Exception:
    if name is None or mode is None:
        raise Exception(
            "At least part of 'user_data' is "
            f"None\nname: {name}\nmode: {mode}\nuser_data: "
            f"{user_data}")
        # TODO: Change this to a try-except?

    else:
        # Add logic to determine which boxes and sliders to use:
        boxes = a_dice_boxes if mode == "average" else r_dice_boxes
        sliders = a_dice_sliders if mode == "average" else r_dice_sliders

        # Check if the checkbox is checked:
        if dpg.get_value(boxes[name]):
            # If the box is checked, set the slider's default to 1:
            dpg.set_value(sliders[name], 1)
            # If the box is checked, show the slider:
            dpg.show_item(sliders[name])

        else:
            # If the box is unchecked, set the slider's default to 0:
            dpg.set_value(sliders[name], 0)
            # If the box is unchecked, hide the slider:
            dpg.hide_item(sliders[name])


# Create a helper function to set the value of a_rolls in create_avg():
def change_a_rolls(sender, app_data, user_data):
    # TODO: Create a docstring for function avg_button_callback()
    '''Docstring'''

    # Declare global a_rolls to be able to modify the variable:
    global a_rolls

    # Set a_rolls to equal app_data:
    a_rolls = app_data

    # Set the label to roll as "Roll My Dice {#-of-rolls} times!"
    dpg.set_item_label("roll_button_a", f"Roll My Dice {a_rolls} times!")


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

    # For each dice, set the slider's value to count:
    for name in dice_names:
        count = dpg.get_value(sliders[name])

        # If count is found, set count to the slider's value,
        # and add it to appropriate dictionary as {name: count}:
        if count:
            count = dpg.get_value(sliders[name])
            selected[name] = count

    # After gathering all of the dice, call create_results(mode)
    # to create the results screen:
    create_results(mode)


# Create function housing the logic for all modes,
# using the dice chosen in each mode's screen:
def create_results(mode):
    # TODO: Create a docstring for function create_results_reg():
    '''Docstring'''

    # Determine which mode and create their result screens
    # with tag, label, title, and color:
    selected = r_selected_items if mode == "regular" else a_selected_items
    tag = "regular_result_screen" if mode == "regular" else "average_result_screen"
    label = "Regular Result(s) Screen" if mode == "regular" else "Average Result(s) Screen"
    title = "Regular Mode Results" if mode == "regular" else f"Average Mode Results Over {a_rolls} Rolls"
    line = "__________________________"

    # Check if there is already a Result Screen, delete it if so:
    if dpg.does_item_exist(tag):
        dpg.delete_item(tag)

    # Within a window display "Regular Result(s) Screen"
    # or "Average Result(s) Screen":
    with dpg.window(
        label=label,
        tag=tag,
        show=False
        ):

        # Add the title of the screen:
        dpg.add_text(title, color=title_color)
        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

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

                # If in "regular" mode, get a random number from
                # 1 to sides, then increase total by value:
                if mode == "regular":
                    value = rd.randint(1, sides)
                    total += value

                    # If there were more than one item selected:
                    if len(selected) > 1:
                        # Create a group for each result:
                        with dpg.group():

                            dpg.add_spacer()
                            dpg.add_text(f"{label}: {value}")
                            dpg.add_spacer(height=10)
                            dpg.add_text(
                                line,                    color=sep_color)
                        dpg.add_spacer(height=10)

                    # If there was only one item selected:
                    elif len(selected) == 1:
                        with dpg.group():
                            dpg.add_spacer()
                            dpg.add_text(f"{label}: {value}")
                        dpg.add_spacer()

                    else:
                        raise Exception("Please select at least one dice to play.")
                    # TODO: Change this to try-except

                else:
                    # For [a_rolls] times, generate a random
                    # integer between 1 and sides and store
                    # in a list:
                    value_list = [rd.randint(1, sides) for _ in range(a_rolls)]
                    value_sum = sum(value_list)

                    # Add value_sum to total:
                    total += value_sum

                    # Create variable avg. It's the sum of
                    # value_sum divided by a_rolls:
                    avg = value_sum / a_rolls

                    # Append avg to the end of list all_values:
                    all_values.append(avg)

                    # If more than one item was selected:
                    if len(selected) > 1:
                        # Create a group for each average result:
                        with dpg.group():

                            dpg.add_spacer()
                            dpg.add_text(f"{label}: {avg: .2f}")
                            dpg.add_spacer(height=10)
                            dpg.add_text(
                                line,
                                color=sep_color)
                            dpg.add_spacer(height=10)

                    elif len(selected) == 1:
                        with dpg.group():
                            dpg.add_spacer()
                            dpg.add_text(f"{label}: {avg}")
                        dpg.add_spacer()

                    else:
                        raise Exception("Please select at least one dice to play.")
                        # TODO: Change this to try-except
                    dpg.add_spacer()

        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

        if mode == "regular":
            # Add text to label "Total Value of All 
            # Your Dice: "
            dpg.add_text("Total Value of All of Your Dice: ", color=total_text_color)
            dpg.add_spacer()

            # Add text to show the total:
            dpg.add_text(f"{total}", color=total_color)

        else:
            # If a_rolls == 0, raise an exception as we cannot divide by zero:
            if a_rolls == 0:
                raise Exception(
                    "Please roll at least one time, or we "
                    "cannot calculate your average!!"
                    )

            # TODO: Create a comment for elif a_rolls is None
            #
            elif a_rolls is None:
                raise Exception("a_rolls == None")
            # TODO: Can I change this to Try Except? Maybe just put a popup here?

            # Otherwise, display the average:
            else:
                # TODO: Create a comment for avg_total
                #
                avg_total = (sum(all_values)) / a_rolls

                # Add text to label "Average Of All Dice,
                # After Rolling {a_rolls} times: "
                dpg.add_text(
                    "Average Of All Dice, After Rolling "
                    f"{a_rolls} times: ", color=total_text_color
                    )
                dpg.add_spacer()

                # Add text to show the total average:
                dpg.add_text(f"{avg_total: .2f}", color=total_color)

    # Call footer() with parent = "regular_mode"
    # or parent = "average_mode":


    # Map the screen name in the dictionary screens:
    screens[tag] = tag
    show_screen(tag)


# *** Footer ***
# TODO: Create function to add a footer to house the "Back" button

# Add a footer to every screen:
def footer(parent):
    print("footer")
    pass
    # With a group that uses parent:


        # Add text "Go Back to Welcome Screen":


        # Add button to return to Welcome screen:



# *** Setup and Run ***

# FIXME: Continue to add screens to this as they are built
# Create function that starts each screen:
def program_setup():
    create_welcome()
    create_menu()
    create_regular()
    create_average()
    show_screen("welcome")


# Run the program that initializes each screen (and functions):
program_setup()

# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
