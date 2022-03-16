import gspread
from os import system
from pyfiglet import figlet_format
from termcolor import colored
import os
import sys

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

def clear():
    """
    Clears the screen to allow for the next content to be displayed.
    """
    print('\033c')


def introduction():
    """
    Introduction screen to Love Movies using pyfiglet.
    Asks user to press 'Enter' 
    """
    print(' Welcome to\n')
    print(figlet_format('Love Movies', font = 'standard'))
    input(colored('Press Enter key to continue\n', color="green"))
    clear()

def movie_choice():
    """
    
    Displays ticket prices and max no. of tickets per transaction.
    Presents user with choice of 4 movies and asks user for input.
    """
    print('Please select the movie you would like to see. All tickets cost €10.')
    print('Max number of tickets per transaction: 6.\n')
    print('1. The Batman')
    print('2. Star Wars: The Empire Strikes Back')
    print('3. Lord of the Rings: The Two Towers')
    print('4. Iron Man\n')

    while True:
        movie_select = input(colored('Enter Movie Choice by entering 1, 2, 3 or 4.\n', color="green"))
        movie_select.strip()

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
    clear()
    print('Please Choose the number of seats you would like.')
    print('Remember, the maximum number of seats is 6.')
    print(colored('If you would like to return to the movie selection page, please type "x" \n', color="cyan"))

    while True:
        seat_choice = input(colored('Number of Seats:\n', color="green"))
        seat_choice.strip().lower()

        if seat_choice.isdigit():
            if int(seat_choice) >= 1 and int(seat_choice) <= 6:
                global movies
                movies[int(index)] = int(seat_choice)
                return
        print('Sorry, we were looking for a number between 1 and 6')
        if seat_choice == 'x':
            clear()
            os.execl(sys.executable, sys.executable, *sys.argv)


def check_available_seats(index):
    """

    Pulls latest seats by slicing off bottom row of Google Sheet.
    Takes user input of number of seats chosen.
    Adds users choice of seats to current value.
    Updates latest seat figures to Google Sheets.
    """
    clear()
    print(colored('Booking Seats...', color="cyan"))
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
    clear()
    global snack_price
    snack_price = 0
    while True:
        print('Would you like any snacks?.\n')
        print('1. Large Popcorn - €4')
        print('2. Nachos - €5')
        print('3. Big bag of sweets - €3')
        print('4. Hot Dog - €6')
        print('5. No Snacks')
        print(colored('If you would like to return to the movie selection page, please type "x" \n', color="cyan"))
        snack_select = input(colored('Choose a snack by entering 1, 2, 3, 4 or to skip type 5.\n', color="green"))
        snack_select.strip().lower()
        if snack_select == '1':
            print('Large Popcorn\n')
            snack_price += 4
            order_complete = is_order_complete()
            if order_complete == True:
                break
            clear()
        elif snack_select == '2':
            print('Nachos\n')
            snack_price += 5
            order_complete = is_order_complete()
            if order_complete == True:
                break
            clear()
        elif snack_select == '3':
            print('Big bag of sweets\n')
            snack_price += 3
            order_complete = is_order_complete()
            if order_complete == True:
                break
            clear()
        elif snack_select == '4':
            print('Hot Dog\n')
            snack_price += 6
            order_complete = is_order_complete()
            if order_complete == True:
                break
            clear()
        elif snack_select == '5':
            print('No More Snacks\n')
            snack_price += 0
            order_complete = is_order_complete()
            if order_complete == True:
                break
            clear()
        elif snack_select == 'x':
            clear()
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print(colored('Sorry, we were looking for a number between 1 and 5.\n', color="red"))
            

def is_order_complete():
    """
    
    Asks user if order is complete, if yes then end while loop. If no then continue with order.
    """
    clear()
    print(colored('Are you done with your order?', color="cyan"))
    order_complete = input('Yes or No?\n')
    order_complete.strip().lower()
    if order_complete == 'yes':
        return True
    elif order_complete == 'no':
        return False
    else:
        print(colored('We were looking for an answer of yes or no, please try again.', color="red"))


def get_contact_details():
    """
    
    Asks user for name and phone number to be used later.
    Phone number is validated using a while loop with an .isdigit() == False
    """
    clear()
    print('For the booking we will need your name and phone number. Please fill out both below\n')
    name = input(colored('Please write your name: \n', color="green"))
    phone_number = input(colored('Please write your phone number: \n', color="green"))
    while phone_number.isdigit() == False:
        phone_number = input(colored('Phone number can only contain numbers, please try again: \n', color="red"))
    calculate_price(name, phone_number)
        

def calculate_price(name, phone_number):
    """
    
    Calculates the total cost of all tickets purchased and any snacks.
    Tells user their name, phone number and total.
    """
    clear()
    ticket_total = 0

    for i in range(0, len(movies)):
        ticket_total = ticket_total + movies[i] * 10

    overall_total = int(ticket_total) + int(snack_price)

    print('Thank you for booking', name)
    print('If we need to contact you we will call this number:', phone_number)
    print('The total price of tickets and snacks is €', overall_total)

def main():
    """

    Runs all functions
    """
    introduction()
    movie_select = movie_choice()
    number_of_seats(movie_select)
    check_available_seats(movies)
    snack_choice()
    get_contact_details()


main()
