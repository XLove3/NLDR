# <span style="color:forestgreen">Future Edits and Features</span>


*****
<span style="color:forestgreen; background-color:lightyellow">__<-- Back to [README](README.md#in-the-future)__</span>
*****


## Table of Contents
- [Future Edits and Features](#future-edits-and-features)
  - [Table of Contents](#table-of-contents)
    - [In Average Mode Results:](#in-average-mode-results)
    - [Find areas of reused code:](#find-areas-of-reused-code)
    - [In global variables:](#in-global-variables)
    - [Everywhere there's an Exception:](#everywhere-theres-an-exception)
    - [Make the code more secure:](#make-the-code-more-secure)
    - [In `change_a_rolls()`:](#in-change_a_rolls)
    - [In Average Mode:](#in-average-mode)
    - [In `create_regular()` and `create_average()`:](#in-create_regular-and-create_average)
    - [Closing everything:](#closing-everything)
    - [In the documentation.md file:](#in-the-documentationmd-file)
    - [Create new modes:](#create-new-modes)

*****

### In Average Mode Results:

- Show the list of every roll made per dice with the results, available by clicking something and it appearing underneath it.

- Example: "Each individual roll: 2, 8, 6, ..., 3."

<br>

### Find areas of reused code:

- _Such as: `dpg.add_spacer()` and `dpg.add_separator`:_

  - Make easy to use variables for these.

  - Make little functions for other code that is reused a lot

<br>

### In global variables:

- Turn color variables into a dictionary.

<br>

### Everywhere there's an Exception:

- Refactor that function to use try-except.

- In the try-except except branches, use a popup that can be shown to the user. The program stays just the same when returning from the popup.

<br>

### Make the code more secure:

- Add try-except wherever the program could break.

- In the try-except except branches, use a popup that can be shown to the user. The program stays just the same when returning from the popup.

<br>

### In `change_a_rolls()`:

- Make this function dynamic to work with any function that has a need for a `**_rolls` variable.

- Refactor any place that uses `a_rolls` to use the new dynamic `change_rolls()` function.

<br>

### In Average Mode:

- Instead of just the average (to 2 decimal places), refactor to include (all or some) of the following:
  - The average rounded to the nearest integer.

  - The average rounded to 2 decimal places.

  - The average rounded to 10 decimal places.

  - The entire average to whatever decimal places.

  - A slider for the user to choose between 1 and ? decimal places.

<br>

### In `create_regular()` and `create_average()`:

- Refactor both into `create_mode(mode)` to make it more dynamic and reusable as more modes are added.

<br>

### Closing everything:

- Add a button to every page saying "I'm Done Playing" that closes the viewport/entire program.

<br>

### In the documentation.md file:

- This file will include an in-depth documentation of functions and variables.

<br>

### Create new modes:

- Still developing some ideas for this!
