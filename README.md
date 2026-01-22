# Calendar and Reminder Application

A simple desktop application built using Python and Tkinter that allows users to set reminders for specific dates and times.

## Features
- Add reminders for a specific time
- Background reminder checking
- Local data storage using JSON

## Project Approach
The project was first implemented as a single script.
Later, reminder handling logic was separated into a small module to improve clarity and safety.

A background thread checks reminders, while UI updates are handled using Tkinter’s main event loop.

## Limitations
- Designed for single-user local use
- Uses JSON instead of a database
- Notification system is basic

## What I Learned
- Tkinter GUI development
- Background threading in Python
- Thread-safe UI updates
- Structuring code for better readability
