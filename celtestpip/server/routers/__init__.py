"""Router package exporting all modular endpoints for CELTESTPIP."""

from celtestpip.server.routers.exams import router as exams_router
from celtestpip.server.routers.practices import router as practices_router
from celtestpip.server.routers.vocabulary import router as vocabulary_router
from celtestpip.server.routers.user import router as user_router
from celtestpip.server.routers.clerk import router as clerk_router
from celtestpip.server.routers.assets import router as assets_router
from celtestpip.server.routers.pages import router as pages_router

__all__ = [
    "exams_router",
    "practices_router",
    "vocabulary_router",
    "user_router",
    "clerk_router",
    "assets_router",
    "pages_router",
]
