from application.common.exception import ServiceException
from fastapi import APIRouter, HTTPException, status

router = APIRouter()

fake_users_db = {1: {"name": "John Doe"}, 2: {"name": "Jane Doe"}}


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": user["name"]}
