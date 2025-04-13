from pydantic import BaseModel
# 데이터 검증용 Pydantic 모델 
# Pydantic이란 : Python 라이브러리로 타입 유효성 검사, 자동 형 변환
from datetime import datetime 

# 게시글 생성 시 사용하는 입력 모델 (요청용)
class PostCreate(BaseModel):
    title: str
    content: str
    author: str

# 게시글 조회 시 사용하는 출력 모델 (응답용)
# PostCreate를 받아서 코드 재사용 
class PostRead(PostCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
    # orm_mode 설정: SQLAlchemy 객체를 그대로 반환해도 Pydantic이 인식 가능하게 함
