def read_textfile(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text
