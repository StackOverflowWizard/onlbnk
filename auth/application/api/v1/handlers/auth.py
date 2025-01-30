from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post("/verify", status_code=status.HTTP_200_OK)
async def verify_handler(token: str):
    if not token:
        raise HTTPException(status_code=400, detail="Token is required")
    # Заглушка для проверки токена
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Token is valid"}
