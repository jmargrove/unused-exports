from typing import Set
import os


def typescript_file_filter(dir: str):
    print(os.getcwd())


    files = os.listdir(dir)

    filtered_files: Set[str] = set()
    wd = os.getcwd()
    for file in files:
        if file.endswith(".ts"):
            filtered_files.add(f"{wd}/{dir}/{file}")

    return filtered_files
