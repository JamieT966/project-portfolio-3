import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_movies')

movies = SHEET.worksheet('movies')

movie_list = movies.get_all_values()

movies = [0,0,0,0]

def movie_choice():
    """
    
    Introduction, ticket prices and max no. of tickets per transaction.
    Presents user with choice of 4 movies and asks user for input.
    """
    print('Welcome to Love Movies\n')
    print('Please select the movie you would like to see. All tickets cost €10.')
    print('Max number of tickets per transaction: 6.\n')
    print('1. The Batman')
    print('2. Star Wars: The Empire Strikes Back')
    print('3. Lord of the Rings: The Two Towers')
    print('4. Iron Man\n')

    while True:
        movie_select = input('Enter Movie Choice by entering 1, 2, 3 or 4.\n')

        if movie_select == '1':
            print('Batman\n')
            return '0'
            number_of_seats(0)
        elif movie_select == '2':
            print('Star Wars\n')
            return '1'
            number_of_seats(1)
        elif movie_select == '3':
            print('LOTR\n')
            return '2'
            number_of_seats(2)
        elif movie_select == '4':
            print('Iron Man\n')
            return '3'
            number_of_seats(3)
        else:
            print('Sorry, we were looking for a number between 1 and 4.\n')


def number_of_seats(index):
    """

    Asks user for input. Number of seats required up to a maximum of 6.
    """
    print('Please Choose the number of seats you would like.')
    print('Remember, the maximum number of seats is 6.\n')

    while True:
        seat_choice = input('Number of Seats:')

        if seat_choice.isdigit():
            if int(seat_choice) >= 1 and int(seat_choice) <= 6:
                global movies
                movies[int(index)] = int(seat_choice)
                return
        print('Sorry, we were looking for a number between 1 and 6')

def check_available_seats(index):
    """

    Currently appends latest list to Google Sheets
    """
    print('Checking available seats...')
    movies = SHEET.worksheet('movies')
    seats = SHEET.worksheet('movies').get_all_values()
    available_seats = seats[-1]
    print(available_seats)
    movies.append_row(index)
    print('Seats selected.')


def main():
    """

    Runs all functions
    """
    movie_select = movie_choice()
    number_of_seats(movie_select)
    check_available_seats(movies)
    print(movie_select)
    print(movies)


main()

print(movie_list)
