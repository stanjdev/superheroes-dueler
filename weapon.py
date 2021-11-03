import random
from ability import Ability

# Inheritance of the Ability class
class Weapon(Ability):
  # Polymorphism - overriding the already existing 'attack' method
  def attack(self):
    random_value = random.randint(self.max_damage // 2, self.max_damage)
    return random_value

