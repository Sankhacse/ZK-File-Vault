# common/utils.py
import json
import os

def load_users(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_users(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)