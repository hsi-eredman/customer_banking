"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Initialized instance of the `Account` class. 0 is supplied as a place holder
    # Until the interest is calculated.
    account = Account(balance, 0)

    # Calculate interest earned
    interest = account.balance * (interest_rate/100 * months/12)

    # Update the CD account balance by adding the interest earned
    updated_balance = account.balance + interest

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    account.set_interest(interest)

    # Return the updated balance and interest earned.
    return  account.balance, account.interest
