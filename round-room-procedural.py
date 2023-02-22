from sys import exit


def start():
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
        # hit north room door
        north_room()

    elif "light" in next_action and "on" in next_action:
        text = """
        You now see you are in round room 5x5.
        There are two doors in the room: a north door and a west door.
        There is also a window.
        What do you do?
        """
        print(text)
        main_loop()

    else:
        dead("You stumble around the room in the dark until you starve.")


def main_loop():
    while True:
        next_door = input("> ")

        if "north" in next_door:
            north_room()
        elif "west" in next_door:
            west_room()
        elif "window" in next_door.split(' '):
            window()
        else:
            print("I've got no idea what that means.")


def north_room():
    print("You are now in the north room. There are some cracked walnut shells lying around in the far corner.")


def west_room():
    print("You've entered the west room.")
    print("In front of you is a tea party.")
    print("Alice, the March Hare and the Mad Hatter are passing cups and pastries around.")


def window():
    print("You approach the window and look out.")
    print("You are looking upon a small, dimly-lit inner courtyard, 1x1.")
    print("You see clotheslines with the neighbour's laundry hanging on them.")
    print("Apparently, they haven't gotten a single matching pair of socks.")

    print("What do you do now?")
    main_loop()


def dead(reason):
    print(reason, "Game over!")
    exit(0)


start()