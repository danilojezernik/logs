from pymongo import MongoClient

from src import env

from src.database.hsalen.private import logging_private
from src.database.hsalen.public import logging_public


client = MongoClient(env.DB_CONNECTION_LOGGING)

# HYPNOSIS STUDIO ALEN COLLECTION
proces = client[env.DB_PROCES_LOGGING]


def drop_log():
    proces.logging_private.drop()
    proces.logging_public.drop()
    pass


def seed_log():
    proces.logging_private.insert_many(logging_private)
    proces.logging_public.insert_many(logging_public)
    pass
