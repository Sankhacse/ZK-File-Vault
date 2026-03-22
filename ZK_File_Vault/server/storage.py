# server/storage.py
import os

BASE = "server/vault_storage"

def save_file(username, filename, data):
    user_dir = os.path.join(BASE, username)
    os.makedirs(user_dir, exist_ok=True)

    path = os.path.join(user_dir, filename)
    with open(path, "wb") as f:
        f.write(data)

def list_files(username):
    user_dir = os.path.join(BASE, username)
    if not os.path.exists(user_dir):
        return []
    return os.listdir(user_dir)

def get_file(username, filename):
    path = os.path.join(BASE, username, filename)
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return f.read()