import random

class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = list()

  def add_hero(self, hero):
    self.heroes.append(hero)

  def remove_hero(self, name):
    foundHero = False
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        foundHero = True
    if not foundHero:
      return 0

  def view_all_heroes(self):
    for hero in self.heroes:
      print(hero.name)

  def stats(self):
    for hero in self.heroes:
      kd = hero.kills / hero.deaths
      print(f'{hero.name} Kill/Deaths: {kd}')

  def revive_heroes(self, health=100):
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  def attack(self, other_team):
    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents) > 0:
      hero1 = random.choice(living_heroes)
      opponent1 = random.choice(living_opponents)

      winner, loser = hero1.fight(opponent1)
      if loser in living_heroes:
        living_heroes.remove(loser)
      elif loser in living_opponents:
        living_opponents.remove(loser)

    winning_team = self if len(living_heroes) > len(living_opponents) else other_team
    print(f'{winning_team.name} wins!')




