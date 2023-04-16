class MyError(RuntimeError):
    def __init__(self, error_messages: str):
        self.error_messages = error_messages
