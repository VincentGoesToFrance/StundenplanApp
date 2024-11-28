from flask import Flask, render_template, g
import sqlite3
import mysql.connector 

app = Flask(__name__)

# routen
@app.route("/")
def hello_world():
    return """
        <h1>existierende testrouten</h1>
        <a href='./calender'>calender</a><br>
        <a href='./bwsa/name'>bwsa-x</a><br>
        <a href='./stundenplan'>stundenplan</a><br>
        <a href='./login'>login</a><br>
        <a href='./football'>football</a><br>
        <a href='./sqlite'>sqlite</a><br>
        <a href='./mariadb'>mariadb</a><br>
        """



@app.route("/calender")
def calender():
    return render_template("calender.html")

@app.route("/bwsa/<username>")
def bwsa(username):
    return "<p>test you</p>"

#ifabfrage, bis welches jahr angezeigt werden soll. leerer stundenplan mit stundenplan/ , ansonsten mit jahr? db mit mehreren jahren
@app.route("/stundenplan/<int:jahr>/<int:kalenderwoche>")
def stundenplan(jahr, kalenderwoche):
    kalender = show_sqlite_db(jahr, kalenderwoche)
    return render_template("stundenplan.html", kalender=kalender)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/football")
def football():
    return render_template("football.html")

# datenbank

#sqlite
app.config["DATABASE_sqlite"] = "./static/db/kalender.db"

def get_sqlite_db():
    g.db = sqlite3.connect(app.config['DATABASE_sqlite'])
    g.db.row_factory = sqlite3.Row #konvertiert db in ein wörterbuch und gibt dieses dann aus 
    return g.db

# @app.cli.command('show_db') 
def show_sqlite_db(jahr, kalenderwoche):
    db = get_sqlite_db()  # Verbindung zur DB holen
    cursor = db.execute('SELECT * FROM kalenderwochen where kalenderwoche=? and jahr=?', (kalenderwoche, jahr))  # Alle Zeilen aus der Tabelle abfragen
    rows = cursor.fetchall()  # Alle Zeilen holen
    return rows
    
# # Zeilen im Terminal ausgeben
# for row in rows:
# #    print(f"ID: {row['id']}, Username: {row['username']}")

@app.route("/sqlite")
def sqlite():
    kalender = show_sqlite_db()
    return render_template("sqlite.html", liste=kalender)


#mariaDB
def get_mariadb_db():
    mariadb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test_stundenplanDB"
    )
    return mariadb

def show_mariadb_db():
    db = get_mariadb_db()  # Verbindung zur DB holen
    mycursor = db.cursor()
    mycursor.execute("select * from dozenten")
    myresult = mycursor.fetchall()
    return myresult

@app.route("/mariadb")
def mariadb():
    test = show_mariadb_db()
    print(test)
    return render_template("mariadb.html", liste=test)

if __name__ == '__main__':
    app.run()