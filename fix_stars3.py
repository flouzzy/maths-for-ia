with open("jalon-99.tex", "r", encoding="utf-8") as f:
    content = f.read()

# Replace ANY instance of `\quad $\bigstar` followed by something and `}` with just the clean stars.
import re
content = re.sub(r'\\quad \$\\bigstar.*?\}', r'\\quad $\\bigstar\\bigstar\\star\\star\\star$}', content)

with open("jalon-99.tex", "w", encoding="utf-8") as f:
    f.write(content)
