# <span style="color:forestgreen">Installation Guide</span>


*****
<span style="color:forestgreen; background-color:lightyellow">__<-- Back to [README](README.md#installation)__</span>
*****


Welcome to the __Installation Guide__! This guide will walk you through installing everything you need to run the __Neat Little Dice Roller__.

<br>

## Table of Contents

- [Installation Guide](#installation-guide)
  - [Table of Contents](#table-of-contents)
  - [Installation Instructions](#installation-instructions)
    - [\*\* Developer's Note \*\*](#-developers-note-)
    - [Installing git, Python 3, pip, and DearPyGui](#installing-git-python-3-pip-and-dearpygui)
      - [Installing and setting up git:](#installing-and-setting-up-git)
      - [Check if you have Python 3 installed:](#check-if-you-have-python-3-installed)
      - [Install Python 3:](#install-python-3)
      - [ pip, or other package installer:](#-pip-or-other-package-installer)
      - [Install DearPyGui:](#install-dearpygui)
    - [Installing the Program](#installing-the-program)
      - [Clone the repository:](#clone-the-repository)
  - [Optional Step: Run the Application/Executable File](#optional-step-run-the-applicationexecutable-file)
    - [Verify That You Have the Application/Executable File](#verify-that-you-have-the-applicationexecutable-file)
    - [Create the Application/Executable File](#create-the-applicationexecutable-file)
    - [Create the Desktop Shortcut](#create-the-desktop-shortcut)
      - [If you're using Windows:](#if-youre-using-windows)
      - [If you're using macOS:](#if-youre-using-macos)
    - [Run and Play the Game:](#run-and-play-the-game)

*****

## Installation Instructions

The only installations that __Neat Little Dice Roller__  need are git, Python 3, pip (or other package installer), DearPyGui, and of course the actual program files.

<br>

### <span style="color:firebrick">** Developer's Note **</span>

_<span style="color:firebrick">I developed this program using MacOS. The language in this README may reflect that such as "Terminal" vs "Command Prompt", or "cmd+C" vs "ctrl+C", etc, despite my best efforts to include both... __Please just substitute the appropriate command in it's place!__</span>_ :smiley:

- _<span style="color:firebrick">The __Terminal__ (MacOS) or __Command Prompt__ (Windows) are where you type in the command line commands.</span>_

- _<span style="color:firebrick">Keyboard shortcuts often use __cmd+C__ (cmd = command)(MacOS) or __ctrl+C__ (ctrl = control)(Windows).</span>_
  - _<span style="color:firebrick">** Please Note**  Replace "C" with whatever shortcut is needed.</span>_

<br>

### Installing git, Python 3, pip, and DearPyGui

#### <span style="color:limegreen">Installing and setting up git:</span>

You will have a different method of installation, depending on your operating system.

<br>

__<u>Check if git is installed:</u>__

- Open the __Terminal__ or __Command Prompt__
  - Type `git --version`
    - If git is installed correctly, the command will display the installed version.

<br>

__<u>Install:</u>__

_<span style="color:firebrick">If you already have git installed you can skip this section!</style>_

- <span style="color:mediumaquamarine">Windows:</span>
  - Download the installer from the Git website and run it.
    - https://git-scm.com/downloads/win

- <span style="color:mediumaquamarine">macOS:</span>
    - Open the __Terminal__

    - Type `brew install git`
      - If for some reason homebrew is not installed, install it here:
        - https://brew.sh/

<br>

__<u>Configure:</u>__
- Set your username:
  - Type `git config --global user.name "Your Name"`

- Set your email:
  - Type `git config -- global user.email "your.email@example.com"`

<br>

#### <span style="color:limegreen">Check if you have Python 3 installed:</span>

- Open the __Terminal__ or __Command Prompt__

- Type `python3 --version`
  - If Python 3 is installed correctly, the command will display the installed version

<br>

#### <span style="color:limegreen">Install Python 3:</span>

_<span style="color:firebrick">If you already have Python 3 installed you can skip this section!</span>_

- Go to the official Python 3 downloads page:
  - https://www.python.org/downloads/
    - It should have the appropriate version for your computer on this page. 

  - Click the yellow button labeled __Download Python 3.13.5__ 
         	<span style="color:#C49102">*** _This is the current version as of creation of this README. Your version may be higher, depending on when you've found this!_ ***</span>

  - This should download to your downloads folder (or elsewhere depending on your computer settings.)

- Run the installer:
  - Find your downloaded installer, and run it.

    - <span style="color:red">__Important:__ If you are on Windows, make sure to check the box labeled __Add Python to PATH__</span>

- When the installation is finished, verify your installation:
  - We'll do this ths same way we checked for a Python 3 installation in the first place:
    - Open the __Terminal__ or __Command Prompt__

    - Type `python3 --version`
      - If Python 3 is installed correctly, the command will display the installed version

<br>

#### <span style="color:limegreen"> pip, or other package installer:</span>

<span style="color:firebrick">_The next step after this one involves using a package installer. Most Python 3 installations come with pip already installed, and my instructions use pip. Obviously feel free to pick the one you are most comfortable with._</span> 

- Open the __Terminal__ or __Command Prompt__

- Type `pip --version`
  - It will give you the currently installed version of pip.

If pip is not already installed, you can find instructions elsewhere online. One place is __[pip's documentation](https://pip.pypa.io/en/stable/installation/)__.

<br>

#### <span style="color:limegreen">Install DearPyGui:</span>

- Open the __Terminal__ or __Command Prompt__
  - Type `pip install dearpygui`

- Check that the installation worked:
  - Type `pip show dearpygui`
    - This should show you information about the installed dearpygui package

<br>

### Installing the Program

#### <span style="color:limegreen">Clone the repository:</span>

- Navigate to the __[main page](https://github.com/XLove3/NLDR)__ of this repository:

- Above the list of files, click the button __<> Code__

- Copy the url for the repository (using HTTPS):
  - Make sure you are on the __Local__ tab, and __HTTPS__ is the underlined method of copying

  - Click on the __copy button__ (two overlapping squares) to the right of the URL

- Open __Terminal__ or __Command Prompt__

- Navigate to the file location where you would like this repository to live using `cd`

- Type `git clone`, and then paste the URL you copied earlier

    `git clone https://github.com/XLove3/NLDR.git`

- Press enter to create your local copy of the program files

***

## Optional Step: Run the Application/Executable File

The program files include an __application/executable file__ that you can run the game by instead of running the game from the __Terminal__ or __Command Prompt__.

<br>

### Verify That You Have the Application/Executable File

Check for your application/executable file:

- Locate your main program folder "NLDR"
  - Inside of "NLDR", locate the "dist" folder

- Inside of "dist", locate the application/executable file "main"

- If "main" exists here, you have the application/executable file needed

<br>

### Create the Application/Executable File

Create the executable file:

  _<span style="color:firebrick">If you already have the application/executable file "main" installed you can skip this section!</span>_

- Download PyInstaller:
  - `pip install pyinstaller`

- `cd` to the NLDR folder housing main.py file

- Run PyInstaller:
  - `pyinstaller --onefile main.py`

- Find the dist folder in the NLDR folder
  - Inside is the <span style="color:forestgreen">Neat Little Dice Game</span> `.exe` executable file __main__ (or if on __macOS__, the application __main__)

<br>

### Create the Desktop Shortcut

Your instructions differ depending on operating system.

#### If you're using Windows:

- Right click on the desktop

- Select `New > Shortcut`

- Choose "Browse" and find your executable file

- Select the `.exe` executable file

- Click "OK"

- Click "Next"

  - Enter a name for your shortcut (like "NLDR", "Neat Little Dice Roller", "Any Other Name", etc.)

  - Click "Finish"

<br>

#### If you're using macOS:

- Open Finder and find the application
  - NLDR folder -> dist folder -> application

- Right click/ctrl+click on the application

- Choose "Make Alias"

- Rename the alias (like "NLDR", "Neat Little Dice Roller", "Any Other Name", etc.)

- Drag the alias to the desktop

<br>

### Run and Play the Game:

- Double-click on the renamed alias icon on the desktop (or in Finder)

- Wait a few seconds

- Play the game!
