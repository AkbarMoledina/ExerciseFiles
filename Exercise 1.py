__author__ = 'Akbar'

''' Create a List of your favorite songs. Then create a list of your
favorite movies. Join the two lists together (Hint: List1 + List2). Finally,
append your favorite book to the end of the list and print it. '''

favouriteSongs = ["Can't Stop", "Pokemon Theme Song", "Welcome to planet URF"]
favouriteMovies = ["Star Wars", "Planet Bboy", "Enter the Dragon"]

favourites = favouriteSongs + favouriteMovies
favourites.append("Honoured Enemy")

print(favourites)