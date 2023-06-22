import datetime
import database

menu = """ Please select any one of the following

1) Add a new movie
2) view upcoming movies
3) view all movies
4) watch a movie
5) view watched movie
6) Exit


Your selection:

"""

welcome = "Welcome to the movie watchlist application"

print(welcome)
database.create_tables()
#database.delete_qwery()



def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")

    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    print("---- \n")


def print_username_list_of_movies(username,movies):
    print(f"Movies watched by {username} are ")
    print("-----\n")
    for movie in movies:
        print(movie[1])
    print('--------\n')


def prompt_watched_movies():
    movie_title = input("Enter the title: ")
    username = input("Enter the username")
    database.watch_movies(username = username,title=movie_title)





while(user_input:= input(menu))!="6":
    if user_input == '1':
        prompt_add_movie()
    elif user_input == '2':
        movies = database.get_movies(upcoming=True)
        print(movies)
        print_movie_list("upcoming",movies)
    elif user_input == '3':
        movies = database.get_movies()
        print(movies)
        print_movie_list("All",movies)
    elif user_input == '4':
        prompt_watched_movies()
    elif user_input == '5':
        username = input("Get the username: ")
        movies = database.get_watched_movies(username)
        print(movies)
        print_username_list_of_movies(username, movies)
    else:
        print("invalid input please try again later")