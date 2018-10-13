import random

class Virus(object):

	def __init__(self, name, mortality_rate):
		self.name = name
		self.mortality_rate = mortality_rate

class Person(object):

	def __init__(self, _id, is_vaccinated, infected=False):
		self._id = _id
		self.is_vaccinated = is_vaccinated
		self.infected = infected

		self.is_alive = True
		self.infection = None

	def interact(self, other_person):


		# person interact with the person object
		# make sure both of them are alive
		assert other_person.is_alive == True
		assert self.is_alive == True

		# one must be infected in order to interact
		# person who isn't infected must not be vaccinated
		# random number from 0-1 and compare it to the virus mortality rate:
		# 	if number is less, they get infected
		#	if number is more, they don't get infected
		if self.infected == True and other_person.infected == False and other_person.is_vaccinated == False:
			random_number = random.uniform(0,1)
			if random_number < self.infection.mortality_rate:
				other_person.infected = True
			else:
				other_person.infected = False
				other_person.is_vaccinated = True
		elif self.infected == False and self.is_vaccinated == False and other_person.infected == True:
			random_number = random.uniform(0,1)
			if random_number < other_person.infection.mortality_rate:
				self.infected = True
			else:
				self.infected = False
				self.is_vaccinated = True
		else:
			print("no interaction")







# add people into the population
population = []

person0 = Person(0, True, infected= True)
person1 = Person(1, True)
person2 = Person(2, False)
person3 = Person(3, True)
person4 = Person(4, False)
person5 = Person(5, True)

population.append(person0)
population.append(person1)
population.append(person2)
population.append(person3)
population.append(person4)
population.append(person5)




# if people in the population are infected: add the virus to their infection.
virus = Virus("Ebola", 0.6)
for person in population:
	if person.infected == True:
		person.infection = virus



# let people interact with each other!
person0.interact(person4)














