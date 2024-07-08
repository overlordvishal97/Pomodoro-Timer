# Pomodoro-Timer
This is a Pomodoro timer application built with tkinter. The Pomodoro Technique is a time management method that involves working in focused 25-minute increments, called "sessions," separated by 5-minute breaks. After four sessions, a longer break of 20 minutes is taken.

# Usage
Run the code in a Python environment with tkinter installed.
A window will appear with a tomato image, a timer, and two buttons: "Start" and "Reset".
Click the "Start" button to begin a Pomodoro session.
The timer will count down from 25 minutes (or 5 minutes for a break).
When the timer reaches 0, a checkmark will be added to the "Correct" label, and the next session will begin.
Click the "Reset" button to reset the timer and the checkmarks.

# Features
Pomodoro timer with 25-minute work sessions and 5-minute breaks
Long break of 20 minutes after four sessions
Checkmarks to track completed sessions
User-friendly GUI interface
Customizable colors and fonts

# Technical Details
The application uses the tkinter library to create the GUI.
The timer_start function is called when the "Start" button is clicked, which starts the Pomodoro timer.
The count_down function is called every second to update the timer.
The timer_reset function is called when the "Reset" button is clicked, which resets the timer and the checkmarks.
