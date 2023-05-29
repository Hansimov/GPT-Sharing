import os
import csv
from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()


def generate_CI_output():
    """
    Generate test data for CI_output directory
    """
    # Create CI_output directory
    os.makedirs("CI_output", exist_ok=True)

    # Generate data for GPU_tests
    generate_program_data(
        "GPU_tests", ["matrix_multiplication_test", "image_processing_test"]
    )

    # Generate data for CPU_tests
    generate_program_data(
        "CPU_tests", ["sorting_algorithm_test", "prime_number_generation_test"]
    )


def generate_program_data(program_name, test_cases):
    """
    Generate data for a program

    :param program_name: Name of program
    :param test_cases: List of test cases
    """
    # Create program directory
    program_dir = os.path.join("CI_output", program_name)
    os.makedirs(program_dir, exist_ok=True)

    # Generate data for each datetime
    for datetime in ["2023-05-01-14-04-31", "2023-05-02-15-30-00"]:
        # Create datetime directory
        datetime_dir = os.path.join(program_dir, datetime)
        os.makedirs(datetime_dir, exist_ok=True)

        # Generate regression.csv file
        generate_regression_csv(datetime_dir)

        # Generate data for each test case
        for test_case in test_cases:
            generate_test_case_data(datetime_dir, test_case)


def generate_regression_csv(datetime_dir):
    """
    Generate regression.csv file

    :param datetime_dir: Path to datetime directory
    """
    try:
        # Simulate data for regression.csv file
        result_difference = np.random.normal(loc=0.0, scale=1.0, size=4)
        time_difference = np.random.normal(loc=0.0, scale=0.1, size=4)
        data = [["test_case", "result_difference", "time_difference"]]
        data.extend(
            [[i + 1, result_difference[i], time_difference[i]] for i in range(4)]
        )

        # Write data to regression.csv file using Pandas
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_csv(os.path.join(datetime_dir, "regression.csv"), index=False)
    except Exception as e:
        print(f"Error generating regression.csv file: {e}")


def generate_test_case_data(datetime_dir, test_case):
    """
    Generate data for a test case

    :param datetime_dir: Path to datetime directory
    :param test_case: Name of test case
    """
    try:
        # Create test case directory
        test_case_dir = os.path.join(datetime_dir, test_case)
        os.makedirs(test_case_dir, exist_ok=True)

        # Simulate data for log file using Faker
        log_data = (
            f"[INFO] {test_case} started at {fake.date_time_this_year()}\n"
            f"[INFO] Processing input 1\n"
            f"[WARNING] {fake.sentence()}\n"
            f"[INFO] Processing input 2\n"
            f"[ERROR] {fake.sentence()}\n"
            f"[INFO] {test_case} finished at {fake.date_time_this_year()}\n"
        )

        # Write data to log file
        with open(os.path.join(test_case_dir, f"{test_case}.log"), "w") as f:
            f.write(log_data)

        # Simulate data for csv file using NumPy
        result = np.random.choice(["PASS", "FAIL"], size=4)
        time = np.random.uniform(low=0.5, high=1.5, size=4)
        data = [["input", "result", "time"]]
        data.extend([[i + 1, result[i], time[i]] for i in range(4)])

        # Write data to csv file using Pandas
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_csv(os.path.join(test_case_dir, f"{test_case}.csv"), index=False)
    except Exception as e:
        print(f"Error generating test case data: {e}")


if __name__ == "__main__":
    generate_CI_output()
