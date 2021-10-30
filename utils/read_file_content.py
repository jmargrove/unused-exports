def read_file_content(path: str):
    f = open(path, "r")
    content = f.read()
    return content
