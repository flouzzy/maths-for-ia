import re

content = "__INLINE_CODE_0__"
parts = re.split(r'(__(?:MATH_BLOCK|CODE_BLOCK|INLINE_CODE)_\d+__)', content)
print("Before:", parts)
for i in range(len(parts)):
    if not re.match(r'__(?:MATH_BLOCK|CODE_BLOCK|INLINE_CODE)_\d+__', parts[i]):
        parts[i] = parts[i].replace('_', '\\_')
print("After:", parts)
