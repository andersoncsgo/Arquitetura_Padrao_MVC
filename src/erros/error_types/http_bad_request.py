class HttpBadRequestError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.status_code = 400
        self.name = "BadRequest"
        self.message = message
