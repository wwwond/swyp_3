from sqlalchemy import Column, Integer, String, Text, TIMESTAMP,VARCHAR, func
from database import Base, engine
# Base 클래스와 DB 엔진을 가져옴 (database.py에서 정의한 것)

class Post(Base):
    # 테이블 이름 설정 → 실제 DB에 생성될 이름
    __tablename__ = "posts_test"

    # 동일한 테이블이 여러 번 정의되는 경우 충돌 방지 
    __table_args__ = {'extend_existing': True}  # 중복 정의 허용

    id = Column(Integer, primary_key=True, index=True) # 기본키
    title = Column(VARCHAR(100)) # 제목 
    content = Column(Text) # 내용
    author = Column(VARCHAR(50)) # 작성자
    created_at = Column(TIMESTAMP, server_default=func.now()) # 생성 시간

if __name__ == "__main__":
    print("테이블 생성 안됨") # .py 출력 확인용 
    Base.metadata.create_all(bind=engine)  # DB에 테이블 생성
    print("테이블 생성 완료")