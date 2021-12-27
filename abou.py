import MySQLdb.cursors
from flask import Flask, render_template, request, redirect, url_for,flash,json,session

from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'projet_bd'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('Acceuil.html' )
@app.route('/base')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  *  FROM client")
    data = cur.fetchall()
    cur.close()
    return render_template('liste_emp.html', emps=data )
@app.route('/explorer')
def expo():
    return render_template('explorer.html' )

@app.route('/Accueil')
def maison():
    return render_template('Acceuil.html' )

@app.route('/inscrire')
def kah():
    return render_template('exojava.html' )

@app.route('/toyota')
def toyota():
    return render_template('toyota.html' )

@app.route('/mercedes')
def mercedes():
    return render_template('mercedes.html' )

@app.route('/bmw')
def bmw():
    return render_template('bmw.html' )

@app.route('/ford')
def ford():
    return render_template('ford.html' )

@app.route('/renault')
def renault():
    return render_template('renault.html' )

@app.route('/statistiques')
def statistiques():
    return render_template('statistiques.html' )

@app.route('/kj')
def kj():
    return render_template('kj.html' )

@app.route('/kn')
def kn():
    return render_template('kn.html' )

@app.route('/deco')
def deco():
    return render_template('deco.html' )


@app.route('/sign',methods=['POST','GET'])
def sign():
    if request.method=="GET":
        return "Login via the login form"
    if request.method=='POST':
        nom_client=request.form['nom_client']
        Email=request.form['Email']
        mot_de_passe=request.form['mot_de_passe']
        date_naissance=request.form['date_naissance']
        pays=request.form['pays']
        genre=request.form['genre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO client (nom_client, Email, mot_de_passe,date_naissance,pays,genre) VALUES (%s, %s, %s, %s, %s,%s)",
                    (nom_client, Email, mot_de_passe,date_naissance,pays,genre))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/login',methods=['POST','GET'])
def login():
    msg = ""
    # voir si l'utilisateur exist
    if request.method == "POST"and 'Email' in request.form and 'mot_de_passe' in request.form:
        Email = request.form['Email']
        mot_de_passe = request.form['mot_de_passe'].encode('UTF-8')
    # on a utilisé if pour voir si le methode est post et ensuite verifier si le nom et le mot de pass existe
    # dans la suite nous allons verifier si le compte existe dans les compte de notre table client
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM client WHERE Email=%s AND mot_de_passe=%s', (Email, mot_de_passe,))
    compte = cursor.fetchone()
    # si compte existe dans les tables en out database
    if compte:
        # on crée une session de donné , au quel on pourra accéder avec un autre root
        session['loggedin'] = True
        session["id_client"] = compte["id_client"]
        session["mot_de_passe"] = compte["mot_de_passe"]
        # redirect to home page
        return redirect(url_for('deco'))
    else:
        # si compte n'existe pas ou le nom ou le mot de pass n'existe pas
        return redirect(url_for('kn'))
    return render_template('Acceuil.html', msg=msg)

@app.route('/logout',methods=['POST','GET'])
def logout():
    logout_user()
    if session.get('vous etiez connecté'):
        del session['vous etiez connecté']
    flash('vous venez de vous déconnecter')
    return redirect(url_for(home))


import MySQLdb
from matplotlib import pyplot as plt

@app.route('/stat')
def stat():
    con = mysql.connection.cursor()
    con.execute("select * from voiture")
    data = con.fetchall()  # data from database
    con.execute("select pays,poids from voiture")
    data_ = con.fetchall()
    x = []
    y = []
    for i in data_:
        x.append(i[0])  # x column contain data(1,2,3,4,5)
        y.append(i[1])  # y column contain data(1,2,3,4,5)
    plt.plot(x, y)
    plt.show()
    return render_template("stat.html", value=data)


from flask import Flask, render_template
import numpy as np
import pandas
import matplotlib.pyplot as plt
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64

variables = pandas.read_csv('C:\\Users\\HP\\Documents\\bd_avancées\\voiture.csv',sep=";")
prix = variables['prix']
poids = variables['poids']
@app.route('/test')
def chartTest():
    plt.hist(prix)
    plt.savefig('static/image/hu.png')
    return render_template('mon.html', name='new_plot', url='/static/image/hu.png')
    plt.hist(poids)
    plt.savefig('static/image/km.png')
    return render_template('mon.html', name='new_plot', url='/static/image/km.png')


app.run(debug=True)