"""Offline Clerk Authentication Provider Mock.

Emulates Clerk single-session and guest responses so the Next.js frontend hydrates smoothly
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
    """Mock Clerk client guest session for offline guest testing."""
    return {
        "response": {
            "status": "ok",
            "object": "client",
            "id": "client_guest",
            "sessions": [],
            "sign_in": None,
            "sign_up": None,
            "last_active_session_id": None,
            "last_authentication_strategy": None,
            "cookie_expires_at": None,
            "captcha_bypass": False,
            "created_at": 1794636868387,
            "updated_at": 1794636868387,
        },
        "client": None,
    }


@router.get("/v1/environment")
@router.get("/v1/environment/{subpath:path}")
def mock_clerk_environment(subpath: str = "") -> Dict[str, Any]:
    """Mock Clerk environment configuration."""
    return {
        "authConfig": {"singleSessionMode": True},
        "auth_config": {
            "object": "auth_config",
            "id": "aac_guest",
            "single_session_mode": True,
            "identification_requirements": [["email_address"], []],
            "identification_strategies": ["email_address"],
            "first_factors": ["email_code"],
            "second_factors": [],
        },
        "displayConfig": {},
        "display_config": {
            "object": "display_config",
            "id": "display_config_guest",
            "instance_environment_type": "production",
            "application_name": "CELTESTPIP",
            "home_url": "/",
            "sign_in_url": "/exams",
            "sign_up_url": "/exams",
            "logo_link_url": "/",
        },
        "userSettings": {},
        "user_settings": {
            "attributes": {
                "email_address": {"enabled": True, "required": True},
            },
        },
    }

