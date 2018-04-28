Die Datenschutzgrundverordnung -kurz DSGVO- ist oft schon aufgrund Ihres langen
Namens furchteinflößend für uns Entwickler. Hinzu kommt, dass es in den letzten
Monaten von vielen Seiten Ängste geschürt werden ("20 Millionen Strafe! 4
Prozent des weltweiten Umsatzes! Die Anforderungen sind unmöglich zu erfüllen!").

Unser erster Ratschlag daher: **Don't panic!**

Die Verordnung erscheint auf den ersten Blick kompliziert und schwer zugänglich,
sie folgt allerdings sehr vernünftigen Prinzipien, so dass die gestellten
Anforderungen in sich schlüssig sind und sich oft aus "gesundem Menschenverstand"
ableiten lassen. Aber verschaffen wir uns erstmal einen Überblick:

# Die DSGVO aus Flughöhe

Der Gesetzestext umfasst insgesamt 99 Artikel
welche in 11 Kapitel unterteilt sind. Für Unternehmen und Organisation direkt
relevant sind dabei insbesondere die Kapitel I bis V. Diese regeln folgende
Dinge:

* **Kapitel I** enthält *allgemeine Bestimmungen* und stellt klar, wann und für
  wen die DSGVO überhaupt gilt. Wer nicht sicher ist, ob die Verordnung
  überhaupt anwendbar ist sollte also zunächst hier einen Blick hineinwerfen.
* **Kapitel II** definiert *Grundsätze* für die Verarbeitung von
  personenbezogenen Daten: Hier wird aufgelistet, unter welchen Bedingungen
  eine Organisation, ein Unternehmen oder eine staatliche Behörde überhaupt
  die Daten von Personen verarbeiten darf (und wann nicht).
* **Kapitel III** beschreibt die Rechte der betroffenen Person und unterteilt
  sich nochmals in fünf Abschnitte: 
  * **Abschnitt 1** definiert sogenannte *Transparenzrechte* und legt damit
    fest, in welcher Art eine betroffen Person darüber informiert werden soll,
    wie, wo und wofür ihre Daten verarbeitet werden.
  * **Abschnitt 2** regelt, welche Auskunftsrechte eine betroffene Person
    hat.
  * **Abschnitt 3** befasst sich mit dem Recht der betroffenen Person, die
    Löschung oder Richtigstellung von Daten zu verlangen.
  * **Abschnitt 4** regelt das Recht auf Einschränkung der
    Verarbeitung sowie die Auskunfts- und Einspruchsrechte beim Einsatz
    automatisierter Entscheidungsverfahren.
  * **Abschnitt 5** definiert schließlich Ausnahmen von den genannten
    Rechten, z.B. wenn es um die *nationale Sicherheit* geht.
* **Kapitel IV** befasst sich mit den Pflichten und Rechten des
  *Verantwortlichen* sowie des *Auftragsverarbeiters* und ist wiederum in
  mehrere Abschnitte unterteilt:
  * **Abschnitt 1** definiert die Pflichten der beiden.
  * **Abschnitt 2** regelt die Sicherheit personenbezogener Daten.
  * **Abschnitt 3** befasst sich mit der Datenschutz-Folgenabschätzung.
  * **Abschnitt 4** beschreibt die Rolle des Datenschutzbeauftragten.
  * **Abschnitt 5** schließlich beschreibt Verhaltensregeln und Möglichkeiten
    der Zertifizierung.
* **Kapitel V** beschäftigt sich schließlich mit der Übermittlung von Daten
  in sogenannte Drittländer sowie an internationale Organisationen.

Dies fünf Kapitel enthalten fast genau 50 % der Artikel der DSGVO und 
sind für alle "Datenverarbeiter" die relevanteste Informationsquelle. Das
heißt aber nicht, dass die restlichen Kapitel unbedeutend sind, denn sie haben
indirekt große Auswirkungen: **Kapitel VIII** beispielsweise regelt die
Beschwerdemöglichkeiten sowie die Vergabe von Sanktionen und **Kapitel IX**
befasst sich mit *besonderen Verarbeitungssituationen* in denen es z.B. um die
Wahrung der Meinungsfreiheit oder die Verarbeitung von Beschäftigtendaten geht.

# Die DSGVO umsetzen

Jetzt wo wir einen ersten Überblick über die relevantesten Bereiche der
Gesetzgebung haben stellt sich natürlich die Frage: **Wo fange ich an?**

Wie so oft im Leben, gibt es auch hier keine eindeutige Antwort: Startups
und kleine Unternehmen deren primärer Geschäftszweck nicht das Sammeln von
Nutzerdaten ist werden sich hier naturgemäß sehr viel einfacher tun als
große Unternehmen die eine Vielzahl von Nutzerdaten sammeln und verarbeiten.

Der Ansatz den wir hier vorstellen ist auf **kleine Unternehmen und Startups**
zugeschnitten und ergibt sich aus unserer Erfahrung bei der Arbeit mit diesen.
Wir erheben dabei keinen Anspruch darauf den besten Ansatz zu kennen, haben
in der Praxis bei der Umsetzung der DSGVO damit aber gute Erfahrungen
gesammelt.

## Schritt 1: Gilt die DSGVO für uns überhaupt?

Die erste Frage ist natürlich

## Schritt 2: Zieldefinition

Ist klar, dass die DSGVO greift ist es nützlich sich zunächst klarzumachen,
welches Ziel wir bei der Umsetzung verfolgen, wie also der **Idealzustand**
nach erfolgreicher Zielerreichung aussehen würde. Stark vereinfacht lautet die
Antwort folgendermaßen:

* **Alle Prozesse die personenbezogene Daten verarbeiten sind systematisch
  erfasst und dokumentiert (falls nötig)**. Für jeden einzelnen Prozess sind
  in diesem Fall mindestens folgende Dinge in der Dokumentation enthalten:
  * Der Namen und die Kontaktdaten der Verantwortlichen und deren Datenschutzbeauftragten.
  * Der Zweck der Datenverarbeitung.
  * Die Kategorien der verarbeiteten Daten.
  * Die rechtliche Grundlage der Datenverarbeitung.
  * Die Stellen sowie ggf. Auftragsverarbeiter welche die Daten verarbeiten.
  * Die Löschfristen für die Daten, falls möglich.
  * Die technischen und organisatorischen Maßnahmen zum Schutz der Daten.
  * Falls nötig eine Datenschutz-Folgenabschätzung.
  Auftragsverarbeiter führen ebenfalls ein angepasstes Verfahrensverzeichnis.
* **Alle Prozesse minimieren die erhobenen Daten und besitzen datenschutzfreundliche
  Voreinstellungen**.
* **Nötige Einwilligungen aller betroffenen Personen zur Verarbeitung von Daten
  sind rechtssicher erfasst und dokumentiert.**
* **Die Daten sind durch technische und organisatorische Maßnahmen geschützt**.
  Diese Maßnahmen umfassen u.a.:
  * Methoden zum Schutz von Daten wie Pseudonymisierung, Anonymisierung oder Verschlüsselung.
  * Verfahren zur Sicherstellung der Vertraulichkeit, Integrität, Verfügbarkeit
    und Belastbarkeit der Systeme für die Datenverarbeitung.
  * Verfahren zur regelmäßigen Überprüfung der Maßnahmen.
* **Betroffenrechte werden gewährt und umgesetzt**. Dies betrifft im Einzelnen
  die Rechte auf...
  * ...Auskunft zu Art und Herkunft der Daten
  * ...Auskunft zu Verarbeitungszwecken sowie Speicherdauer der Daten
  * ...Auskunft zu den Empfängern der Daten
  * ...Auskunft zu Garantien bei Übertragung in Drittländer / zu internationalen Organisationen
  * ...Löschung der Daten
  * ...Berichtigung der Daten
  * ...Erhalt der Daten
  * ...Portierung der Daten
  * ...Einschränkung der Verarbeitung der Daten
  * ...manuelle Prüfung von automatisierten Entscheidungen
  * ...Beschwerde bei einer Aufsichtsbehörde
  sowie die Pflicht, auf die obigen Rechte klar hinzuweisen
* **Mit allen Auftragsverarbeitern liegen Veträge über die Verarbeitung und
  den Schutz der Daten vor.**
* **Werden Daten gemeinschaftlich verarbeitet bestehen Regelungen zu den
  Verantwortungsbereichen der einzelnen Verantwortlichen**.
* **Es existieren Prozesse für den Fall des Verlusts personenbezogener Daten**.
  Dies betrifft insbesondere die Benachrichtigung von Betroffenen und
  Aufsichtsbehörden im Falle von Datenverlust.
* **Es wurde ein Datenschutzbeauftragter bestellt (falls erforderlich)**.

Nicht alle oben aufgeführten Pfichten sind für alle Unternehmen gleichermaßen
verbindlich. Beispielsweise definiert [Artikel 30]({{'gdpr-article-30'|href}})
Ausnahmen für die Notwendigkeit der Führung eines Verfahrensverzeichnis.
[Artikel 37]({{'gdpr-article-37'|href}}) definiert zudem die Notwendigkeit
für die Bestellung eines betrieblichen Datenschutzbeauftragten.

## Schritt 2: Bestandsaufnahme & Dokumentation bestehender Prozesse

Nachdem man weiß wo man hin möchte sollte man als nächstes klären, wo man
gerade steht. Hierzu ist es nötig, sich einen Überblick über die eigene
Datenverarbeitung zu verschaffen und alle dabei
zutage geförderten Prozesse sorgfältig zu dokumentieren. Das ist dabei gleich
doppelt nützlich, denn die DSGVO verlangt von Unternehmen in verschiedenen
Bereichen eine ausführliche Dokumentation. Folgende Fragen sollten hierbei
beantwortet werden:

### Welche Art von Daten werden verarbeitet?

Hier geht es darum, alle Prozesse zu erfassen, die in irgendeiner Art und
Weise personenbezogene Daten verarbeiten. Für jeden der Prozesse sollte dabei
folgendes in Erfahrung gebracht werden.

Dies können Daten sein bei denen der Personenbezug direkt klar ist, wie
z.B. E-Mail Adressen oder Namen. Aber auch Daten die indirekt auf eine einzelne
Person bezogen werden können fallen hierunter, wie z.B. GPS-Daten oder
Nachrichten die von einer Person verfasst wurden (insofern sie nicht
anonymisiert wurden). Wer nicht sicher ist, was "Personenbezug" meint sollte
sich nochmals die [Definition]({{'gdpr-index-personenbezogene-daten'|href}})
oder den [relevanten Artikel]({{'gdpr-article-4'|href}}) hierzu anschauen.

### Zu welchem Zweck werden die Daten verarbeitet?

Hier geht es darum festzuhalten, zu welchem Zweck die Daten verarbeitet werden.
Für E-Mail Adressen könnte der Zweck z.B. sein, Kunden einen Newsletter zu schicken.

### Unter welchen Voraussetzungen verarbeiten wir diese Daten?

Schließlich sollte ersichtlich sein, unter welchen Bedingungen die Verarbeitung
erfolgt. Kapitel II und insbesondere die [Artikel 5]({{'gdpr-article-5'|href}})
sowie [6]({{'gdpr-article-6'|href}}) helfen hier weiter. Eine zweifelsfreie
Feststellung der Rechtmäßigkeit ist enorm wichtig, denn grundsätzlich gilt:
Alles was nicht explizit erlaubt ist, ist verboten.

### Wie und wo haben wir die Einwilligung zur Verarbeitung erhalten und dokumentiert?

Ergibt sich aus der vorherigen Frage, dass eine Einwilligung zur Verarbeitung
nötig war, sollte geklärt werden wann, wo und in welcher Form diese
Einwilligung erteilt wurde.

### Wo, wie und von wem werden die Daten verarbeitet?

Da die DSGVO strikte Voraussetzungen

## Schritt 3: Nötige Maßnahmen identifizieren

