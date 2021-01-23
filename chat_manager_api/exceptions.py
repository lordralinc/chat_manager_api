class ChatManagerAPIException(Exception):

    def __init__(
            self,
            id: int = 0,
            error: str = "",
            **kwargs
    ):
        self.id = id
        self.error = error
        self.kwargs = kwargs

    def __repr__(self):
        return f"<ChatManagerAPIException: id={self.id}, msg={self.error}>"

    def __str__(self):
        return f"[{self.id}] {self.error}"
