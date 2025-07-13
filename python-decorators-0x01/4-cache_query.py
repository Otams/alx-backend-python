import time
import sqlite3 
import functools

# ✅ Simple in-memory cache
query_cache = {}

# ✅ Decorator to manage DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Returning cached result ✅")
            return query_cache[query]
        print("Executing query and caching result 🗃️")
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

# ✅ Function using both decorators
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ✅ First call (caches the result)
users = fetch_users_with_cache(query="SELECT * FROM users")

# ✅ Second call (uses cache)
users_again = fetch_users_with_cache(query="SELECT * FROM users")
