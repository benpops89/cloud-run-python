from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def homepage(request):
    return PlainTextResponse("Hello World!")

routes = [
    Route("/", endpoint=homepage),
]

app = Starlette(routes=routes)
