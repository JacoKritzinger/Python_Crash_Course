# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())





new_cars = ['bmw','audi','golf','suzuki']
used_cars = []

while new_cars:
	current_car =  new_cars.pop()
	print(f"getting {current_car.title()} ready to go")
	used_cars.append(current_car)

print("The following cars have been used")
for used_car in used_cars:
	print(used_car.title())