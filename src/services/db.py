from pymongo import MongoClient

from src import env

from src.database.hsalen.private import logging_private
from src.database.hsalen.public import logging_public
from src.database.admin.user import user_dict

client = MongoClient(env.DB_CONNECTION_LOGGING)

# HYPNOSIS STUDIO ALEN COLLECTION
proces = client[env.DB_PROCES_PRIVATE_HSA_LOGGING]


def drop_log():
    proces.logging_private.drop()
    proces.logging_public.drop()
    proces.user_dict.drop()
    pass


def seed_log():
    proces.logging_private.insert_many(logging_private)
    proces.logging_public.insert_many(logging_public)
    proces.user_dict.insert_many(user_dict)
    pass
