# Scenario_2.1

import time
import sys


class Main():
    print("Welcome to our program below are the functions our program can perform...")

    time.sleep(2)

    choice = input("1. Convert Meters to Feet.\n"
                   "2. Convert Feet to Meters.\n"
                   "3. Convert Centimeter to Inches.\n"
                   "4. Convert Inches to Centimeter.\n"
                   "5. Convert Kilograms to Pounds.\n"
                   "6. Convert Pounds to Kilograms.\n"
                   "7. Convert Milligram to Ounce.\n"
                   "8. Convert Ounce to Milligram.\n"
                   "9. Convert Hours to Minutes.\n"
                   "10. Convert Minutes to Hours.\n"
                   "11. Convert Minutes to Seconds.\n"
                   "12. Convert Seconds to Minutes\n"
                   "13. To EXIT PRESS (13).\n"
                   "-> ")

    if choice == "13":
        print("\nSee you again :)")

    if choice == "1":
        answer_1 = float(input("Please Enter Meters.. "))
        ans_1 = answer_1 * 3.28084
        print(ans_1)
        original_stdout = sys.stdout
        with open('newfile.txt', 'w') as f:
            sys.stdout = f
            print("Value is Feet is ", ans_1)

    if choice == "2":
        answer_2 = float(input("Please Enter Feet.. "))
        ans_2 = round(answer_2 / 3.28, 3)
        print(ans_2)
        original_stdout1 = sys.stdout
        with open('newfile_2.txt', 'w') as f:
            sys.stdout = f
            print("Value is Meters is ", ans_2)

    if choice == "3":
        answer_3 = float(input("Please Enter Centimeter... "))
        ans_3 = round(answer_3 / 2.54, 3)
        print(ans_3)
        original_stdout1 = sys.stdout
        with open('newfile_3.txt', 'w') as f:
            sys.stdout = f
            print("Value in Inches is ", ans_3)

    if choice == "4":
        answer_4 = float(input("Please Enter Inches... "))
        ans_4 = round(answer_4 * 2.54, 3)
        print(ans_4)
        original_stdout4 = sys.stdout
        with open('Inches_To_Centimeters.txt', 'w') as f:
            sys.stdout = f
            print("Value in Centimeters is", ans_4)

    if choice == "5":
        answer_5 = float(input("Please Enter Kilograms... "))
        ans_5 = round(answer_5 * 2.2, 3)
        print(ans_5)
        original_stdout5 = sys.stdout
        with open('Kilograms_to_Pounds.txt', 'w') as f:
            sys.stdout = f
            print("Value in Pounds is", ans_5)

    if choice == "6":
        answer_6 = float(input("Please Enter Pounds... "))
        ans_6 = round(answer_6 * 0.45359237, 3)
        print(ans_6)
        original_stdout6 = sys.stdout
        with open('Kilograms_to_Pounds.txt', 'w') as f:
            sys.stdout = f
            print("Value in Kilograms is", ans_6)

    if choice == "7":
        answer_7 = float(input("Please Enter Milligrams... "))
        ans_7 = (answer_7 * 1000)
        print(ans_7)
        original_stdout7 = sys.stdout
        with open('Milligrams_to_Ounces.txt', 'w') as f:
            sys.stdout = f
            print("Value in ounces is", ans_7)

    if choice == "8":
        answer_8 = float(input("Please Enter Ounces... "))
        ans_8 = (answer_8 * 28349.523125)
        print(ans_8)
        original_stdout8 = sys.stdout
        with open('Ounces_to_Milligrams.txt', 'w') as f:
            sys.stdout = f
            print("Value in Milligrams is", ans_8)

    if choice == "9":
        answer_9 = float(input("Please Enter Hours... "))
        ans9 = (answer_9 * 60)
        print(ans9)
        original_stdout9 = sys.stdout
        with open("Hours_to_Minutes.txt", 'w') as f:
            sys.stdout = f
            print("Value in Minutes is ", ans9)

    if choice == "10":
        answer_10 = float(input("Please Enter Minutes... "))
        ans10 = (answer_10 * 0.0166666667)
        print(ans10)
        original_stdout10 = sys.stdout
        with open("Minutes_to_hours", 'w') as f:
            sys.stdout = f
            print("Value in Hours is ", ans10)

    if choice == "11":
        answer_11 = float(input("Please Enter Minutes... "))
        ans_11 = (answer_11 * 60)
        print(ans_11)
        original_stdout11 = sys.stdout
        with open("Minutes_to_Hours.txt", 'w') as f:
            sys.stdout = f
            print("Values in Seconds is ", ans_11)

    if choice == "12":
        answer_12 = float(input("PLease Enter Seconds..."))
        ans_12 = (answer_12 / 60)
        print(ans_12)
        original_stdout12 = sys.stdout
        with open("Seconds_to_Minutes.txt", 'w') as f:
            sys.stdout = f
            print("Value in Minutes is ", ans_12)








