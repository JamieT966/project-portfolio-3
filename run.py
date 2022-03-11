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

def movie_choice():
    """
    Introduction, ticket prices and max no. of tickets per transaction.
    Presents user with choice of 4 movies and asks user for input.
    """
    print('Welcome to Love Movies\n')
    print('Please select the movie you would like to see. All tickets cost €10.')
    print('Max number of tickets per transaction: 6.\n')
    print('a. The Batman')
    print('b. Star Wars: The Empire Strikes Back')
    print('c. Lord of the Rings: The Two Towers')
    print('d. Iron Man\n')
    movie_choice = input('Enter Movie Choice by entering a, b, c or d.\n')

movie_choice()