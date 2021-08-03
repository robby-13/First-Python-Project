MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies():
    for movie in movies:
        print_movies(movie)

def print_movies(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}\n")


def find():
    user_input = input("Enter title of movie you would like to find: ")
    for movie in movies:
        if movie['title'] == user_input:
            print_movies(movie)

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add()
            pass
        elif selection == "l":
            list_movies()
            pass
        elif selection == "f":
            find()
            pass
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
