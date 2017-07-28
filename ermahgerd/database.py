from flask import g
from peewee import PostgresqlDatabase


db = PostgresqlDatabase('ermahgerd')


def connect_db():
    db.connect()
    return db


def get_db():
    """Open a db connection if there isn't one for the current app context"""
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db


def close_db(error):
    """Close db at the end of each request"""
    if hasattr(g, 'db'):
        g.db.close()

