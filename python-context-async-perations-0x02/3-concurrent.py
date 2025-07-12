import asyncio
import aiosqlite

DB_PATH = "ALX_prodev.db"  # Replace with your actual SQLite DB file

async def async_fetch_users():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FROM user_data")
        rows = await cursor.fetchall()
        await cursor.close()
        print("All users:")
        for row in rows:
            print(row)

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FROM user_data WHERE age > 40")
        rows = await cursor.fetchall()
        await cursor.close()
        print("\nUsers older than 40:")
        for row in rows:
            print(row)

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
