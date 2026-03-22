# server/server.py
from fastapi import FastAPI, UploadFile, File
from server.auth import generate_challenge, verify, get_public_v
from server.storage import save_file, list_files, get_file

app = FastAPI()

sessions = {}

@app.post("/login/start")
def login_start(username: str, x: int):
    v = get_public_v(username)
    if v is None:
        return {"error": "User not found"}

    c = generate_challenge(username, x)
    return {"challenge": c}

@app.post("/login/verify")
def login_verify(username: str, y: int):
    if verify(username, y):
        sessions[username] = True
        return {"status": "success"}
    return {"status": "fail"}

@app.post("/upload")
async def upload(username: str, file: UploadFile = File(...)):
    if username not in sessions:
        return {"error": "Not authenticated"}

    data = await file.read()
    save_file(username, file.filename, data)
    return {"status": "uploaded"}

@app.get("/files")
def files(username: str):
    return {"files": list_files(username)}

@app.get("/download")
def download(username: str, filename: str):
    data = get_file(username, filename)
    if data is None:
        return {"error": "Not found"}
    return data