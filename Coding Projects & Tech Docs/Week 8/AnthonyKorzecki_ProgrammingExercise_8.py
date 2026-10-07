import re


def validate_phone_number(phone_str):
    """
    This function is called by the main function to check if the phone
    number entered by the user matches a valid phone number pattern
    using regular expressions.

    Parameters:
        phone_str (str): The raw phone number string entered by the user.

    Variables:
        cleaned_phone (str): A temporary variable that holds the user's
        input with any accidental outer whitespace removed so extra spaces
        don't fail the check.

        phone_pattern (str): The regex pattern string used to check the format.
        Looks for 10 digits total, allowing optional parentheses on the area
        code and optional dashes or spaces between digit groups.

        matched (re.Match | None): Stores the result of re.fullmatch. It will
        hold a match object if the string is valid, or None if it fails.

    Logic:
        1. Strip whitespace from phone_str and assign to cleaned_phone.
        2. Set up the phone_pattern raw string.
        3. Run re.fullmatch to make sure the entire string matches the
        pattern with no extra characters hanging off the end.
        4. Use an IF statement to check if matched holds an actual match.
        5. If True, return True to the caller.
        6. If False, return False to the caller.

    Return:
        Returns a boolean (True or False) indicating whether the phone
        number entered is valid.
    """
    # stripping accidental spaces off the front and back so
    # hitting spacebar by mistake doesn't fail an otherwise good number.
    cleaned_phone = phone_str.strip()

    # regex pattern for standard US phone numbers:
    # ^(\(\d{3}\)|\d{3}) handles 3 digits with or without parentheses
    # [ -]? allows a dash, space, or no separator at all
    # \d{3} checks for the next 3 digits
    # [ -]? handles the second separator
    # \d{4}$ ensures it ends with the last 4 digits
    phone_pattern = r"^(\(\d{3}\)|\d{3})[ -]?\d{3}[ -]?\d{4}$"

    # running fullmatch so that extra junk at the beginning or end
    # won't pass through like it might with regular re.match.
    matched = re.fullmatch(phone_pattern, cleaned_phone)

    # checking if fullmatch found a valid pattern match.
    if matched:
        # the phone number matches our rules, so we send True back.
        return True
    else:
        # something didn't match the format, so we return False.
        return False


def validate_ssn(ssn_str):
    """
    This function verifies whether the Social Security Number entered by
    the user follows standard 9-digit SSN formatting rules.

    Parameters:
        ssn_str (str): The raw SSN string passed in from the user input.

    Variables:
        cleaned_ssn (str): A temporary string to store the input with
        leading and trailing whitespace stripped off.

        ssn_pattern (str): The regex pattern string requiring 3 digits,
        an optional dash, 2 digits, an optional dash, and 4 digits.

        matched (re.Match | None): Holds the match object from re.fullmatch
        to check if the string passed the pattern check.

    Logic:
        1. Clean outer whitespace from ssn_str.
        2. Build the ssn_pattern regex string.
        3. Run re.fullmatch against the cleaned input.
        4. If matched exists, return True to the caller.
        5. If matched is None, return False to the caller.

    Return:
        Returns a boolean (True or False) showing if the SSN is valid.
    """
    # removing any accidental spacebar spaces from the ends.
    cleaned_ssn = ssn_str.strip()

    # pattern looks for:
    # 3 digits at the start (\d{3})
    # an optional dash (-?)
    # 2 digits in the middle (\d{2})
    # an optional dash (-?)
    # 4 digits at the end (\d{4})
    ssn_pattern = r"^\d{3}-?\d{2}-?\d{4}$"

    # testing the string with fullmatch to prevent extra numbers from passing.
    matched = re.fullmatch(ssn_pattern, cleaned_ssn)

    # checking whether the regex found an exact match.
    if matched:
        # format is good, return True back to caller.
        return True
    else:
        # bad format or wrong number of digits, return False.
        return False


def validate_zip_code(zip_str):
    """
    This function checks if the postal ZIP code entered by the user is
    either a standard 5-digit code or an extended 9-digit ZIP+4 code.

    Parameters:
        zip_str (str): The raw ZIP code string entered by the user.

    Variables:
        cleaned_zip (str): Stores the sanitized input string without outer
        spaces.

        zip_pattern (str): The regex pattern that matches 5 digits, plus
        an optional group containing a dash and 4 extra digits.

        matched (re.Match | None): Holds the result of re.fullmatch to tell
        us if the postal code matched the pattern.

    Logic:
        1. Strip whitespace from zip_str and store in cleaned_zip.
        2. Set up zip_pattern to look for 5 digits and optional +4 group.
        3. Evaluate the cleaned string with re.fullmatch.
        4. Return True if a match was found.
        5. Return False if no match was found.

    Return:
        Returns a boolean (True or False) indicating if the ZIP is valid.
    """
    # cleaning off any leading or trailing spaces.
    cleaned_zip = zip_str.strip()

    # regex pattern for postal codes:
    # \d{5} requires the first 5 numbers
    # (-\d{4})? makes the dash and extra 4 digits optional as a group
    zip_pattern = r"^\d{5}(-\d{4})?$"

    # running fullmatch to make sure no extra characters or letters slip in.
    matched = re.fullmatch(zip_pattern, cleaned_zip)

    # checking if the ZIP code matched the pattern.
    if matched:
        # valid 5-digit or 9-digit code found.
        return True
    else:
        # invalid postal format, return False.
        return False


def run_tests():
    """
    This function runs automated test cases through our three validator
    functions to prove that both valid and invalid inputs are handled
    correctly by the regular expressions.

    Parameters:
        None

    Variables:
        phone_tests (list): List of sample phone numbers paired with
        their expected boolean outcome.

        ssn_tests (list): List of sample SSNs paired with their expected
        boolean outcome.

        zip_tests (list): List of sample ZIP codes paired with their
        expected boolean outcome.

    Logic:
        1. Build test lists containing valid inputs and invalid edge cases.
        2. Loop through phone tests, run
        validate_phone_number, and print status.
        3. Loop through SSN tests, run validate_ssn, and print status.
        4. Loop through ZIP tests, run validate_zip_code, and print status.

    Return:
        None
    """
    # setting up test cases for phone numbers
    # (various valid formats + broken ones)
    phone_tests = [
        ("941-555-0199", True),
        ("(941) 555-0199", True),
        ("941 555 0199", True),
        ("9415550199", True),
        ("555-0199", False),
        ("941-555-01999", False),
        ("abc-def-ghij", False),
    ]

    # setting up test cases for SSNs (dashes, no dashes, bad groups, letters)
    ssn_tests = [
        ("000-12-3456", True),
        ("000123456", True),
        ("00-123-4567", False),
        ("000-12-345", False),
        ("123-45-678a", False),
    ]

    # setting up test cases for ZIP codes
    # (5-digit, ZIP+4, wrong length, letters)
    zip_tests = [
        ("34236", True),
        ("34236-1234", True),
        ("3423", False),
        ("342361", False),
        ("34236-12", False),
        ("ABCDE", False),
    ]

    print("\n--- Running Test Cases ---")

    # testing phone numbers
    print("\nTesting Phone Numbers:")
    for value, expected in phone_tests:
        result = validate_phone_number(value)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"  [{status}] Input: '{value}' -> "
            "Result: {result} (Expected: {expected})"
        )

    # testing SSNs
    print("\nTesting SSNs:")
    for value, expected in ssn_tests:
        result = validate_ssn(value)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"  [{status}] Input: '{value}' -> "
            "Result: {result} (Expected: {expected})"
        )

    # testing ZIP codes
    print("\nTesting ZIP Codes:")
    for value, expected in zip_tests:
        result = validate_zip_code(value)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"  [{status}] Input: '{value}' -> "
            "Result: {result} (Expected: {expected})"
        )

    print("\n--- Tests Complete ---\n")


def main():
    """
    Main driver function that handles running the test suite, getting
    interactive input from the user, and reporting back whether each item
    is valid or invalid.

    Parameters:
        None

    Variables:
        user_phone (str): Stores the phone number entered by the user.

        user_ssn (str): Stores the SSN entered by the user.

        user_zip (str): Stores the ZIP code entered by the user.

        phone_is_valid (bool): Stores whether
        the user's phone passed validation.

        ssn_is_valid (bool): Stores whether the user's SSN passed validation.

        zip_is_valid (bool): Stores whether the user's ZIP passed validation.

    Logic:
        1. Run run_tests to demonstrate that the regex patterns work.
        2. Prompt the user to enter a phone number, SSN, and ZIP code.
        3. Pass each input into its respective validation function.
        4. Print out whether each item entered was valid or invalid.

    Return:
        None
    """
    # running automated tests first to satisfy assignment requirements.
    run_tests()

    print("=== Input Validation Program ===")

    # asking the user for a phone number to test.
    user_phone = input("Enter a phone number to validate: ")

    # asking the user for a Social Security Number.
    user_ssn = input("Enter a Social Security Number to validate: ")

    # asking the user for a ZIP code.
    user_zip = input("Enter a ZIP code to validate: ")

    # calling our validator functions and storing the booleans.
    phone_is_valid = validate_phone_number(user_phone)
    ssn_is_valid = validate_ssn(user_ssn)
    zip_is_valid = validate_zip_code(user_zip)

    # displaying the results for each input.
    print("\n--- Validation Results ---")

    # checking phone validity
    if phone_is_valid:
        print(f"Phone Number '{user_phone}': VALID")
    else:
        print(f"Phone Number '{user_phone}': INVALID")

    # checking SSN validity
    if ssn_is_valid:
        print(f"Social Security Number '{user_ssn}': VALID")
    else:
        print(f"Social Security Number '{user_ssn}': INVALID")

    # checking ZIP code validity
    if zip_is_valid:
        print(f"ZIP Code '{user_zip}': VALID")
    else:
        print(f"ZIP Code '{user_zip}': INVALID")


# boilerplate check to ensure main only executes when run directly.
if __name__ == "__main__":
    main()
