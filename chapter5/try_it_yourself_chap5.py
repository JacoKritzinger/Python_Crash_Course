# 5.1
fruit = 'pinapple'
print("is fruit == 'pinapple'? I predict True.")
print(fruit == 'mango')

# 5.2
fruit = 'Pinnapple'
print("is fruit  == 'pinapple'? I predict True.")
print(fruit == 'pinapple')

# 5.3
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 5.4
# aliens = {'color': 'green', 'speed': 'slow'}
# for alien in aliens:
#     if alien 'color' = "green"
#         print("5 points")
#     else:
#         print("10 points")

    

# 5.5
 # aliens = {'color': 'green', 'speed': 'slow'}
# for alien in aliens:
#     if alien 'color' = "green"
#         print("5 points")
#       elif alien "color" = "yellow"
#       print("10 points")
#     else:
#         print("10 points")


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