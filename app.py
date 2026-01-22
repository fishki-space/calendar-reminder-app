import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from threading import Thread
import time

from reminder_manager import ReminderManager


class CalendarReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Reminder App")
        self.root.geometry("400x300")

        self.manager = ReminderManager()
        self.running = True

        self.create_ui()
        self.start_reminder_thread()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_ui(self):
        ttk.Label(self.root, text="Calendar & Reminder App",
                  font=("Arial", 14, "bold")).pack(pady=20)

        ttk.Button(self.root, text="Add Sample Reminder",
                   command=self.add_sample_reminder).pack(pady=10)

        ttk.Button(self.root, text="Exit",
                   command=self.on_close).pack(pady=10)

    def add_sample_reminder(self):
        today = datetime.now().strftime("%Y-%m-%d")
        reminder = {
            "time": (datetime.now().strftime("%H:%M")),
            "text": "Sample Reminder",
            "type": "General",
            "triggered": False
        }
        self.manager.add_reminder(today, reminder)
        messagebox.showinfo("Added", "Sample reminder added for now.")

    def start_reminder_thread(self):
        thread = Thread(target=self.check_reminders, daemon=True)
        thread.start()

    def check_reminders(self):
        while self.running:
            now = datetime.now()
            due = self.manager.get_due_reminders(now)
            for reminder in due:
                self.root.after(0, self.show_notification, reminder)
            time.sleep(60)

    def show_notification(self, reminder):
        messagebox.showinfo("Reminder", reminder["text"])

    def on_close(self):
        self.running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarReminderApp(root)
    root.mainloop()
