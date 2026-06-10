import timeit

setup = """
from rename_files import clean_filename
filename = 'Jalon 108 (Livrable IA).md'
"""

stmt = "clean_filename(filename)"

time = timeit.timeit(stmt, setup=setup, number=100000)
print(f"Time for 100,000 runs: {time:.4f} seconds")
