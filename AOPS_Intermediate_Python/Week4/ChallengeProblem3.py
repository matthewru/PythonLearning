import random

class Pokemon:

    def __init__(self, name, health, att, defense):
        self.name = name
        self.health = health
        self.att = att
        self.defense = defense

    def __str__(self):
        profile = self.name
        profile += ' (' + str(self.health) + ')'
        profile += '\n'
        profile += 'ATT: ' + str(self.att)
        profile += ' DEF: ' + str(self.defense) + '\n'
        return profile

    def calculate_damage(self, otherPokemon):
        r = random.uniform(0.85, 1)
        damage = (((12 / 5) * (self.att / otherPokemon.defense)) + 2) * r
        return damage

    def attack(self, otherPokemon):
        inflictedDamage = int(round(self.calculate_damage(otherPokemon)))
        otherPokemon.health = otherPokemon.health - inflictedDamage
        print(str(self.name) + ' does ' + str(inflictedDamage) + ' damage!\n')
        if otherPokemon.health <= 0:
            print(str(otherPokemon.name) + ' has fainted!')
            print(str(otherPokemon.name) + ' has won the battle!')


#testing
e = Pokemon('Eevee', 55, 55, 40)
c = Pokemon('Croagunk', 48, 61, 40)

print(e)
print(c)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)
print(c)
c.attack(e)
print(e)
e.attack(c)



