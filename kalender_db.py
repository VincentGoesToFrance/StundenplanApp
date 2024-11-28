from datetime import date, timedelta
import sqlite3


def kalenderwochen_daten(jahr):
    wochen = []
    aktuelles_datum = date(jahr, 1, 1)

    # Erster Montag finden
    while aktuelles_datum.weekday() != 0:  # Montag = 0
        aktuelles_datum += timedelta(days=1)

    while True:
        start_datum = aktuelles_datum
        end_datum = start_datum + timedelta(days=6)
        kw = start_datum.isocalendar()[1]
        
        # Wenn das start_datum im nächsten Jahr ist, breche ab
        if start_datum.year != jahr:
            if start_datum.weekday() != 0:
                wochen[-1]["jahr"] = jahr+1
            break
        
        wochen.append({
            "jahr": jahr,
            "kalenderwoche": kw,
            "start_datum": start_datum.strftime('%d.%m.%Y'),# "05.06.2028"
            "end_datum": end_datum.strftime('%d.%m.%Y'),
        })
        
        aktuelles_datum += timedelta(days=7)
    
    return wochen

# Ausgabe für das Jahr 2024
wochen_2024 = kalenderwochen_daten(2024)
# for woche in wochen_2024:
#     print(f"Jahr: {woche['jahr']}, KW: {woche['kalenderwoche']}, Start: {woche['start_datum']}, Ende: {woche['end_datum']}")



#sqlite3 db erstellen

connection = sqlite3.connect("kalender.db")
cursor = connection.cursor()

# Tabelle löschen, falls sie existiert
cursor.execute("DROP TABLE IF EXISTS kalenderwochen")

# Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS kalenderwochen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jahr INTEGER NOT NULL,
    kalenderwoche INTEGER NOT NULL,
    start_datum DATE NOT NULL,
    end_datum DATE NOT NULL
)
""")
connection.commit()

# Daten einfügen
for woche in wochen_2024:
    # Sicherstellen, dass start_datum und end_datum als datetime.date Objekte übergeben werden
    cursor.execute("""
    INSERT INTO kalenderwochen (jahr, kalenderwoche, start_datum, end_datum)
    VALUES (?, ?, ?, ?)
    """, (woche['jahr'], woche['kalenderwoche'], 
          woche['start_datum'],
          woche['end_datum']))

connection.commit()
connection.close()
