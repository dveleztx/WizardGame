
#   Instructions for Wizard Game 


## 1. Build Game Loop
======================

### Define functions and main
```
def main():
	pass


def print_header():
	pass


def game_loop():
	pass

	print("-------------------------")
	print("      Wizard Game")
	print("-------------------------")
	print()

if __name__ = "__main__":
	main()
	
```
### Build main() and print_header() up

```
def main():
	print_header()
	game_loop()


def print_header():
	print("-------------------------")
	print("      Wizard Game")
	print("-------------------------")
	print()

```

## 2. Modeling with classes

### Build game_loop()
```
while True:

	cmd = input("Do you [a]ttack, [r]unway, or [l]ook around? ")
	if cmd  == "a":
		print("attack")
	elif cmd == "r":
		print("runaway")
	elif cmd == "l":
		print("look around")
	else:
		print("OK, exiting game...bye!")

```

### Create creatures list in game_loop()

```

	creatures = [

	]

	hero = None

```
### Create actors.py class
```

class Wizard:
	pass


class Creature:
	pass


```

### Import actors and instantiate hero as a Wizard
```
import Wizard

	hero = actors.Wizard()
```

### But then change it up to make it more readable
```
from actors import Wizard, Creature

	hero = Wizard()

	creatures = [
		Creature(),
		Creature(),
		Creature(),
		Creature(),
		Creature()
	]

```

## 3. Initializing classes and creating objects
### Build Creature Object
```

# self is a pointer to itself
class Creature:
	def __init__(self, name, level):
		self.name = name
		self level = level

# Do the same thing with Wizard Object
class Wizard:
	def __init__(self, name, level):
		self.name = name
		self level = level


	# Can create an attack method!
	#def attack(self, other_creature):
		#pass

```

### Create Creatures

```

	creatures = [
		Creature("Toad", 1),
		Creature("Tiger", 12),
		Creature("Bat", 3),
		Creature("Dragon", 50),
		Creature("Evil Wizard", 1000)
	]

	#Print Creatures look ugly
	#print(creatures)

	hero = Wizard("David", 75)

```

### Create repr dunder to print creature list Creature class
```

	def __repr__(self):
		return "Creature: {} of level {}".format(
			self.name, self.level
			)


```
## 4. Adding behaviors to the wizard
### Build game_loop logic in game_loop()
```

	# Create an active creature when you are exploring
	active_creature = random.choice(creatures)
	print("A {} of level {} has appeared from a dark and foggy forest..."
		.format(active_creature.name, active_creature.level))
	print()

```
### Create attack logic
```

	# Build up Wizard class
	def attack(self, creature):
		print("The wizard {} attacks {}!".format(
				self.name, creature.name))
			

	# Build actions on game_loop()
	cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
	if cmd == "a":
		hero.attack(active_creature)


	# Continue building up Wizard class

	my_roll = random.randint(1, 12) * self.level
	creature_roll = random.randint(1, 12) * creature.level

	print("You roll {}...".format(my_roll))
	print("{} rolls {}...".format(creature.name, creature_roll))

	if my_roll >= creature_roll:
		print("The wizard has handily triumped over {}".format(creature.name))
		return True
	else:
		print("The wizard has been DEFEATED!!!")
		return False


	# Create conditional results for the combat in game_loop()
	if cmd == "a":
		if hero.attack(active_creature):
			creatures.remove(active_creature)
		else:
			print("The wizard runs and hiddes taking time to recover...")
			time.sleep(5)
			print("The wizard returns revitalized!")
	elif cmd == "l":
		print("The wizard {} takes in the surroundings and sees:".format(hero.name))
		for c in creatures:
			print(" * A {} of level {}".format(c.name, c.level))
	elif cmd == "r":
		print("The wizard has become unsure of his power and flees!")


```
## 5. Exploring specialized (derived) classes
### Enhance the combat system and make it more diverse
```

	# If no creatures are left, end game
	if not creatures:
		print("You've defeated all the creatures, well done!")
		break

	# Create defensive roll on Creature class
	def get_defensive_roll(self):
		return random.randint(1, 12) * self.level

	# Edit the combat rolls in Wizard class
	# Comment out creature roll and add the following line
	creature_roll = creature.get_defensive_roll()

```
### Customize creatures in game_loop()
```

	creatures = [
		SmallAnimal("Toad", 1),
		Creature("Tiger", 12),
		SmallAnimal("Bat", 3),
		Dragon("Dragon", 50),
		Wizard("Evil Wizard", 1000)
	]


```
## 6. Creating the creature hierarchy
### Make Wizard a subclass of Creature
```

class Wizard(Creature):
	#def __init__(self, name, level):
		#super().__init__(name, level)

	# Change roll 
	my_roll = self.get_defensive_roll()

# Create SmallAnimal class
class SmallAnimal(Creature):
	pass

# Add SmallAnimal import in program.py
from actors import Wizard, Creature, SmallAnimal


# Build SmallAnimal class
class SmallAnimal(Creature):
	def get_defensive_roll(self):
		base_roll = random.randint(1, 12) * self.level
		return base_roll / 2


		# Use super for base_roll
		base_roll = super().get_defensive_roll()


# Build Dragon class
class Dragon(Creature):
	def __init__(self, name, level, scaliness, breathes_fire):
		super().__init__(name,level)
		self.breathes_fire = breathes_fire
		self.scaliness = scaliness

	def get_defensive_roll(self):
		base_roll = super().get_defensive_roll()
		fire_modifier = None
		if self.breathes_fire:
			fire_modifier = 5
		else:
			fire_modifier = 1

		fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE IF FALSE

		fire_modifier = 5 if self.breathes_fire else 1
		scale_modifier = self.scaliness / 10

		return base_roll * fire_modifier * scale_modifier


```
### Change Creatures with new features
```

	creatures = [
		SmallAnimal("Toad", 1)
		Creature("Tiger", 12)
		SmallAnimal("Bat", 3)
		Dragon("Dragon", 50, 75, True)
		Wizard("Evil Wizard", 1000)
	]
```

Credit to [Michael Kennedy](https://github.com/mikeckennedy)
