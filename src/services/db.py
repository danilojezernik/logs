from pymongo import MongoClient

from src import env

from src.database.logging import logging

client = MongoClient(env.DB_CONNECTION_LOGGING)
proces = client[env.DB_PROCES_LOGGING]


def drop_log():
    proces.logging.drop()
    pass


def seed_log():
    proces.logging.insert_many(logging)
    pass
