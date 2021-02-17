# number = "Enter a number, and I'll tell you if it's even or odd: "
# number += "Enter 'quit' to end the program."
# message= ""

# while message != "quit":
# 	message = input(number)
# 	message  =int(message)
# 	if number % 2 == 0:
# 		print(f"\nThe number {number} is even.")
# 	else:
# 		print(f"\nThe number {number} is odd.")
	
	
prompt = "\nEnter a number, and I'll tell you if it's even or odd:"
prompt += "Enter 'quit' to end the program."
active = True

while active:
	number = input(prompt)

	if  number == "quit":
		active = False
	elif int(number) % 2 == 0:
		print(f"\nThe number {number} is even.")
	elif int(number) % 2 != 0:
		print(f"\nThe number {number} is odd.")
 

