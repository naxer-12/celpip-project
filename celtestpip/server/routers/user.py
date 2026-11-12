"""User Profile, Membership, and Practice Credits endpoints.

Provides unlocked mock status so all testers automatically have Pro access
and unlimited credits without requiring external billing or account setup.
"""

from typing import Dict, Any
from fastapi import APIRouter

router = APIRouter(tags=["User"])


@router.get("/api/user/membership")
def get_user_membership() -> Dict[str, Any]:
    """Return active Pro membership details for testing."""
    return {
        "isPremium": True,
        "isPro": True,
        "credits": 9999,
        "user": {
            "id": "tester",
            "email": "tester@celtestpip.local",
            "firstName": "CELPIP",
            "lastName": "Tester",
        },
    }


@router.get("/api/user/credits")
def get_user_credits() -> Dict[str, Any]:
    """Return unlimited test-taker practice credits."""
    return {"credits": 9999, "isPro": True, "isPremium": True}
