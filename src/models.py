from .db import get_connection


class Task:
    @staticmethod
    def create(title, priority="medium", due_date=None):
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO tasks (title, priority, due_date) VALUES (?, ?, ?)",
                (title, priority, due_date),
            )
            conn.commit()

    @staticmethod
    def update(task_id, title=None, priority=None, due_date=None):
        updates = []
        params = []
        if title:
            updates.append("title=?")
            params.append(title)
        if priority:
            updates.append("priority=?")
            params.append(priority)
        if due_date:
            updates.append("due_date=?")
            params.append(due_date)
        if not updates:
            return
        params.append(task_id)
        with get_connection() as conn:
            conn.execute(f"UPDATE tasks SET {', '.join(updates)} WHERE id=?", params)
            conn.commit()

    @staticmethod
    def list(show_all=False, sort_by="due_date"):
        valid_sort = sort_by if sort_by in ["due_date", "priority", "id"] else "id"
        with get_connection() as conn:
            if show_all:
                q = f"SELECT * FROM tasks ORDER BY is_done, {valid_sort}"
            else:
                q = f"SELECT * FROM tasks WHERE is_done=0 ORDER BY {valid_sort}"
            return conn.execute(q).fetchall()

    @staticmethod
    def mark_done(task_id):
        with get_connection() as conn:
            conn.execute("UPDATE tasks SET is_done=1 WHERE id=?", (task_id,))
            conn.commit()

    @staticmethod
    def delete(task_id):
        with get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            conn.commit()
