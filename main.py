# main.py
from fastapi import FastAPI
from routers import post_router

app = FastAPI()
# 인스턴스 생성: app은 FastAPI 객체입니다.

# 라우터 포함
app.include_router(post_router.router)
# post_router 

@app.get("/")
def read_root():
    return {"message": "FastAPI is connected to SQL"}# 반환값은 JSON 형태로 응답을 보냅니다.