from fastapi import APIRouter, Depends
from app.user import database, schemas,models
from sqlalchemy.orm import Session
from app.user.repository import User_Repository
router = APIRouter()


@router.post("/create_user")
def create(request: schemas.User_Login, db: Session=Depends(database.get_db)):
    return User_Repository.create(request=request, db=db)

@router.get("/show_user/{id}")
def get_user_by_id(id: int, db: Session=Depends(database.get_db)):
    return User_Repository.show_user_by_id(id,db)

@router.get("/show_all_user")
def show_all_user(db: Session=Depends(database.get_db)):
    return User_Repository.show_all(db)

@router.delete("/delete_user/{id}")
def delete_user(id: int, db: Session=Depends(database.get_db)):
    return User_Repository.delete(id, db)

@router.patch("/edit_profile/{id}")
def edit_profile(id: int, request: schemas.UseBase, db: Session=Depends(database.get_db)):
    return User_Repository.edit_profile(id, request,db)

