import motor.motor_asyncio
from data.config import CONNECT_STR_MONGO


client = motor.motor_asyncio.AsyncIOMotorClient(CONNECT_STR_MONGO)
db = client["memo-flashcards"]
ACCOUNTS = db["Account"]


async def insert_many(collection, data: list) -> int:
    await collection.insert_many(data)


async def insert_one(collection, data: dict) -> int:
    await collection.insert_one(data)


async def find_one(collection, elements: dict) -> dict or None:
    return await collection.find_one(elements)


async def find_many(collection, elements: dict) -> list:
    answer = []
    async for document in collection.find(elements):
        answer.append(document)
    return answer


async def get_all(collection) -> list:
    answer = list()
    async for doc in collection.find():
        answer.append(doc)
    return answer


async def delete(collection, id_) -> None:
    await collection.delete_one({"_id": id_})


async def update(collection, id_, doc: dict) -> None:
    await collection.update_one({"_id": id_}, {'$set': doc})