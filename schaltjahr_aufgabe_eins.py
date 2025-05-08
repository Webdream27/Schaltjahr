"""************************************************
Einsendeaufgabe 3.1
************************************************"""

# Einlesen des Wertes
jahr = int(input("Bitte geben Sie ein Jahr ein zur Überprüfung ob dies ein Schaltjahr ist:"))

# Ausgabe des Wertes
if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
     print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")

