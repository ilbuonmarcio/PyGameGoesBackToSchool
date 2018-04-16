import random

class Player:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self, other):
        other.hp -= self.dmg

    def heal(self):
        self.hp += random.randint(5, 25)

player1 = Player("Marcioz", 100, 20)
player2 = Player("Cyonti", 70, 30)

current_player = player1
waiting_player = player2

while True:
    print("Turno di", current_player.name)
    move = input("(a: attacca, h: guarisciti) Azione: ")
    if move == "a":
        current_player.attack(waiting_player)
        print("Il giocatore", current_player.name, "ha attaccato! Vita di",
              waiting_player.name, "rimanente:", waiting_player.hp)
    elif move == "h":
        current_player.heal()
        print("Il giocatore", current_player.name,
              "si é guarito! Vita disponibile:", current_player.hp)
    else:
        print("Hai sbagliato comando e perso tempo! Tocca all'avversario!")

    if(waiting_player.hp) <= 0:
        print(waiting_player.name, "ha perso!\nFine del gioco!")
        exit()

    current_player, waiting_player = waiting_player, current_player
