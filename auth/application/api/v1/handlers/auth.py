from application.common.exception import ServiceException
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post("/verify", status_code=status.HTTP_200_OK)
async def verify_handler(token: str):
    try:
        return {"token": "secret"}
    except ServiceException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
