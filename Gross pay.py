# Write a program to prompt the user for hours and rate per hour to compute gross pay.

def calculate_pay():
    while True:
        try:
            hours = float(input("Enter Hours: "))
            rate = float(input("Enter Rate: "))
            break
        except ValueError:
            print("Error, please enter numeric input")

    pay = hours * rate
    print("Pay:", pay)

calculate_pay()