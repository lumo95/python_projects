# Name: Money
# Created By: Luke Molloy
# Date: 10/9/16


def run():

    income = float(input("Enter your monthly Income.\n"))

    exp = float(input("Enter your monthly Expenditure\n"))

    calculate(income, exp)


def calculate(income, expenditure):
    result = income - expenditure

    if result < 0:
        print("Total income: €" + str(income) + "\n")
        print("Total expenditure: €" + str(expenditure) + "\n")
        print("You have a deficit of: €" + str(result))
        future = result * 3
        print("Expected losses over 3 months: €" + str(future))

    else:
        print("Total income: €" + str(income) + "\n")
        print("Total expenditure: €" + str(expenditure) + "\n")
        print("You have a monthly profit of: €" + str(result))
        future = result * 3
        print("Expected profit gained over 3 months: €" + str(future))

run()
