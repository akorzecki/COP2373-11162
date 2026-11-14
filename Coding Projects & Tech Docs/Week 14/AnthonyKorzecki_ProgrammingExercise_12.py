import csv
import os

import numpy as np


def load_exam_grades(filename):
    """
    This function is called by the main "analyze_student_grades" function to
    read student exam records from a CSV file and load the numeric grades
    into a two-dimensional numpy array.

    Parameters:
        filename (str): The name or path of the CSV file containing
        student names and exam grades.

    Variables:
        exam_headers (list): A list of strings storing the column headers
        for each exam extracted from the first row of the CSV file.

        grade_rows (list): A temporary two-dimensional list used to collect
        each student's numeric exam scores before converting to an ndarray.

        csv_file (TextIOWrapper): File object used to read the CSV dataset.

        reader (csv.reader): CSV reader iterator used to parse rows from
        the open file.

        header_row (list): The first row of the CSV file containing column
        titles.

        row (list): A single student's record from the CSV file containing
        first name, last name, and exam scores.

        numeric_scores (list): A temporary list holding one student's exam
        grades converted from strings to floating-point numbers.

        grades_array (numpy.ndarray): A two-dimensional numpy array of
        floating-point exam grades where rows represent students and
        columns represent exams.

    Logic:
        1. Initialize empty lists for exam_headers and grade_rows.
        2. Open the CSV file in read mode and create a csv.reader object.
        3. Read the header row and slice from index 2 onward to capture
        the exam titles while skipping first and last name columns.
        4. Loop through each remaining student row in the reader,
        converting exam score strings into floats and appending them to
        grade_rows.
        5. Convert grade_rows into a contiguous numpy ndarray using
        np.array with dtype=float, and return both exam_headers and
        grades_array to the caller.

    Return:
        Returns a tuple containing exam_headers (list) and grades_array
        (numpy.ndarray).
    """
    # initializing lists to hold the exam column titles and student scores
    # before building the numpy array.
    exam_headers = []
    grade_rows = []

    # opening the CSV file from the previous programming exercise in read mode
    # so we can extract the header and numeric grade columns.
    with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        # reading the first row to separate the exam titles from the
        # string-based student name columns.
        header_row = next(reader)
        exam_headers = header_row[2:]

        # looping through each student record in the CSV file and converting
        # their exam scores from text strings to floating-point numbers.
        for row in reader:
            if row:
                numeric_scores = [float(score) for score in row[2:]]
                grade_rows.append(numeric_scores)

    # converting the 2D list of numeric scores into a numpy ndarray so we
    # can perform fast batch and axis-based statistical operations.
    grades_array = np.array(grade_rows, dtype=float)
    return exam_headers, grades_array


def display_exam_statistics(exam_headers, grades_array):
    """
    This function is called by "analyze_student_grades" to calculate and
    print column-by-column statistics as well as pass/fail counts for each
    individual exam using numpy axis operations and Boolean arrays.

    Parameters:
        exam_headers (list): Column titles corresponding to each exam.

        grades_array (numpy.ndarray): Two-dimensional array of student
        grades where rows are students and columns are exams.

    Variables:
        exam_means (numpy.ndarray): One-dimensional array containing the
        arithmetic mean for each exam column.

        exam_medians (numpy.ndarray): One-dimensional array containing the
        median grade for each exam column.

        exam_stds (numpy.ndarray): One-dimensional array containing the
        standard deviation for each exam column.

        exam_mins (numpy.ndarray): One-dimensional array containing the
        lowest score for each exam column.

        exam_maxs (numpy.ndarray): One-dimensional array containing the
        highest score for each exam column.

        passed_counts (numpy.ndarray): One-dimensional array storing the
        number of students scoring 60 or above on each exam.

        failed_counts (numpy.ndarray): One-dimensional array storing the
        number of students scoring below 60 on each exam.

        index (int): Loop index used to align each exam header with its
        corresponding column statistics.

        exam_name (str): Title of the current exam being displayed.

    Logic:
        1. Compute mean, median, standard deviation, minimum, and maximum
        along axis=0 to collect statistics down each exam column.
        2. Create Boolean arrays for passing (>= 60) and failing (< 60)
        grades and sum along axis=0 to count passes and fails per exam.
        3. Loop through each exam index and print the formatted statistics
        and pass/fail totals.

    Return:
        None
    """
    # using axis=0 tells numpy to calculate each statistic down the rows
    # for every individual exam column in the dataset.
    exam_means = np.mean(grades_array, axis=0)
    exam_medians = np.median(grades_array, axis=0)
    exam_stds = np.std(grades_array, axis=0)
    exam_mins = np.min(grades_array, axis=0)
    exam_maxs = np.max(grades_array, axis=0)

    # applying comparison operators produces Boolean arrays of the same
    # shape; summing along axis=0 counts True values (1s) for each exam.
    passed_counts = np.sum(grades_array >= 60, axis=0)
    failed_counts = np.sum(grades_array < 60, axis=0)

    print("\n--- Statistics by Exam ---")
    # looping through each exam column to display its summary metrics
    # and pass/fail counts clearly.
    for index, exam_name in enumerate(exam_headers):
        print(f"\n{exam_name}:")
        print(f"  Mean:               {exam_means[index]:.2f}")
        print(f"  Median:             {exam_medians[index]:.2f}")
        print(f"  Standard Deviation: {exam_stds[index]:.2f}")
        print(f"  Minimum:            {exam_mins[index]:.2f}")
        print(f"  Maximum:            {exam_maxs[index]:.2f}")
        print(f"  Students Passed:    {passed_counts[index]}")
        print(f"  Students Failed:    {failed_counts[index]}")


def display_overall_statistics(grades_array):
    """
    This function is called by "analyze_student_grades" to compute and
    display summary statistics and the overall pass percentage across all
    exams combined.

    Parameters:
        grades_array (numpy.ndarray): Two-dimensional array containing all
        student exam grades.

    Variables:
        overall_mean (float): Arithmetic mean across every grade in the
        entire dataset.

        overall_median (float): Median value across all grades combined.

        overall_std (float): Standard deviation across all grades combined.

        overall_min (float): Lowest single grade across all exams.

        overall_max (float): Highest single grade across all exams.

        passing_grades (numpy.ndarray): One-dimensional array extracted by
        applying a Boolean mask (grades_array >= 60) to select all passing
        scores.

        total_grades (int): Total number of exam scores in the dataset.

        total_passed (int): Total number of passing scores (60 or above).

        pass_percentage (float): Percentage of all exam grades that met or
        exceeded the passing threshold of 60.

    Logic:
        1. Call numpy statistical functions without an axis argument to
        aggregate mean, median, standard deviation, min, and max across
        the entire array.
        2. Apply a Boolean mask to isolate all grades >= 60 into a 1D
        array and use np.size to count total grades and passing grades.
        3. Calculate the overall pass percentage and print all overall
        dataset metrics.

    Return:
        None
    """
    # omitting the axis argument causes numpy to evaluate all elements
    # in the 2D array as a single combined dataset.
    overall_mean = np.mean(grades_array)
    overall_median = np.median(grades_array)
    overall_std = np.std(grades_array)
    overall_min = np.min(grades_array)
    overall_max = np.max(grades_array)

    # using a Boolean array as a mask selects only elements >= 60 into a
    # 1D array so we can measure the pass count with np.size.
    passing_grades = grades_array[grades_array >= 60]
    total_grades = np.size(grades_array)
    total_passed = np.size(passing_grades)
    pass_percentage = (total_passed / total_grades) * 100

    print("\n--- Overall Statistics (All Exams Combined) ---")
    print(f"  Overall Mean:               {overall_mean:.2f}")
    print(f"  Overall Median:             {overall_median:.2f}")
    print(f"  Overall Standard Deviation: {overall_std:.2f}")
    print(f"  Overall Minimum:            {overall_min:.2f}")
    print(f"  Overall Maximum:            {overall_max:.2f}")
    print(f"  Overall Pass Percentage:    {pass_percentage:.2f}%")


def analyze_student_grades():
    """
    This main coordinator function loads the student grades CSV dataset,
    displays the first few rows to verify array structure, and delegates
    per-exam and overall statistical reporting to helper functions.

    Parameters:
        None

    Variables:
        script_dir (str): Directory path where this Python script is saved.

        csv_filename (str): Full file path to the grades.csv file located in
        the same directory as this script.

        exam_headers (list): List of exam column names returned by
        load_exam_grades.

        grades_array (numpy.ndarray): Two-dimensional numpy array of
        student exam scores returned by load_exam_grades.

    Logic:
        1. Determine the directory containing the running script and build
        the full path to "grades.csv".
        2. Call load_exam_grades to import the CSV data into a numpy
        ndarray.
        3. Print the first 5 rows of grades_array using numpy slicing
        to inspect the dataset structure.
        4. Call display_exam_statistics to output per-exam metrics and
        pass/fail counts.
        5. Call display_overall_statistics to output combined dataset
        metrics and overall pass percentage.

    Return:
        None
    """
    # resolving the directory where this script resides so grades.csv is
    # always found regardless of the terminal's active working directory.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filename = os.path.join(script_dir, "grades.csv")

    # loading the exam headers and numeric grades into a numpy array.
    exam_headers, grades_array = load_exam_grades(csv_filename)

    # slicing the first 5 rows of the 2D array to preview the dataset
    # structure before running statistical calculations.
    print("First 5 rows of the student grades dataset:")
    print(grades_array[:5])

    # running column-level and dataset-wide statistical analyses.
    display_exam_statistics(exam_headers, grades_array)
    display_overall_statistics(grades_array)


if __name__ == "__main__":
    analyze_student_grades()
