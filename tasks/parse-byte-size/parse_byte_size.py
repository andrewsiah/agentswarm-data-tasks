def parse_byte_size(*args):
    # Validate all supplied values before checking arity or string shape.
    for value in args:
        if type(value) is not str:
            raise TypeError("byte size must be an exact built-in str")

    if len(args) != 1:
        raise ValueError("expected exactly one byte-size string")

    value = args[0]
    units = {
        "GiB": 1024 ** 3,
        "MiB": 1024 ** 2,
        "KiB": 1024,
        "B": 1,
    }

    unit = None
    for suffix, multiplier in units.items():
        if value.endswith(suffix):
            unit = suffix
            number = value[:-len(suffix)]
            break

    if unit is None or not 1 <= len(number) <= 9:
        raise ValueError("invalid byte-size format")

    # Use ASCII comparisons rather than isdigit(), which accepts Unicode digits.
    if any(char < "0" or char > "9" for char in number):
        raise ValueError("invalid byte-size format")

    if number != "0" and number[0] == "0":
        raise ValueError("invalid byte-size format")

    return int(number) * units[unit]
