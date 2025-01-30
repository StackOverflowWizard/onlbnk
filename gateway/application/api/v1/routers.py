import httpx
from fastapi import APIRouter, HTTPException

AUTH_SERVICE_URL = "http://auth:8000"
USERS_SERVICE_URL = "http://users:8001"

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USERS_SERVICE_URL}/users/{user_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="User not found")
        return response.json()


@router.post("/auth/verify")
async def verify_token(token: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/auth/verify", json={"token": token})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Invalid token")
        return response.json()
