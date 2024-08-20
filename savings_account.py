"""Import the Account class from the Account.py file."""
from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Initialized instance of the `Account` class. 0 is supplied as a place holder
    # Until the interest is calculated.
    account = Account(balance, 0)

    # Calculate interest earned
    interest = account.balance * (interest_rate/100 * months/12)

    # Update the savings account balance by adding the interest earned
    updated_balance = account.balance + interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    account.set_interest(interest)

    # Return the updated balance and interest earned.
    return  account.balance, account.interest