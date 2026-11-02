class BankAcct:
    """
    This class represents a bank account that maintains essential account
    state data, supports balance modifications (deposits and withdrawals),
    allows interest rate adjustments, and calculates accrued interest over time.

    Attributes:
        name (str): The account holder's name.
        account_number (str): The unique account identifier.
        amount (float): The current balance in the account.
        interest_rate (float): The annual interest rate stored as a decimal
            (e.g., 0.03 represents 3.0%).
        accrued_interest (float): Stores the most recently calculated interest
            amount based on day calculations.

    Methods:
        adjust_interest_rate(new_rate): Modifies the account's annual interest rate.
        deposit(deposit_amount): Adds funds to the account balance.
        withdraw(withdraw_amount): Deducts funds from the account balance.
        get_balance(): Returns the current account balance.
        calculate_interest(days): Calculates simple interest based on the number of days.
        __str__(): Returns a formatted string displaying account balance and interest.
    """

    def __init__(self, name, account_number, amount, interest_rate):
        """
        Initializes a new BankAcct object with required state information.

        Parameters:
            name (str): The name of the account holder.
            account_number (str): The identifier string for the bank account.
            amount (float): Starting balance for the account.
            interest_rate (float): Starting annual interest rate as a decimal.

        Return:
            None
        """
        # Assigning constructor arguments to instance variables
        # so that each instantiated object maintains its own unique state.
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

        # Tracking accrued interest internally so __str__ can display
        # the latest calculated interest amount alongside the balance.
        self.accrued_interest = 0.0

    def adjust_interest_rate(self, new_rate):
        """
        Adjusts the annual interest rate for the account.

        Parameters:
            new_rate (float): The new interest rate expressed as a decimal.

        Logic:
            1. Verify that the provided rate is non-negative.
            2. Update self.interest_rate if valid, or alert the user of invalid input.

        Return:
            None
        """
        # Validating that the new interest rate isn't set to a negative number.
        if new_rate >= 0:
            self.interest_rate = float(new_rate)
            print(f"Interest rate updated to {self.interest_rate * 100:.2f}%.")
        else:
            print(
                "Error: Interest rate cannot be negative. Rate remains unchanged."
            )

    def deposit(self, deposit_amount):
        """
        Deposits a positive monetary amount into the account.

        Parameters:
            deposit_amount (float): The amount of money to deposit.

        Logic:
            1. Check if the deposit amount is greater than zero.
            2. If valid, increment self.amount by deposit_amount.
            3. If invalid, output an error message and make no balance change.

        Return:
            float: The updated account balance.
        """
        # Ensuring we don't process zero or negative deposit transactions.
        if deposit_amount > 0:
            self.amount += float(deposit_amount)
            print(f"Successfully deposited ${deposit_amount:,.2f}.")
            return self.amount
        else:
            print("Error: Deposit amount must be greater than zero.")
            return self.amount

    def withdraw(self, withdraw_amount):
        """
        Withdraws money from the account if sufficient funds are available.

        Parameters:
            withdraw_amount (float): The amount of money to deduct.

        Logic:
            1. Check if withdraw_amount is greater than zero.
            2. Check if the account has enough funds to cover the withdrawal.
            3. Deduct amount if valid; otherwise, output the appropriate error.

        Return:
            float: The updated account balance.
        """
        # Verifying that the withdrawal amount is valid and doesn't overdraft the account.
        if withdraw_amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return self.amount
        elif withdraw_amount > self.amount:
            print(
                f"Error: Insufficient funds. Requested ${withdraw_amount:,.2f}, "
                f"but balance is only ${self.amount:,.2f}."
            )
            return self.amount
        else:
            self.amount -= float(withdraw_amount)
            print(f"Successfully withdrew ${withdraw_amount:,.2f}.")
            return self.amount

    def get_balance(self):
        """
        Returns the current account balance.

        Parameters:
            None

        Return:
            float: The current balance of the account.
        """
        # Simple accessor to give the caller the current balance.
        return self.amount

    def calculate_interest(self, days):
        """
        Calculates simple interest accrued over a given number of days
        using a standard 365-day year.

        Parameters:
            days (int): The number of days interest is calculated for.

        Logic:
            1. Check that days is an integer greater than or equal to 0.
            2. Compute interest: principal * annual_rate * (days / 365).
            3. Store the result in self.accrued_interest.
            4. Return the calculated interest value.

        Return:
            float: The calculated interest amount.
        """
        # Making sure the elapsed time value is a valid non-negative number of days.
        if days >= 0:
            # Using the standard interest formula: I = P * r * (t / 365)
            self.accrued_interest = (
                self.amount * self.interest_rate * (days / 365.0)
            )
            return self.accrued_interest
        else:
            print("Error: Number of days cannot be negative.")
            return 0.0

    def __str__(self):
        """
        Provides a user-friendly string representation of the account object,
        displaying account holder info, balance, and interest amounts.

        Parameters:
            None

        Return:
            str: Formatted string summary of the account status.
        """
        # Formatting state variables with two-decimal precision for currency values.
        return (
            f"--- Bank Account Summary ---\n"
            f"Account Holder   : {self.name}\n"
            f"Account Number   : {self.account_number}\n"
            f"Current Balance  : ${self.amount:,.2f}\n"
            f"Annual Rate      : {self.interest_rate * 100:.2f}%\n"
            f"Accrued Interest : ${self.accrued_interest:,.2f}\n"
            f"----------------------------"
        )


def test_bank_acct():
    """
    Test harness function designed to exercise and verify all methods and state
    behavior of the BankAcct class, including object initialization, deposits,
    withdrawals, interest adjustment, day-based interest math, and __str__ display.

    Parameters:
        None

    Variables:
        acct (BankAcct): The test bank account object.
        days_to_calc (int): Number of days passed to test interest calculation.
        calculated_int (float): Returned interest from calculation method.

    Logic:
        1. Instantiate BankAcct with initial values.
        2. Display the newly created account state using __str__().
        3. Test valid and invalid deposit methods.
        4. Test valid and overdrawn withdrawal methods.
        5. Test interest rate adjustment.
        6. Calculate interest across a 30-day billing cycle.
        7. Print the updated account object to show updated balance and interest.

    Return:
        None
    """
    print("=== STARTING BANKACCT CLASS TEST HARNESS ===\n")

    # Step 1: Instantiating a new BankAcct object with initial parameters.
    # $1,000.00 initial balance at 3.5% (0.035) annual interest rate.
    print("[1] Creating new account for Jane Doe...")
    acct = BankAcct(
        name="Jane Doe",
        account_number="ACT-884920",
        amount=1000.00,
        interest_rate=0.035,
    )

    # Printing the object directly invokes __str__() by default.
    print(acct)
    print()

    # Step 2: Testing deposit operations (both valid and invalid).
    print("[2] Testing deposit operations...")
    acct.deposit(250.50)
    print(f"Verified balance via get_balance(): ${acct.get_balance():,.2f}")
    # Testing an invalid deposit value
    acct.deposit(-50.00)
    print()

    # Step 3: Testing withdrawal operations (valid and excessive).
    print("[3] Testing withdrawal operations...")
    acct.withdraw(100.25)
    print(f"Verified balance via get_balance(): ${acct.get_balance():,.2f}")
    # Attempting to withdraw more than the available balance
    acct.withdraw(5000.00)
    print()

    # Step 4: Testing interest rate adjustment.
    print("[4] Testing interest rate adjustment...")
    # Raising interest rate to 4.25% (0.0425)
    acct.adjust_interest_rate(0.0425)
    # Testing invalid negative rate
    acct.adjust_interest_rate(-0.01)
    print()

    # Step 5: Testing day-based interest calculation.
    days_to_calc = 30
    print(
        f"[5] Calculating accrued interest for a {days_to_calc}-day period..."
    )
    calculated_int = acct.calculate_interest(days_to_calc)
    print(
        f"Interest calculated over {days_to_calc} days: ${calculated_int:,.2f}"
    )
    print()

    # Step 6: Verifying final display using __str__().
    print("[6] Final account status check (__str__ representation):")
    print(acct)

    print("\n=== TEST HARNESS COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    test_bank_acct()
