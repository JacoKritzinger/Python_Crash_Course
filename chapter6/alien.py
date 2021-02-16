# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# Human_1={'color':'white', 'arms':'2', 'legs': '2','eyes':'2', 'nose':'1','fingers':'10', 'age':23,'name':'Jaco'}
# print(Human_1['name'])
# print(Human_1['age'])
# print(Human_1['fingers'])

# for key, value in Human_1.items():
# 	print(f"\nKey: {key}")
# 	print(f"Value: {value}")

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
➊ for alien_number in range(30):
➋ new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
➌ aliens.append(new_alien)
# Show the first 5 aliens.
➍ for alien in aliens[:5]:
print(alien)
print("...")
# Show how many aliens have been created.
➎ print(f"Total number of aliens: {len(aliens)}")