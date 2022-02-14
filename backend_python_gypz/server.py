from starlette.applications import Starlette
from starlette.middleware import Middleware
from router import Router
from starlette.middleware.cors import CORSMiddleware

middleware = [Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])]
app = Starlette(debug=True, routes=Router.get_routes(), middleware=middleware)
