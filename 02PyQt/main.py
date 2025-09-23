import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# 音乐文件存储目录（请替换为你的实际 MP3 文件夹路径）
MUSIC_DIR = "./music"  # 请替换为你的音乐文件夹路径

@app.get("/music/{filename}")
async def get_music_file(filename: str):
    """提供指定 MP3 文件的下载/流式传输"""
    file_path = os.path.join(MUSIC_DIR, filename)
    if os.path.exists(file_path) and os.path.isfile(file_path) and file_path.lower().endswith(".mp3"):
        return FileResponse(file_path, media_type="audio/mpeg")
    return {"error": "文件不存在或格式不正确"}

if __name__ == "__main__":
    uvicorn.run(
        app,  # 这种无法热重载
        host="127.0.0.1",
        port=8080,
        log_level="debug"
    )