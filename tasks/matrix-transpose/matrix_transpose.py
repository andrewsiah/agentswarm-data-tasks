def matrix_transpose(rows):
    if not isinstance(rows, list):
        raise TypeError()
    if not rows:
        return None
    return [[r[j] for r in rows] for j in range(len(rows))]
