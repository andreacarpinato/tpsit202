import flask
from flask import jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di webAPI.</p>"

@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    print(request.args)
    if 'id' in request.args:
        id = int(request.args['id'])

    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)

books = [
{'id': 0,
'title': 'Il nome della Rosa',
'author': 'Umberto Eco',
'year_published': '1980'},
{'id': 1,
'title': 'Il problema dei tre corpi',
'author': 'Liu Cixin',
'published': '2008'},
{'id': 2,
'title': 'Fondazione',
'author': 'Isaac Asimov',
'published': '1951'}
]

app.run()