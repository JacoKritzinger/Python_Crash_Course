# 5.1
fruit = 'pinapple'
print("is fruit == 'pinapple'? I predict True.")
print(fruit == 'mango')

# 5.2
fruit = 'Pinnapple'
print("is fruit  == 'pinapple'? I predict True.")
print(fruit == 'pinapple')

# 5.3

# 5.4

# 5.5

# 5.6 
age = 8
if age < 2:
    print("Person is a baby")
elif age < 4:
    print("Person is a todler")
elif age < 13:
    print("Person is a teenager")
elif age < 20:
    print("Person is a Adult")
elif age < 65:
    print("Person is a elder")
elif age >= 65:
   print("Person is a elder")

# 5.7


# 5.8
active_users = ['andrew', 'carolina', 'david','Piet']
user = 'admin'

if user not in active_users:
    print(f"Hello {user.title()}, would you like to see a report today.")
else:
    print(f"Hello {user.title()},thanks for logging in.")

# 5.10
current_users = ('Cody','Shaun','Frank','Erika','Rea')
new_users = ('Rudy','Thabo','Sindy','Quinton','Ethan')

if new_users:
    for current_user in current_users:
        print(f"This username has already been used")


# 5.11       
common_numbers = (1,2,3,4,5,6)