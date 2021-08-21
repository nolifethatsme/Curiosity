import logging
from datetime import datetime
from decimal import Decimal
from os.path import isfile, isdir, basename, abspath, dirname
from os import mkdir

from pandas import Timestamp
import pandas as pd
import pandas_schema as pd_schema
import pandas_schema.validation as pd_validation
import numpy as np
import datetime
import inspect
import sys
from collections import defaultdict


def list_duplicates(seq):
    tally = defaultdict(list)
    for i, item in enumerate(seq):
        tally[item].append(i)
    return ((key, locs) for key, locs in tally.items() if len(locs) > 1)


class CSVLoader:
    def __init__(self, file_path: str = ""):
        #: str = None):
        # Ensure we don't have an empty string value.
        if len(file_path) == 0:
            raise AttributeError("File path cannot be None or empty.")
        else:
            self.filename = basename(file_path)  # MED ... .csv
            self.filepath = abspath(file_path)  # /home/.../.csv
            self.validate_filename()
            self.validate_file_validity()
            self.df: pd.DataFrame = self.load_csv()

    def validate_filename(self):
        if not (
            self.filename.endswith(".csv") and self.filename.startswith("MED_DATA_")
        ):
            raise SystemError(f"File {self.filepath} malformed or not found.")

    def validate_file_validity(self):
        data = []
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = f.readlines()
            f.close()
        if len(data) <= 1:
            raise SystemError(f"File {self.filepath} is empty or has no data.")

    def load_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.filepath)


class CSVFileObject(CSVLoader):
    """
    This class represents a CSV file.
    """

    def __init__(self, file_path: str = ""):
        super().__init__(file_path=file_path)
        self.logger = logging.getLogger("CSVFileObject")
        self._float_validation = [
            pd_validation.CustomElementValidation(
                lambda n: self._check_float(n), "is not a float"
            )
        ]
        self._int_validation = [
            pd_validation.CustomElementValidation(
                lambda i: self._check_int(i), "is not integer"
            )
        ]
        self._null_validation = [
            pd_validation.CustomElementValidation(
                lambda d: not pd.isnull(d), "this field cannot be null"
            )
        ]
        self._timestamp_validation = [
            pd_validation.CustomElementValidation(
                lambda t: self._check_timestamp(t), "is not timestamp"
            )
        ]
        self._unique_validation = [
            pd_validation.CustomSeriesValidation(
                validation=lambda x: ~x.duplicated(keep=False), message="is not unique"
            )
        ]
        self._create_folders()
        self._validate_data()

    def _check_float(self, num):
        """
        Custom element validation for floats.
        """
        return isinstance(num, float)

    def _check_int(self, num):
        """
        Custom element validation for integers.
        """
        return isinstance(num, int)


    @staticmethod
    def _check_timestamp(timestamp):
        """
        Custom element validation for timestamps.
        """
        # This checks to see if the object being passed through is either
        # a datetime.datetime object or a pandas.Timestamp object.
        ts = list(map(int, timestamp.split(":")))
        # ts = [int(part) for part in timestamp.split(":")]
        return (
            0 <= ts[0]
            and ts[0] < 24
            and 0 <= ts[1]
            and ts[1] < 60
            and 0 <= ts[2]
            and ts[2] < 60
        )

    def _generate_schema(self) -> pd_schema.Schema:
        return pd_schema.Schema(
            [
                pd_schema.Column(
                    "batch_id",
                    self._int_validation
                    + self._null_validation
                    + self._unique_validation,
                ),
                pd_schema.Column(
                    "timestamp", self._timestamp_validation + self._null_validation
                ),
            ]
            + [
                pd_schema.Column(
                    f"reading{i}", self._float_validation + self._null_validation
                )
                for i in range(1, 11)
            ]
        )

    def _create_folders(self):
        if not isdir(self.filepath.replace(self.filename, "") + "clean/"):
            mkdir(self.filepath.replace(self.filename, "") + "clean/")
        if not isdir(self.filepath.replace(self.filename, "") + "errors/"):
            mkdir(self.filepath.replace(self.filename, "") + "errors/")

    def _validate_data(self):
        errors = self._generate_schema().validate(self.df)
        errors_index_rows = [e.row for e in errors]
        data_clean = self.df.drop(index=errors_index_rows)

        err_rows, err_cols, err_message = (
            [e.row for e in errors],
            [e.column for e in errors],
            [e.message for e in errors],
        )
        pd.DataFrame({"row": err_rows, "col": err_cols, "message": err_message}).to_csv(
            self.filepath.replace(self.filename, "")
            + "errors/"
            + self.filename[:-4]
            + "_errors.csv",
            index=False,
        )
        data_clean.to_csv(
            self.filepath.replace(self.filename, "")
            + "clean/"
            + self.filename[:-4]
            + "_clean.csv",
            index=False,
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise RuntimeError(
            f"Insufficient arguments (2 required, {len(sys.argv)} provided)"
        )

    filename: str = sys.argv[1]

    csv_file_object = CSVFileObject(file_path=filename)
