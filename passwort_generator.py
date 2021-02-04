# Passwort Generator
# User hat die Möglichkeit die Länge des PWs zu bestimmen.
# Ebenso kann der User entscheiden, welche Kombinationsmöglichkeiten aus Buchstaben, Zahlen und Sonderzeichen er möchte

import string
import random

# Globale Variablen zum Speichern von Buchstaben, Zahlen und Sonderzeichen
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATION = string.punctuation

def password_length():
	# Frage den User nach gewünschter Länge des PW
	# Rückgabe als Int

	length = input("Bitte gebe die Länge des Passworts an (als Zahl): ")
	return int(length)

def password_generator(choice, length):
	# Generiert ein zufälliges Passwort mit gewünschter Länge des Users
    
	# choice: Liste aus boolean Werten, die die Wahl des Nutzers wiederspiegelt
        # 0 item ---> Zahl
        # 1 item ---> Buchstaben
        # 2 item ---> Sonderzeichen

	# string Konstante
	string_password = string_constant(choice)

	# string -> liste -> shuffle die Liste
	string_password = list(string_password)
	random.shuffle(string_password)

	# zufälliges passwort generieren
	random_password = random.choices(string_password, k=length)

	# passwort zu string
	random_password = ''.join(random_password)
	return random_password

def password_combination():
	# User kann Passwortkombination auswählen
	# PW kann aus Zahlen, Buchstaben und Sonderzeichen bestehen
	# Eingabe durch True/False Werte
	# Ausgabe einer Liste mit 3 boolean Werten

	#	0 item ---> Zahlen
	#	1 item ---> Buchstaben
	#	2 item ---> Sonderzeichen

	# Abfrage der Passwortkombination
	digits = input("Zahlen im PW ? (True oder False): ")
	letters = input("Buchstaben im PW ? (True oder False): ")
	puncts = input("Sonderzeichen im PW ? (True oder False): ")

	# String Eingabe umwandeln in den richtigen boolean type
	try:
		digits = eval(digits.title()) # z.B. digits = eval("True") = True
		puncts = eval(puncts.title())
		letters = eval(letters.title())
		return [digits, letters, puncts]

	# fange falsche Eingabe ab und gebe default aus
        # falsche Eingabe: NameError: name '...' is not defined
	except NameError: 
		print("Falsche Eingabe. Gebe entweder True oder False ein")
                
	return [True, True, True]

def string_constant(choice_list):
	# Ausgabe eines zusammengesetzten Strings, basierend auf der Wahl der Passwortkombination

	# 0 item ---> Zahlen
	#	falls True, füge Zahl zu string hinzu
	# 1 item ---> Buchstaben
	#	falls True, füge Buchstaben zu string hinzu
	# 2 item ---> Sonderzeichen
	#	falls True, füge Sonderzeichen zu string hinzu

	string_constant = ''

	string_constant += DIGITS if choice_list[0] else ''
	string_constant += LETTERS if choice_list[1] else ''
	string_constant += PUNCTUATION if choice_list[2] else ''

	return string_constant

if __name__ == '__main__':
	length = password_length()
	choice_list = password_combination()
	password = password_generator(choice_list, length)

	print(password)
