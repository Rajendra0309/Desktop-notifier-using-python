# Desktop Notifier Using Python

A simple desktop notification application built with Python that allows users to schedule notifications with custom messages.

## Features

- Set custom notification title and message
- Choose time delay in seconds or minutes
- Simple and intuitive GUI interface

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)
- plyer 2.1.0

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Rajendra0309/Desktop-notifier-using-python.git
   cd Desktop-notifier-using-python
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```
python desktop_notifier.py
```

1. Enter a notification title
2. Enter your notification message
3. Set the time delay (1-60)
4. Select time unit (seconds or minutes)
5. Click "Set Notification"

## How It Works

1. **User Interface**: Created with Tkinter, providing input fields for title, message, and time settings.
2. **Notification System**: Uses the plyer library to display desktop notifications.
3. **Timer Function**: Schedules notifications based on the specified time delay.

## Project Structure

- `desktop_notifier.py`: Main application file containing the GUI and notification logic
- `requirements.txt`: List of required Python packages
- `.gitignore`: Specifies files to be ignored by Git