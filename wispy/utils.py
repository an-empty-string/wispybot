def read_file(filename):
    """
    Read an entire file in one go. Handle file descriptor closing.
    """
    with open(filename) as f:
        contents = f.read()
    return contents
