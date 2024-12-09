from remove_silence import remove_silence

import os
import sys


def process_directory(directory):
    """
    Processes all files in the given directory by removing silence from each file.

    Args:
        directory (str): The path to the directory containing the files to be processed.

    Returns:
        None
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            remove_silence(file_path)
            print(f"Processed {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_silence_batch.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)

    process_directory(directory)
