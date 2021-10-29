import random

class Hero:
  def __init__(self, name, starting_health = 100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def add_ability(self, ability):
    pass

  def attack(self):
    pass

  def defend(self, incoming_damage):
    pass

  def take_damage(self, damage):
    pass

  def is_alive(self):
    pass

  def fight(self, opponent):
    match = [self.name, opponent.name]
    random_index = random.randint(0, 1)
    winner = match[random_index]
    opposite_index = 0 if random_index == 1 else 1
    loser = match[opposite_index]
    print(f"{winner} defeats {loser}!")


# This is only run when this hero.py script is run directly. 
# It is blocked when this script is imported by another script. For testing.
if __name__ == "__main__":
  # my_hero = Hero("Grace Hopper", 200)
  # print(my_hero.name)
  # print(my_hero.current_health)
  hero1 = Hero("Wonder Woman", 300)
  hero2 = Hero("Dumbledore", 250)

  hero1.fight(hero2)

