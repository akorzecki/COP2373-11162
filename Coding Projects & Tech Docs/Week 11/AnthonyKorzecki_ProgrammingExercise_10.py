import csv


def write_student_grades(filename="grades.csv"):
    """
    This function prompts an instructor for the number of students to record,
    collects each student's name and exam grades, and writes the records to
    a CSV file with appropriate headers using the csv module and with keyword.

    Parameters:
        filename (str): The destination filename to write grade records to.
        Defaults to "grades.csv".

    Variables:
        student_count (int): Stores how many student records the instructor
        wants to enter during the session.

        header (list): List of column header strings written as the first row.

        first_name (str): Temporary storage for the student's first name.

        last_name (str): Temporary storage for the student's last name.

        exam1 (int): Integer score for student's Exam 1.

        exam2 (int): Integer score for student's Exam 2.

        exam3 (int): Integer score for student's Exam 3.

        csv_file (file object): File handle managed by the with statement context.

        writer (csv.writer): CSV writer object used to format rows to disk.

    Logic:
        1. Prompt user for number of students and validate input is positive.
        2. Open target CSV file in write mode ('w') using the "with" context
           manager and newline='' to prevent blank rows.
        3. Instantiate csv.writer and write the header row.
        4. Loop through student_count, gathering names and 3 integer exam scores.
        5. Write each validated record as a new row in the CSV file.
        6. Display confirmation message once writing completes.

    Return:
        None
    """
    # Prompt the instructor for student count with basic validation
    # to avoid negative or non-integer loop counts.
    while True:
        try:
            student_count = int(
                input("Enter the number of students to record: ")
            )
            if student_count > 0:
                break
            print("Please enter a positive whole number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    header = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    # Open file using with statement so the handle closes automatically
    # even if an exception occurs during writing operations.
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write out table header first
        writer.writerow(header)

        # Loop to gather data for each individual student
        for student_idx in range(1, student_count + 1):
            print(f"\n--- Entering data for Student #{student_idx} ---")
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()

            # Helper loop to ensure exam inputs convert cleanly to ints
            exam_scores = []
            for exam_num in range(1, 4):
                while True:
                    try:
                        score = int(
                            input(f"Enter grade for Exam {exam_num}: ")
                        )
                        exam_scores.append(score)
                        break
                    except ValueError:
                        print("Error: Exam grade must be an integer. Retry.")

            # Unpack collected exam grades into row record
            record = [first_name, last_name, *exam_scores]
            writer.writerow(record)

    print(f"\nSuccessfully saved {student_count} record(s) to '{filename}'.")


def read_student_grades(filename="grades.csv"):
    """
    This function reads records from the specified grades CSV file using the
    csv module and displays the data formatted in aligned tabular columns.

    Parameters:
        filename (str): The filename of the CSV file to read and display.
        Defaults to "grades.csv".

    Variables:
        csv_file (file object): File handle managed by the with statement.

        reader (csv.reader): CSV reader instance used to parse rows.

        header (list): First row extracted containing column titles.

        row (list): Each sequential student record list read from the file.

        sep_line (str): Visual hyphen-based divider string matching table width.

    Logic:
        1. Enclose open call in a try/except block to intercept FileNotFoundError
           gracefully if the target file does not exist.
        2. Open file in read mode ('r') using the "with" context manager.
        3. Extract the header row via next() and print formatted column headers.
        4. Print a clean divider line.
        5. Iterate through remaining rows, aligning text columns to the left
           and numerical scores to the right using f-string width specifiers.

    Return:
        None
    """
    try:
        # Open CSV file using with statement for safe resource handling
        with open(
            filename, mode="r", newline="", encoding="utf-8"
        ) as csv_file:
            reader = csv.reader(csv_file)

            # Retrieve header row first to set column titles
            header = next(reader, None)
            if not header:
                print(f"Error: '{filename}' is empty.")
                return

            # Print table headers with fixed column widths for alignment
            print("\n" + "=" * 56)
            print(
                f"{header[0]:<14} {header[1]:<14} "
                f"{header[2]:>8} {header[3]:>8} {header[4]:>8}"
            )
            print("-" * 56)

            # Iterate through rows and print aligned values
            for row in reader:
                # Expecting 5 items per student row: fname, lname, ex1, ex2, ex3
                if len(row) == 5:
                    print(
                        f"{row[0]:<14} {row[1]:<14} "
                        f"{row[2]:>8} {row[3]:>8} {row[4]:>8}"
                    )
            print("=" * 56)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found.")


def main():
    """
    Coordinates the program workflow by first invoking the write routine
    to build the CSV dataset, followed by the read routine to verify
    and render the output in tabular form.
    """
    target_csv = "grades.csv"

    print("=== Student Grade Record System ===")
    write_student_grades(target_csv)

    print("\nReading generated grade records...")
    read_student_grades(target_csv)


if __name__ == "__main__":
    main()
