import flask
from flask import Flask, render_template, redirect, url_for, request,jsonify
import sqlite3 as sq
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def usernameEsistente(username):
    esistente=False
    with sqlite3.connect('data.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Utenti")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    if dbUser==username:
                        esistente= True
    return esistente

@app.route('/',methods=['GET','POST'])
def __main__():
    return render_template('homepage.html')

@app.route('/iscrizione',methods=['GET','POST'])
def iscrizione():
    error = None
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        #verifica se cè gia nome utente,inserisci quindi nome in db
        userEsiste=usernameEsistente(username)
        if userEsiste == True:
            error='username gia usato'
            username = request.form['username']
        else :
            conn=sq.connect('data.db')
            c=conn.cursor()
            print(f'INSERT INTO Utenti("Nome","password") VALUES ("{name}", "{password}")')
            c.execute(f'INSERT INTO Utenti("Nome","password") VALUES ("{name}", "{password}")')
            c.execute('commit') #salva modifiche db
            c.close()
            conn.close()

            return accesso()
@app.route('/accesso',methods=['GET','POST'])
def accesso():

    return render_template(index.html)

def send(nameDest,idMitt,testo):
    t = datetime.datetime.now() #ora invio messaggio
    conn=sq.connect('data.db')
    c=conn.cursor()
    idDest=c.execute(f'Select id FROM Utenti(idDest,idMitt,testo,ora,ricevuto) WHERE name="{nameDest}"" ')
    c.execute(f'Insert INTO Messagi VALUES ("{idDest}", "{idMitt},"{testo}","{t}","no")')
    c.execute('commit') #salva modifiche db
    c.close()
    conn.close()


'''
URL PER MANDARE MESSAGGI
http://93.88.120.15:8082/api/v1/send?id_mitt=1&text=ciao&id_dest=2

URL PER RICEVERE MESSAGGI
http://93.88.120.15:8082/api/v1/receive?id_dest=2

URL PER JSON DI TUTTI GLI UTENTI'''
@app.route('/api/v1/user_list',methods=['GET']) 
def lista():
    conn=sq.connect('data.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Utenti")
    users=c.fetchall()
    c.close()
    conn.close()    
    for c in users:
        users[c]={users[c]}
        print(users[2])
    return jsonify(users)

    

app.run()