class Enemy:

    def __init__(self, x):
        self.lives = x
        
    def attack(self):
        print("Ouch!\n")
        self.lives -= 20

    def check_health(self):
        print("I have " + str(self.lives) + " HP left!\n")


class LargeEnemy:

    def move_enemy(self):
        print("I am moving")


class BossEnemy(Enemy, LargeEnemy):
    pass

tony = BossEnemy(100)
tony.move_enemy()
tony.check_health()
