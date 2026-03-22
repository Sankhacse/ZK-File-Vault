from fastapi import FastAPI, UploadFile, File
from server.auth import generate_challenge, verify, get_public_v
from server.storage import save_file, list_files, get_file
from common.utils import load_users, save_users
from common.config import p, g, q

app = FastAPI()

# In-memory session store
sessions = {}

# =========================
# ROOT (optional, removes 404)
# =========================
@app.get("/")
def home():
    return {"message": "ZK File Vault Server is running 🚀"}


# =========================
# REGISTER USER
# =========================
@app.post("/register")
def register(username: str, password: str):
    users = load_users("server/users.json")

    if username in users:
        return {"error": "User already exists"}

    # Schnorr key generation
    s = int.from_bytes(password.encode(), 'big') % q
    v = pow(g, s, p)

    users[username] = {"v": v}
    save_users("server/users.json", users)

    return {"status": "registered"}


# =========================
# LOGIN START (ZKP Step 1)
# =========================
@app.post("/login/start")
def login_start(username: str, x: int):
    v = get_public_v(username)

    if v is None:
        return {"error": "User not found"}

    c = generate_challenge(username, x)
    return {"challenge": c}


# =========================
# LOGIN VERIFY (ZKP Step 2)
# =========================
@app.post("/login/verify")
def login_verify(username: str, y: int):
    if verify(username, y):
        sessions[username] = True
        return {"status": "success"}

    return {"status": "fail"}


# =========================
# UPLOAD FILE
# =========================
@app.post("/upload")
async def upload(username: str, file: UploadFile = File(...)):
    if username not in sessions:
        return {"error": "Not authenticated"}

    data = await file.read()
    save_file(username, file.filename, data)

    return {"status": "uploaded"}


# =========================
# LIST FILES
# =========================
@app.get("/files")
def files(username: str):
    if username not in sessions:
        return {"error": "Not authenticated"}

    return {"files": list_files(username)}


# =========================
# DOWNLOAD FILE
# =========================
@app.get("/download")
def download(username: str, filename: str):
    if username not in sessions:
        return {"error": "Not authenticated"}

    data = get_file(username, filename)

    if data is None:
        return {"error": "File not found"}

    return data