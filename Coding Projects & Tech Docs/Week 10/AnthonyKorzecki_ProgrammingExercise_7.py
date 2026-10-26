import re


def extract_sentences(paragraph_text):
    """
    This function takes a string containing a paragraph and extracts
    all individual sentences using a regular expression look-ahead pattern
    adapted from Section 7.4 of the textbook.

    Parameters:
        paragraph_text (str): The raw text paragraph entered by the user
        to be parsed into separate sentences.

    Variables:
        sentence_pattern (str): The regex pattern based on Section 7.4,
        modified to allow sentences starting with
        digits as well as capital letters.
        Uses non-greedy matching and a positive
        look-ahead to check for sentence
        termination without consuming subsequent tokens.

        extracted_sentences (list):
        A list of strings containing each individual
        sentence matched by re.findall.

    Logic:
        1. Define the regex pattern using non-greedy
        matching and look-ahead logic,
        allowing uppercase letters and digits at the start of each sentence.
        2. Apply re.findall() with re.DOTALL and re.MULTILINE flags so sentences
        spanning across newlines and ending at
        line breaks are properly captured.
        3. Return the list of matched sentences back to the caller.

    Return:
        Returns a list of strings, where each item is a single sentence
        extracted from the original input text.
    """
    # regular expression pattern adapted from section 7.4 of the textbook.
    # we modified the leading set and look-ahead set from [A-Z] to [A-Z0-9]
    # so that sentences starting with numbers are properly captured.
    # the .*? ensures lazy/non-greedy matching up to the punctuation mark,
    # and the positive look-ahead (?= [A-Z0-9]|$) makes sure we don't consume
    # the start of the next sentence or get tripped up by abbreviations.
    sentence_pattern = r"[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)"

    # scanning the paragraph with re.findall
    # using both dotall and multiline flags.
    # dotall lets the dot match across newlines,
    # while multiline lets $ recognize
    # line endings as string boundaries.
    extracted_sentences = re.findall(
        sentence_pattern, paragraph_text, flags=re.DOTALL | re.MULTILINE
    )

    # returning the list of matched sentences back to the calling function.
    return extracted_sentences


def analyze_paragraph():
    """
    This function serves as the main driver for the program. It prompts
    the user to enter a paragraph, passes the text to the extraction function,
    and displays each parsed sentence along with the total sentence count.

    Parameters:
        None

    Variables:
        user_paragraph (str): The input string entered by the user containing
        the text to be analyzed.

        sentences (list): Storage list holding
        the individual sentences returned
        from the extract_sentences function.

        total_sentences (int): Count of the total number of sentences
        successfully identified in the paragraph.

    Logic:
        1. Prompt the user to enter a paragraph of text.
        2. Pass the input text to extract_sentences()
        to get the list of sentences.
        3. Determine the total number of extracted sentences using len().
        4. Check if any sentences were found. If so, iterate through the list
        and print each individual sentence with an arrow prefix.
        5. Display the final sentence count to the user.
        6. If no valid sentences were found, notify the user.

    Return:
        None
    """
    # prompting the user to enter the paragraph to analyze.
    # this string can contain multiple sentences, newlines, and numbers.
    user_paragraph = input("Enter a paragraph to analyze:\n")

    # calling the extract_sentences function to parse out individual sentences
    # using our regular expression look-ahead logic.
    sentences = extract_sentences(user_paragraph)

    # determining the total count of parsed
    # sentences using the length of the list.
    total_sentences = len(sentences)

    # checking if at least one valid sentence was captured from the user input.
    if total_sentences > 0:
        print("\nExtracted Sentences:")
        # iterating over the list of sentences to print each one individually.
        # using an arrow prefix to match
        # the display convention from section 7.4.
        for sentence in sentences:
            print(f"-> {sentence.strip()}")

        # displaying the final count of sentences identified in the paragraph.
        print(f"\nTotal sentences found: {total_sentences}")
    # if no sentences matched the criteria, display a notification.
    else:
        print("\nNo valid sentences were detected in the input provided.")


if __name__ == "__main__":
    analyze_paragraph()
