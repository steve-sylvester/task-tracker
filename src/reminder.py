import threading
import time
from datetime import datetime, timedelta

from src.config import CHECK_INTERVAL, GREEN, YELLOW
from src.utils import colorize
from .models import Task


def check_due_soon():
    now = datetime.now()
    tomorrow = now + timedelta(days=1)

    tasks = Task.list(show_all=False)
    for t in tasks:
        if not t["due_date"]:
            continue
        try:
            due = datetime.strptime(t["due_date"], "%Y-%m-%d")
        except ValueError:
            continue

        if now <= due <= tomorrow:
            print(
                colorize(f"⏰ Reminder: '{t['title']}' is due {t['due_date']}", YELLOW)
            )
        if due < now:
            print(
                colorize(
                    f"⚠️  Overdue task: '{t['title']}' (was due {t['due_date']})", GREEN
                )
            )

    # schedule next run
    threading.Timer(CHECK_INTERVAL, check_due_soon).start()


def start_reminders():
    print(colorize("🔔 Reminder service started (checks every 60s)...", YELLOW))
    check_due_soon()
