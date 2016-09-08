from peewee import *

db = PostgresqlDatabase('flask_dojo')


class BaseModell(Model):
    class Meta:
        database = db


class Counter(BaseModell):
    method = CharField()
    time = DateTimeField()
