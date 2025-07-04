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

# Color variables:
instruction_color = [102, 178, 255]
tip_color = [160, 160, 160]
title_color = [255, 102, 0]
main_header_color = [0, 255, 255]
sep_color = [144, 30, 2]
total_text_color = [37, 206, 65]
total_color = [51, 255, 51]
back_color = [226, 226, 13]


# *** Starting Setup ***

# Create context and viewport, and setup DearPyGui:
dpg.create_context()
dpg.create_viewport(title='Neat Little Dice Roller')
dpg.setup_dearpygui()


# *** Beginning Functions: ***

# Create the screen each time the screen is visited:
def create_screen(tag, create_func, show=False):
    '''Creates a given screen new every time it is visited.

    Parameters
    -----------
    tag : str
        The tag of the screen to be created.
    create_func : function
        The function you wish to use to create the screen.
    to create the screen.
    show : bool : default = False
        If set to True, will automatically show the
        screen being created.
    '''

    # Delete the existing screen if it exists:
    if dpg.does_item_exist(tag):

        dpg.delete_item(tag)

    # Call the function passed as create_func:
    create_func()

    # Show the screen if applicable:
    if show:

        show_screen(tag)


# Show screen according to name of screen:
def show_screen(name):
    '''Shows the given screen in the viewport.

    Parameters:
    -----------
    name : str
        The name of ths screen to be displayed.
    '''

    if name in screens:

        # Loop through the values in the dictionary screens and hide each item:
        for screen in screens.values():
            dpg.hide_item(screen)

        # Show the screen with the name from the argument name:
        dpg.show_item(screens[name])

    else:
        raise Exception(f"screen '{name}' was not found.")


# *** Welcome Screen ***

# Create the screen to start the game:
def create_welcome():
    '''Creates the Welcome screen.

    Includes game information, and a button to progress to
    the rest of the game.

    Parameters
    -----------
    none
    '''

    # Within a window "Welcome":
    with dpg.window(
        label="Welcome",
        tag="welcome",
        show=False,
        width=850
    ):

        # Add Title:
        dpg.add_text("Neat Little Dice Roller", color=title_color)

        dpg.add_separator()

        # Explain the game:
        dpg.add_text("Welcome to the Neat Little Dice Roller!")

        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_text(
            "--> Pick from 7 different-sided dice "
            "(2, 4, 6, 10, 12, 20, and 100).",
            color=instruction_color
        )

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_text(
            "--> After you choose which dice you'd like "
            "to roll, pick how many of each die you'd "
            "like to roll (up to 5).",
            color=instruction_color
        )

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_text(
            "--> If you choose Regular Mode, Roll the "
            "Dice! and you'll receive the result of "
            "each die's roll, as well as the total "
            "from all the dice rolled.",
            color=instruction_color
        )

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_text(
            "--> If you choose Average Mode, you'll "
            "also choose how many times to roll the "
            "dice. (1 - 5,000)",
            color=instruction_color
        )

        dpg.add_spacer()
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

        dpg.add_text(
            "*****  Are you ready to play the game?  *****"
        )

        dpg.add_spacer()
        dpg.add_spacer()

        # Add a button that progresses the game to Main Menu:
        dpg.add_button(
            label="Play the Neat Little Dice Game!",
            tag="play",
            callback=lambda: show_screen("main_menu")
        )

        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()

    # Map the screen name in the dictionary screens:
    screens["welcome"] = "welcome"


# *** Main Menu ***

# Create the screen to choose mode:
def create_menu():
    '''Creates the Main Menu screen.

    Includes information on each mode, and a button to progress
    to each mode available.

    Parameters
    -----------
    none
    '''

    # Within a window "Main Menu":
    with dpg.window(
        label="Main Menu",
        tag="main_menu",
        show=False,
        width=850
    ):

        # Add title/instruction:
        dpg.add_text(
            "Main Menu:",
            color=title_color
        )

        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

        dpg.add_text(
            "Please choose which mode you would "
            "like to play.",
            color=instruction_color
        )

        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()
        dpg.add_spacer()

        # Within a horizontal group:
        with dpg.group(horizontal=True):

            dpg.add_spacer()
            dpg.add_spacer()
            dpg.add_spacer()

            # Create a group to hold Regular Mode text and button:
            with dpg.group(width=375):

                dpg.add_spacer()
                dpg.add_spacer()

                # Add text to describe Regular Mode:
                dpg.add_text(
                    "Regular Mode:",
                    color=main_header_color
                )

                dpg.add_spacer()

                dpg.add_text(
                    "Regular Mode allows you to choose "
                    "from 7 different-sided dice. "
                    "Then you choose how many of those "
                    "dice you'd like. Roll the dice, "
                    "and you'll get the results of "
                    "each dice chosen.",
                    wrap=325,
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

                dpg.add_spacer()
                dpg.add_spacer()
                dpg.add_spacer()

            # Add space between the Regular Mode and Average Mode groups:
            dpg.add_spacer(width=25)

            # Create a group to hold Average Mode text and button:
            with dpg.group(width=375):

                dpg.add_spacer()
                dpg.add_spacer()

                # Add text to describe Average Mode:
                dpg.add_text(
                    "Average Mode:",
                    color=main_header_color
                )

                dpg.add_spacer()

                dpg.add_text(
                    "Average Mode allows you to choose "
                    "from 7 different-sided dice. Then you "
                    "choose how many of those dice you'd like. "
                    "Choose the number of rolls you'd like all "
                    "of the dice to be rolled. We'll then "
                    "calculate the average of each dice over "
                    "all of your rolls.",
                    wrap=325,
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

                dpg.add_spacer()
                dpg.add_spacer()
                dpg.add_spacer()
                dpg.add_spacer()

        # Call footer() with parent = "main_menu":
        if dpg.does_item_exist("main_menu"):

            footer("main_menu")

        # Map the screen name in the dictionary screens:
        screens["main_menu"] = "main_menu"


# *** Regular Mode ***

# Create the main Regular Mode window with checkboxes,
# sliders, and a button:
def create_regular():
    '''Create the Regular Mode gameplay screen.

    Includes a checkbox for each kind of dice, and a slider
    only visible when checked to choose how many of each
    kind of dice.

    Parameters
    ----------
    none
    '''

    # Clear the dictionaries r_dice_boxes and r_dice_sliders:
    r_dice_boxes.clear()
    r_dice_sliders.clear()

    # If any tags still exist, set their value to zero and hide them:
    for tag in r_dice_sliders.values():

        if dpg.does_item_exist(tag):

            dpg.set_value(tag, 0)
            dpg.hide_item(tag)

    # Within a window "Regular Mode":
    with dpg.window(
        label="Regular Mode",
        tag="regular_mode",
        show=False,
        width=850
    ):

        # Add instructions for the game:
        dpg.add_text(
            "Welcome to Regular Mode!",
            color=title_color
        )

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
            "please select whether you'd like 1 to 10 of each "
            "dice chosen.",
            color=instruction_color
        )

        dpg.add_spacer()

        dpg.add_separator()

        dpg.add_spacer()

        # Loop through the dictionary dice_names to
        # dynamically set the tag for each checkbox and slider:
        for name in dice_names:

            # Add each checkbox and slider tags
            # in their respective dictionaries:
            r_boxtag = (
                f"{name}_box_r"
                if name != "One Hundred"
                else "one_hundred_box_r"
            )
            r_slidetag = (
                f"{name}_slider_r"
                if name != "One Hundred"
                else "one_hundred_slider_r"
            )

            # Create the tags for the boxes and sliders:
            r_dice_boxes[name] = r_boxtag
            r_dice_sliders[name] = r_slidetag

            # Delete any existing r_boxtag:
            if dpg.does_item_exist(r_boxtag):

                dpg.delete_item(r_boxtag)

            # Delete any existing r_slidetag:
            if dpg.does_item_exist(r_slidetag):

                dpg.delete_item(r_boxtag)

            # Create a horizontal group to house each checkbox and slider:
            with dpg.group(horizontal=True):
                # Add checkbox and use a callback toggle_slide
                # to toggle each slider next to its box:

                # Add a checkbox with a slider
                # that's only visible when checked:
                dpg.add_checkbox(
                    label=name,
                    tag=r_boxtag,
                    callback=toggle_slide,
                    user_data=("regular", name),
                    default_value=False
                )

                dpg.add_spacer()

                # Add a slider for each box:
                dpg.add_slider_int(
                    tag=r_slidetag,
                    min_value=1,
                    max_value=10,
                    width=200
                )

                dpg.add_spacer()
                dpg.add_spacer()

                # Make sure slider is hidden by default:
                dpg.hide_item(r_slidetag)
                # Set the value of the slider to 0:
                dpg.set_value(r_slidetag, 0)
                # Ensure slider is hidden at first:
                dpg.hide_item(r_slidetag)

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_separator()

        dpg.add_spacer()
        dpg.add_spacer()

        # Add the button to process the information:
        dpg.add_button(
            label="Roll My Dice!",
            tag="roll_button_r",
            callback=lambda: gather_dice("regular")
        )

        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()

        # Call footer() with parent = "regular_mode":
        if dpg.does_item_exist("regular_mode"):

            footer("regular_mode")

        # Map the screen name in the dictionary screens:
        screens["regular_mode"] = "regular_mode"

    # Loop through dice_names to reset each toggle of the sliders:
    for name in dice_names:

        r_boxtag = r_dice_boxes[name]
        r_slidetag = r_dice_sliders[name]

        # Set checkbox to unchecked:
        dpg.set_value(r_boxtag, False)

        # Make sure the box has the correct callback and user data:
        dpg.set_item_callback(r_boxtag, toggle_slide)
        dpg.set_item_user_data(r_boxtag, ("regular", name))

        # Hide the slider explicitly:
        if dpg.does_item_exist(r_slidetag):

            dpg.set_value(r_slidetag, 0)
            dpg.hide_item(r_slidetag)


# *** Average Mode ***

# Create the main Average Mode window with checkboxes, sliders, and a button:
def create_average():
    '''Create the Average Mode gameplay screen.

    Includes a checkbox for each kind of dice, and a slider only
    visible when checked to choose how many of each kind of dice.
    Also has a slider for number of rolls.

    Parameters
    ----------
    none
    '''

    # Clear the dictionaries a_dice_boxes and a_dice_sliders:
    a_dice_boxes.clear()
    a_dice_sliders.clear()

    # If any tags still exist, set their value to zero and hide them:
    for tag in r_dice_sliders.values():

        if dpg.does_item_exist(tag):

            dpg.set_value(tag, 0)
            dpg.hide_item(tag)

    # Within a window "Average Mode":
    with dpg.window(
        label="Average Mode",
        tag="average_mode",
        show=False,
        width=850
    ):

        # Add instructions for the game:
        dpg.add_text(
            "Welcome to Average Mode!",
            color=title_color
        )

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
            "please select whether you'd like 1 to 10 of each "
            "dice chosen.",
            color=instruction_color
        )

        dpg.add_spacer()

        dpg.add_separator()

        dpg.add_spacer()

        # Loop through the dictionary dice_names to
        # dynamically set the tag for each checkbox and slider:
        for name in dice_names:

            # Add each checkbox and slider tags
            # in their dictionaries:
            a_boxtag = (
                f"{name}_box_a"
                if name != "One Hundred"
                else "One_Hundred_box_a"
            )
            a_slidetag = (
                f"{name}_slider_a"
                if name != "One Hundred"
                else "One_Hundred_slider_a"
            )

            # Create the tags for the boxes and sliders:
            a_dice_boxes[name] = a_boxtag
            a_dice_sliders[name] = a_slidetag

            # Delete any existing a_boxtag:
            if dpg.does_item_exist(a_boxtag):

                dpg.delete_item(a_boxtag)

            # Delete any existing a_slidetag:
            if dpg.does_item_exist(a_slidetag):

                dpg.delete_item(a_slidetag)

            # Create a horizontal group to house each checkbox and slider:
            with dpg.group(horizontal=True):
                # Add checkbox and use a callback toggle_slide
                # to toggle each slider next to its box:

                # Add a checkbox with a slider
                # that's only visible when checked:
                dpg.add_checkbox(
                    label=name,
                    tag=a_boxtag,
                    callback=toggle_slide,
                    user_data=("average", name),
                    default_value=False
                )

                dpg.add_spacer()

                # Add a slider for each box:
                dpg.add_slider_int(
                    tag=a_slidetag,
                    min_value=1,
                    max_value=10,
                    width=200,
                    default_value=0
                )

                dpg.add_spacer()
                dpg.add_spacer()

                # Make sure slider is hidden by default:
                dpg.hide_item(a_slidetag)
                # Set the value of the slider to 0:
                dpg.set_value(a_slidetag, 0)
                # Ensure slider is hidden at first:
                dpg.hide_item(a_slidetag)

        dpg.add_spacer()
        dpg.add_spacer()

        dpg.add_separator()

        dpg.add_spacer()
        dpg.add_spacer()

        # Add instructions for picking how many rolls to average over:
        dpg.add_text(
            "Before you press the button, let me know how "
            "many times you'd like me to roll your dice for "
            "the Average. You can choose from 1 to 5000."
        )

        dpg.add_text(
            "It may be easier to directly enter the number "
            "if you want a precise number. If you would "
            "like to directly enter the number, please "
            "ctrl+click\n(command+click on macOS)",
            color=tip_color
        )

        dpg.add_spacer()
        dpg.add_spacer()

        # Add a slider Avg Input from 1-5000 with callback
        # change_a_rolls to continuously update a_rolls to 
        # this value:
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

        dpg.add_spacer()
        dpg.add_spacer()

        # Add a button to process the information:
        dpg.add_button(
            label=f"Roll My Dice {a_rolls} times!",
            tag="roll_button_a",
            callback=lambda: gather_dice("average")
        )

        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()

        # Call footer() with parent = "average_mode":
        if dpg.does_item_exist("average_mode"):

            footer("average_mode")

        # Map the screen name in the dictionary screens:
        screens["average_mode"] = "average_mode"


# *** Results Screen ***

# Create function housing the logic for all modes,
# using the dice chosen in each mode's screen:
def create_results(mode):
    '''Create the Results screen for a given mode of gameplay.

    Includes the logic for determining random rolls. Display's
    the results of the rolls or the average of the rolls,
    depending on mode.

    Parameters
    ----------
    mode : str
        The mode user chose to play.
    '''

    # Create a variable line to place between each dice result:
    line = "__________________________"

    # Determine which mode was used and create their result screens variables
    # with tag, label, title, and color:
    selected = (
        r_selected_items
        if mode == "regular"
        else a_selected_items
    )
    tag = (
        "regular_result_screen"
        if mode == "regular"
        else "average_result_screen"
    )
    label = (
        "Regular Result(s) Screen"
        if mode == "regular"
        else "Average Result(s) Screen"
    )
    title = (
        "Here are your Regular Mode Results!"
        if mode == "regular"
        else f"Here are your Average Mode Results Over {a_rolls} Rolls!"
    )

    # Check if there is already a Result Screen tag, delete it if so:
    if dpg.does_item_exist(tag):

        dpg.delete_item(tag)

    # Within a window "Regular Results Screen"
    # or "Average Results Screen":
    with dpg.window(
        label=label,
        tag=tag,
        show=False,
        width=850
    ):

        # Add the title of the screen:
        dpg.add_text(title, color=title_color)

        dpg.add_spacer()

        dpg.add_separator()

        dpg.add_spacer()

        # Initialize variable to track total:
        total = 0

        # Initialize variable to hold all_values list:
        all_values = []

        # Loop through the items in r_selected_items with name and count:
        for name, count in selected.items():

            # Initialize a variable to hold the number of sides:
            sides = dice_names[name]

            # Loop through a range of 1 to count+1:
            for i in range(1, int(count) + 1):

                # Create the label for each item:
                label = f"{name}-sided die #{i}"

                # If in "regular" mode, get a random number from
                # 1 to sides, then increase total by value:
                if mode == "regular":

                    value = rd.randint(1, sides)
                    total += value

                    # If there was more than one item selected:
                    if len(selected) > 1:

                        # Create a group for each regular result:
                        with dpg.group():

                            dpg.add_spacer()

                            dpg.add_text(f"{label}:   {value}")

                            dpg.add_spacer(height=10)

                            dpg.add_text(
                                line,                    color=sep_color
                            )

                        dpg.add_spacer(height=10)

                    # If there was only one item selected:
                    elif len(selected) == 1:

                        with dpg.group():

                            dpg.add_spacer()

                            dpg.add_text(f"{label}:   {value}")

                            dpg.add_spacer()

                            dpg.add_text(
                                line,
                                color=sep_color
                            )

                        dpg.add_spacer(height=10)

                    # Otherwise, raise and Exception:
                    else:

                        raise Exception(
                            "Please select at least one dice to play."
                        )

                # If in "average" mode:
                elif mode == "average":

                    # For [a_rolls] times, generate a random
                    # integer between 1 and sides and store
                    # in a list. _ used as placeholder as we
                    # do not care about the index:
                    value_list = [rd.randint(1, sides) for _ in range(a_rolls)]

                    # Find the sum of all values in value_list:
                    value_sum = sum(value_list)

                    # Add value_sum to total:
                    total += value_sum

                    # Create variable avg. It's the sum of
                    # value_sum divided by a_rolls:
                    avg = value_sum / a_rolls

                    # Append avg to the end of list all_values:
                    all_values.append(avg)

                    # If there was more than one item selected:
                    if len(selected) > 1:

                        # Create a group for each average result:
                        with dpg.group():

                            dpg.add_spacer()

                            # Round the average to 2 decimal places:
                            dpg.add_text(f"{label}:   {avg: .2f}")

                            dpg.add_spacer(height=10)

                            dpg.add_text(
                                line,
                                color=sep_color
                            )

                        dpg.add_spacer(height=10)

                    # If there was only one item selected:
                    elif len(selected) == 1:

                        with dpg.group():

                            dpg.add_spacer()

                            dpg.add_text(f"{label}:   {value}")

                            dpg.add_spacer(height=10)

                            dpg.add_text(
                                line,
                                color=sep_color
                            )

                        dpg.add_spacer()

                    # If no items were selected, raise an Exception:
                    else:

                        raise Exception(
                            "Please select at least one dice to play."
                        )

                    dpg.add_spacer(height=10)

                # If mode is not valid, raise an Exception:
                else:

                    raise Exception(
                        "Please play from available modes "
                        "'regular' or 'average'."
                    )

        dpg.add_spacer()
        dpg.add_separator()
        dpg.add_spacer()

        # For Regular Mode total:
        if mode == "regular":

            # Add text to label "Total Value of All
            # Your Dice: "
            dpg.add_text(
                "Total Value of All of Your Dice: ",
                color=total_text_color
            )

            dpg.add_spacer()
            dpg.add_spacer()

            # Add text to show the total:
            dpg.add_text(f"{total}", color=total_color)

        # Otherwise: If mode is "average":
        elif mode == "average":

            # If a_rolls == 0, raise an Exception as we cannot divide by zero:
            if a_rolls == 0:

                raise Exception(
                    "Please roll at least one time, or we "
                    "cannot calculate your average!!"
                )

            # If a_rolls is None, raise an exception as we
            # cannot process it as a non integer value:
            elif a_rolls is None:

                raise Exception("a_rolls == None")

            # If a_rolls is not None nor zero, display the average:
            else:

                # Create a variable avg_total to hold the sum of
                # all_values divided by a_rolls:
                avg_total = (sum(all_values)) / a_rolls

                # Add text to label "Average Of All Dice,
                # After Rolling {a_rolls} times: "
                dpg.add_text(
                    "Average Of All Dice, After Rolling "
                    f"{a_rolls} times:   ", color=total_text_color
                )

                dpg.add_spacer()
                dpg.add_spacer()

                # Add text to show the total average rounded to
                # 2 decimal places:
                dpg.add_text(
                    f"{avg_total: .2f}",
                    color=total_color
                )

        # If mode is neither 'regular' or 'average', raise an Exception:
        else:

            raise Exception("Please choose from one of the available modes.")

        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()
        dpg.add_spacer()

    # Call footer() with parent = "regular_mode"
    # or parent = "average_mode" using tag:
    if dpg.does_item_exist(tag):

        footer(tag)

    # Map the screen name in the dictionary screens:
    screens[tag] = tag
    show_screen(tag)


# *** Additional Functions ***

# Create function to toggle the sliders when boxes are checked and unchecked:
def toggle_slide(sender, app_data, user_data):
    '''Toggles a slider to be hidden or show.add()

    Parameters
    ----------
    sender : str
        The unique tag of the slider.
    app_data : int
        The current value of the slider.
    user_data : tuple (str, str)
        The user data sent from the slider.
    '''
    print(f"user_data = {user_data}")
    # Separate user_data into mode and name:
    mode, name = user_data

    # Check if user_data returns None, and if so, raise an Exception:
    if name is None or mode is None:

        raise Exception(
            "At least part of 'user_data' is "
            f"None:\n  name: {name}\n  mode: {mode}\n  user_data: "
            f"{user_data}"
        )

    # Add logic to determine which boxes and sliders to use:
    boxes = (
        a_dice_boxes
        if mode == "average"
        else r_dice_boxes
    )
    sliders = (
        a_dice_sliders
        if mode == "average"
        else r_dice_sliders
    )

    # Exit this function if name is not found:
    if name not in boxes or name not in sliders:

        return

    # Create a variable to check if a box is checked:
    is_checked = dpg.get_value(boxes[name])

    # If the box is checked set the value of sliders[name] to
    # 1 and show the item:
    if is_checked:

        dpg.set_value(sliders[name], 1)
        dpg.show_item(sliders[name])

    # If the box is unchecked set the value of sliders[name] to
    # 0 and hide the item:
    else:

        dpg.set_value(sliders[name], 0)
        dpg.hide_item(sliders[name])


# Create a helper function to set the value of a_rolls in create_avg():
def change_a_rolls(sender, app_data, user_data):
    '''Changes the value of global variable a_rolls as the slider moves.

    Parameters
    ----------
    sender : str
        The unique tag of the slider.
    app_data : int
        The current value of the slider.
    user_data : None
        Currently no expected user_data.
    '''

    # Declare global a_rolls to be able to modify the variable:
    global a_rolls

    # Set a_rolls to equal app_data which will be the current
    # value of the slider:
    a_rolls = app_data

    # Set the button label to roll as "Roll My Dice {#-of-rolls} times!":
    dpg.set_item_label("roll_button_a", f"Roll My Dice {a_rolls} times!")


# Create function to gather results of choosing dice:
def gather_dice(mode):
    '''Counts how many of each dice were selected and calls the Results Screen.

    Parameters
    ----------
    mode : str
        The mode the user is playing.
    '''

    # Determine which mode the information comes from,
    # and set it to selected and sliders:
    selected = (
        a_selected_items
        if mode == "average"
        else r_selected_items
    )
    sliders = (
        a_dice_sliders
        if mode == "average"
        else r_dice_sliders
    )

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


# Create a callback for the Back to Welcome Screen button:
def back_callback():
    '''Calls a function to reset the selections and shows the Welcome screen.

    Parameters
    ----------
    none
    '''

    # Reset all selections with function reset_selections()
    # and show Welcome screen:
    reset_selections()
    show_screen("welcome")


# Create a function to reset all selections:
def reset_selections():
    '''Resets all of the selections already made.

    Parameters
    ----------
    none
    '''

    # Declare global a_rolls to be able to modify the variable:
    global a_rolls

    # Reset Regular Mode sliders to 0 and hide the item(s):
    for slider_tag in r_dice_sliders.values():

        dpg.set_value(slider_tag, 0)
        dpg.hide_item(slider_tag)

    # Reset Average Mode sliders to 0:
    for slider_tag in a_dice_sliders.values():

        dpg.set_value(slider_tag, 0)

    # Reset Regular Mode boxes to unchecked:
    for box_tag in r_dice_boxes.values():

        dpg.set_value(box_tag, False)

    # Reset Average Mode boxes to unchecked:
    for box_tag in a_dice_boxes.values():

        dpg.set_value(box_tag, False)

    # Clear the _selected dictionaries and set a_rolls back to 0:
    r_selected_items.clear()
    a_selected_items.clear()
    a_rolls = 0


# *** Footer ***

# Add a footer to every screen:
def footer(parent):
    '''Creates a footer to display a button to return to Welcome screen.

    Parameters
    ----------
    parent : str
        The unique tag of the screen the footer should attach to.
    '''

    # If the parent exists:
    if dpg.does_item_exist(parent):

        # With a group that uses parent:
        with dpg.group(parent=parent):

            dpg.add_spacer()

            dpg.add_separator()

            dpg.add_spacer()
            dpg.add_spacer()
            dpg.add_spacer()
            dpg.add_spacer()

            # Add the footer text:
            dpg.add_text(
                "Return to Welcome Screen",
                color=back_color
            )

            dpg.add_spacer()
            dpg.add_spacer()

            dpg.add_separator()

            dpg.add_spacer()
            dpg.add_spacer()

            # Add a button to use back_callback to return to Welcome Screen:
            dpg.add_button(
                label="  <--  ",
                callback=back_callback
            )

            dpg.add_spacer()
            dpg.add_spacer()

    # If the parent does not exist raise an Exception:
    else:

        raise Exception(
            f"Cannot display footer - parent '{parent}' is not found."
        )


# *** Setup and Run ***

# Create function that starts each screen as needed, and display
# Welcome screen first:
def program_setup():
    '''Create each screen needed to begin the program and show Welcome screen.

    Parameters
    ----------
    none
    '''

    # Create Welcome screen, and show it:
    create_screen("welcome", create_welcome, show=True)

    # Create Main Menu screen:
    create_screen("main_menu", create_menu)

    # Create Regular Mode screen:
    create_screen("regular_mode", create_regular)

    # Create Average Mode screen:
    create_screen("average_mode", create_average)


# Run the program that initializes each screen (and functions),
# and leads through the game:
program_setup()


# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
