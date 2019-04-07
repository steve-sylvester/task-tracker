from datetime import datetime

from .config import CYAN, DATE_FORMAT, GRAY, GREEN, RED, RESET, YELLOW


def colorize(text, color):
    return f"{color}{text}{RESET}"


def fmt_task(t):
    status = colorize("✅", GREEN) if t["is_done"] else colorize("⏳", YELLOW)
    due = t["due_date"] if t["due_date"] else "-"
    pr_color = {"low": CYAN, "medium": YELLOW, "high": RED}.get(t["priority"], RESET)
    priority_str = colorize(t["priority"].upper(), pr_color)

    due_fmt = colorize(due, GRAY) if t["is_done"] else due
    return f"[{status}] #{t['id']} | {t['title']} | {priority_str} | Due: {due_fmt}"


def validate_date(date_str):
    if not date_str:
        return None
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return date_str
    except ValueError:
        raise ValueError(f"Invalid date format, expected {DATE_FORMAT}")
