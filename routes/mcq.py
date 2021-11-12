from fastapi import APIRouter
from models.mcq import Mcq
from config.db import conn
from schemas.mcq import serializeDict, serializeList
from bson import ObjectId


mcq = APIRouter()


# route to get all the mcqs


@mcq.get('/')
async def get_all_mcq():
    return serializeList(conn.mcqdb.mcq.find())


# route to create mcq


@mcq.post('/')
async def create_mcq(mcq: Mcq):
    conn.mcqdb.mcq.insert_one(dict(mcq))
    return serializeList(conn.mcqdb.mcq.find())


# route to get one mcq


@mcq.get('/{id}')
async def get_one_mcq(id):
    return serializeDict(conn.mcqdb.mcq.find_one({"_id": ObjectId(id)}))


# route to update the mcq


@mcq.put('/{id}')
async def update_mcq(id, mcq: Mcq):
    conn.mcqdb.mcq.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(mcq)})
    return serializeDict(conn.mcqdb.mcq.find_one({"_id": ObjectId(id)}))


# route to delet the mcq


@mcq.delete('/{id}')
async def delete_mcq(id):
    return serializeDict(conn.mcqdb.mcq.find_one_and_delete({"_id": ObjectId(id)}))
