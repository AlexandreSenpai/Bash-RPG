from typing import Any

class Monster():
  
  _dodge_chance = 0.1

  def __init__(self, 
               name: str, 
               xp_reward: int,
               atk_damage: int, 
               health: int=100):
    self.name = name
    self._atk_damage = atk_damage
    self._health = health
    self._xp_reward = xp_reward

  def attack(self, enemy: Any):
    print(f'{self.name} has attacked {enemy.name}')
    enemy.take_damage = self._atk_damage
  
  @property
  def reward(self):
    return self._xp_reward

  @property
  def health(self):
    return self._health

  @health.setter
  def take_damage(self, damage: int):
    self._health -= damage
    if(self._health <= 0):
      self.is_dead = True
      print(f'{self.name} has died.')
  

