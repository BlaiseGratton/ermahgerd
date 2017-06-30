import os

from flask import Flask, jsonify, request

from ermahgerd import ermahgerd


app = Flask(__name__)
DEBUG = os.environ.get('PORT') == '1'
PORT = int(os.environ.get('PORT', 8000))
HOST = '0.0.0.0'


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


@app.route('/trernsferm', methods=['POST'])
def trernsferm_terxt():
    text = request.get_json()

    if not text:
        return jsonify({ 'message': 'no post content' }), 400

    try:
        terxt = map(prersers_erterm, text)
        return jsonify(terxt), 200
    except KeyError:
        return jsonify({ 'message': 'key error in dictionary' }), 400
    

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
