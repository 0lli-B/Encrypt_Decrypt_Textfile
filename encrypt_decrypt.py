import os

FILE = input('Bitte den Namen der Datei eingeben, die ver- oder entschlüsselt werden soll (inkl. Endung): ')
KEY = input('Bitte den Namen der Datei eingeben, welche die Schlüssel enthält (inkl. Endung): ')  # key.txt
CHOICE = input('Zum Verschlüsseln geben sie bitte ein V ein;\nZum Entschlüsseln geben sie bitte ein E ein:\n')

V_schluessel = {} #Dictionary zum Verschlüsseln
E_schluessel = {} #Distionary zum Entschlüsseln

with open(KEY, 'r', encoding="ISO-8859-1") as key_file:
    for line in key_file:
        zuordnung = line.split(':')  # Buchstaben der Zeile trennen
        V_schluessel[zuordnung[0]] = zuordnung[1]  # den linken Teil als Schlüssel dem Dictionary übergeben, den rechten Teil als zugehörigen Wert
        key_entschluesseln = zuordnung[1].strip()  # entfernt den Zeilenumbruch aus dem Wert
        wert_entschluesseln = zuordnung[0] + '\n'  # fügt den Zeilenumbruch wieder dem Wert zu
        E_schluessel[key_entschluesseln] = wert_entschluesseln  # umgekehrt, also zum Entschlüsseln

with open(FILE, 'r', encoding="ISO-8859-1") as datei:  # Encoding für Sonderzeichen
    with open('new_file_for_encrypt.txt', 'w', encoding="ISO-8859-1") as new_file:  # neue Datei für Ergebnis
        zaehler = 0  # für passende Stelle
        for line in datei:
            for letter in line:
                if CHOICE == 'V' or CHOICE == 'v':  # verschlüsseln ausgewählt
                    if letter in V_schluessel:  # Falls der Buchstabe ein Key im Dictionary zum Verschlüsseln ist
                        new_file.seek(zaehler)  # An die passende Position im FILE springen
                        new_file.write(V_schluessel[letter])  # den Werte des zugehörigen Schlüssels einfügen
                        zaehler += 1
                    else:
                        new_file.seek(zaehler)
                        new_file.write(letter)  # das Zeichen unverändert einfügen
                        zaehler += 1
                elif CHOICE == 'E' or CHOICE == 'e':  # entschlüsseln ausgewählt
                    if letter in E_schluessel:
                        new_file.seek(zaehler)
                        new_file.write(E_schluessel[letter])
                        zaehler += 1
                    else:
                        new_file.seek(zaehler)
                        new_file.write(letter)
                        zaehler += 1
                else:
                    print("Keine sinnvolle Eingabe!\nProgramm sollte neu gestartet werden.")
                    break

# Veränderten Inhalt in ursprüngliche Datei einfügen
with open(FILE, 'w', encoding="ISO-8859-1") as datei:
    with open('new_file_for_encrypt.txt', 'r', encoding="ISO-8859-1") as new_file:
        datei.seek(0)  # Anfangsposition in der urspünglicher Datei
        datei.truncate()  # Entfernt Inhalt danach, also alles
        zaehler_2 = 0
        for line in new_file:  # über Zielinhalt iterieren
            for letter in line:
                datei.seek(zaehler_2)
                datei.write(letter)
                zaehler_2 += 1

os.remove('new_file_for_encrypt.txt')  # zweite Datei löschen, diese wurde nur als Zwischenschritt benötigt