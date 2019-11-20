import random

#Variables

Location = ()
Animal = ()
Salt = str("Salz")

#Imports

ImportLocations = open("Locations.txt", "r", encoding="utf8")
LocationList = ImportLocations.readlines()

ImportAnimals = open("Animals.txt", "r", encoding="utf8")
AnimalList = ImportAnimals.readlines()

#Lists

#LocationList = ["Tibetianisches", "Nigerianisches", "Usbekistanisches", "Uruguayanisches", "Australisches", "Napolitanisches", "Bäretswiler"]
LocationCount = len(LocationList)

#AnimalList = ["Schildkröten", "Nasenbären", "Antilopen", "Neger", "Blauarschaffen", "Giraffen"]
AnimalCount = len(AnimalList)


RandomLocation = random.randrange(0,LocationCount)

RandomAnimal = random.randrange(0,AnimalCount)

RandomPrice = random.randrange(1, 5334)

GeneratedSalt = (LocationList[RandomLocation].capitalize().strip() + " " + AnimalList[RandomAnimal].capitalize().strip() + " " + Salt)

print (GeneratedSalt)
print (str(RandomPrice) + "$")

ImportLocations.close()
ImportAnimals.close()