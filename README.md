
# 🔐 ZK File Vault

### Zero-Knowledge Secure File Storage using Schnorr Protocol

---


## 🧠 Overview

This project implements a **secure file vault system** where:

* Users authenticate using **Zero-Knowledge Proof (ZKP)**
* Files are encrypted on the **client-side before upload**
* The server **never sees passwords or actual file data**

👉 This ensures that even if the server is compromised,
**user credentials and files remain secure**

---

## 🔑 Core Idea

Traditional systems:
❌ Send password / hash to server
❌ Server can be attacked

This project:
✅ Proves knowledge of password without revealing it
✅ Uses **Schnorr Identification Protocol**

---

## 🔐 Authentication Flow (ZKP)

## CLIENT                          SERVER

REGISTER
→ Generate secret `s`
→ Compute `v = g^s mod p`
→ Send `(username, v)`

LOGIN

1. Client generates:
   `x = g^r mod p`
   → sends to server

2. Server sends challenge:
   `c`

3. Client responds:
   `y = r + c*s mod q`

4. Server verifies:
   `g^y == x * v^c mod p`

👉 Password is **never transmitted**

---

## 🔐 File Security

* Encryption: **AES-256-GCM**
* Key Derivation: **Argon2**

### Flow:

Password → Key → Encrypt File → Upload

👉 Server stores only:

* encrypted file
* cannot decrypt it

---

## 📁 Project Structure

```
ZK-File-Vault/
│
├── client/
│   ├── client.py        # CLI client
│   ├── schnorr.py       # ZKP logic
│   ├── crypto.py        # encryption
│
├── server/
│   ├── server.py        # FastAPI backend
│   ├── auth.py          # authentication logic
│   ├── storage.py       # file storage
│
├── common/
│   ├── config.py        # shared config
│   ├── utils.py         # helpers
│
├── requirements.txt
└── README.md
```

---

# 🚀 HOW TO RUN (LOCAL SETUP)

## 🔹 Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Step 2: Start the server

```bash
uvicorn server.server:app --reload
```

👉 Server runs at:

```
http://127.0.0.1:8000
```

---

## 🔹 Step 3: Open API docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 Step 4: Register a user

Use `/register` endpoint:

```
username: sankha
password: xyz
```

---

## 🔹 Step 5: Run the client

Open a new terminal:

```bash
python -m client.client
```

---

## 🔹 Step 6: Login

Enter:

```
Username: sankha
Password: xyz
```

---

## 🔹 Step 7: Upload file

```
Enter file path: test.txt
```

👉 File will be:

* encrypted locally
* uploaded securely

---

## 🔹 Step 8: Verify upload

Go to `/docs` → `/files`

```
username: sankha
```

👉 Output:

```
["test.txt"]
```

---

# 🌐 RUN ON RENDER (CLOUD)

## 🔹 Deploy backend

* Push code to GitHub
* Connect repo to Render
* Use:

Build:

```
pip install -r requirements.txt
```

Start:

```
uvicorn server.server:app --host 0.0.0.0 --port 10000
```

---

## 🔹 Access server

```
https://your-app.onrender.com
```

Docs:

```
https://your-app.onrender.com/docs
```

---

## 🔹 Connect client

Edit:

```
common/config.py
```

```python
SERVER_URL = "https://your-app.onrender.com"
```

---

## 🔹 Run client again

```bash
python -m client.client
```

---

# 📡 API ENDPOINTS

## 🔐 Authentication

* POST `/register`
* POST `/login/start`
* POST `/login/verify`

---

## 📂 File Operations

* POST `/upload`
* GET `/files`
* GET `/download`

---

## 🧪 Utility

* GET `/` → server status
* GET `/docs` → API UI

---

# 🛡️ SECURITY FEATURES

* Zero-Knowledge Authentication
* No password storage
* Client-side encryption
* AES-256-GCM
* Argon2 key derivation

---

# ⚠️ LIMITATIONS

* Render free tier → temporary storage
* No database (JSON-based storage)
* Small cryptographic parameters (demo purpose)

---

# 🎯 DEMO FLOW (FOR PRESENTATION)

1. Open `.com` → show server running
2. Open `/docs`
3. Register user
4. Run client → login
5. Upload file
6. Show `/files`
7. Explain encryption + ZKP

---

# 💡 KEY HIGHLIGHT

👉 Even if server is hacked:

* Password is safe
* File content is safe

---

# 🔥 FINAL NOTE

This project demonstrates a strong combination of:

* Cryptography
* Backend development
* Secure system design

