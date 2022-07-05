import motor.motor_asyncio
from data.config import CONNECT_STR_MONGO


client = motor.motor_asyncio.AsyncIOMotorClient(CONNECT_STR_MONGO)
db = client["memo-flashcards"]

CARDS = db["Cards"]

async def insert_document(collection, data: dict, multiple=False) -> None or int:
    if multiple:
        await collection.insert_many(data)
    else:
        await collection.insert_one(data)


async def find_document(collection, elements: dict, multiple=False) -> list or dict:
    if multiple:
        answer = []
        async for document in collection.find(elements):
            answer.append(document)
        return answer
    else:
        return await collection.find_one(elements)


async def get_all_documents(collection) -> list:
    answer = list()
    async for doc in collection.find():
        answer.append(doc)
    return answer


async def delete_document(collection, id_) -> None:
    await collection.delete_one({"_id": id_})


async def update_document(collection, id_, doc: dict) -> None:
    await collection.update_one({"_id": id_}, {'$set': doc})
