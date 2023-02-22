import sys
import random

class Room(object):
    def __init__(self, description, monster, loot): # wird aufgerufen, wenn ein neues Objekt der Klasse angelegt wird , jeweils mindestens ein Argument: 1. Argument normal "self" => bezieht sich auf sich selber
        self.description = description
        self.monster = monster
        self.loot = loot # kann man erwerben

    def __print__(self):
        print(self.description)

    def enter(self):   # hier könnt man noch mehr Funktionen als Print anfügen, damit es Sinn macht
        self.__print__()


class NorthRoom(Room):
    def enter(self):
        super(NorthRoom, self).enter()
        print(
        """
        The rest is not implemented yet.
        """)
        sys.exit(0)


class WestRoom(Room):
    def enter(self):
        super(WestRoom, self).enter()
        print(
        """
        The rest is not implemented yet.
        """)
        sys.exit(0)


class Window(Room): # hat die Superklasse Room, ist eine Sorte Room
    def enter(self):
        super(Window, self).enter()   #ruft die Parent-Klasse von Window auf => Room
        return "start room"


class StartRoom(Room):# ist auch eine Sorte Room
    def enter(self):
        super(StartRoom, self).enter()
        next_action = input("> ")

        if "walk" in next_action and "walls" in next_action:
            # hit north room door
            return "north room"

        elif "light" in next_action and "on" in next_action:
            text = """
        You now see you are in round room 5x5.
        There are two doors in the room: a north door and a west door.
        There is also a window.
        What do you do?
            """
            print(text)
            while True:
                next_door = input("> ")

                if "north" in next_door:
                    return "north room"
                elif "west" in next_door:
                    return "west room"
                elif "window" in next_door.split(' '):
                    return "window"
                else:
                    print("I've got no idea what that means.")

        else:
            print("""
                You stumble around the room in the dark until you starve.
                Game over.
                """)
            sys.exit(0)


class Rat(object):
    def __init__(self, name, lives, description, fight_alternative):
        self.name = name
        self.lives = lives
        self.description = description
        self.fight_alaternative = fight_alternative
        self.power = random.randint(1,10)

    def take_damage(self, damage):
        self.lives = self.lives - damage

    def deal_damage(self):
        return self.power


class Game(object): # hier wird alles initialisiert, was man später braucht, danach play(Hauptschleife)
    def __init__(self):
        self.won = False

        rat_mary = Rat("Mary", 10, "used to have a little lamb. Now she mostly spends her days knitting or getting random rage fits.", "little lamb")
        rat_rodrigo = Rat("Rodrigo", 8, "blabla", "bla")

        start_room_description = """
        You are in a dark room.
        What do you do?
        """
        north_room_description = "You are now in the north room. There are some cracked walnut shells lying around in the far corner."
        west_room_description = """
        You've entered the west room.
        In front of you is a tea party.
        Alice, the March Hare and the Mad Hatter are passing cups and pastries around.
        """
        window_description = """
        You approach the window and look out.
        You are looking upon a small, dimly-lit inner courtyard, 1x1.
        You see clotheslines with the neighbour's laundry hanging on them.
        Apparently, they haven't gotten a single matching pair of socks.
        """

        little_lamb_figurine = {"name": "Little Lamb Figurine", "material": "wood"}

        self.start_room = StartRoom(start_room_description, None, None)
        self.north_room = NorthRoom(north_room_description, rat_mary, "walnut shells")
        self.west_room = WestRoom(west_room_description, None, little_lamb_figurine)
        self.window = Window(window_description, rat_rodrigo, None)
        self.game_map = {
            "start room" : self.start_room,
            "north room": self.north_room,
            "west room": self.west_room,
            "window": self.window
        }

        welcome_screen = """
        ================= Gup cakes and giant rats 1.0 =====================
        Welcome to the adventure game Gup Cakes and Giant Rats.
        Find your way through the magic kingdom. Get the Intergalactic cookbook.
        And don't get eaten by the rats.
        Good luck.
        Use your keyboard for text entry.
        """
        print(welcome_screen)


    def play(self): # Hauptschleife von dem Spiel, die durch alle Räume geht
        current_room = self.start_room  # aktueller Raum ist Startraum
        while (not self.won): # solange ich nicht gewonnen habe, wird auf den nächsten Raum gesetzt
            next_room_name = current_room.enter() # hier wird ein Sttring zurück gegeben, z.B. Startraum, jeder raum kennt seinen nächsten Raum
            current_room = self.game_map[next_room_name]  # aktueller Raum wird auf nächsten Raum gesetzt aus Variable game_name_map


new_game = Game() # neue Spiel wird auf Objekt Spiel gesetzt
new_game.play() # fängt an neues Spiel zu Spielen