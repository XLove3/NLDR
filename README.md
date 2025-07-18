# <span style="color:forestgreen">Neat Little Dice Roller</span>


## Table of Contents

- [Neat Little Dice Roller](#neat-little-dice-roller)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Structure of the Program](#structure-of-the-program)
  - [Installation](#installation)
  - [Running the Program](#running-the-program)
  - [Documentaion](#documentaion)
  - [In the Future](#in-the-future)
  - [Contact and Collaboration](#contact-and-collaboration)
- [Thank you for playing _Neat Little Dice Roller_!](#thank-you-for-playing-neat-little-dice-roller)

*****

## Description

The __Neat Little Dice Roller__ currently includes two modes of game play. One allows the user to choose from several different-sided dice. Then they choose how many of each dice they'd like to roll. The program rolls those dice, and provides the number rolled for each, as well as the total of all the dice rolls. 

The other mode also allows the user to choose from several different-sided dice. They choose how many of each dice they'd like to roll. Afterwards, the user chooses how many times they want to roll all of the dice. It then displays the average of each die over the number of times the dice were rolled, and the average of all the numbers rolled from each dice over all the rolls.

<br>

## Structure of the Program

- <span style="color:lightsalmon">Welcome</span> screen:
  - Button that routes to the Main Menu screen

- <span style="color:lightsalmon">Main Menu</span> screen:
  - Button that routes to the Regular Mode screen

  - Button that routes to the Average Mode screen

  - _<span style="color:limegreen">** Footer **</span> - See Below_

- <span style="color:lightsalmon">Regular Mode</span> screen:
  - 7 checkboxes to choose different-sided dice - when checked, each checkbox has a slider for number of dice from 1 -  10
    - 2 sided dice  -->  slider from 1-10
    - 4 sided dice  -->  slider from 1-10
    - 6 sided dice  -->  slider from 1-10
    - 10 sided dice  -->  slider from 1-10
    - 12 sided dice  -->  slider from 1-10
    - 20 sided dice  -->  slider from 1-10
    - 100 sided dice  -->  slider from 1-10

  - Button that routes to the Regular Mode Results screen

  - _<span style="color:limegreen">** Footer **</span> - See Below_

- <span style="color:lightsalmon">Average Mode</span> screen
  - 7 checkboxes to choose different-sided dice - when checked, each checkbox has a slider for number of dice from 1 -  10
    - 2 sided dice  -->  slider from 1-10
    - 4 sided dice  -->  slider from 1-10
    - 6 sided dice  -->  slider from 1-10
    - 10 sided dice  -->  slider from 1-10
    - 12 sided dice  -->  slider from 1-10
    - 20 sided dice  -->  slider from 1-10
    - 100 sided dice  -->  slider from 1-10

  - Slider to choose how many rolls each dice should make, 1 - 5000

  - Button that routes to the Average Mode Results screen

  - _<span style="color:limegreen">** Footer **</span> - See Below_

- <span style="color:lightsalmon">Regular Mode Results</span> screen
  - Displays the result of each chosen dice's random roll, from 1 - the number of sides on the dice

  - Displays the total sum of all of the dice rolled

  - _<span style="color:limegreen">** Footer **</span> - See Below_

- <span style="color:lightsalmon">Average Mode Results</span> screen
  - Displays the average of all of each dice's rolls, each from 1 - the number of sides on the dice, over the total number of rolls chosen

  - Display's the average of all of the rolls made with all of the dice chosen, over the total number of rolls chosen

  - _<span style="color:limegreen">** Footer **</span> - See Below_

- <span style="color:limegreen">** Footer **</span> - At the bottom of each screen except Welcome screen
  - Button that routes back to the Welcome screen

<br>

## Installation

Please see the __[Installation Guide](installation_guide.md)__ for instructions on installing everything you need to run the __<span style="color:forestgreen">Neat Little Dice Roller</span>__ from git to the program files.

<br>

## Running the Program

To run the program after you've installed everything needed: 

- Open the __Terminal__ or __Command Prompt__

- Navigate to the folder holding this program using `cd`

- Type `python3 main.py`

<br>

## Documentaion

Please see the __[Documentation Guide](documentation.md)__ for the documentation for __Neat Little Dice Roller__.

__<span style="color:firebrick">** Please Note **</span>__

<span style="color:firebrick">This document is still under construction.</span>

<br>

## In the Future

I have a bunch of ideas of how to improve this project, and will be adding new ones occasionally too!

Please see some of my ideas in my __[Future Ideas](future_ideas.md)__ guide.

<br>

## Contact and Collaboration

If you have any great ideas for this project (or anything I might be interested in, please email me! (Check out my __[GitHub profile](https://github.com/XLove3)__   for my email.))

If you choose to work on this project, or if you would just like to see what git flow I followed for the program, I created a __[Git Flow](git_flow.md)__ document to help me through the process.

(_Though, admittedly, I am still working on the __"work in small pieces"__ thing!!!_ :wink:)


*****


__<span style="color:firebrick">** Please Note **</span>__

_<span style="color:firebrick">Rerun the program as many times as you'd like, however between each time running the game, you'll want to __close the main window__, as it will not re-open until the previous one is closed.</span>_


# <span style="color:forestgreen">Thank you for playing _Neat Little Dice Roller_!</span>
