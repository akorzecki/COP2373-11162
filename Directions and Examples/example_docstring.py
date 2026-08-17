def write_sales_to_file(sales, filename="sales.txt"):
    """
    Writes a list of sales amounts to a text file.

    Parameters:
        sales (list of float): A list containing individual sales amounts.
        filename (str): The name of the file where sales will be written.

    Variables:
        file (TextIO): File object used to write data to the file.
        sale (float): Individual sales amount from the sales list.

    Logic:
        1. Open the file in write mode.
        2. Loop through the sales list.
        3. Write each sale amount to the file on a new line.
        4. Close the file automatically using a context manager.

    Return:
        None
    """
    # Open the file in write mode
    with open(filename, "w") as file:
        # Loop through each sale in the list
        for sale in sales:
            # Write the sale amount to the file
            file.write(f"{sale}\n")


def read_sales_and_total(filename="sales.txt"):
    """
    Reads sales amounts from a file and calculates the total sales.

    Parameters:
        filename (str): The name of the file containing sales data.

    Variables:
        file (TextIO): File object used to read data from the file.
        total (float): Accumulator used to store the total sales amount.
        line (str): Each line read from the file representing a sale.

    Logic:
        1. Open the file in read mode.
        2. Initialize total to 0.0.
        3. Loop through each line in the file.
        4. Convert the line to a float and add it to total.
        5. Return the total sales amount.

    Return:
        float: The total of all sales read from the file.
    """
    # Initialize total sales to zero
    total = 0.0

    # Open the file in read mode
    with open(filename, "r") as file:
        # Read each line from the file
        for line in file:
            # Convert the line to a float and add to total
            total += float(line.strip())

    # Return the total sales amount
    return total


def display_total_sales():
    """
    Calls the function that reads and totals sales, then displays the result.

    Parameters:
        None

    Variables:
        total_sales (float): The total sales amount returned from
                             the read_sales_and_total function.

    Logic:
        1. Call the read_sales_and_total function.
        2. Store the returned value in total_sales.
        3. Display the total sales to the user.

    Return:
        None
    """
    # Call the function to read and total sales
    total_sales = read_sales_and_total()

    # Display the total sales
    print(f"Total Sales: ${total_sales:.2f}")


# Program entry point
if __name__ == "__main__":
    # Create a list of sample sales amounts
    sales_list = [120.50, 89.99, 45.00, 210.75]

    # Write the sales data to a file
    write_sales_to_file(sales_list)

    # Read the file and display the total sales
    display_total_sales()
