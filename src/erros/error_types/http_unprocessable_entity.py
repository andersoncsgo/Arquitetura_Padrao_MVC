class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.status_code = 422
        self.name = "UnprocessableEntity"
        self.message = message
