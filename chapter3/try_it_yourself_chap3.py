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

person[2] = ["james"]