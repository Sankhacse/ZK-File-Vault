# client/schnorr.py
import random
from common.config import p, g, q

def generate_keys(password):
    s = int.from_bytes(password.encode(), 'big') % q
    v = pow(g, s, p)
    return s, v

def generate_commitment():
    r = random.randint(1, q-1)
    x = pow(g, r, p)
    return r, x

def compute_response(r, c, s):
    return (r + c * s) % q