class TaskError(Exception):
    """Base class for TaskTrack app errors."""


class ValidationError(TaskError):
    pass
