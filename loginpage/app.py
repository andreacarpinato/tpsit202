from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

def validate(username, password):
    completion = False
    with sqlite3.connect('/home/andrea/Scrivania/loginpage/static/db.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion

def usernameEsistente(username):
    esistente=False
    with sqlite3.connect('/home/andrea/Scrivania/loginpage/static/db.db') as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    if dbUser==username:
                        esistente= True
    return esistente



def check_password(hashed_password, user_password): #ritorna true o false se sono uguali dal db
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route('/register',methods=['GET', 'POST'])  
def create():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2= request.form['password2']
        userEsiste=usernameEsistente(username)
        while userEsiste == True:
            error='username gia usato'
            username = request.form['username']
            
        while password != password2:
            error= 'password diverse'
            password = request.form['password']
            password2= request.form['password2']

        conn=sqlite3.connect('/home/andrea/Scrivania/loginpage/static/db.db')
        c=conn.cursor()
        print(f'INSERT INTO USERS ("username", "password") VALUES ("{username}", "{password}")')
        c.execute(f'INSERT INTO USERS ("username", "password") VALUES ("{username}", "{password}")')
        c.execute('commit') #salva modifiche db
        c.close()
        conn.close()
        
    return render_template('register.html', error=error)


@app.route('/secret')
def secret():
    return "This is a secret page!"

if __name__== "__main__":
    app.run()