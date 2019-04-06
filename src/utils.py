from datetime import datetime

from .config import DATE_FORMAT


def fmt_task(t):
    status = "✅" if t["is_done"] else "⏳"
    due = t["due_date"] if t["due_date"] else "-"
    return f"[{status}] #{t['id']} | {t['title']} | {t['priority']} | Due: {due}"


def validate_date(date_str):
    if not date_str:
        return None
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return date_str
    except ValueError:
        raise ValueError(f"Invalid date format, expected {DATE_FORMAT}")
