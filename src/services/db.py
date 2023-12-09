from pymongo import MongoClient

from src import env

from src.database.hsalen.backend import backend_logs
from src.database.hsalen.private import logging_private
from src.database.hsalen.public import logging_public
from src.database.admin.user import user_dict

client = MongoClient(env.DB_CONNECTION_LOGGING)
proces = client[env.DB_PROCES]


def drop_log():
    proces.logging_private.drop()
    proces.logging_public.drop()
    proces.backend_logs.drop()
    proces.user_dict.drop()
    pass


def seed_log():
    proces.logging_private.insert_many(logging_private)
    proces.logging_public.insert_many(logging_public)
    proces.backend_logs.insert_many(backend_logs)
    proces.user_dict.insert_many(user_dict)
    pass
