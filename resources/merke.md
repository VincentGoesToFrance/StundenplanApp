# Fremdschlüssel für m:n-Beziehungen stehen immer in der Zwischentabelle und nicht in den Haupttabellen.
# Fremdschlüssel für 1:n-Beziehungen stehen in der Tabelle der "n"-Seite.
# Die ForeignKeys müssen am Ende definiert werden. 

<br> ich: woher weiß der tabellenbetrachter, dass die dozenten ein fach haben?

chatgpt: Warum "sehen" Dozenten ihre Fachrichtungen nicht direkt?

    Die Tabelle Dozent selbst enthält keine Information über Fachrichtungen, weil das ein Designmerkmal der relationalen Datenbank ist:
    Jede Tabelle speichert nur ihre eigenen Attribute. Dadurch bleibt das Datenbankschema normalisiert und flexibel.

    Der Zusammenhang zwischen Dozenten und Fachrichtungen wird erst durch die Zwischentabelle dozenten_fach hergestellt.

<br>