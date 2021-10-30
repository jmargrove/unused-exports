from utils.typescript_file_filter import typescript_file_filter
from utils.find_exports import find_exports
from utils.find_executed_exports import find_executed_exports


def main(dir: str):
    # Filter for the typescript files
    filtered_files = typescript_file_filter(dir)
    # Create a set of the exports
    exports = find_exports(filtered_files)
    # Check if the export is used
    unused_exports = find_executed_exports(exports, filtered_files)
    # print exports
    print("exports", unused_exports)


main("./tests/data")
