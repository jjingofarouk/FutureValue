def calculate_future_value(principal, daily_rate, days):
    """
    Calculate the future value of an investment with daily compounded interest.

    Parameters:
    principal (float): The initial amount of money invested.
    daily_rate (float): The daily interest rate (as a decimal, e.g., 0.01 for 1%).
    days (int): The number of days the money is invested for.

    Returns:
    float: The future value of the investment.
    """
    return principal * (1 + daily_rate) ** days

def main():
    try:
        # Input from the user
        principal = float(input("Enter the initial investment amount in dollars: "))
        daily_rate = float(input("Enter the daily interest rate (as a percentage, e.g., 1 for 1%): ")) / 100
        days = int(input("Enter the number of days: "))
        
        # Calculate future value
        future_value = calculate_future_value(principal, daily_rate, days)
        
        # Display the result
        print(f"The future value of the investment after {days} days is: ${future_value:.2f}")
    
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
