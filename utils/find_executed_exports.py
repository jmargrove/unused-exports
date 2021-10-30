from utils.read_file_content import read_file_content
from typing import Set
import re


def find_executed_exports(exports: Set[str], files: Set[str]):
    unused_exports = exports.copy()
    for file in files:
        content = read_file_content(file)
        for export in exports:
            found_execution = re.findall(r"import {adder", content)
            if found_execution:
                unused_exports.remove(export)

    return unused_exports
