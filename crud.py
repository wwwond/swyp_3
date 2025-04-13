from sqlalchemy.orm import Session
from datetime import datetime
import model, schemas

# CREATE - 게시글 생성
def create_post(db: Session, post: schemas.PostCreate):
    db_post = model.Post(**post.dict()) # 받은 데이터로 Post 객체 생성
    db.add(db_post)                     # DB 세션에 객체 추가
    db.commit()                         # DB에 commit
    db.refresh(db_post)                 # db_post 재실행
    return db_post                      # 반환 

# READ - 전체 게시글 조회
def get_posts(db: Session):
    return db.query(model.Post).all() 

# READ - 단일 게시글 조회
def get_post(db: Session, post_id: int):
    return db.query(model.Post).filter(model.Post.id == post_id).first()

# UPDATE - 게시글 수정 
def update_post(db: Session, post_id: int, post: schemas.PostCreate):
    db_post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if db_post is None:
        return None                         # 없으면 none 반환
    for key, value in post.dict().items():
        setattr(db_post, key, value)        # 새로운 데이터로 필드 업데이트
    db_post.created_at = datetime.utcnow()  # 현재 시각으로 수정
    db.commit()
    db.refresh(db_post)
    return db_post

# DELETE - 게시글 삭제
def delete_post(db: Session, post_id: int):
    db_post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if db_post is None:
        return False                        # 수정과 별개로 삭제를 실패의 의미로 false로 반환하게 하였습니다. 
    db.delete(db_post)                      # 게시물 삭제
    db.commit()                             # db 반영
    return True                             # 삭제되어 True로 반환