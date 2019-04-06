from src.db import init_db
from src.models import Task

print("Initializing DB...")
init_db()

print("Creating tasks...")
Task.create("Write documentation", "high", "2025-11-10")
Task.create("Refactor modules", "medium")

print("Listing tasks:")
for t in Task.list():
    print(dict(t))

print("Marking one done...")
Task.mark_done(1)

print("Final state:")
for t in Task.list(show_all=True):
    print(dict(t))
