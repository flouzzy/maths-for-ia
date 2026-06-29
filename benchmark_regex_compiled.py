import timeit

setup = r'''
from rename_files import clean_filename as clean_filename_old

REPLACEMENTS = {
    '$-mathbb{R}^n$': 'Rn',
    '$-mathcal{L}^p$': 'Lp',
    '$-mathbb{R}$': 'R',
    'Ã©': 'e',
    'Ã¨': 'e',
    'Ãª': 'e',
    'Ã«': 'e',
    'Ã ': 'a',
    'Ã¢': 'a',
    'Ã´': 'o',
    'Ã»': 'u',
    'Ã§': 'c',
    'Ã®': 'i',
    'Ã¯': 'i',
    'Ã': 'e',
}

def clean_filename_old(filename):
    new_name = filename
    for bad, good in REPLACEMENTS.items():
        new_name = new_name.replace(bad, good)
    new_name = new_name.replace('$', '')
    new_name = new_name.replace('\\', '')
    return new_name

import re
# Sort the keys by length to match the longest first.
# Include $ and \\ for removal as well.
replacements = dict(REPLACEMENTS)
replacements['$'] = ''
replacements['\\'] = ''

# Sort keys by length in descending order to avoid partial matches
sorted_keys = sorted(replacements.keys(), key=len, reverse=True)
pattern = re.compile('|'.join(re.escape(k) for k in sorted_keys))

def replacer(match):
    return replacements[match.group(0)]

def clean_filename_new(filename):
    return pattern.sub(replacer, filename)

filenames = [
    r"Jalon 1 - L'Ã©quation.md",
    r"Jalons Ã©tranges $-mathbb{R}^n$ et Ã§a \foo$.md",
    r"Normal file name.md",
    r"A long filename with lots of Ã© Ã¨ Ãª and Ã« and Ã§ and maybe $-mathbb{R}$ and \$ things.md",
    r"Another completely normal filename without any weird chars.md"
] * 1000
'''

stmt_old = """
for f in filenames:
    clean_filename_old(f)
"""

stmt_new = """
for f in filenames:
    clean_filename_new(f)
"""

print("Old:", timeit.timeit(stmt_old, setup=setup, number=100))
print("New:", timeit.timeit(stmt_new, setup=setup, number=100))
