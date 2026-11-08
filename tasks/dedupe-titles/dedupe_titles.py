import unicodedata


def _normalize_title(title: str) -> frozenset[str]:
    text = unicodedata.normalize("NFKC", title).casefold()
    pieces: list[str] = []
    in_decimal_run = False
    for ch in text:
        if ch.isdecimal():
            if not in_decimal_run:
                pieces.append(" num ")
                in_decimal_run = True
        else:
            in_decimal_run = False
            if ch.isalnum():
                pieces.append(ch)
            else:
                pieces.append(" ")
    return frozenset("".join(pieces).split())


def find_duplicates(rows: list[dict[str, str]]) -> list[list[str]]:
    active: list[tuple[str, frozenset[str]]] = []
    for row in rows:
        row_id = row["id"] if isinstance(row, dict) else row.id
        title = row["title"] if isinstance(row, dict) else row.title
        tokens = _normalize_title(title)
        if tokens:
            active.append((row_id, tokens))

    n = len(active)
    if n < 2:
        return []

    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri = find(i)
        rj = find(j)
        if ri != rj:
            if ri < rj:
                parent[rj] = ri
            else:
                parent[ri] = rj

    for i in range(n):
        tokens_i = active[i][1]
        len_i = len(tokens_i)
        for j in range(i + 1, n):
            tokens_j = active[j][1]
            len_j = len(tokens_j)
            if 5 * min(len_i, len_j) < 4 * max(len_i, len_j):
                continue
            inter = len(tokens_i & tokens_j)
            union_size = len_i + len_j - inter
            if 5 * inter >= 4 * union_size:
                union(i, j)

    components: dict[int, list[str]] = {}
    for i in range(n):
        root = find(i)
        components.setdefault(root, []).append(active[i][0])

    result = [sorted(group) for group in components.values() if len(group) >= 2]
    result.sort()
    return result
