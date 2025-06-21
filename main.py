# Import DearPyGui and the Random module:
import dearpygui.dearpygui as dpg, random as rd

# Callback function to print "user_data: "
# and the user_data sent to the function:
def callback(sender, app_data, user_data):
    # TODO: Add a docstring to function callback()
    '''Docstring'''

    print(f"user_data: {user_data}")


# DPG - create context:
dpg.create_context()
# DPG - create viewport with the game title,
# and a starting width, height. Viewport is resizable:
dpg.create_viewport(title='Neat Little Dice Roller', width=1000, height=600)
# DPG - set up DearPyGui:
dpg.setup_dearpygui()


# Create a new window with an appropriate label:
with dpg.window(label="Main"):
    # Initialize some data to send to callback function:
    data = "From 'Main' window, button 'Push!'"

    # Add some text above the button (to be removed or later changed):
    dpg.add_text("Push the button!")

    # Add a button with the label "Push!", value as data,
    # and callback the callback function:
    dpg.add_button(label="Push!", user_data=data, callback=callback)


# DPG - Show the Viewport:
dpg.show_viewport()
# DPG - Start DearPyGui
dpg.start_dearpygui()
# DPG - Destroy Context
dpg.destroy_context()
