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

@app.route("/stundenplan/")
def stundenplan_index():
    return render_template("stundenplan.html")

#ifabfrage, bis welches jahr angezeigt werden soll. leerer stundenplan mit stundenplan/ , ansonsten mit jahr? db mit mehreren jahren
@app.route("/stundenplan/<int:jahr>/<int:kalenderwoche>")
def stundenplan(jahr, kalenderwoche):
    kalender = show_sqlite_kalender_db(jahr, kalenderwoche)
    liste = show_sqlite_stundenplan_db()
    return render_template("stundenplan.html", kalender=kalender, liste=liste)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/football")
def football():
    return render_template("football.html")

# datenbank

#sqlite
app.config["DATABASE_sqlite_kalender"] = "./static/db/kalender.db"
app.config["DATABASE_sqlite_stundenplan"] = "./static/db/stundenplan.db"

def get_sqlite_kalender_db():
    g.db = sqlite3.connect(app.config['DATABASE_sqlite_kalender'])
    g.db.row_factory = sqlite3.Row #konvertiert db in ein wörterbuch und gibt dieses dann aus 
    return g.db

def get_sqlite_stundenplan_db():
    g.db = sqlite3.connect(app.config['DATABASE_sqlite_stundenplan'])
    g.db.row_factory = sqlite3.Row #konvertiert db in ein wörterbuch und gibt dieses dann aus 
    return g.db

# @app.cli.command('show_db') 
def show_sqlite_kalender_db(jahr, kalenderwoche):
    db = get_sqlite_kalender_db()  # Verbindung zur DB holen
    cursor = db.execute('SELECT * FROM kalenderwochen where kalenderwoche=? and jahr=?', (kalenderwoche, jahr))  # Alle Zeilen aus der Tabelle abfragen
    rows = cursor.fetchall()  # Alle Zeilen holen
    return rows

def show_sqlite_stundenplan_db(table=None):
    db = get_sqlite_stundenplan_db()  # Verbindung zur DB holen
    # cursor = db.execute('SELECT name FROM sqlite_master WHERE type="table"')
    if table != None:
        cursor = db.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()  # Alle Zeilen holen
        return rows
    else:
        cursor = db.execute('SELECT * FROM klassen')
        rows = cursor.fetchall()
        liste = [rows[1]['jahrgang'], get_themen()]
        return liste
    
def get_themen():
    db = get_sqlite_stundenplan_db()
    cursor = db.execute('SELECT * FROM themen')
    rows = cursor.fetchall()
    return rows[18]["schulfach"]

    
# # Zeilen im Terminal ausgeben
# for row in rows:
# #    print(f"ID: {row['id']}, Username: {row['username']}")

stundenplan_tabellen = ["angestellte", "klassen", "fachrichtungen", "schüler", "themen", "fach_angestellte"]

@app.route("/sqlite/")
def sqlite():
    return render_template("sqlite.html")

@app.route("/sqlite/<tabellenname>")
def sqlite_tabellen(tabellenname):
    if tabellenname not in stundenplan_tabellen:
        return "<h1>You stupid motherfucker!</h1>"
    stundenplan = show_sqlite_stundenplan_db(tabellenname)
    return render_template("sqlite.html", liste=stundenplan)

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