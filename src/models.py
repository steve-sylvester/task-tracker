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
    def list(show_all=False):
        with get_connection() as conn:
            if show_all:
                q = "SELECT * FROM tasks ORDER BY is_done, due_date"
            else:
                q = "SELECT * FROM tasks WHERE is_done=0 ORDER BY due_date"
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
