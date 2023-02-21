intro_text = """
================= Gup cakes and giant rats 1.0 =====================
Welcome to the adventure game Gup Cakes and Giant Rats.
Find your way through the magic kingdom. Get the Intergalactic cookbook.
And don't get eaten by the rats.
Good luck.
Use your keyboard for text entry.
"""
print(intro_text)

beginning_text = """
You are in a dark room.
What do you do?
"""
print(beginning_text)

next_action = input("> ")

if "walk" in next_action and "walls" in next_action:
    print("You stumble through a door.")
    print("You look around.")
    print("There are some chracked walnut shells lying around in the far corner")

elif "light" in next_action and "turn" in next_action and "on" in next_action:
    text = """
    You now see you are in round room 5x5.
    There are two doors in the room: a north door and a west door.
    There is also a window.
    What do you do?
    """
    print(text)

    while True: # Spiel main loop => Endlosschleife
        next_door = input("> ")

        if next_door == "north":
            print("You are now in the north room. There are some cracked walnut shells lying around in the far corner.")
        elif "west" in next_door: # rel ungenau
            print("You've entered the west room.")
            print("In front of you is a tea party.")
            print("Alice, the March Hare and the Mad Hatter are passing cups and pastries around.")
        elif "window" in next_door.split(' '): # teilt in Leerzeichen muss ein einzelnes Wort sein
            print("You approach the window and look out.")
            print("You are looking upon a small, dimly-lit inner courtyard, 1x1.")
            print("You see clotheslines with the neighbour's laundry hanging on them.")
            print("Apparently, they haven't gotten a single matching pair of socks.")
        else:
            print("I've got no idea what that means.")

else:
    print("You stumble around the room in the dark until you starve.")
    print("Game over.")