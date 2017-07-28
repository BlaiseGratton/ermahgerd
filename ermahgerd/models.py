from peewee import *
from .database import db, get_db


class BaseModel(Model):
    class Meta:
        database = db


class ExtraArpabet(BaseModel):
    word = TextField(unique=True)
    date_created = DateTimeField()


class ArpabetSyllable(BaseModel):
    value = TextField()
    order = IntegerField()
    word = ForeignKeyField(
            ExtraArpabet,
            related_name='arpabet_syllables'
           )


def init_db():
    db = get_db()
    with db.transaction():
        db.create_tables(
            [ArpabetSyllable, ExtraArpabet],
            safe=True
        )
    db.close()

