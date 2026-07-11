import re

with open('generate_tex_final_v2.py', 'r') as f:
    c = f.read()

# Replace the broken marker regex
c = c.replace(r"(__(?:MATH|CODE|INLINE_CODE)_BLOCK_\d+__)", r"(__(?:MATH_BLOCK|CODE_BLOCK|INLINE_CODE)_\d+__)")
c = c.replace(r"__(?:MATH|CODE|INLINE_CODE)_BLOCK_\d+__", r"__(?:MATH_BLOCK|CODE_BLOCK|INLINE_CODE)_\d+__")

with open('generate_tex_final_v2.py', 'w') as f:
    f.write(c)
