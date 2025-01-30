import httpx
from fastapi import APIRouter, HTTPException

AUTH_SERVICE_URL = "http://auth:8000"
USERS_SERVICE_URL = "http://users:8001"

router = APIRouter()


@router.get("/gateway/users/{user_id}")
async def get_user(user_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{USERS_SERVICE_URL}/users/{user_id}", timeout=5.0)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="User service error")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="User service unavailable")


@router.post("/gateway/auth/verify")
async def verify_token(token: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{AUTH_SERVICE_URL}/auth/verify", json={"token": token}, timeout=5.0)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Auth service error")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Auth service unavailable")
