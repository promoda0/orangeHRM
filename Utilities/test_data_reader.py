import json
import logging
from typing import Dict, Any

class TestDataReader:
    @staticmethod
    def read_json(file_path: str) -> Dict[str, Any]:
        """
        Read data from JSON file
        :param file_path: Path to JSON file
        :return: Dictionary of test data
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            logging.info(f"Successfully read JSON file: {file_path}")
            return data
        except FileNotFoundError:
            logging.error(f"JSON file not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON format in file: {file_path}")
            raise

    # Add methods for Excel/CSV if needed