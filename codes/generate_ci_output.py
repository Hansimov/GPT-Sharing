import os
import csv
import datetime
from faker import Faker
import numpy as np
import pandas as pd
import shutil
from typing import Union

np.random.seed(0)
fake = Faker()
fake.seed_instance(0)


class Program:
    def __init__(self, name: str, test_cases: list[str]):
        self.name = name
        self.test_cases = test_cases

    def generate_data(self):
        # Create program directory
        program_dir = self.create_directory(os.path.join("CI_output", self.name))

        # Generate data for each datetime in range
        start_date = datetime.date(2023, 5, 1)
        end_date = datetime.date(2023, 5, 31)
        delta = datetime.timedelta(days=1)
        current_date = start_date
        while current_date <= end_date:
            datetime_str = current_date.strftime("%Y-%m%d-%H%M%S")
            # Create datetime directory
            datetime_dir = self.create_directory(
                os.path.join(program_dir, datetime_str)
            )

            # Generate regression.csv file
            self.generate_regression_csv(datetime_dir)

            # Generate data for each test case
            for test_case in self.test_cases:
                self.generate_test_case_data(datetime_dir, test_case)

            current_date += delta

    @staticmethod
    def create_directory(path: str) -> str:
        """
        Create a directory

        :param path: Path to directory
        :return: Path to created directory
        """
        os.makedirs(path, exist_ok=True)
        return path

    def generate_regression_csv(self, datetime_dir: str):
        """
        Generate regression.csv file

        :param datetime_dir: Path to datetime directory
        """
        try:
            # Calculate data for regression.csv file
            data = self.calculate_regression_data(datetime_dir)

            # Write data to regression.csv file using Pandas
            self.write_csv(os.path.join(datetime_dir, "regression.csv"), data)
        except Exception as e:
            print(f"Error generating regression.csv file: {e}")

    def calculate_regression_data(
        self, datetime_dir: str
    ) -> list[list[Union[str, float]]]:
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

    def write_csv(self, file_path: str, data: list[list[Union[str, float]]]):
        """
        Write data to csv file using Pandas

        :param file_path: Path to csv file
        :param data: Data to write
        """
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_csv(file_path, index=False)

    def generate_test_case_data(self, datetime_dir: str, test_case: str):
        """
        Generate data for a test case

        :param datetime_dir: Path to datetime directory
        :param test_case: Name of test case
        """
        # Create test case directory
        test_case_dir = self.create_directory(os.path.join(datetime_dir, test_case))

        # Simulate data for log file using Faker
        log_data = self.simulate_log_data(test_case)

        # Write data to log file
        self.write_file(os.path.join(test_case_dir, f"{test_case}.log"), log_data)

        # Simulate data for csv file using NumPy
        csv_data = self.simulate_csv_data()

        # Write data to csv file using Pandas
        self.write_csv(os.path.join(test_case_dir, f"{test_case}.csv"), csv_data)

    def simulate_log_data(self, test_case: str) -> str:
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

    def write_file(self, file_path: str, data: str):
        """
        Write data to file

        :param file_path: Path to file
        :param data: Data to write
        """
        with open(file_path, "w") as f:
            f.write(data)

    def simulate_csv_data(self) -> list[list[Union[str, float]]]:
        """
        Simulate data for csv file using NumPy

        :return: Simulated csv data
        """
        result = np.random.choice(["PASS", "FAIL"], size=4)
        time = np.random.uniform(low=0.5, high=1.5, size=4)
        data = [["input", "result", "time"]]
        data.extend([[i + 1, result[i], time[i]] for i in range(4)])
        return data


class GPUProgram(Program):
    def __init__(self):
        super().__init__(
            "GPU_tests", ["matrix_multiplication_test", "image_processing_test"]
        )


class CPUProgram(Program):
    def __init__(self):
        super().__init__(
            "CPU_tests", ["sorting_algorithm_test", "prime_number_generation_test"]
        )


class NetworkProgram(Program):
    def __init__(self):
        super().__init__("Network_tests", ["ping_test", "bandwidth_test"])


class StorageProgram(Program):
    def __init__(self):
        super().__init__("Storage_tests", ["read_write_test", "file_transfer_test"])


def generate_CI_output():
    """
    Generate test data for CI_output directory
    """
    # Remove CI_output directory if it exists
    if os.path.exists("CI_output"):
        shutil.rmtree("CI_output")

    # Create CI_output directory
    Program.create_directory("CI_output")

    # Generate data for GPU_tests
    GPUProgram().generate_data()

    # Generate data for CPU_tests
    CPUProgram().generate_data()

    # Generate data for additional programs and test cases
    NetworkProgram().generate_data()
    StorageProgram().generate_data()


if __name__ == "__main__":
    generate_CI_output()
