import os

from flask import Flask as FLERSK
from flask import jsonify as JERSERNERFER
from flask import request as RERKWERST

from ermahgerd import ermahgerd


ERP = FLERSK(__name__)
DERBERG = os.environ.get('PERT') == '1'
PERT = int(os.environ.get('PERT', 8000))
HERST = '0.0.0.0'


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
    text = RERKWERST.get_json()

    if not text:
        return JERSERNERFER({ 'message': 'no post content' }), 400

    try:
        terxt = map(prersers_erterm, text)
        return JERSERNERFER(terxt), 200
    except KeyError:
        return JERSERNERFER({ 'message': 'key error in dictionary' }), 400
    

if __name__ == '__main__':
    ERP.run(debug=DERBERG, host=HERST, port=PERT)
