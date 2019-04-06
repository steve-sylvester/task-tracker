import argparse

from . import commands, db


def main():
    parser = argparse.ArgumentParser(description="🧩 TaskTrack - simple task manager")
    sub = parser.add_subparsers(dest="command")

    # Add
    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("title")
    add_p.add_argument(
        "--priority", choices=["low", "medium", "high"], default="medium"
    )
    add_p.add_argument("--due", help="Due date (YYYY-MM-DD)")
    add_p.set_defaults(func=commands.add_task)

    # List
    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("--all", action="store_true")
    list_p.set_defaults(func=commands.list_tasks)

    # Done
    done_p = sub.add_parser("done", help="Mark task as done")
    done_p.add_argument("id", type=int)
    done_p.set_defaults(func=commands.done_task)

    # Delete
    del_p = sub.add_parser("delete", help="Delete task")
    del_p.add_argument("id", type=int)
    del_p.set_defaults(func=commands.delete_task)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    db.init_db()
    args.func(args)


if __name__ == "__main__":
    main()
