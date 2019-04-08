from datetime import datetime

from .config import DATE_FORMAT
from .models import Task
from .utils import fmt_task, validate_date


def add_task(args):
    due = validate_date(args.due)
    Task.create(title=args.title, priority=args.priority, due_date=args.due)
    print("✅ Task added.")


def list_tasks(args):
    tasks = Task.list(show_all=args.all, sort_by=args.sort)
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(fmt_task(t))


def done_task(args):
    Task.mark_done(args.id)
    print(f"✨ Task #{args.id} marked as done.")


def delete_task(args):
    Task.delete(args.id)
    print(f"🗑️ Task #{args.id} deleted.")


def edit_task(args):
    due = validate_date(args.due)
    Task.update(args.id, title=args.title, priority=args.priority, due_date=due)
    print(f"📝 Task #{args.id} successfully updated.")