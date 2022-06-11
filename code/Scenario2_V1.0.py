# Scenario_2 Version1.0

import sys


class Main():
    print("Welcome to our program below are the functions our program can perform...")


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
                   "-> ")


    if choice == "1":
        answer_1 = float(input("Please Enter Meters.. "))
        ans_1 = answer_1 * 3.28084
        print(ans_1)

    if choice == "2":
        answer_2 = float(input("Please Enter Feet.. "))
        ans_2 = round(answer_2 / 3.28, 3)
        print(ans_2)

    if choice == "3":
        answer_3 = float(input("Please Enter Centimeter... "))
        ans_3 = round(answer_3 / 2.54, 3)
        print(ans_3)

    if choice == "4":
        answer_4 = float(input("Please Enter Inches... "))
        ans_4 = round(answer_4 * 2.54, 3)
        print(ans_4)

    if choice == "5":
        answer_5 = float(input("Please Enter Kilograms... "))
        ans_5 = round(answer_5 * 2.2, 3)
        print(ans_5)

    if choice == "6":
        answer_6 = float(input("Please Enter Pounds... "))
        ans_6 = round(answer_6 * 0.45359237, 3)
        print(ans_6)

    if choice == "7":
        answer_7 = float(input("Please Enter Milligrams... "))
        ans_7 = (answer_7 * 1000)
        print(ans_7)

    if choice == "8":
        answer_8 = float(input("Please Enter Ounces... "))
        ans_8 = (answer_8 * 28349.523125)
        print(ans_8)

    if choice == "9":
        answer_9 = float(input("Please Enter Hours... "))
        ans9 = (answer_9 * 60)
        print(ans9)

    if choice == "10":
        answer_10 = float(input("Please Enter Minutes... "))
        ans10 = (answer_10 * 0.0166666667)
        print(ans10)

    if choice == "11":
        answer_11 = float(input("Please Enter Minutes... "))
        ans_11 = (answer_11 * 60)
        print(ans_11)

    if choice == "12":
        answer_12 = float(input("PLease Enter Seconds..."))
        ans_12 = (answer_12 / 60)
        print(ans_12)

