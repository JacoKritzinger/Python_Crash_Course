# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
# 		if requested_topping in available_toppings:
# 				print(f"Adding {requested_topping}.")
# 		else:
# 				print(f"Sorry, we don't have {requested_topping}.")


			


available_drinks =["coke", 'sprite', 'fanta', 'tab' ,'water', 'alcoholic']
requested_drinks =['sprite', 'juice', 'coffie', 'coke']

for requested_drink in requested_drinks:
	if requested_drink in available_drinks:
		print(f'Bringing {requested_drink}')
	else:
		print(f'Sorry we dont have {requested_drink}')