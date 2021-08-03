

class NullBotAPIException(Exception):

    def __init__(
            self,
            error: int,
            description: str = ""
    ):
        self.error = error
        self.description = description

    def __repr__(self):
        return f"<NullBotAPIException:code={self.error}, msg={self.description}>"

    def __str__(self):
        return f"[{self.error}] {self.description}"
