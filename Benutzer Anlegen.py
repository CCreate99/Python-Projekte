import hashlib

class create_Benutzer:
    benutzername = input("Wählen Sie einen Beutzernamen: ")
    passwort = pwhash = hashlib.md5(bytes(input("Wählen Sie ein Passwort: "), "utf-8"))

if __name__ == "__main__":
    benutzer1 = create_Benutzer()
    pw = False
    while pw == False:
        check_b = input("Geben Sie ihren Benutzernamen ein: ")

        if (benutzer1.benutzername == check_b):
            print("Ihr Benutzername ist korrekt")
        else:
            print("Ihr Benutzername ist falsch")

        trypw = hashlib.md5(bytes(input("Geben Sie ihr Passwort ein: "), "utf-8"))

        if(benutzer1.passwort.hexdigest() == trypw.hexdigest()):
            print("Ihre Daten waren Korrekt, Sie werden weitergeleitet...")
            print(benutzer1.passwort.hexdigest())
            pw = True
        else:
            print("Ihr Passwort war nicht Korrekt. Versuchen Sie es noch einmal")
