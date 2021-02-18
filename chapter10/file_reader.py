# with open('text_folder/pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents)

file_path = "text_folder/pi_digits.txt"

with open(file_path) as file_object:
	contents = file_object.read()
print(contents.rstrip())

file_path = "text_folder/pi_digits.txt"

with open(file_path) as file_object
	lines = file_object.readlines()
	pi_string = ""
for line in lines:
	print(line.rstrip())
		contents = file_object.read()
print(contents.rstrip())