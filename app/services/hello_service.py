from app.models.hello import HelloResponse


class HelloService:
    """Service responsible for greeting logic."""

    def get_greeting(self) -> HelloResponse:
        return HelloResponse(message="¡Hola desde FastAPI!")


def get_hello_service() -> HelloService:
    return HelloService()
