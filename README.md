# GitClone:
https://github.com/VincentGoesToFrance/stundenplan

# individuell
virtuelle umgebung: python -m venv .venv
. .venv/bin/activate
pip install flask, mysql.connector
(wenn (base) dann conda deactivate)

# Testdatenbank mit SQLITE test_stundenplanDB.sql

./static/db/test_stundenplan.sql öffnen und kommentieren bzw. auskommentieren der entsprechenden DB

SQLITE installieren
Schema(./static/db/test_stundenplanDB.sql) in SQLITE einfügen:
    definieren: test_stundenplanDB.sql
    terminal: sqlite3 ./static/db/test_stundenplanDB.db
    terminal: .read ./static/db/test_stundenplanDB.sql

SQLITE-Befehle:
.databases
.tables
.quit

MariaDB installieren
Schema in MariaDB einfügen:
    definieren: test_stundenplanDB.sql
    terminal: mysql -u root -p < ./static/db/test_stundenplanDB.sql
    terminal: passwort eingeben

MariaDB-Befehle:
mysql -u root -p -> passwort
show databases;
use <database>;
show tables <database>
