import crud
import models
import schemas
from database import get_db
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session 
# Task 5 - Import Here

# ------------------------------

app = FastAPI()


@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

# Task 5 - Code here
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip:int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not sound")
    return db_user

@app.get("/users/email/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    if user_email is None:
        raise HTTPException(status_code=400, detail="Invalid Email")
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db=db, user=user)

@app.put("/users", response_model=schemas.User)
def update_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return crud.update_user(db=db, user=user)
    raise HTTPException(status_code=400, detail="User Not Found.")

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db:Session=Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user:
        return crud.delete_user(db, user_id=user_id)
    raise HTTPException(status_code=404, detail="User not found.")