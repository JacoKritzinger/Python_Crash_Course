favorite_movies = {
	'jack': ['karati kallie','king kong'],
	'jul': ['jack and jul','titanic'],
	'josh':['avatar','sleeping beuty'],
	'drake':['jake and josh','avatar'],
	'pieter':['karati kallie','jack and jul'],
	}

for name,movies in favorite_movies.items():
	print(f"\n{name.title()}'s favorite movies are:")
	for movie in movies:
		print(f'\t{movie.title()}')