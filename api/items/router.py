from typing import List

from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session

from api.items import crud, schemas
from ..dependencies import get_db


router = APIRouter()



@router.post("/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.items.get_items(db, skip=skip, limit=limit)
    return items