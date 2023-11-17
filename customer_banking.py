# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter Saving Account balance: "))
    saving_interest_rate = float(input("Enter Saving Account interest rate: "))
    saving_month = int(input("Enter months for saving account: "))
    # Call the create_savings_account function and pass the variables from the user.
   
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, saving_interest_rate, saving_month)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f" interst earned on saving account: $ {interest_earned_savings: ,.2f}")
    print(f"Updated saving account balance ${updated_savings_balance: ,.2f} for {saving_month} month")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_account_balance = float(input("Enter CD Account balance: "))
    cd_Account_interest_rate = float(input("Enter CD Account interest rate: "))
    cd_account_month = int(input("Enter months for CD Account: "))
    # Call the create_cd_account function and pass the variables from the user.
    
    updated_cd_balance, interest_earned = create_cd_account(cd_account_balance, cd_Account_interest_rate, cd_account_month)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f" interst earned on CD account: ${interest_earned: ,.2f}")
    print(f"Updated CD account balance ${updated_cd_balance: ,.2f} for {cd_account_month} month")
if __name__ == "__main__":
    # Call the main function.
    main()