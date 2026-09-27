import functools


def get_user_expenses():
    """
    This function gathers monthly expenses from the user by repeatedly
    prompting for an expense type and its corresponding dollar amount until
    an empty input is provided.

    Parameters:
        None

    Variables:
        expenses (list): A list of tuples storing each entry in the format
        (expense_type, expense_amount).

        expense_type (str): The label or name of the expense entered by the
        user. Serves as a sentinel to stop input collection when left blank.

        expense_amount (float): The validated dollar value associated with
        the current expense type.

    Logic:
        1. Initialize an empty list named expenses to store the entries.
        2. Enter an indefinite while loop to gather user input.
        3. Prompt the user for the expense category/type.
        4. Check if the input is empty; if so, break out of the collection loop.
        5. Enter an inner validation loop to prompt for the expense amount.
        6. Validate that the amount is numeric and non-negative. If invalid,
        display an error message and re-prompt.
        7. Append the valid (expense_type, expense_amount) tuple to expenses.
        8. Return the completed list of expenses to the caller.

    Return:
        list: Returns the populated list containing (str, float) tuples
        representing all recorded expenses.
    """
    # creating the empty list to store all the expense entries.
    # each item will be added as a (type, amount) tuple pair.
    expenses = []

    # printing directions to show the user how to input their data
    # and letting them know how to end the loop.
    print("--- Monthly Expense Tracker ---")
    print(
        "Enter each expense type and amount."
        "Press Enter on an empty type when finished.\n"
    )

    # while loop runs until user enters a blank string to stop.
    while True:
        # prompt user for expense category and strip out whitespace.
        expense_type = input(
            "Enter expense type (or press Enter to finish): "
        ).strip()

        # checking if the user just pressed enter to stop entering data.
        # if the string is empty, we break out of the loop.
        if len(expense_type) == 0:
            break

        # nested while loop to make sure the amount entered is actually valid
        # so the program doesn't crash on bad inputs.
        while True:
            try:
                # casting the user input to a float to handle dollars and cents.
                expense_amount = float(
                    input(f"Enter amount for '{expense_type}': $")
                )

                # making sure the user didn't enter a negative number.
                if expense_amount < 0:
                    print(
                        "Error: Expense amount "
                        "cannot be negative. Please try again."
                    )
                    continue

                # if it passed the check, break out of the inner loop.
                break

            except ValueError:
                # if user typed in text or letters, catch it and re-prompt.
                print(
                    "Error: Invalid numerical value. Please enter numbers only."
                )

        # appending the clean category and value pair to the master list.
        expenses.append((expense_type, expense_amount))

        # extra print statement just for visual spacing in the terminal.
        print()

    # returning the full expenses list back to caller for processing.
    return expenses


def calculate_total_expense(expenses):
    """
    This function calculates the total sum of all recorded expenses
    using the functools.reduce method and a lambda function.

    Parameters:
        expenses (list): A list of tuples in the
        format (expense_type, expense_amount).

    Variables:
        amounts_only (list): A list comprehension extracting just the float
        amounts from each tuple in the expenses list.

        total (float): The accumulated sum produced by applying functools.reduce
        over the amounts_only list.

    Logic:
        1. Extract the numerical dollar amounts from the expenses tuples
        using list comprehension.
        2. Apply functools.reduce with a lambda
        addition function across the list.
        3. Return the calculated sum to the caller.

    Return:
        float: Returns the combined sum of all expenses.
    """
    # pulling just the dollar amounts out of our tuples using comprehension.
    amounts_only = [item[1] for item in expenses]

    # running functools.reduce with a lambda addition function
    # to add up all the amounts into a single final total.
    total = functools.reduce(lambda x, y: x + y, amounts_only)

    # returning the final calculated total back to the caller.
    return total


def find_highest_expense(expenses):
    """
    This function determines the highest individual expense category
    using the functools.reduce method and a lambda function.

    Parameters:
        expenses (list): A list of tuples in the
        format (expense_type, expense_amount).

    Variables:
        highest (tuple): The resulting tuple (expense_type, expense_amount)
        with the highest dollar amount.

    Logic:
        1. Apply functools.reduce across the list of tuples.
        2. In each pairwise reduction step, compare the float amounts (index 1).
        3. Return whichever tuple possesses the greater amount.
        4. Return the overall highest tuple to the caller.

    Return:
        tuple: Returns the (str, float) tuple
        representing the highest recorded expense.
    """
    # using functools.reduce with a lambda conditional to compare adjacent
    # tuples and keep the one with the larger dollar amount.
    highest = functools.reduce(lambda a, b: a if a[1] >= b[1] else b, expenses)

    # returning the winning tuple with the highest expense back to caller.
    return highest


def find_lowest_expense(expenses):
    """
    This function determines the lowest individual expense category
    using the functools.reduce method and a lambda function.

    Parameters:
        expenses (list): A list of tuples in
        the format (expense_type, expense_amount).

    Variables:
        lowest (tuple): The resulting tuple (expense_type, expense_amount)
        with the lowest dollar amount.

    Logic:
        1. Apply functools.reduce across the list of tuples.
        2. In each pairwise reduction step, compare the float amounts (index 1).
        3. Return whichever tuple possesses the smaller amount.
        4. Return the overall lowest tuple to the caller.

    Return:
        tuple: Returns the (str, float) tuple
        representing the lowest recorded expense.
    """
    # using functools.reduce with a lambda conditional to compare adjacent
    # tuples and keep the one with the smaller dollar amount.
    lowest = functools.reduce(lambda a, b: a if a[1] <= b[1] else b, expenses)

    # returning the winning tuple with the lowest expense back to caller.
    return lowest


def display_expense_summary(total, highest_expense, lowest_expense):
    """
    This function formats and displays the final financial summary,
    including the total sum, highest category, and lowest category.

    Parameters:
        total (float): The combined total of all entered expenses.

        highest_expense (tuple): The tuple representing the highest expense
        in the format (expense_type, expense_amount).

        lowest_expense (tuple): The tuple representing the lowest expense
        in the format (expense_type, expense_amount).

    Variables:
        None

    Logic:
        1. Print decorative delimiter headers for output formatting.
        2. Print formatted total expense with 2 decimal precision.
        3. Print formatted highest expense label and dollar amount.
        4. Print formatted lowest expense label and dollar amount.
        5. Print closing delimiter.

    Return:
        None
    """
    # printing header border for clean output formatting.
    print("\n" + "=" * 40)
    print("         MONTHLY EXPENSE SUMMARY")
    print("=" * 40)

    # printing formatted total with comma and two decimal places.
    print(f"Total Expenses:   ${total:,.2f}")

    # displaying the category label and dollar amount for highest expense.
    print(
        f"Highest Expense:  {highest_expense[0]} (${highest_expense[1]:,.2f})"
    )

    # displaying the category label and dollar amount for lowest expense.
    print(f"Lowest Expense:   {lowest_expense[0]} (${lowest_expense[1]:,.2f})")

    # printing closing border line.
    print("=" * 40)


def main():
    """
    This is the primary driver function that coordinates data collection,
    analysis calculations, validation checks, and presentation of results.

    Parameters:
        None

    Variables:
        user_expenses (list): Stores the collection of expense tuples returned
        from the input gathering function.

        total_spent (float): Stores the aggregated total calculated by
        the reduction function.

        highest_record (tuple): Stores the tuple containing the highest category
        and value.

        lowest_record (tuple): Stores the tuple containing the lowest category
        and value.

    Logic:
        1. Call get_user_expenses to populate user_expenses.
        2. Check if the list contains any items. If empty, print an alert
        and terminate execution.
        3. Call calculate_total_expense to compute aggregate expenditure.
        4. Call find_highest_expense to determine the top expense tuple.
        5. Call find_lowest_expense to determine the lowest expense tuple.
        6. Pass the results to display_expense_summary to print the final report.

    Return:
        None
    """
    # calling function to grab all the expenses from the user.
    user_expenses = get_user_expenses()

    # checking if the user actually entered anything.
    # if the list is empty, display message and stop so reduce doesn't crash.
    if len(user_expenses) == 0:
        print("\nNotice: No expenses were entered. Program terminating.")
        return

    # calculating the total sum of all expenses using reduce.
    total_spent = calculate_total_expense(user_expenses)

    # grabbing the highest expense tuple using reduce.
    highest_record = find_highest_expense(user_expenses)

    # grabbing the lowest expense tuple using reduce.
    lowest_record = find_lowest_expense(user_expenses)

    # passing all the final calculations off to the display function.
    display_expense_summary(total_spent, highest_record, lowest_record)


if __name__ == "__main__":
    main()
