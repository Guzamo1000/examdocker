from sqlalchemy.orm import Session
from app.user import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.User_Login, db: Session):
    new_user=models.User(name=request.name, number_phone=request.number_phone, email=request.emai, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", "object": new_user}

def delete(id: int, db: Session):
    user=db.query(models.User).filter(models.User==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} is not exis")
    user.delete(synchronize_session=False)
    db.commit()
    return {"status": "sucess", "object": user}

def show_all(db: Session):
    user=db.query(models.User).all()
    return user
def show_user_by_id(id: int, db: Session):
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} is not exis")
    return user.first()

def edit_profile(id: int, request: schemas.UseBase, db: Session):
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} is not exis")
    user.update(request)
    db.commit()
    return {"status":"success", "object": request}