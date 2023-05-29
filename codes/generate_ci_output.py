import os
import csv
import datetime
from faker import Faker
import numpy as np
import pandas as pd
from typing import Union

np.random.seed(0)
fake = Faker()
fake.seed_instance(0)


def generate_CI_output():
    """
    Generate test data for CI_output directory
    """
    # Create CI_output directory
    create_directory("CI_output")

    # Generate data for GPU_tests
    generate_program_data(
        "GPU_tests", ["matrix_multiplication_test", "image_processing_test"]
    )

    # Generate data for CPU_tests
    generate_program_data(
        "CPU_tests", ["sorting_algorithm_test", "prime_number_generation_test"]
    )

    # Generate data for additional programs and test cases
    generate_program_data("Network_tests", ["ping_test", "bandwidth_test"])
    generate_program_data("Storage_tests", ["read_write_test", "file_transfer_test"])


def generate_program_data(program_name: str, test_cases: list[str]):
    """
    Generate data for a program

    :param program_name: Name of program
    :param test_cases: List of test cases
    """
    # Create program directory
    program_dir = create_directory(os.path.join("CI_output", program_name))

    # Generate data for each datetime in range
    start_date = datetime.date(2023, 5, 1)
    end_date = datetime.date(2023, 5, 31)
    delta = datetime.timedelta(days=1)
    current_date = start_date
    while current_date <= end_date:
        datetime_str = current_date.strftime("%Y-%m%d-%H%M%S")
        # Create datetime directory
        datetime_dir = create_directory(os.path.join(program_dir, datetime_str))

        # Generate regression.csv file
        generate_regression_csv(datetime_dir)

        # Generate data for each test case
        for test_case in test_cases:
            generate_test_case_data(datetime_dir, test_case)

        current_date += delta


def create_directory(path: str) -> str:
    """
    Create a directory

    :param path: Path to directory
    :return: Path to created directory
    """
    os.makedirs(path, exist_ok=True)
    return path


def generate_regression_csv(datetime_dir: str):
    """
    Generate regression.csv file

    :param datetime_dir: Path to datetime directory
    """
    try:
        # Calculate data for regression.csv file
        data = calculate_regression_data(datetime_dir)

        # Write data to regression.csv file using Pandas
        write_csv(os.path.join(datetime_dir, "regression.csv"), data)
    except Exception as e:
        print(f"Error generating regression.csv file: {e}")


def calculate_regression_data(datetime_dir: str) -> list[list[Union[str, float]]]:
    """
    Calculate data for regression.csv file

    :param datetime_dir: Path to datetime directory
    :return: Calculated data
    """
    data = [["test_case", "result_difference", "time_difference"]]
    for test_case_dir in os.listdir(datetime_dir):
        if os.path.isdir(os.path.join(datetime_dir, test_case_dir)):
            test_case_csv = os.path.join(
                datetime_dir, test_case_dir, f"{test_case_dir}.csv"
            )
            if os.path.exists(test_case_csv):
                df = pd.read_csv(test_case_csv)
                result_difference = df["result"].value_counts().get("PASS", 0) - df[
                    "result"
                ].value_counts().get("FAIL", 0)
                time_difference = df["time"].max() - df["time"].min()
                data.append([test_case_dir, result_difference, time_difference])
    return data


def simulate_regression_data() -> list[list[Union[str, float]]]:
    """
    Simulate data for regression.csv file

    :return: Simulated data
    """
    result_difference = np.random.normal(loc=0.0, scale=1.0, size=4)
    time_difference = np.random.normal(loc=0.0, scale=0.1, size=4)
    data = [["test_case", "result_difference", "time_difference"]]
    data.extend([[i + 1, result_difference[i], time_difference[i]] for i in range(4)])
    return data


def write_csv(file_path: str, data: list[list[Union[str, float]]]):
    """
    Write data to csv file using Pandas

    :param file_path: Path to csv file
    :param data: Data to write
    """
    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_csv(file_path, index=False)


def generate_test_case_data(datetime_dir: str, test_case: str):
    """
    Generate data for a test case

    :param datetime_dir: Path to datetime directory
    :param test_case: Name of test case
    """
    # Create test case directory
    test_case_dir = create_directory(os.path.join(datetime_dir, test_case))

    # Simulate data for log file using Faker
    log_data = simulate_log_data(test_case)

    # Write data to log file
    write_file(os.path.join(test_case_dir, f"{test_case}.log"), log_data)

    # Simulate data for csv file using NumPy
    csv_data = simulate_csv_data()

    # Write data to csv file using Pandas
    write_csv(os.path.join(test_case_dir, f"{test_case}.csv"), csv_data)


def simulate_log_data(test_case: str) -> str:
    """
    Simulate data for log file using Faker

    :param test_case: Name of test case
    :return: Simulated log data
    """
    start_time = fake.date_time_this_year()
    end_time = start_time + datetime.timedelta(minutes=5)
    log_data = (
        f"[INFO] {test_case} started at {start_time}\n"
        f"[INFO] Processing input 1\n"
        f"[WARNING] {fake.sentence()}\n"
        f"[INFO] Processing input 2\n"
        f"[ERROR] {fake.sentence()}\n"
        f"[INFO] {test_case} finished at {end_time}\n"
    )
    return log_data


def write_file(file_path: str, data: str):
    """
    Write data to file

    :param file_path: Path to file
    :param data: Data to write
    """
    with open(file_path, "w") as f:
        f.write(data)


def simulate_csv_data() -> list[list[Union[str, float]]]:
    """
    Simulate data for csv file using NumPy

    :return: Simulated csv data
    """
    result = np.random.choice(["PASS", "FAIL"], size=4)
    time = np.random.uniform(low=0.5, high=1.5, size=4)
    data = [["input", "result", "time"]]
    data.extend([[i + 1, result[i], time[i]] for i in range(4)])
    return data


if __name__ == "__main__":
    generate_CI_output()
