from random import randint

from typing import Any

class Human:
  
  _level = 1
  _xp = 0
  _atk_damage = 2
  _dodge_chance = 0.1
  _is_dead = False

  def __init__(self, 
               name: str,
               health: int=100):
    self.name = name
    self._health = health

  def greetings(self) -> str:
    greeting_options = ['Hello!', 'Hi!', 'Hey!']
    greeting = greeting_options[randint(0, len(greeting_options)-1)]
    print(f'{self.name} said {greeting}')
    return greeting
  
  def attack(self, enemy: Any) -> None:
    print(f'{self.name} has attacked {enemy.name}')
    enemy.take_damage = self.atk_damage
  
  def run(self) -> None:
    print(f'{self.name} started to run.')
  
  def jump(self) -> None:
    print(f'{self.name} has jumped.')
  
  def level_up(self) -> None:
    if self._xp >= 100:
      self._xp = 0
      self._level += 1
      print(f'{self.name} has leveled up!')

  @property
  def experience(self) -> int:
    return self._xp

  @experience.setter
  def gain_xp(self, xp_amount: int) -> None:
    self._xp += xp_amount

  @property
  def health(self) -> int:
    return self._health

  @health.setter
  def take_damage(self, damage: int) -> None:
    self._health -= damage
    if(self._health <= 0):
      self._is_dead = True
      print(f'{self.name} has died.')

  

