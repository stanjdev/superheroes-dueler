import random
from ability import Ability
from armor import Armor

class Hero:
  def __init__(self, name, starting_health = 100):
    self.abilities = list()
    self.armor = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def add_ability(self, ability):
    self.abilities.append(ability)

  def attack(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def add_armor(self, armor):
    self.armor.append(armor)

  def defend(self, incoming_damage):
    if self.current_health <= 0:
      return 0 
    total_block = 0
    for armor in self.armor:
      total_block += armor.block()
    return abs(total_block - incoming_damage)

  def take_damage(self, damage):
    self.current_health -= self.defend(damage)

  def is_alive(self):
    return self.current_health > 0

  def fight(self, opponent):
    if len(self.abilities) < 1 or len(opponent.abilities) < 1: 
      # At least one hero doesn't have abilities. Not fair.
      print("Draw")
      return
    fighting = True
    while fighting:
      self.take_damage(opponent.attack()) # decrement health
      opponent.take_damage(self.attack()) # decrement health
      if not self.is_alive() and not opponent.is_alive():
        print('Draw! Both heroes are defeated.')
        fighting = False
      elif not self.is_alive() or not opponent.is_alive():
        winner = self.name if self.is_alive() else opponent.name
        print(self.name, self.current_health)
        print(opponent.name, opponent.current_health)
        print(f"{winner} won!")
        fighting = False


    



    # match = [self.name, opponent.name]
    # random_index = random.randint(0, 1)
    # winner = match[random_index]
    # opposite_index = 0 if random_index == 1 else 1
    # loser = match[opposite_index]
    # print(f"{winner} defeats {loser}!")



# This is only run when this hero.py script is run directly. 
# It is blocked when this script is imported by another script. For testing.
if __name__ == "__main__":
  # my_hero = Hero("Grace Hopper", 200)
  # print(my_hero.name)
  # print(my_hero.current_health)
  # hero1.fight(hero2)

  # ability = Ability("Great Debugging", 50)
  # ability2 = Ability("Smarty Pants", 90)
  # armor1 = Armor('Vibranium Shield', 150)
  # armor2 = Armor('Iron Man Suit', 100)
  # hero = Hero("Grace Hopper", 200)
  # hero.add_ability(ability)
  # hero.add_ability(ability2)
  # hero.add_armor(armor1)
  # hero.add_armor(armor2)
  # hero.take_damage(50)
  # print(hero.is_alive())
  # print(hero.current_health)
  # print(hero.attack())
  # print(hero.defend())
  # hero.take_damage(140000)
  # print(hero.is_alive())
  # print(hero.current_health)


  hero1 = Hero("Wonder Woman", 300)
  hero2 = Hero("Dumbledore", 250)
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Laser Eyes", 130)
  ability3 = Ability("Wizard Wand", 180)
  ability4 = Ability("Super Beard", 120)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  hero1.fight(hero2)

