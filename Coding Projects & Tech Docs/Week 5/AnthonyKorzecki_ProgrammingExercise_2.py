def get_spam_keywords():
    """
    This function sets up and returns the master collection of 30 spam
    keywords and phrases that we'll be scanning the message against.

    Parameters:
        None

    Variables:
        keywords (tuple of str): An immutable collection holding the 30
        target spam phrases used for checking the user's message.

    Logic:
        1. Build the tuple with all 30 spam trigger phrases.
        2. Send the tuple back to whichever function called it.

    Return:
        keywords (tuple of str): The 30 spam keywords used for scanning.
    """
    # setting up an immutable tuple of 30 spam trigger words and phrases.
    # a tuple makes sense here over a list because these reference words
    # are constants and shouldn't be accidentally touched or modified later.
    keywords = (
        "act now",
        "apply now",
        "buy direct",
        "call now",
        "cash bonus",
        "click here",
        "congratulations",
        "dear friend",
        "exclusive deal",
        "expire",
        "fast cash",
        "free gift",
        "giveaway",
        "guaranteed",
        "increase sales",
        "instant",
        "limited time",
        "make money",
        "no credit check",
        "no hidden fees",
        "no obligation",
        "order now",
        "risk-free",
        "save big",
        "special promotion",
        "urgent",
        "winner",
        "win",
        "100% free",
        "$$$",
    )

    # handing the keywords tuple back to the
    # caller so it can use it for scanning.
    return keywords


def get_user_email():
    """
    This function handles grabbing the user's email message from the console,
    allowing them to enter multiple lines until they submit a blank line,
    and then glues it all together into a clean string.

    Parameters:
        None

    Variables:
        lines (list of str): An accumulator list that stores every line of text
        the user inputs.
        user_line (str): A temporary variable used to hold each line of input
        as it comes in.
        full_message (str): The final combined string of all the input lines
        put together.

    Logic:
        1. Print out directions telling the user how to enter their message.
        2. Start a while loop to keep grabbing lines until an empty line is hit.
        3. Make sure the user didn't just submit a blank message.
        4. Join all the collected lines with spaces and strip outer whitespace.
        5. Return the full text string to the caller.

    Return:
        full_message (str): The complete assembled email text string.
    """
    # printing instructions to let the user know how to input their email text
    # and how to tell the program when they're done typing.
    print("Please enter the email message you would like to scan.")
    print(
        "When you are finished entering text, press Enter on an empty line:\n"
    )

    # establishing an accumulator list to hold onto each line the user types in.
    lines = []

    # while loop keeps looping to catch multiple
    # lines of text until the user breaks.
    while True:
        # prompt the user for a line and store it in our temp variable.
        user_line = input()

        # check if the user hit enter on an empty line.
        # if they already gave us text, we know
        # they're finished, so we can break.
        if user_line.strip() == "":
            if len(lines) > 0:
                break
            else:
                # if lines is still empty, they just hit enter
                # immediately without typing.
                # prompt them with an error message so they
                # actually give us some text.
                print("Error: The message cannot be blank. Please enter text.")
                continue

        # append the current line to the lines list accumulator.
        lines.append(user_line)

    # gluing all the stored lines into one single string with spaces in between
    # and stripping out any leftover whitespace on the ends.
    full_message = " ".join(lines).strip()

    # sending the finished string back to the caller.
    return full_message


def scan_message(message, keywords):
    """
    This function takes the email text and the keywords, runs a case-insensitive
    scan across the message to count how many times each spam phrase pops up,
    tallies the spam score, and tracks what was caught.

    Parameters:
        message (str): The full email message text
            passed in from the input function.
        keywords (tuple of str): The 30 spam phrases we are searching for.

    Variables:
        casefold_msg (str): Lowercased/casefolded copy of the
            message so we can do case-insensitive matching.
        spam_score (int): Accumulator variable that tallies up each occurrence
        of a spam phrase found in the text.
        detected_phrases (dict): Dictionary tracking
            each triggered spam word as a key
        and the number of times it appeared as the value.
        term_clean (str): Normalized lowercased
            copy of the active search phrase.
        count (int): Temp variable holding how many
            times the active word was found.

    Logic:
        1. Lowercase the message using casefold
            to handle case-insensitive searching.
        2. Initialize the spam_score accumulator and detected_phrases dictionary.
        3. Loop through each spam phrase in the keywords tuple.
        4. Count how many times the phrase appears in the message using count().
        5. If it hits at least once, add the count to the spam_score accumulator
           and store the word and its count in our dictionary.
        6. Return the total score and dictionary back to the caller.

    Return:
        spam_score (int): The total accumulated spam score.
        detected_phrases (dict of str: int): Dictionary containing the matched
        phrases and their occurrence counts.
    """
    # normalizing the user's message using casefold() so capitalized letters
    # don't slip past our search check.
    casefold_msg = message.casefold()

    # setting up the accumulator for the score and the dictionary to hold hits.
    spam_score = 0
    detected_phrases = {}

    # iterating through each word in the keywords tuple one by one.
    for term in keywords:
        # making sure the keyword is also lowercased
        # so it matches the casefolded text.
        term_clean = term.casefold()

        # running count() to see how many times this specific phrase shows up.
        count = casefold_msg.count(term_clean)

        # checking if the phrase showed up at all (at least 1 time).
        if count > 0:
            # updating our spam_score accumulator with
            # however many times it appeared.
            spam_score += count

            # logging the triggered word and its frequency into our dictionary.
            detected_phrases[term] = count

    # returning both the updated score accumulator and our hits dictionary.
    return spam_score, detected_phrases


def evaluate_likelihood(spam_score):
    """
    This function checks the final spam score against a set of threshold ranges
    to figure out the likelihood that the message is actually spam.

    Parameters:
        spam_score (int): The total spam points calculated by the scan function.

    Variables:
        likelihood_message (str): The descriptive message rating the spam
        probability based on the score.

    Logic:
        1. Compare the score against set point
        brackets using an if-elif-else block.
        2. Assign the matching rating string to the likelihood_message variable.
        3. Return that string back to the caller.

    Return:
        likelihood_message (str): The text description of the spam risk level.
    """
    # running an if-elif chain to check what point range the spam score lands in
    # so we can set the right description.
    if spam_score == 0:
        likelihood_message = "This message does not appear to be spam."
    elif 1 <= spam_score <= 2:
        likelihood_message = "This message has a low likelihood of being spam."
    elif 3 <= spam_score <= 5:
        likelihood_message = (
            "This message has a moderate likelihood of being spam."
        )
    elif 6 <= spam_score <= 9:
        likelihood_message = (
            "This message has a high likelihood of being spam."
        )
    else:
        # if it's 10 or above, it falls through to this catch-all high alert.
        likelihood_message = "This message is almost certainly spam."

    # sending the result back to the caller.
    return likelihood_message


def display_results(spam_score, likelihood, detected_phrases):
    """
    This function formats and outputs the whole breakdown to the user,
    showing their total score, the likelihood rating, and every keyword
    that triggered points.

    Parameters:
        spam_score (int): The final numeric score.
        likelihood (str): The risk evaluation string.
        detected_phrases (dict): The dictionary
            holding the detected words and counts.

    Variables:
        divider (str): String border made using
        string multiplication for clean formatting.
        detail_lines (list of str): List used to
            hold each formatted keyword line before printing.

    Logic:
        1. Build divider borders with the string multiplication operator.
        2. Print the centered header block.
        3. Display the score and the likelihood rating.
        4. If phrases were detected, loop
            through the dictionary, format them into lines,
           and join them with newlines.
        5. If nothing triggered, let the user know the message came back clean.

    Return:
        None
    """
    # building a divider line using string multiplication
    # to make the output look clean.
    divider = "=" * 50

    # printing the header box and centering the title text.
    print("\n" + divider)
    print("SPAM SCAN REPORT".center(50))
    print(divider)

    # outputting the main score and likelihood lines to the screen.
    print(f"Total Spam Score : {spam_score}")
    print(f"Likelihood       : {likelihood}")
    print("-" * 50)

    # checking if our dictionary has any entries in it.
    if len(detected_phrases) > 0:
        print("Detected Trigger Words/Phrases:")

        # accumulator list to store each line we
        # want to display for caught phrases.
        detail_lines = []
        for word, count in detected_phrases.items():
            detail_lines.append(f'  * "{word}" - found {count} time(s)')

        # using join to neatly print all the lines separated by a newline.
        print("\n".join(detail_lines))
    else:
        # if the dictionary is empty, nothing matched, so we let the user know.
        print("No spam trigger words or phrases were detected in the message.")

    # printing the closing border line to cap off the report block.
    print(divider + "\n")


def run_spam_scanner():
    """
    This function acts as the main driver/status coordinator for the program.
    It calls each helper function in order to gather input, run the scan,
    evaluate results, and display the final report.

    Parameters:
        None

    Variables:
        keywords (tuple of str): The 30 spam
            phrases grabbed from get_spam_keywords.
        email_message (str): The email text returned from get_user_email.
        score (int): The numeric spam score returned from scan_message.
        detected_phrases (dict): The dictionary of
            matches returned from scan_message.
        likelihood (str): The risk level string
            returned from evaluate_likelihood.

    Logic:
        1. Call get_spam_keywords to load the phrase list.
        2. Call get_user_email to prompt and capture the user's message.
        3. Call scan_message to calculate the score and track matched words.
        4. Call evaluate_likelihood to turn the score into a readable rating.
        5. Call display_results to print out the final report block.

    Return:
        None
    """
    # grab our tuple of 30 spam keywords.
    keywords = get_spam_keywords()

    # prompt the user and store their email text in email_message.
    email_message = get_user_email()

    # run the scanner function and unpack both the score accumulator
    # and the matched phrases dictionary.
    score, detected_phrases = scan_message(email_message, keywords)

    # pass the score into our likelihood function to get the status message.
    likelihood = evaluate_likelihood(score)

    # pass the collected data off to display_results to output the report.
    display_results(score, likelihood, detected_phrases)


if __name__ == "__main__":
    # kicking off the program loop by calling our main driver function.
    run_spam_scanner()
