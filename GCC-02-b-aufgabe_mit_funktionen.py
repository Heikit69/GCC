# Achtung: 
# usereingabe = (input("> ").casefold()) ##casefold: in Kleinbuchstaben, ß in ss, umlaute bleiben

def start():
    intro_text = """
    ================= Finde das geeheime Cup Cake Rezept =====================
    Willkommen in dem adventure game Rezept Cup Cake.
    Du willst das geheime Cup Cake Rezept finden, doch wo ist es versteckt?
    Viel Glück.
    Schreibe Text, um dich zu bewegen.
    """
    print(intro_text)

    beginning_text = """
    =======================================================================================================
    Du kommst in eine Wohnung mit mehreren Zimmern.
    Du suchst nach dem geheimen Cup Cake-Rezept
    Hinweis: mit EXIT  kommst du jeweils eine Ebene zurück, HILFE zeigt eine Übersicht der möglichen Befehle
    """
    print(beginning_text)

    next_action = input("> ").casefold() ##casefold: in Kleinbuchstaben, ß in ss, umlaute bleiben

    if "wo" in next_action.split(' ') and "bin" in next_action.split(' '):
        print("Du bist in einem Flur. Es gehen 3 Räume davon ab")
        main_loop()
    elif "hilfe" in next_action:
        hilfe("wo bin | exit")
    else:
        dead("Du hast leider keinen Plan")
    
def main_loop():
    while True:
        next_action = input("> ").casefold()

        if "flur" in next_action:
            flur()
        elif "räume" in next_action.split(' ') or "raeume" in next_action.split(' '):
            raeume()
        elif "exit" in next_action:
            start()
        elif "hilfe" in next_action:
            hilfe("flur | räume | exit")
        else:
            print("Ich weiss nicht, was du meinst.")


def flur():
    print("Du bist in einem Flur. es gehen 3 Räume davon ab")
    main_loop()

def raeume():
    print("Es geht ein Raum nach links ab.")
    print("2 weitere Räume sind an der Wand gegenüber des Eingangs")
    while True:
        next_action_raeume = input(">> ").casefold()
        if "links" in next_action_raeume.split(' ') and "gehe" in next_action_raeume.split(' '):
            wohnzimmer()
        elif "gegenüber" in next_action_raeume.split(' ') and "welche" in next_action_raeume.split(' '):
            gegenueber()
        elif "gerade" in next_action_raeume or "vor" in next_action_raeume:
            bad()
        elif "weiter" in next_action_raeume.split(' ') and "rechts" in next_action_raeume.split(' '):
            kueche()
        elif "exit" in next_action_raeume:
            start()
        elif "hilfe" in next_action_raeume:
            hilfe("gehe links | welche gegenüber | vor | gerade | weiter rechts | exit")
        else:
            print("Ich weiss nicht, was du meinst.")

def wohnzimmer():
    print("Du bist im Wohnzimmer")
    while True:
        next_action_raeume = input(">>> ").casefold()
        if "was" in next_action_raeume.split(' '):
            was("wohnzimmer")
        elif "exit" in next_action_raeume:
            raeume()
        elif "hilfe" in next_action_raeume:
            hilfe("was | exit")
        else:
            print("Ich weiss nicht, was du meinst.")

def bad():
    print("Du bist im Bad") 
    while True:
        next_action_raeume = input(">>> ").casefold()
        if "was" in next_action_raeume.split(' '):
            was("bad")
        elif "exit" in next_action_raeume:
            raeume()
        elif "hilfe" in next_action_raeume:
            hilfe("was | exit")
        else:
            print("Ich weiss nicht, was du meinst.")

def kueche():
    print("Du bist jetzt in der Küche")
    while True:
        next_action_raeume = input(">>> ")
        if "regal" in next_action_raeume.split(' ') and "gehe" in next_action_raeume.split(' '):
            regal()
        elif "was" in next_action_raeume.split(' '):
            print("Hier befindet sich ein Regal und ein Fenster")
        elif "fenster" in next_action_raeume.split(' ') and "gehe" in next_action_raeume.split(' '):
            fenster()
        elif "exit" in next_action_raeume:
            raeume()
        elif "hilfe" in next_action_raeume:
            hilfe("was | fenster | regal | exit")
        else:
            print("Ich weiss nicht, was du meinst.")

def dead(reason):
    print(reason, "\nGame over!")
    exit(0)

def gegenueber():
    print("Das Zimmer direkt gegenüber ist das Bad")
    print("Das Zimmer weiter rechts ist die Küche") 

def fenster():
    print("Du siehst eine schöne Aussicht")
    kueche()

def regal():
    print("In dem Regal steht ein Buch und ein Ordner")
    while True:
        next_action_raeume = input(">>>> ").casefold()
        if "buch" in next_action_raeume.split(' ') and "öffne" in next_action_raeume.split(' '):
            buch()
        elif "ordner" in next_action_raeume.split(' ') and "öffne" in next_action_raeume.split(' '):
            ordner()
        elif "exit" in next_action_raeume:
            kueche()
        elif "hilfe" in next_action_raeume:
            hilfe("öffne buch | öffne ordner | exit")
        else:
            print("Ich weiss nicht, was du meinst.")

def buch():
    print("Das Buch enthält kein Cup-Cake-Rezept")
    kueche()

def ordner():
    print("****************** Gewonnen ****************")
    print("Du hast das geheime Cup-Cake Rezept gefunden")
    print("****************** Gewonnen ****************")

def was(raum):
    print("Hier gibt es absolut nichts!")
    ziele = {
        "wohnzimmer" : wohnzimmer,
        "bad": bad
    }
    ziele[raum]() # aus dictionary kann ich keine Funktion ausführen, sondern anderen Wert zuweisen (Funktionsnahme)#
    # () bewirkt den Aufruf der Funktion

def hilfe(befehle):
    print("Versuche es mit folgenden Befehlen:")
    print(befehle)

start()