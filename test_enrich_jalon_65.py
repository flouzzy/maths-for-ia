import re
import os

with open("jalon-65/Jalon-65.md", "r", encoding="utf-8") as f:
    content = f.read()

print("Original content:")
print(content[:500])
