import os
import json

from flask import Flask as FLERSK
from flask import jsonify as JERSERNERFER
from flask import request as RERKWERST
from flask import g
from peewee import PostgresqlDatabase

from .database import close_db, connect_db, db, get_db
from .ermahgerd import ermahgerd
from .models import init_db


################################################################################
# Application config ###########################################################

ERP = FLERSK(__name__)
DERBERG = os.environ.get('DEBUG') == '1'
PERT = int(os.environ.get('PORT', 8000))
HERST = '0.0.0.0'


################################################################################
# Manage db connections ########################################################

@ERP.teardown_appcontext
def clean_up(error):
    return close_db(error)

@ERP.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized database')


################################################################################
# Routes and helper methods ####################################################

def prersers_erterm(text_item):
    """
    Expects an object that has a `text` property;
    if you are reinserting this into a document, etc., you may want to 
    have another property which somehow identifies where the text came
    from... this method simply returns that object untouched other than
    the `text` property
    """
    text_item['text'] = ermahgerd(text_item['text'])
    return text_item

@ERP.route('/trernsferm', methods=['POST'])
def trernsferm_terxt():
    text = json.loads(RERKWERST.get_json())

    if not text:
        return JERSERNERFER({ 'message': 'no post content' }), 400

    try:
        terxt = map(prersers_erterm, text)
        return JERSERNERFER(terxt), 200
    except KeyError:
        return JERSERNERFER({ 'message': 'key error in dictionary' }), 400


################################################################################
# App start ####################################################################

if __name__ == '__main__':
    ERP.run(debug=DERBERG, host=HERST, port=PERT)

