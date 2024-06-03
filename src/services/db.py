from pymongo import MongoClient

from src import env

from src.database.backend import backend_logs
from src.database.private import logging_private
from src.database.public import logging_public
from src.database.admin.user import user_dict
from src.database.geo_data import geo_data_log

client_hsa = MongoClient(env.DB_CONNECTION_LOGGING)
client_portfolio_dj = MongoClient(env.DB_CONNECTION_LOGGING_PDJ)
proces_hsa = client_hsa[env.DB_PROCES]
proces_portfolio_dj = client_hsa[env.DB_PROCES]


def drop_log():
    proces_hsa.logging_private.drop()
    proces_hsa.logging_public.drop()
    proces_hsa.backend_logs.drop()
    proces_hsa.geo_data_log.drop()

    proces_hsa.user_dict.drop()

    proces_portfolio_dj.logging_private.drop()
    proces_portfolio_dj.logging_public.drop()
    proces_portfolio_dj.backend_logs.drop()
    proces_portfolio_dj.geo_data_log.drop()

    proces_portfolio_dj.user_dict.drop()
    pass


def seed_log():
    proces_hsa.logging_private.insert_many(logging_private)
    proces_hsa.logging_public.insert_many(logging_public)
    proces_hsa.backend_logs.insert_many(backend_logs)
    proces_hsa.geo_data_log.insert_many(geo_data_log)

    proces_hsa.user_dict.insert_many(user_dict)

    proces_portfolio_dj.logging_private.insert_many(logging_private)
    proces_portfolio_dj.logging_public.insert_many(logging_public)
    proces_portfolio_dj.backend_logs.insert_many(backend_logs)
    proces_portfolio_dj.geo_data_log.insert_many(geo_data_log)

    proces_portfolio_dj.user_dict.insert_many(user_dict)
    pass
