from utils.read_file_content import read_file_content
from typing import Set
import re


def find_exports(files: Set[str]):
    exports: Set[str] = set()
    for file in files:
        content = read_file_content(file)
        found_exports = re.findall(r"export const .+=", content)
        for found_export in found_exports:
            clean_export = re.sub(r"export const ", "", found_export)
            clean_assign = re.sub(r"\s.+", "", clean_export)
            exports.add(clean_assign)
    return exports
