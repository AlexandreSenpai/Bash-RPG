from entities.humans import human
from entities.monsters import monster

franco = human.Human("Franco")
urbuz = monster.Monster('Urbuz', 50)


franco.greetings()
franco.attack(urbuz)
print(franco.health)
print(urbuz.health)