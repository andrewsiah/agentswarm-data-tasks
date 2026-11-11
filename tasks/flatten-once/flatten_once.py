def flatten_once(values: list) -> list:
    if type(values) is not list:
        raise TypeError("Values must be an integer list.")

    for sublist in values:
        if type(sublist) is not list:
            raise TypeError("All elements in values must be lists.")

        for item in sublist:
            if type(item) is not int:
                raise TypeError("Each item must be integer.")


    if len(values) > 100:
        raise ValueError("Values list must not exceed length of 100.")
    result = []
    for sublist in values:
        if len(sublist) > 100:
            raise ValueError("Inner list must not exceed length of 100.")

        for item in sublist:
            if item < -1000000000 or item > 1000000000:
                raise ValueError(f"Invalid value of an element: {item}")
            result.append(item)

    return result 
