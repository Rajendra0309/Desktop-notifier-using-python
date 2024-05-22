# Desktop-notifier-using-python

1. **Importing Libraries**:
   - The code begins by importing the necessary libraries:
     - `Tkinter`: This is a standard GUI (Graphical User Interface) library for Python.
     - `notification` from `plyer`: Plyer is a Python library for accessing features of your hardware, like notifications.
     - `messagebox` from `tkinter`: This is used for displaying dialog boxes for messages or errors.

2. **Setting Constants**:
   - `BG_COLOR`: This variable holds the background color for the GUI.

3. **Function Definitions**:
   - `noti_printer()`: This function is responsible for printing a notification with the title and message entered by the user.
   - `timer()`: This function sets a timer based on the user input and schedules the notification to be printed after the specified time.

4. **Creating the GUI Window**:
   - A Tkinter window is created with the title "Desktop Notifier" and configured with a specific size and background color.

5. **Creating GUI Elements**:
   - Labels, entry fields, spinboxes, buttons, and radio buttons are created using Tkinter widgets.
   - Labels are used to display text instructions.
   - Entry fields allow users to input text.
   - Spinbox is used for selecting a time interval.
   - Button is used to trigger setting the notification.
   - Radio buttons are used to select between seconds and minutes for the time interval.

6. **Layout Management**:
   - The `grid()` method is used to arrange the widgets in rows and columns within the window.

7. **Mainloop**:
   - The `mainloop()` method is called on the Tkinter window, which starts the event loop and keeps the window open until it is closed by the user.

Overall, this code creates a simple desktop notifier application where users can input a title, message, and time interval to schedule a notification. When the time elapses, a notification pops up on the desktop with the specified title and message.
