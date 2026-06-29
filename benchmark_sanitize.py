import timeit

setup_uncached = r'''
import re
def run_uncached():
    for _ in range(100):
        filename = r"Jalon 1 (Test ? Title / with \ chars).md"
        filename = re.sub(r'[\\/*?:"<>|$]', '-', filename)
'''

setup_cached = r'''
import re
INVALID_CHAR_PATTERN = re.compile(r'[\\/*?:"<>|$]')
def run_cached():
    for _ in range(100):
        filename = r"Jalon 1 (Test ? Title / with \ chars).md"
        filename = INVALID_CHAR_PATTERN.sub('-', filename)
'''

stmt_uncached = "run_uncached()"
stmt_cached = "run_cached()"

time_uncached = timeit.timeit(stmt_uncached, setup=setup_uncached, number=100000)
time_cached = timeit.timeit(stmt_cached, setup=setup_cached, number=100000)

print(f"Uncached Time (100,000 runs): {time_uncached:.4f} seconds")
print(f"Cached Time (100,000 runs):   {time_cached:.4f} seconds")
print(f"Improvement: {(time_uncached - time_cached) / time_uncached * 100:.2f}%")
