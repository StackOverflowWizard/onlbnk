from application.common.exception import ServiceException
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_handler(
    user_id: int,
):
    try:
        return {"user_id": user_id}
    except ServiceException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
