# JEE-MAIN-RESULT-SIMULATOR-PORTAL 

**Overview of Project**
This is a fun Python mini-project I built using Tkinter that simulates the highly anticipated (and stressful!) JEE Main scorecard release. Instead of running in a boring terminal, it uses a custom GUI to ask for your details, randomly generates marks for Physics, Chemistry, and Maths, and calculates your percentile.

Based on the category you enter (General, OBC, SC, ST, PWD), the code uses hardcoded cutoff logic to tell you whether you qualified for JEE Advanced or not. It’s entirely random and meant just for fun—it doesn't fetch any real NTA data!

**Features**
Custom GUI Interface: Redirects standard print() and input() functions directly into a dark-themed Tkinter window so the whole experience feels like an actual desktop app.

Smart Input Validation: It won't let you crash the app with bad inputs.

Stops you if you leave a field blank.

Forces the Application Number to be numbers only.

Checks that your Date of Birth is a proper length.

Validates your category strictly to the available options.

Randomized Scoring: Every time you run it, you get a new score out of 300.

Category Cutoffs: Realistic(ish) percentile cutoffs to see if you qualify. There's also a funny little easter egg for the PWD category.

Technology Used
Language: Python 3.x

**Libraries:**

tkinter (for the GUI, standard with Python)

random (to generate the shift data and marks)

builtins (to override the default print/input behavior)

Steps to Install & Run the Project
Make sure you have Python installed on your computer. You don't need to install any external packages using pip since Tkinter comes pre-installed with Python.

Clone this repository or just download the .py file (e.g., jee_simulator.py).

Open your terminal or command prompt.

Navigate to the folder where you saved the file.

Run the script by typing:

Bash
python jee_simulator.py
The app window should pop up immediately!

**Instructions for Testing**
If you want to test how the code handles different scenarios, try these out while running the app:

The "Empty" Test: When prompted for your name or application number, try hitting Cancel or leaving it totally blank. A popup error should yell at you to fill it in.

The "Bad Typist" Test: When asked for your Application Number, type letters instead of numbers (e.g., "123ABC"). It will throw an error and ask again.

The "Wrong Category" Test: When asked for your category at the very end, type something random like "ALIEN" or misspell "GENERAL". It will block it until you enter a valid Indian reservation category.

The "Lucky/Unlucky" Test: Run the app 2-3 times to see the random number generator in action. Sometimes you'll fail miserably, and sometimes you'll clear the cutoff for JEE Advanced!
