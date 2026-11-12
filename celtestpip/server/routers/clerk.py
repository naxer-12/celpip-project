"""Offline Clerk Authentication Provider Mock.

Emulates Clerk single-session responses so the Next.js frontend hydrates smoothly
without external network calls, network errors, or authentication dialogs.
"""

from typing import Dict, Any
from fastapi import APIRouter

router = APIRouter(tags=["Clerk Auth"])


@router.get("/v1/client")
@router.post("/v1/client")
@router.get("/v1/client/{subpath:path}")
@router.post("/v1/client/{subpath:path}")
def mock_clerk_client(subpath: str = "") -> Dict[str, Any]:
    """Mock Clerk client session for offline guest testing."""
    return {
        "response": {
            "status": "ok",
            "client": {
                "id": "client_tester",
                "sessions": [
                    {
                        "id": "sess_tester",
                        "status": "active",
                        "user": {
                            "id": "tester",
                            "primaryEmailAddress": {"emailAddress": "tester@celtestpip.local"},
                        },
                    }
                ],
                "lastActiveSessionId": "sess_tester",
            },
        }
    }


@router.get("/v1/environment")
@router.get("/v1/environment/{subpath:path}")
def mock_clerk_environment(subpath: str = "") -> Dict[str, Any]:
    """Mock Clerk environment configuration."""
    return {
        "authConfig": {"singleSessionMode": True},
        "userSettings": {},
        "displayConfig": {},
    }
