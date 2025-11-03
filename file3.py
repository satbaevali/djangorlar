import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(10, 20)
        self.defense = random.randint(5, 10)

    def attack(self, opponent):
        damage = max(0, self.attack_power - opponent.defense)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def heal(self):
        heal_amount = random.randint(5, 15)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} points!")

def simulate_battle(player1, player2):
    print(f"Battle Start: {player1.name} vs {player2.name}")
    round_num = 1
    while player1.is_alive() and player2.is_alive():
        print(f"\n--- Round {round_num} ---")
        if random.random() < 0.5:
            player1.attack(player2)
        else:
            player2.attack(player1)
        if random.random() < 0.3:
            player1.heal()
        if random.random() < 0.3:
            player2.heal()
        time.sleep(0.5)
        print(f"{player1.name}: {player1.health} HP | {player2.name}: {player2.health} HP")
        round_num += 1

    winner = player1 if player1.is_alive() else player2
    print(f"\n🏆 Winner: {winner.name}")

if __name__ == "__main__":
    p1 = Player("Knight")
    p2 = Player("Orc")
    simulate_battle(p1, p2)
