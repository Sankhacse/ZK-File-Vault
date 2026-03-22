# server/auth.py
import random
from common.config import p, g
from common.utils import load_users

USERS_DB = "server/users.json"

challenges = {}

def get_public_v(username):
    users = load_users(USERS_DB)
    return users.get(username, {}).get("v")

def generate_challenge(username, x):
    c = random.randint(1, 10)
    challenges[username] = (x, c)
    return c

def verify(username, y):
    users = load_users(USERS_DB)
    v = users[username]["v"]
    x, c = challenges[username]

    left = pow(g, y, p)
    right = (x * pow(v, c, p)) % p

    return left == right