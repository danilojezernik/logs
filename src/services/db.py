from pymongo import MongoClient

from src import env

from src.database.hsalen.logging_private import logging_private
from src.database.hsalen.logging_public import logging_public

client = MongoClient(env.DB_CONNECTION_LOGGING)

# HYPNOSIS STUDIO ALEN COLLECTION
private_hsa = client[env.DB_PROCES_PRIVATE_HSA_LOGGING]
public_hsa = client[env.DB_PROCES_PUBLIC_HSA_LOGGING]


def drop_log():
    private_hsa.logging.drop()
    public_hsa.logging.drop()
    pass


def seed_log():
    private_hsa.logging.insert_many(logging_private)
    public_hsa.logging.insert_many(logging_public)
    pass
