def read_file(file_name):
    with open(file_name) as file:
        return [line.strip() for line in file]
