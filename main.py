from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 시에는 특정 도메인으로 제한하는 것이 안전
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return FileResponse("dist/index.html")  # Vue 빌드 후 경로 설정

@app.get("/{path:path}")
def serve_static_files(path: str):
    file_path = os.path.join("dist", path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return FileResponse("dist/index.html")