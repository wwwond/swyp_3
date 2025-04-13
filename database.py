from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:dbdbdbdb@localhost:3306/test_db"
# 실제 db 주소
 
engine = create_engine(DATABASE_URL)
# 🔌 SQLAlchemy 엔진 생성: 실제 DB와 연결을 관리하는 객체

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# DB와 트랜잭션을 다룰 수 있는 세션을 생성하는 팩토리
# 직접 commit 필요, # 자동 플러시 비활성화 → flush도 직접 호출 가능

Base = declarative_base()
# 모델 정의 시 상속받을 베이스 클래스 생성