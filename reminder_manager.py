import json
import os
from datetime import datetime


class ReminderManager:
    def __init__(self, file_path="reminders.json"):
        self.file_path = file_path
        self.reminders = self.load_reminders()

    def load_reminders(self):
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def save_reminders(self):
        with open(self.file_path, "w") as f:
            json.dump(self.reminders, f, indent=2)

    def add_reminder(self, date_str, reminder):
        self.reminders.setdefault(date_str, []).append(reminder)
        self.save_reminders()

    def get_reminders_for_date(self, date_str):
        return self.reminders.get(date_str, [])

    def delete_reminder(self, date_str, index):
        del self.reminders[date_str][index]
        if not self.reminders[date_str]:
            del self.reminders[date_str]
        self.save_reminders()

    def get_due_reminders(self, now):
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M")

        due = []
        for reminder in self.reminders.get(date_str, []):
            if reminder["time"] == time_str and not reminder.get("triggered"):
                reminder["triggered"] = True
                due.append(reminder)

        if due:
            self.save_reminders()

        return due
