#3.1
names= ['john', 'martin', 'luke', 'jamie']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])#-1 is the last one from the back

#3.2
# message= f"Hello {names[0]} how are you!?"
# print(message)

for name in names:
	print(f'hello {name} how are you')

#3.3

cars=['bmw', 'ferrari', "honda"]
for car in cars:
	print(f'How nice would it be to own a {car.title()}')


#3.4
persons = ['joe', 'jack', 'jamy']
for person in persons:
	print(f'i would like to invite {person.title()} to my dinner')

#3.5
persons = ['joe', 'jack', 'jamy']
print(f"{persons[2].title()} Would not be able to make it.")

del persons[2]
print(persons)

persons.insert(2, 'Joline')
print(persons)
for person in persons:
	print(f'i would like to invite {person.title()} to my dinner') 


#3.6
persons.insert(0,'juba')
persons.insert(2,'rulf')
persons.insert(4,'kold')
for person in persons:
	print(f'Deur {person.title()}, Would you like to join my dinner party')

#3.7
message = "I can only invite 2 people to my dinner party"
persons.pop(3)
persons.pop(2)
persons.pop(0)
print(message)

for person in persons:
	print(f'Hello {person}, would you still attend my dinner party?')

del persons[2]
del persons[1]
del persons[0] 
print(persons)


#3.8
locations =['paris','germany','sweden','netherlands','italy']
print(locations)
print(sorted(locations))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(sorted(locations))
locations.sort(reverse = True)
print(locations)

#3.9

persons = ['joe', 'jack', 'jamy']
print(len(persons))

#3.10 
locations =['paris','germany','sweden','netherlands','italy','frans','japan']
print(locations)
print(sorted(locations))
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort(reverse = True)
del locations[0]
print(locations)
locations.pop(2)
print(locations)
locations.insert(3,'dubai')
print(locations)

#3.11
locations.insert(3,'spain')
print(locations)