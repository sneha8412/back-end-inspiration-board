def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False