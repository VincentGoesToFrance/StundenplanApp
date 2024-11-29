# GitClone:
https://github.com/VincentGoesToFrance/stundenplan

git-Befehle:
    git add .
    git commit -m "x"
    git push -u origin main

# nach ordner
virtuelle umgebung: python -m venv .venv
. .venv/bin/activate (linux)
.\.venv\Scripts\Activate (windows)
pip install flask mysql.connector
pip freeze //schauen was in der virtuellen umgebung installiert ist
(wenn (base) dann conda deactivate)

flask --app app run --debug

# Testdatenbank mit SQLITE test_stundenplanDB.sql

./static/db/test_stundenplan.sql öffnen und kommentieren bzw. auskommentieren der entsprechenden DB

SQLITE installieren
kalender_db.py skript ausführen, db-datei nach ./static/db
Schema(./static/db/test_stundenplanDB.sql) in SQLITE einfügen:
    definieren: test_stundenplanDB.sql
    terminal: sqlite3 ./static/db/test_stundenplanDB.db
    windows: 
    terminal: .read ./static/db/test_stundenplanDB.sql

SQLITE-Befehle:
.databases
.tables
.quit
pragma table_info(<tabellenname>)

MariaDB installieren
Schema in MariaDB einfügen:
    definieren: test_stundenplanDB.sql
    terminal: mysql -u root -p < ./static/db/test_stundenplanDB.sql
    terminal: passwort eingeben

MariaDB-Befehle:
mysql -u root -p -> passwort /hardcoded!
show databases;
use <database>;
show tables <database>
