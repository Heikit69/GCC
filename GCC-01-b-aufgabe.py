intro_text = """
================= Finde das geeheime Cup Cake Rezept =====================
Willkommen in dem adventure game Rezept Cup Cake.
Du willst das geheime Cup Cake Rezept finden, doch wo ist es versteckt?
Viel Glück.
Verwende die Tastatur, um dich zu bewegen.
"""
print(intro_text)

beginning_text = """
Du kommst in eine Wohnung mit mehreren Zimmern.
Du suchst nach dem geheimen Cup Cake-Rezept?
"""
print(beginning_text)

next_action = None

while next_action != "exit":
    next_action = input("> ")
  
    if "wo" in next_action.split(' ') and "bin" in next_action.split(' '):
        print("Du bist in einem Flur. es gehen 3 Räume davon ab")
    elif "räume" in next_action.split(' '):
        print("Es geht ein Raum nach links ab.")
        print("2 weitere Räume sind an der Wand gegenüber des Eingangs")
        next_action_raeume = None
        while next_action_raeume != "exit":
            next_action_raeume = input(">> ")
            if "links" in next_action_raeume.split(' ') and "gehe" in next_action_raeume.split(' '):
                print("Du bist jetzt im Wohnzimmer")
            elif "gegenüber" in next_action_raeume.split(' ') and "welche" in next_action_raeume.split(' '):
                print("Das Zimmer direkt gegenüber ist das Bad")
                print("Das Zimmer weiter rechts ist die Küche")
                next_action_raeume_gegenueber = None
                while next_action_raeume_gegenueber != "exit":
                    next_action_raeume_gegenueber = input(">>> ")
                    if "direkt" in next_action_raeume_gegenueber.split(' ') and "gegenüber" in next_action_raeume_gegenueber.split(' ') or "Bad" in next_action_raeume_gegenueber.split(' '):
                        print("Du bist jetzt im Wohnzimmer")
                    elif "gegenüber" in next_action_raeume_gegenueber.split(' ') and "welche" in next_action_raeume_gegenueber.split(' '):
                        print("Das Zimmer direkt gegenüber ist das Bad")
                        print("Das Zimmer weiter rechts ist die Küche")
                        
                    elif "exit" in next_action_raeume_gegenueber.split(' ') or "raus" in next_action_raeume_gegenueber.split(' ') or "zurück" in next_action_raeume.split(' '):
                        raus = 1
                    else:
                        print("Ich weiss nicht, was du meinst.")
            elif "exit" in next_action_raeume.split(' ') or "raus" in next_action_raeume.split(' ') or "zurück" in next_action_raeume.split(' '):
                raus = 1
            else:
                print("Ich weiss nicht, was du meinst.")
    else:
        print("Ich weiss nicht, was du meinst.")

print("Leider verloren.")
print("Game over.")