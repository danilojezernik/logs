from pymongo import MongoClient

from src import env

from src.database.hsalen.private import logging_private
from src.database.hsalen.public import logging_public


client = MongoClient(env.DB_CONNECTION_LOGGING)

# HYPNOSIS STUDIO ALEN COLLECTION
private_hsa = client[env.DB_PROCES_PRIVATE_HSA_LOGGING]
public_hsa = client[env.DB_PROCES_PUBLIC_HSA_LOGGING]


def drop_log():
    private_hsa.logging_private.drop()
    public_hsa.logging_public.drop()
    pass


def seed_log():
    private_hsa.logging_private.insert_many(logging_private)
    public_hsa.logging_public.insert_many(logging_public)
    pass
