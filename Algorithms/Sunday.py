def sundaySearch(pattern: str, d: str) -> int:
    m, n = len(pattern), len(d)
    occurrence = {}
    for j in range(m):
        occurrence[pattern[j]] = j
    i = 0
    result = []
    while i <= n - m:
        if pattern == d[i:i + m]:
            result.append(i)
            i += 1
        else:
            next_char = d[i + m] if i + m < n else None
            if next_char in occurrence:
                i += m - occurrence[next_char]
            else:
                i += m - occurrence.get(d[i + m - 1], -1)
    return result
