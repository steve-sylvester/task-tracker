from datetime import datetime
from models import Task
from utils import fmt_task
from config import DATE_FORMAT

def add_task(args):
    Task.create(
        title=args.title,
        priority=args.priority,
        due_date=args.due
    )
    print("✅ Task added.")

def list_tasks(args):
    tasks = Task.list(show_all=args.all)
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