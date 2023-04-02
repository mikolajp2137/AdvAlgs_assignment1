import re

def wildSundaySearch(pattern, text):
    """
    Returns all occurrences of the pattern in the text using Sunday's algorithm with support for wildcards.
    :param pattern: the pattern to search for
    :param text: the text to search in
    :return: a list of starting indices of all occurrences of the pattern in the text
    """
    m = len(pattern)
    n = len(text)
    indices = []
    skip_table = {}
    for i in range(m):
        skip_table[pattern[i]] = m - i
    i = 0
    while i <= n - m:
        j = 0
        while j < m and (text[i + j] == pattern[j] or pattern[j] == "?"):
            j += 1
        if j == m:
            indices.append(i)
        if i + m >= n:
            break
        if text[i + m] in skip_table:
            i += skip_table[text[i + m]]
        else:
            i += m + 1
    pattern = r'{}\b'.format(pattern.replace('?', r'\S'))
    return [m.start() for m in re.finditer(pattern, text)]
