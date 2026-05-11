class Character:
    def __init__(self,name,health,attack,blood):
        self.name =name
        self.health=health
        self.attack=attack
        self.blood =blood

    def attack_enemy(self):
        print(f"{self.name} attack with poor {self.attack} and damage {self.blood}")

warrior = Character("Thor",100,50,"rad")
mage =Character("Gandalf",80,70,"black")
archar =Character("Archer",60,80,"white")

warrior.attack_enemy()
mage.attack_enemy()
archar.attack_enemy()