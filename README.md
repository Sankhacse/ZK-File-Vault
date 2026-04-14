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

## 🔑 Core idea

Traditional systems:

* Send password / hash to server
* Server can be attacked

This project:

* Proves knowledge of password without revealing it
* Uses the **Schnorr Identification Protocol**

---

## 🔐 Authentication flow (ZKP)

**Client → Server interaction**

### Register

* Generate secret `s`
* Compute `v = g^s mod p`
* Send `(username, v)` to server

### Login

1. Client computes:

   ```
   x = g^r mod p
   ```

   → sends to server

2. Server sends challenge:

   ```
   c
   ```

3. Client responds:

   ```
   y = r + c*s mod q
   ```

4. Server verifies:

   ```
   g^y == x * v^c mod p
   ```

👉 Password is **never transmitted**

---

## 🔐 File security

* Encryption: **AES-256-GCM**
* Key derivation: **Argon2**

### Flow

```
Password → Key → Encrypt file → Upload
```

👉 Server stores only:

* encrypted file
* cannot decrypt it

---

## 📁 Project structure

```
ZK-File-Vault/
│
├── client/
│   ├── client.py
│   ├── schnorr.py
│   ├── crypto.py
│
├── server/
│   ├── server.py
│   ├── auth.py
│   ├── storage.py
│
├── common/
│   ├── config.py
│   ├── utils.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to run (local setup)

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 2: Start the server

```bash
uvicorn server.server:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### Step 3: Open API docs

```
http://127.0.0.1:8000/docs
```

---

### Step 4: Register a user

Use `/register` endpoint:

```
username: your_name
password: your_password
```

---

### Step 5: Run the client

```bash
python -m client.client
```

---

### Step 6: Login

```
Username: your_name
Password: your_password
```

---

### Step 7: Upload file

```
Enter file path: test.txt
```

👉 File will be:

* encrypted locally
* uploaded securely

---

### Step 8: Verify upload

Go to `/docs` → `/files`

```
username: your_name
```

Output:

```
["test.txt"]
```

---

## 🌐 Running on render (cloud)

### Deploy backend

* Push code to GitHub
* Connect repository to Render

Use:

Build command:

```
pip install -r requirements.txt
```

Start command:

```
uvicorn server.server:app --host 0.0.0.0 --port 10000
```

---

### Access server

```
https://your-app.onrender.com
```

API docs:

```
https://your-app.onrender.com/docs
```

---

### Connect client

Edit:

```
common/config.py
```

```python
SERVER_URL = "https://your-app.onrender.com"
```

---

### Run client

```bash
python -m client.client
```

---

## 📡 API endpoints

### Authentication

* `POST /register`
* `POST /login/start`
* `POST /login/verify`

---

### File operations

* `POST /upload`
* `GET /files`
* `GET /download`

---

### Utility

* `GET /` → server status
* `GET /docs` → API interface

---

## 🛡️ Security features

* Zero-knowledge authentication
* No password storage
* Client-side encryption
* AES-256-GCM encryption
* Argon2 key derivation

---

## ⚠️ Limitations

* Render free tier uses temporary storage
* No database (JSON-based storage)
* Demo-level cryptographic parameters

---

## 🎯 Demo flow

1. Open `.com` → show server running
2. Open `/docs`
3. Register user
4. Run client → login
5. Upload file
6. Show `/files`
7. Explain encryption and ZKP

---

## 💡 Key highlight

Even if the server is compromised:

* Password remains safe
* File content remains encrypted

---

## 🔥 Final note

This project demonstrates a strong combination of:

* Cryptography
* Backend development
* Secure system design

---

