import flask
from flask import Flask, render_template, redirect, url_for, request,jsonify
import sqlite3 as sq

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET','POST'])
def __main__():
    return render_template('homepage.html')


#--------
@app.route('/api/insertdb',methods=['GET','POST'])
def inserisci():
    error = None
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        conn=sq.connect('libri.db')
        c=conn.cursor()
        print(f'INSERT INTO Libri("title","author","year_published") VALUES ("{title}", "{author}","{year}")')
        c.execute(f'INSERT INTO Libri("title","author","year_published") VALUES ("{title}", "{author}","{year}")')
        c.execute('commit') #salva modifiche db
        c.close()
        conn.close()
        return render_template('insert.html')
    else :
        return render_template('insert.html')
    

@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(libri)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    print(request.args)
    if 'id' in request.args:
        id = int(request.args['id'])

    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for libro in libri:
            if libro['id'] == id:
                results.append(libro)
    return jsonify(results)
  #lettura db
libri=[]
with sq.connect('/home/andrea/Scrivania/webapi/webApiDb/libri.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Libri")
    rows = cur.fetchall()
    k=0

    for row in rows:
        a={'id':row[0],'title':row[1],'author':row[2],'year_published':row[3]}
        libri.append(a)
    print(libri)

cur.close()
con.close()

    #for book in books:
    #    if book['id'] == id:
    #        results.append(book)
    #return jsonify(results)



'''
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
'''
if __name__ == "__main__":
    app.run()