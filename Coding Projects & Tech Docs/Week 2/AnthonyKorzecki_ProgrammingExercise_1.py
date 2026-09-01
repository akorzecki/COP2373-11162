def ask_for_tickets(remaining_ticketcount):
    """
    This function is called by the main "postsale_ticket_status" function to
    gather the user's ticket requests and pass them to the caller.

    Parameters:
        remaining_ticketcount (int): The # of remaining tickets,
        as tracked by the postsale function.

    Variables:
        requested_tickets (int): A temporary variable to track the # of tickets
        the user is currently requesting. The request amount isn't directly
        written to the parameter so that it can be checked to ensure
        it is a valid input before being sent off to the caller.

    Logic:
        1. Establish requested_tickets temp variable. Prompts user for their
        ticket request and informs them of order limitaions.
        2. Run an if statement to ensure that the ticket request follows the
        limitations and that the request
        does not exceed the available pool of tickets.
        3. If the IF logic check passes, the new balance
        (original remaining_ticketcount minus the ticket request)
        is returned to the caller for further processing
        4. If the logic check doesn't pass, the user is informed of their error
        and the function simply returns the value it was orignally passed
        back to the caller.

    Return:
        Returns a modified remaining_ticketcount, which represents the updated
        balance of the available ticket pool.
    """
    # Asking user for how many tix they'd like to buy
    # and assigning that value to the accumulator variable.
    # This is necessary to keep track of the active transaction.
    requested_tickets = int(
        input(
            "Please buy some tickets. We haven't made a sale in weeks."
            "We have ten tickets left, and we let you buy 1-4 at a time."
        )
    )
    # checking to make sure the user is buying between 1-4 tickets,
    # as to stick within the rules of the assignment.
    # also checking if the requested ticket amount is not greater than the
    # remaining ticket count as to not sell nonexistent tickets.
    if (
        1 <= requested_tickets <= 4
        and requested_tickets <= remaining_ticketcount
    ):
        # if the if statement check passes,
        # we can return the new ticket_count value to the caller.
        return remaining_ticketcount - requested_tickets
    # if the check fails, something got screwed up. We can re-prompt the user
    # to input a different (hopefully correct) value.
    else:
        print(
            "Error: the ticket count you input is invalid. Please try again."
        )
        # returning the remaining_ticketcount parameter unchanged as to not
        # modify the ticket_count without a true sale.
        return remaining_ticketcount


def postsale_ticket_status():
    """
    This function keeps track of the number of tickets,
    the number of customers, and handles the loop logic
    to ensure that only 20 tickets are sold
    (and that no non-existent tickets are sold).

    Parameters:
        None

    Variables:
        tickets_left (int): Accumulator to count the number of
        tickets that are left to be sold.

        customer_count (int): Accumulator that counts the number of customers
        (transactions) that have taken place.

        new_ticket_count (int): Temporary storage variable used to store the
        pending ticket purchase. Used to ensure that a valid # of tickets
        are being sold during a transaction.

    Logic:
        1. Establish main accumulators (1 and 2)
        2. Start "While" loop that runs while there are valid tickets remaining
        3. Assign the temporary storage variable the returned
        value of the ask_for_tickets function
        4. Compare the temp storage variable with the tickets_left accumulator
        to ensure that there was a transaction
        (that the ticket count decreased by at least 1)
        5. Increase the customer_count accumulator by 1 to mark a new customer
        6. Set the "true" ticket_count accumulator to the value of
        new_ticket_count to ensure the count is up-to-date
        7. If there are more than 0 tickets left, display a message to tell the
        user how many tickets are remaining and continue the loop
        8. If there are 0 tickets remaining, the While loop ends and the
        customer count message is displayed, ending the program loop.

    Return:
        None
    """
    # creating the accumulator variables
    tickets_left = 10  # accumulator 1
    customer_count = 0  # accumulator 2

    # while loop runs while there are still tickets.
    # if not, it stops and the end message displays.
    while tickets_left > 0:
        # running the ask_for_tickets function to get ticket sales from user
        # and assigning the parameter of that function to a new variable for
        # boolean and math operations later.
        new_ticket_count = ask_for_tickets(tickets_left)
        # nested if function runs only if there is a difference between the
        # tickets left previously and the most recent ticket count
        # generated from the ask_for_tickets function.
        if new_ticket_count < tickets_left:
            # since we know at least 1 ticket has been sold,
            # we can safely update the customer accumulator.
            customer_count += 1
            # updating the main tickets_left accumulator
            # to reflect the new ticket availability.
            tickets_left = new_ticket_count
            # balance statement only runs if there are tickets remaining,
            # so that a balance of "0 tickets remaining" never shows.
            if tickets_left > 0:
                print(f"There are {tickets_left} tickets remaining!")
    # this could've been in an else statement, but that would be redundant.
    # once the while loop stops, there must be 0 tickets remaining,
    # meaning we can display the end message w/ customer count.
    print(
        f"There are no tickets remaining and {customer_count} "
        "customers purchased tickets. Come again soon!"
    )


if __name__ == "__main__":
    postsale_ticket_status()
