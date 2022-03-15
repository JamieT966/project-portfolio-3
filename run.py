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
        seat_choice = input('Number of Seats:\n')

        if seat_choice.isdigit():
            if int(seat_choice) >= 1 and int(seat_choice) <= 6:
                global movies
                movies[int(index)] = int(seat_choice)
                return
        print('Sorry, we were looking for a number between 1 and 6')


def check_available_seats(index):
    """

    Pulls latest seats by slicing off bottom row of Google Sheet.
    Takes user input of number of seats chosen.
    Adds users choice of seats to current value.
    Updates latest seat figures to Google Sheets.
    """
    print('Booking Seats...')
    seat_list = SHEET.worksheet('movies')
    seats = SHEET.worksheet('movies').get_all_values()
    available_seats = seats[-1]
    new_seats = []
    for i, j in zip(available_seats, movies):
        new_seats.append(int(i) + j)
    seat_list.append_row(new_seats)
    print('Seats booked.')


def snack_choice():
    """
    
    Presents user with 4 choices of snack and their prices and a choice of no snack.
    """
    print('Would you like any snacks?.\n')
    print('1. Large Popcorn - €4')
    print('2. Nachos - €5')
    print('3. Big bag of sweets - €3')
    print('4. Hot Dog - €6')
    print('5. No Snacks\n')

    global snack_price
    snack_price = 0
    snack_select = input('Choose a snack by entering 1, 2, 3, 4 or to skip type 5.\n')
    while True:
        if snack_select == '1':
            print('Large Popcorn\n')
            snack_price += 4
            order_complete = is_order_complete()
            if order_complete == True:
                break
        elif snack_select == '2':
            print('Nachos\n')
            snack_price += 5
            order_complete = is_order_complete()
            if order_complete == True:
                break
        elif snack_select == '3':
            print('Big bag of sweets\n')
            snack_price += 3
            order_complete = is_order_complete()
            if order_complete == True:
                break
        elif snack_select == '4':
            print('Hot Dog\n')
            snack_price += 5
            order_complete = is_order_complete()
            if order_complete == True:
                break
        elif snack_select == '5':
            print('No More Snacks\n')
            snack_price += 0
            order_complete = is_order_complete()
            if order_complete == True:
                break
        else:
            print('Sorry, we were looking for a number between 1 and 5.\n')
            return False


def is_order_complete():
    """
    
    Asks user if order is complete, if yes then end while loop. If no then continue with order.
    """
    print('Are you done with your order?')
    order_complete = input('Yes or No?\n')
    if order_complete == 'yes':
        return True
    elif order_complete == 'no':
        return False
    else:
        print('We were looking for an answer of yes or no, please try again.')


def calculate_price():
    """
    
    Calculates the total cost of all tickets purchased and any snacks.
    """
    ticket_total = 0

    for i in range(0, len(movies)):
        ticket_total = ticket_total + movies[i] * 10

    print('Total ticket cost:', ticket_total)
    print(snack_price)

def main():
    """

    Runs all functions
    """
    movie_select = movie_choice()
    number_of_seats(movie_select)
    check_available_seats(movies)
    snack_choice()
    calculate_price()
    print(movies)


main()
