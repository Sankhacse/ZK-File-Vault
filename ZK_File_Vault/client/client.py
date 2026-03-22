# client/client.py
import requests
from client.schnorr import generate_keys, generate_commitment, compute_response
from client.crypto import derive_key, encrypt, decrypt
from common.config import SERVER_URL

username = input("Username: ")
password = input("Password: ")

# Step 1: generate keys
s, v = generate_keys(password)

# Step 2: commitment
r, x = generate_commitment()

# Step 3: send to server
res = requests.post(f"{SERVER_URL}/login/start", params={"username": username, "x": x})
c = res.json()["challenge"]

# Step 4: response
y = compute_response(r, c, s)

res = requests.post(f"{SERVER_URL}/login/verify", params={"username": username, "y": y})

if res.json()["status"] != "success":
    print("Login failed")
    exit()

print("Login success!")

# File upload
key = derive_key(password)

filename = input("Enter file path: ")
with open(filename, "rb") as f:
    data = f.read()

enc = encrypt(data, key)

files = {"file": (filename, enc)}
requests.post(f"{SERVER_URL}/upload", params={"username": username}, files=files)

print("Uploaded!")