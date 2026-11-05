"""Tiny SQLite helper for the demo shop."""
import sqlite3


def get_conn(path="shop.db"):
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE IF NOT EXISTS coupons (code TEXT PRIMARY KEY, pct INTEGER NOT NULL)")
    return conn
