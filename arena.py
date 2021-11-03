from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self, team_one='team_one', team_two='team_two'):
    self.team_one = Team(team_one)
    self.team_two = Team(team_two)

  def create_ability(self):
    name = input('What is the ability name? ')
    max_damage = input('What is the max damage of the ability? ')
    return Ability(name, max_damage)

  def create_weapon(self):
    name = input('What is the weapon name? ')
    max_damage = input ('What is the max damage of the weapon? ')
    return Weapon(name, max_damage)

  def create_armor(self):
    name = input('What is the armor name? ')
    max_block = input('What is the max block of the armor? ')
    return Armor(name, max_block)

  def create_hero(self):
    hero_name = input('Hero\'s name: ')
    hero = Hero(hero_name)
    add_item = None
    while add_item != '4':
      add_item = input('[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ')
      if add_item == '1':
        hero.add_ability(self.create_ability())
      elif add_item == '2':
        hero.add_weapon(self.create_weapon())
      elif add_item == '3':
        hero.add_armor(self.create_armor())
    return hero 

  # Pass in self.team_one or self.team_two
  def build_team(self, team):
    num_of_team_members = int(input(f'How many members would you like on Team {team.name}?\n'))
    for i in range(num_of_team_members):
      hero = self.create_hero()
      team.add_hero(hero)

  def team_battle(self):
    self.team_one.attack(self.team_two)

  def show_stats(self):
    self.show_both_team_stats(self.team_one)
    self.show_both_team_stats(self.team_two)
    self.calculate_team_average_kd_ratio(self.team_one)
    self.calculate_team_average_kd_ratio(self.team_two)
    self.print_survivors(self.team_one)
    self.print_survivors(self.team_two)

  # HELPER FUNCTIONS for show_stats()
  def show_both_team_stats(self, team):
    print('\n')
    print(team.name + ' statistics: ')
    team.stats()
    print('\n')

  def calculate_team_average_kd_ratio(self, team):
    team_kills = 0
    team_deaths = 0
    for hero in team.heroes:
      team_kills += hero.kills
      team_deaths += hero.deaths
    if team_deaths == 0:
      team_deaths = 1
    print(team.name + ' average K/D was: ' + str(format(team_kills/team_deaths, '.1f')))

  def print_survivors(self, team):
    for hero in team.heroes:
      if hero.deaths == 0:
        print(f'Survived from Team {team.name}: {hero.name}')




if __name__ == '__main__':
  game_is_running = True

  # Instantiate Game Arena
  arena = Arena('Monkeys', 'Aliens')

  # Build Teams
  arena.build_team(arena.team_one)
  arena.build_team(arena.team_two)

  while game_is_running:
    arena.team_battle()
    arena.show_stats()
    play_again = input("Play Again? y or n: ")
    if play_again.lower() == 'n':
      game_is_running = False
    else:
      arena.team_one.revive_heroes()
      arena.team_two.revive_heroes()
