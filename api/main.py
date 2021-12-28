from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import engine
import users.router as users
import items.router as items

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


