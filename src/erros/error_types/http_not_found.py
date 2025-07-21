class HttpNotFoundError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.status_code = 404
        self.name = "NotFound"
        self.message = message
