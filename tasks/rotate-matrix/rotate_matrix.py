def rotate_matrix(rows):
    if type(rows) is not list:
        raise TypeError("rows must be an exact built-in list")
    for row in rows:
        if type(row) is not list:
            raise TypeError("each row must be an exact built-in list")
        for value in row:
            if type(value) is not int:
                raise TypeError("each value must be an exact built-in int")
    if len(rows) > 100:
        raise ValueError("at most 100 rows allowed")
    for row in rows:
        if len(row) > 100:
            raise ValueError("each row may hold at most 100 values")
        for value in row:
            if value < -1000000000 or value > 1000000000:
                raise ValueError("value out of range [-1000000000, 1000000000]")
    if not rows:
        return []
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise ValueError("ragged matrix: every row must match the first row's length")
    height = len(rows)
    return [[rows[height - 1 - i][j] for i in range(height)] for j in range(width)]
