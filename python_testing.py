def interact(self, person_one, person_two):
		if person_one.infected == True and person_two.infected == False and person_two.is_vaccinated == False:
			print("person_one IS infected")
			random_number = random.uniform(0,1)
			print(random_number)
			if random_number < person_one.infection.mortality_rate:
				print("person got infected :(")
				person_two.infected = True
				person_two.infection = virus
			else:
				print("person survived infection :)")
				person_two.infected = False
		elif person_one.infected == False and person_one.is_vaccinated == False and person_two.infected == True:
			print("person_one is NOT infected")
			random_number = random.uniform(0,1)
			print(random_number)
			if random_number < person_two.infection.mortality_rate:
				print("person got infected :(")
				person_one.infected = True
				person_one.infection = virus
			else:
				print("person survived infection :)")
				person_one.infected = False
		else:
			print("Don't need to interact")



# the updated version with no print statements because i know they are right!
def interact(self, person_one, person_two):

		if person_one.infected == True and person_two.infected == False and person_two.is_vaccinated == False:
			random_number = random.uniform(0,1)
			if random_number < person_one.infection.mortality_rate:
				person_two.infected = True
				person_two.infection = virus
			else:
				person_two.infected = False
		elif person_one.infected == False and person_one.is_vaccinated == False and person_two.infected == True:
			random_number = random.uniform(0,1)
			if random_number < person_two.infection.mortality_rate:
				person_one.infected = True
				person_one.infection = virus
			else:
				person_one.infected = False
		else:
			print("Don't need to interact")

		infected_people = 0
		for person in population:
			if person.infected == True:
				infected_people += 1
		print("there are {} infected people out of the population of {}.".format(infected_people, len(population)))

person0.interact(person0, person1)
person0.interact(person1, person2)
person0.interact(person2, person3)
person0.interact(person3, person4)
person0.interact(person4, person5)

person0.interact(person0, person2)
person0.interact(person1, person3)
person0.interact(person2, person4)
person0.interact(person3, person5)
person0.interact(person4, person0)



# interact method that doesnt need any parameters
# havent finished updating the population index in all the places i called person_one and person_two yet
random_index_one = random.randint(0, len(population) - 1)
		random_index_two = random.randint(0, len(population) - 1)

		if population[random_index_one].infected == True and population[random_index_two].infected == False and population[random_index_two].is_vaccinated == False:
			random_number = random.uniform(0,1)
			if random_number < population[random_index_one].infection.mortality_rate:
				person_two.infected = True
				person_two.infection = virus
			else:
				person_two.infected = False
		elif person_one.infected == False and person_one.is_vaccinated == False and person_two.infected == True:
			random_number = random.uniform(0,1)
			if random_number < person_two.infection.mortality_rate:
				person_one.infected = True
				person_one.infection = virus
			else:
				person_one.infected = False
		else:
			print("Don't need to interact")

		infected_people = 0
		for person in population:
			if person.infected == True:
				infected_people += 1
		print("there are {} infected people out of the population of {}.".format(infected_people, len(population)))








