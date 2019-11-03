import sys


def main():
    """
    Calculates how long it will take the user to purchase her/his dream house with a semiannual raise applied
    """
    annual_salary = float(input("Enter your starting annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream house: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    r = 0.04
    current_savings = 0
    portion_down_payment = 0.25 * total_cost
    
    months = 0
    while current_savings < portion_down_payment:
        investment = (current_savings * r) / 12
        current_savings += investment + (annual_salary / 12 * portion_saved)
        months += 1
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise 

    print(f"Number of months: {months}")
    sys.exit(0)


if __name__ == "__main__":
    main()