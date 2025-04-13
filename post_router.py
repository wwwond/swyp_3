from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import crud, schemas
from database import SessionLocal, engine
import model

# 라우터 생성
router = APIRouter()

# 테이블 생성 (서버 시작 시 한 번만 수행됨)
model.Base.metadata.create_all(bind=engine)

# DB 세션 의존성 주입 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE - 게시글 생성
@router.post("/posts", response_model=schemas.PostRead, status_code=201)
def create(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

# READ - 전체 게시글 조회
@router.get("/posts", response_model=list[schemas.PostRead])
def read_all(db: Session = Depends(get_db)):
    return crud.get_posts(db)

# READ - 특정 게시글 조회
@router.get("/posts/{post_id}", response_model=schemas.PostRead)
def read_one(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# UPDATE - 특정 게시글 수정
@router.put("/posts/{post_id}", response_model=schemas.PostRead)
def update(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# DELETE - 특정 게시글 삭제
@router.delete("/posts/{post_id}", status_code=204)
def delete(post_id: int, db: Session = Depends(get_db)):
    success = crud.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": f"Post {post_id} has been deleted"}


## 예외처리는 특정 게시물을 찾지 못했을 때의 대비해서만 달아놓았습니다.